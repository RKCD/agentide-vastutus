import datetime as dt
import json
import sys
from pathlib import Path
from types import SimpleNamespace as NS

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "agents"))
import radar  # noqa: E402

RSS = b"""<?xml version="1.0"?><rss version="2.0"><channel>
<item><title>AI agentide vastutus muutub</title><link>https://ex.ee/a</link><description>&lt;p&gt;Uus tootevastutus&lt;/p&gt;</description></item>
<item><title>Kohvikuulutus</title><link>https://ex.ee/b</link></item>
</channel></rss>"""
ATOM = b"""<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>Atom AI Act news</title>
<link href="https://ex.eu/x"/><summary>text</summary></entry></feed>"""
HTML = ("<html><body><a href='/lyhike'>lühike</a>"
        "<a href='/uudis/1#x'>Tehisintellekti määruse tähtaegu lükati edasi</a>"
        "<a href='/uudis/1'>Tehisintellekti määruse tähtaegu lükati edasi</a></body></html>").encode()


@pytest.fixture(autouse=True)
def tmp_paths(tmp_path, monkeypatch):
    monkeypatch.setattr(radar, "STATE", tmp_path / "state" / "nähtud.json")
    monkeypatch.setattr(radar, "KULU", tmp_path / "state" / "kulu.jsonl")
    monkeypatch.setattr(radar, "INBOX", tmp_path / "inbox")
    monkeypatch.setattr(radar, "lae_allikad", lambda: [
        {"id": "r", "nimi": "RSS", "tüüp": "rss", "url": "https://ex.ee/feed"},
        {"id": "h", "nimi": "HTML", "tüüp": "html", "url": "https://ex.ee/"},
        {"id": "bad", "nimi": "Katki", "tüüp": "rss", "url": "https://ex.ee/bad"},
    ])
    return tmp_path


def lae(url):
    if url.endswith("/feed"):
        return RSS
    if url.endswith("/bad"):
        raise OSError("404")
    return HTML


class Klient:
    def __init__(self, hinnang=3, viga_kolmandal=False):
        self.kõned, self.hinnang, self.viga = 0, hinnang, viga_kolmandal
        self.messages = self

    def create(self, **kw):
        assert kw["model"] == "claude-haiku-5-5"
        assert "temperature" not in kw
        self.kõned += 1
        if self.viga and self.kõned == 2:
            raise RuntimeError("API alla")
        txt = json.dumps({"hinnang": self.hinnang, "põhjendus": "p", "kokkuvõte": "k"})
        return NS(content=[NS(type="text", text=txt)], usage=NS(input_tokens=1000, output_tokens=100))


TÄNA = dt.date(2026, 10, 19)


def test_parsib_rss_atom_html():
    assert [k.pealkiri for k in radar.parsi_voog(RSS, {"nimi": "x"})][0].startswith("AI agentide")
    assert radar.parsi_voog(ATOM, {"nimi": "x"})[0].url == "https://ex.eu/x"
    k = radar.parsi_html(HTML, {"nimi": "x", "url": "https://ex.ee/"})
    assert len(k) == 1 and k[0].url == "https://ex.ee/uudis/1"  # lühike ja dubleeriv link välja


def test_xml_entiteedirünnak_lükatakse_tagasi():
    pahe = b'<!DOCTYPE x [<!ENTITY a "aaaa"><!ENTITY b "&a;&a;">]><rss><channel><item><title>&b;</title><link>https://e/</link></item></channel></rss>'
    with pytest.raises(Exception):
        radar.parsi_voog(pahe, {"nimi": "x"})


def test_täisjooks_dedup_ja_inbox(tmp_paths):
    kl = Klient()
    t = radar.käivita(klient=kl, täna=TÄNA, lagi=50, lae=lae)
    assert t["uusi"] == 3 and t["filtri_läbinud"] == 2 and t["inboxi"] == 2
    assert len(t["vead"]) == 1 and "bad" in t["vead"][0]
    assert (tmp_paths / "inbox" / "2026-10-19.md").read_text().count("## ") == 2
    # teine jooks: midagi uut pole, kõnesid pole, tühja faili ei teki
    kl2 = Klient()
    t2 = radar.käivita(klient=kl2, täna=TÄNA + dt.timedelta(days=1), lagi=50, lae=lae)
    assert t2["uusi"] == 0 and kl2.kõned == 0 and t2["fail"] is None
    assert not (tmp_paths / "inbox" / "2026-10-20.md").exists()


def test_hinnang_alla_2_ei_lähe_inboxi(tmp_paths):
    t = radar.käivita(klient=Klient(hinnang=1), täna=TÄNA, lagi=50, lae=lae)
    assert t["inboxi"] == 0 and not (tmp_paths / "inbox").exists()


def test_lagi_ja_edasilükkamine(tmp_paths):
    t = radar.käivita(klient=Klient(), täna=TÄNA, lagi=1, lae=lae)
    assert t["kõnesid"] == 1 and "lagi" in t["peatatud"]
    t2 = radar.käivita(klient=Klient(), täna=TÄNA, lagi=50, lae=lae)
    assert t2["hinnatud"] == 1  # ülejäänud kirje töödeldi järgmisel jooksul


def test_api_viga_ei_märgi_nähtuks():
    t = radar.käivita(klient=Klient(viga_kolmandal=True), täna=TÄNA, lagi=50, lae=lae)
    assert "LLM-viga" in t["peatatud"]
    olek = radar.lae_olek()
    assert len(olek["nähtud"]) == 2  # 1 filtrist välja + 1 hinnatud; vea saanud jäi uuesti proovitavaks


def test_kulu_logitakse(tmp_paths):
    radar.käivita(klient=Klient(), täna=TÄNA, lagi=50, lae=lae)
    rida = json.loads((tmp_paths / "state" / "kulu.jsonl").read_text().splitlines()[0])
    assert rida["kõnesid"] == 2 and rida["sisend_tokenid"] == 2000 and rida["hind_usd"] > 0


def test_seed_ja_kuiv_ei_kutsu_llm(tmp_paths):
    t = radar.käivita(klient=None, täna=TÄNA, lagi=50, kuiv=True, lae=lae)
    assert t["kuiv"] and not (tmp_paths / "state").exists()
    t = radar.käivita(klient=None, täna=TÄNA, lagi=50, seed=True, lae=lae)
    assert t["seed"] and len(radar.lae_olek()["nähtud"]) == 3


def test_vana_olek_kustutatakse():
    olek = {"versioon": 1, "nähtud": {"a": {"kuupäev": "2025-01-01", "url": "u"}, "b": {"kuupäev": "2026-10-01", "url": "u"}}}
    radar.salvesta_olek(olek, TÄNA)
    assert list(radar.lae_olek()["nähtud"]) == ["b"]


def test_kontrolli_allikaid():
    def lae_ühe_veaga(url):
        if "riigiteataja" in url:
            raise OSError("403")
        return HTML
    tabel = "\n".join(radar.kontrolli_allikaid(lae_ühe_veaga))
    assert "OK" in tabel and "VIGA" in tabel and "välja lülitatud" in tabel


def test_pärisfailid_laevad():
    # config on päris, mitte monkeypatchitud
    assert radar.lae_märksõnad().search("Tehisintellekti määrus")
    assert not radar.lae_märksõnad().search("kohvik")
