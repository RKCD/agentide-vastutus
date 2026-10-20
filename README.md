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

## Väidete kontrollimine esmaallikast

Töövoog **Loe esmaallikat** (`.github/workflows/allikas.yml`, käsitsi) loeb avaliku õigusteksti ja salvestab otsitud lõigud harusse `kontrolli-logid` (fail `<jooksu nr>.txt`).

- Riigi Teataja: `rt:<akti ID>`. Tööriist leiab ise kehtiva redaktsiooni (`leiaKehtiv`) ja loeb teksti avalikust API-st.
- EL-i aktid: `https://publications.europa.eu/resource/celex/<CELEX>` (CELLAR, eestikeelne tekst). EUR-Lexi veebileht on robotikaitse taga.
- Otsingumustrid on regexid, eraldatud ` || `-ga.

Kontrollitud normil on `data/kaart.yaml`-is `kontrollitud: YYYY-MM-DD`. Olukord on kontrollitud ainult siis, kui kõik selle normid on kontrollitud (`build.py` kontrollib seda).

## Radar (iga päev kell 06:00 UTC)

`agents/radar.py` loeb allikad failist `config/allikad.yaml`, jätab välja juba nähtud kirjed (`state/nähtud.json`), filtreerib märksõnadega (`config/filter.yaml`) ja laseb läbinud kirjed `claude-haiku-5-5` hinnata skaalal 0–3. Hinnang 2+ läheb faili `inbox/YYYY-MM-DD.md`. Inbox on toormaterjal, mitte avalik sisu. Kui uusi olulisi kirjeid pole, ei commit'i midagi.

**Esmakordne käivitus (tee selles järjekorras):**
1. Repo **Settings → Secrets and variables → Actions → New repository secret**: `ANTHROPIC_API_KEY`.
2. **Actions → Radar → Run workflow → toiming: `kontrolli_allikaid`.** Tulemus on töövoo kokkuvõttes. Pane mittetöötavad allikad failis `config/allikad.yaml` `lubatud: false`.
3. **toiming: `seed`.** Märgib praegused kirjed nähtuks ilma LLM-ita, et esimene päris jooks ei hindaks kogu veebilehe vana sisu.
4. **toiming: `radar`** (või oota hommikust ajastust).

Muud käsitsi toimingud: `kuiv` näitab, mitu kirjet läheks hindamisele, ilma LLM-ita ega kirjutamata.

**Kulupiirang.** Ühes jooksus on kõva lagi 50 LLM-kõnet (`max_calls` või `RADAR_MAX_CALLS`). Kirjed, mis lae tõttu hindamata jäävad, ei saa nähtud-märget ja tulevad järgmisel jooksul uuesti. API-viga peatab hindamise samamoodi. Iga jooks lisab rea faili `state/kulu.jsonl` (kõnesid, tokenid, hind).

**Eeldatav kuukulu (hinnang, mõõtmata).** Haiku 5.5 maksab $0,10 / $0,50 miljoni sisend- / väljundtokeni kohta. Hinnanguliselt ~600 sisend- ja ~300 väljundtokenit kõne kohta, ehk ~$0,0002 kõne. Täis lagi (50 kõnet päevas) on ~$0,01 päevas ehk alla $0,50 kuus. Päris number selgub `kulu.jsonl`-ist pärast esimest nädalat.

**Teada piirangud.**
- HTML-allikatel (enamik) hindab Haiku ainult lingi pealkirja, sest artiklit ei laeta. See on tugevalt piiratud sisend, mida hinnangu põhjendus ka ütleb. RSS-allikatel on kirjeldus olemas.
- Allikate aadressid on kontrollimata, kuni oled `kontrolli_allikaid` käivitanud. Mõni leht võib vajada JavaScripti või blokeerida robotid.

## Tõlk (tulekul)

Nädalane PR kaardi uuendusega, Etapp 3.
