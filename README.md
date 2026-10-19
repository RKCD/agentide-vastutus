# Agentide vastutuse kaart Eestis

Avalik leht, mis näitab, millised Eesti ja EL-i normid rakenduvad, kui AI-agent eksib, kes vastutab ja kuhu teatada.

Põhimõte: **agendid teevad, inimene kinnitab.** Avalik sisu muutub ainult siis, kui Pull Request merge'itakse.

## Ülesehitus

| Fail | Mis see on |
|---|---|
| `data/kaart.yaml` | Kogu sisu: stsenaariumid, normid, vastutus, teatamine, lahtised küsimused |
| `templates/index.html.j2` | Lehe mall (üks HTML-fail, ilma raamistikuta) |
| `build.py` | Kontrollib andmefaili ja ehitab `_site/index.html` |
| `CHANGELOG.md` | Muudatuste ajalugu, renderdatakse lehele |
| `KONTROLLIDA.md` | Genereeritud nimekiri väidetest, mida autor peab esmaallikast kontrollima |
| `.github/workflows/pages.yml` | Ehitab ja avaldab lehe GitHub Pagesis iga `main`-i muudatuse järel |

## Lokaalne ehitamine

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python build.py              # -> _site/index.html
python build.py --kontroll   # -> KONTROLLIDA.md
python -m http.server -d _site 8000
```

`build.py` keeldub ehitamast, kui mõnel normil puudub `allika_url`, staatus on tundmatu või `kohaldub_alates` normil puudub kuupäev.

## Sisu muutmine

- Uus norm: lisa stsenaariumi `normid` alla objekt väljadega `akt`, `säte`, `mida_ütleb`, `allika_url`, `tase` (EL/EE), `staatus` (kehtib / kohaldub_alates / eelnõu / tühistatud) ja vajadusel `alates`.
- Kui väide on esmaallikast üle vaadatud: pane stsenaariumile `kontrollitud: YYYY-MM-DD` ja eemalda normilt väli `kontrollida`.
- Ingliskeelne versioon (hiljem): `data/kaart.en.yaml` ja `python build.py --lang en` (-> `_site/en/`).

## Avaldamine

1. Repo **Settings → Pages → Build and deployment → Source: GitHub Actions**.
2. Iga push `main`-i ehitab lehe uuesti. Käsitsi: **Actions → Ehita ja avalda leht → Run workflow**.

## Agendid (tulekul)

- **Radar** (Etapp 2): iga päev, kogub allikatest uusi kirjeid, kirjutab `inbox/`.
- **Tõlk** (Etapp 3): iga nädal, avab PR-i kaardi uuendusega.

Allikate lisamine, töövoogude käsitsi käivitamine ja API eeldatav kuukulu kirjeldatakse siin koos Etapiga 2.
