#!/usr/bin/env python3
"""Loeb esmaallika ja prindib otsitud lõigud. Kasutatakse kaardi väidete kontrollimiseks.

Kasutus:
    python agents/allikas.py URL [URL ...] --otsi "regex" [--otsi "regex"] [--keel est]

EUR-Lexi aktid: kasuta CELLAR-i aadressi https://publications.europa.eu/resource/celex/<CELEX>
(sisu vastavalt Accept-päisele). Riigi Teataja: https://www.riigiteataja.ee/akt/<lühend>
annab lõpliku URL-i (akti ID), tekst tuleb API-st /public-api/api/v1/akt/<id>/txt.
"""

import argparse
import json
import re
import sys
import urllib.error
import urllib.request

from bs4 import BeautifulSoup

UA = "agentide-vastutus-kontroll/0.1 (+https://github.com/RKCD/agentide-vastutus)"
MAHT = 20_000_000


def lae(url: str, keel: str) -> tuple[int, str, str, bytes]:
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, */*;q=0.1",
        "Accept-Language": keel,
    })
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.geturl(), r.headers.get("Content-Type", ""), r.read(MAHT)
    except urllib.error.HTTPError as e:
        return e.code, url, e.headers.get("Content-Type", ""), e.read(200_000)


RT_API = "https://www.riigiteataja.ee/public-api/api/v1/akt/"


def rt_kehtiv(akt_id: str, keel: str) -> tuple[str, str]:
    """rt:<id> -> (kehtiva redaktsiooni txt-URL, päis). Kasutab API JSON-i välja kehtivId."""
    _, _, _, keha = lae(RT_API + akt_id + "?leiaKehtiv=true", keel)
    meta = json.loads(keha)
    kehtiv = str(meta.get("kehtivId") or akt_id)
    p = meta.get("aktiParameetrid", {})
    päis = (f"RT: {p.get('pealkiri')} ({p.get('lyhend')}), kehtiv redaktsioon {kehtiv}, "
            f"kehtivuse algus {p.get('kehtivuseAlgus')}, staatus {meta.get('aktiStaatus')}, "
            f"vaata: https://www.riigiteataja.ee/akt/{kehtiv}")
    return RT_API + kehtiv + "/txt", päis


def tekstiks(tüüp: str, keha: bytes) -> str:
    if "html" in tüüp or "xml" in tüüp or keha.lstrip()[:1] == b"<":
        tekst = BeautifulSoup(keha, "html.parser").get_text("\n")
    else:
        tekst = keha.decode("utf-8", "replace")
    # ELT 2024+ aktides on "Artikkel\xa050": normaliseeri sisetühik, et otsing töötaks.
    tekst = tekst.replace("\xa0", " ").replace("\u202f", " ")
    return re.sub(r"\n\s*\n+", "\n", tekst)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("url", nargs="+")
    p.add_argument("--otsi", action="append", default=[])
    p.add_argument("--keel", default="et, est;q=0.9, en;q=0.5")
    p.add_argument("--konteksti", type=int, default=600)
    p.add_argument("--max", type=int, default=4, help="vasteid mustri kohta")
    p.add_argument("--algus", type=int, default=0, help="prindi teksti algusest N märki")
    p.add_argument("--toores", action="store_true", help="otsi toorest vastusest (HTML-i märgendid alles)")
    a = p.parse_args()

    for url in a.url:
        try:
            if url.startswith("rt:"):
                url, päis = rt_kehtiv(url[3:], a.keel)
                print(f"\n{päis}")
            kood, lõpp, tüüp, keha = lae(url, a.keel)
        except Exception as e:
            print(f"\n##### {url}\nVIGA: {type(e).__name__}: {e}")
            continue
        tekst = keha.decode("utf-8", "replace") if a.toores else tekstiks(tüüp, keha)
        print(f"\n##### {url}\nkood={kood} lõpp-URL={lõpp} tüüp={tüüp} baite={len(keha)} teksti={len(tekst)}")
        if a.algus:
            print("--- algus ---\n" + tekst[:a.algus])
        for muster in a.otsi:
            vasted = list(re.finditer(muster, tekst, re.IGNORECASE))
            print(f"--- /{muster}/ : {len(vasted)} vastet ---")
            for m in vasted[:a.max]:
                s = max(0, m.start() - a.konteksti // 4)
                print("…" + tekst[s:m.start() + a.konteksti].replace("\n", " ⏎ ") + "…\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
