# Kontrollimist vajavad väited

Genereeritud: 2026-10-20 (`python build.py --kontroll`).

Kui väide on esmaallikast üle vaadatud, pane stsenaariumile `kontrollitud: YYYY-MM-DD` ja eemalda normilt `kontrollida` väli.

## Taustanormid

- [ ] **Võlaõigusseaduse muutmise eelnõu (tootevastutus)**, VÕS tootevastutuse sätted (§ 1061 jj) (eelnõu)
  - Väide: Justiits- ja Digiministeerium on koostanud eelnõu uue tootevastutuse direktiivi ülevõtmiseks. Kehtiv VÕS § 1063 loeb tooteks juba praegu ka arvutitarkvara.
  - Allikas: https://www.e-kaubanduseliit.ee/uudised/puudusega-toote-eest-vastutavate-ettevotjate-ring-laieneb
  - **Kontrollida:** Eelnõu esmaallikat (EIS-i kirjet) ei leitud, link on teisene. VÕS § 1063 on kontrollitud kehtivast tekstist (RT 120062026018).

## Agent töötleb või lekitab isikuandmeid (`isikuandmed`)

- [ ] **Isikuandmete kaitse seadus (IKS)**, üldsätted, järelevalve (kehtib)
  - Väide: Täpsustab GDPR-i rakendamist Eestis. Järelevalvet teeb Andmekaitse Inspektsioon.
  - Allikas: https://www.riigiteataja.ee/akt/130062026052?leiaKehtiv
  - **Kontrollida:** Kehtiv redaktsioon on leitud (RT 130062026052), sätet pole veel loetud. Kontrolli järelevalve paragrahv.
- [ ] Vastutuse jaotus (`kes_vastutab`):
  - Vastutav töötleja (agenti kasutav organisatsioon): Vastutab rikkumise ja teatamise eest (GDPR art 33, 82).
  - Volitatud töötleja (agendi pakkuja): Vastutab, kui rikkus talle suunatud nõudeid või tegutses juhiste vastaselt (art 82 lg 2). Peab vastutavat töötlejat rikkumisest põhjendamatu viivituseta teavitama (art 33 lg 2).
- [ ] Teatamine (`kuhu_teatada`):
  - Andmekaitse Inspektsioon: Võimaluse korral 72 tunni jooksul pärast teada saamist. (https://www.aki.ee)

## Agent annab vale info, millele klient tugineb (`vale-info`)

- [ ] **Tarbijakaitseseadus (TKS)**, § 14–16 (ebaausad ja eksitavad kauplemisvõtted) (kehtib)
  - Väide: Keelab ebaausa kauplemisvõtte kasutamise (§ 14). Ebaaus on muu hulgas eksitav kauplemisvõte (§ 15, 16).
  - Allikas: https://www.riigiteataja.ee/akt/103072026030?leiaKehtiv
  - **Kontrollida:** Paragrahvide pealkirjad on kontrollitud kehtivast tekstist (RT 103072026030), sisu veel mitte.
- [ ] Vastutuse jaotus (`kes_vastutab`):
  - Agenti kasutav ettevõtja: Kliendi ees vastutab ettevõtja, kelle nimel agent suhtleb. Moffatti juhtumis ei saanud ettevõte vastutust vestlusrobotile lükata. Eesti kohtupraktikat ei leidnud.
  - AI-süsteemi pakkuja: Vastutab selle eest, et inimene saab teada, et suhtleb AI-ga (art 50 lg 1). Kui ettevõtja ehitab agendi ise, on ta ka pakkuja.
  - Agendi tarnija: Vastutab ettevõtja ees lepingu alusel.
- [ ] Teatamine (`kuhu_teatada`):
  - Tarbijakaitse ja Tehnilise Järelevalve Amet (TTJA): Kui kahju sai tarbija või puudub AI-märgistus. (https://ttja.ee/ariklient/ohutus/tooted-teenused/tehisintellektisusteemid)
  - Finantsinspektsioon: Kui vale info puudutas finantsteenust. (https://www.fi.ee)

## Juurutaja kontrollnimekiri

- [ ] Nimeta, kes otsustab intsidendist teatamise üle ja teatab (AKI 72 tunni jooksul, RIA 24 tunni jooksul, vajadusel Finantsinspektsioon). (https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [ ] Kui agent töötleb isikuandmeid, kasuta ainult tarnijat, kes annab piisava tagatise nõuetekohaseks töötlemiseks, ja sõlmi temaga GDPR art 28 kohane leping. (https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [ ] Kontrolli, et inimene saab teada, et suhtleb AI-ga. AI-määruse art 50 lg 1 on pakkuja kohustus. Kui ehitad agendi ise ja võtad selle kasutusele oma nime all, oled ise pakkuja (art 3 p 3). (https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [ ] Anna suure riskiga otsustes (nt töö, avalikud teenused) inimjärelevalve pädevale ja volitatud inimesele (AI-määrus art 26 lg 2; GDPR art 22). (https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [ ] Ära anna agendile oma maksevahendit ega isikustatud turvavolitusi ilma selge volituse ja piiranguteta. Kasutaja peab astuma kõik vajalikud sammud nende turvaliseks hoidmiseks (PSD2 art 69 lg 2). (https://eur-lex.europa.eu/eli/dir/2015/2366/oj)
