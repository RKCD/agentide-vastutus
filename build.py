#!/usr/bin/env python3
"""Ehitab staatilise lehe failist data/kaart.yaml.

Kasutus:
    python build.py              # ehitab _site/index.html
    python build.py --lang en    # ehitab data/kaart.en.yaml põhjal _site/en/index.html
    python build.py --kontroll   # kirjutab KONTROLLIDA.md (väited, mis vajavad kontrolli)
"""

import argparse
import datetime as dt
import shutil
import sys
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).parent
STAATUSED = {"kehtib", "kohaldub_alates", "eelnõu", "tühistatud", "tagasi_võetud"}
TASEMED = {"EL", "EE"}
MAX_NORME = 4
SÄILITA_MIN, SÄILITA_MAX = 3, 5
KONTROLL_MIN, KONTROLL_MAX = 8, 10


def lae(lang: str) -> dict:
    nimi = "kaart.yaml" if lang == "et" else f"kaart.{lang}.yaml"
    with open(ROOT / "data" / nimi, encoding="utf-8") as f:
        return yaml.safe_load(f)


def valideeri(kaart: dict) -> list[str]:
    """Tagastab vigade loendi. Allikata väidet ei avalda."""
    vead = []

    def norm(n, koht):
        for v in ("akt", "säte", "mida_ütleb", "allika_url", "tase", "staatus"):
            if not n.get(v):
                vead.append(f"{koht}: puudub väli '{v}'")
        url = n.get("allika_url", "")
        if url and not url.startswith("https://"):
            vead.append(f"{koht}: allika_url peab algama https://")
        if n.get("staatus") not in STAATUSED:
            vead.append(f"{koht}: tundmatu staatus '{n.get('staatus')}'")
        if n.get("tase") not in TASEMED:
            vead.append(f"{koht}: tundmatu tase '{n.get('tase')}'")
        if n.get("kontrollitud") and n.get("kontrollida"):
            vead.append(f"{koht}: kontrollitud normil ei tohi olla 'kontrollida' märkust")
        if n.get("staatus") == "kohaldub_alates" and not n.get("alates"):
            vead.append(f"{koht}: staatus kohaldub_alates vajab välja 'alates'")

    for i, n in enumerate(kaart.get("taust", [])):
        norm(n, f"taust[{i}]")

    ids = set()
    for s in kaart["stsenaariumid"]:
        sid = s.get("id", "?")
        if sid in ids:
            vead.append(f"{sid}: korduv id")
        ids.add(sid)
        for v in ("pealkiri", "lühikirjeldus", "näide", "normid", "kes_vastutab",
                  "kuhu_teatada", "viimati_uuendatud"):
            if not s.get(v):
                vead.append(f"{sid}: puudub väli '{v}'")
        if "kontrollitud" not in s:
            vead.append(f"{sid}: puudub väli 'kontrollitud' (vaikimisi false)")
        elif s["kontrollitud"] and not all(n.get("kontrollitud") for n in s.get("normid", [])):
            vead.append(f"{sid}: olukord on kontrollitud, aga mõni norm mitte")
        if len(s.get("normid", [])) > MAX_NORME:
            vead.append(f"{sid}: üle {MAX_NORME} normi")
        for i, n in enumerate(s.get("normid", [])):
            norm(n, f"{sid}.normid[{i}]")
        juhtum = s.get("juhtum")
        if juhtum and not str(juhtum.get("allika_url", "")).startswith("https://"):
            vead.append(f"{sid}.juhtum: puudub https-allikas")
        teha = s.get("mida_teha", [])
        if teha and not 3 <= len(teha) <= 4:
            vead.append(f"{sid}: mida_teha peab olema 3–4 punkti")
        säilita = s.get("mida_säilitada", [])
        if not SÄILITA_MIN <= len(säilita) <= SÄILITA_MAX:
            vead.append(f"{sid}: mida_säilitada peab olema {SÄILITA_MIN}–{SÄILITA_MAX} punkti")
        # YAML teeb "Tekst: jätk" punktist sõnastiku; nõua stringe.
        for väli in ("mida_säilitada", "lahtised_küsimused", "mida_teha"):
            for i, x in enumerate(s.get(väli, [])):
                if not isinstance(x, str):
                    vead.append(f"{sid}.{väli}[{i}]: pole tekst (pane jutumärkidesse)")
        for i, k in enumerate(s.get("kuhu_teatada", [])):
            if not str(k.get("link", "")).startswith("https://"):
                vead.append(f"{sid}.kuhu_teatada[{i}]: puudub https-link")
    kahju = kaart.get("kahju_korral") or {}
    if not kahju.get("sammud") or not kahju.get("hoiatus"):
        vead.append("kahju_korral: puuduvad sammud või hoiatus")
    kontroll = kaart.get("juurutaja_kontroll", [])
    if not KONTROLL_MIN <= len(kontroll) <= KONTROLL_MAX:
        vead.append(f"juurutaja_kontroll: peab olema {KONTROLL_MIN}–{KONTROLL_MAX} punkti")
    for i, x in enumerate(kontroll):
        url = x.get("allika_url")
        if url is not None and not str(url).startswith("https://"):
            vead.append(f"juurutaja_kontroll[{i}]: allika_url peab algama https://")
    return vead


def kontrolli_nimekiri(kaart: dict) -> str:
    rida = ["# Kontrollimist vajavad väited", "",
            f"Genereeritud: {dt.date.today().isoformat()} (`python build.py --kontroll`).",
            "", "Kui väide on esmaallikast üle vaadatud, pane stsenaariumile "
            "`kontrollitud: YYYY-MM-DD` ja eemalda normilt `kontrollida` väli.", ""]

    def normid(loend, pref):
        for n in loend:
            if n.get("kontrollitud"):
                continue
            märkus = n.get("kontrollida", "")
            rida.append(f"- [ ] **{n['akt']}**, {n['säte']} ({n['staatus']}"
                        + (f" {n['alates']}" if n.get("alates") else "") + ")")
            rida.append(f"  - Väide: {n['mida_ütleb'].strip()}")
            rida.append(f"  - Allikas: {n['allika_url']}")
            if märkus:
                rida.append(f"  - **Kontrollida:** {märkus.strip()}")

    rida += ["## Taustanormid", ""]
    normid(kaart.get("taust", []), "taust")
    for s in kaart["stsenaariumid"]:
        if s.get("kontrollitud"):
            continue
        rida += ["", f"## {s['pealkiri']} (`{s['id']}`)", ""]
        normid(s["normid"], s["id"])
        rida.append("- [ ] Vastutuse jaotus (`kes_vastutab`):")
        for k in s["kes_vastutab"]:
            rida.append(f"  - {k['roll']}: {k['selgitus'].strip()}")
        rida.append("- [ ] Teatamine (`kuhu_teatada`):")
        for k in s["kuhu_teatada"]:
            rida.append(f"  - {k['asutus']}: {k['millal']} ({k['link']})")
    rida += ["", "## Juurutaja kontrollnimekiri", ""]
    for x in kaart.get("juurutaja_kontroll", []):
        if x.get("allika_url"):
            rida.append(f"- [ ] {x['tekst'].strip()} ({x['allika_url']})")
    return "\n".join(rida) + "\n"


def ehita(lang: str) -> Path:
    kaart = lae(lang)
    vead = valideeri(kaart)
    if vead:
        print("Andmefailis on vigu, lehte ei ehitata:", file=sys.stderr)
        for v in vead:
            print(f"  - {v}", file=sys.stderr)
        sys.exit(1)

    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    # Jäta välja esimene pealkiri, lehel on oma pealkiri.
    changelog = "\n".join(changelog.splitlines()[1:])

    env = Environment(loader=FileSystemLoader(ROOT / "templates"),
                      autoescape=True, undefined=StrictUndefined)
    html = env.get_template("index.html.j2").render(
        k=kaart,
        changelog_html=markdown.markdown(changelog),
        ehitatud=dt.date.today().isoformat(),
    )
    välja = ROOT / "_site" / ("" if lang == "et" else lang)
    välja.mkdir(parents=True, exist_ok=True)
    (välja / "index.html").write_text(html, encoding="utf-8")
    if lang == "et":
        shutil.copy(ROOT / "templates" / "favicon.svg", ROOT / "_site" / "favicon.svg")
    return välja / "index.html"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--lang", default="et")
    p.add_argument("--kontroll", action="store_true")
    a = p.parse_args()
    if a.kontroll:
        (ROOT / "KONTROLLIDA.md").write_text(kontrolli_nimekiri(lae(a.lang)), encoding="utf-8")
        print("Kirjutatud KONTROLLIDA.md")
        return
    print(f"Ehitatud {ehita(a.lang)}")


if __name__ == "__main__":
    main()
