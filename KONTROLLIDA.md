# Kontrollimist vajavad väited

Genereeritud: 2026-10-20 (`python build.py --kontroll`).

Kui väide on esmaallikast üle vaadatud, pane stsenaariumile `kontrollitud: YYYY-MM-DD` ja eemalda normilt `kontrollida` väli.

## Taustanormid

- [ ] **Tehisintellekti määrus (EL) 2024/1689**, art 113 (kohaldamise algus) (kehtib)
  - Väide: Määrus jõustus 2024. aastal ja hakkab kohalduma etapiviisiliselt. Keelatud tavad kohalduvad alates 2.02.2025, üldotstarbelise AI mudelite reeglid alates 2.08.2025, läbipaistvuskohustused (art 50) alates 2.08.2026.
  - Allikas: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
  - **Kontrollida:** Kuupäevad art 113-st. Kas omnibus muutis ka art 50 kohaldamist.
- [ ] **AI vastutuse direktiivi ettepanek (COM(2022) 496)**, kogu ettepanek (tagasi_võetud)
  - Väide: Ettepanekut ei võetud kunagi vastu. Komisjon võttis selle tagasi, teade avaldati ELT-s 6.10.2025 (C/2025/5423). Põhjus: kokkulepet ei olnud näha. Komisjon hindab, kas esitada uus ettepanek. Praegu jääb lepinguväline vastutus riigisisese õiguse ja uue tootevastutuse direktiivi kanda.
  - Allikas: https://eur-lex.europa.eu/legal-content/ET/TXT/?uri=CELEX:52025XC05423
  - **Kontrollida:** ELT teade C/2025/5423 (6.10.2025) leitud veebiotsingu kaudu, teksti pole veel loetud (EUR-Lex blokeerib robotid).
- [ ] **Tootevastutuse direktiiv (EL) 2024/2853**, art 4 (toote mõiste), art 22 (ülevõtmine) (kohaldub_alates 2026-12-09)
  - Väide: Tarkvara, sh AI-süsteem, loetakse tooteks. Puudusega tootest tekkinud kahju eest vastutab tootja ka ilma süüta. Liikmesriigid peavad direktiivi üle võtma hiljemalt 9.12.2026.
  - Allikas: https://eur-lex.europa.eu/eli/dir/2024/2853/oj
  - **Kontrollida:** Artiklite numbrid (tarkvara kui toode, ülevõtmise tähtaeg).
- [ ] **Võlaõigusseaduse muutmise eelnõu (tootevastutus)**, VÕS tootevastutuse sätted (§ 1061 jj) (eelnõu)
  - Väide: Justiits- ja Digiministeerium on koostanud eelnõu uue tootevastutuse direktiivi ülevõtmiseks. Eesmärk on laiendada vastutavate ettevõtjate ringi ja hõlmata tarkvara.
  - Allikas: https://www.e-kaubanduseliit.ee/uudised/puudusega-toote-eest-vastutavate-ettevotjate-ring-laieneb
  - **Kontrollida:** Allikas on teisene. Leia eelnõu EIS-ist või Riigikogu lehelt, märgi eelnõu number ja menetlusetapp. Paragrahvide vahemik vajab kontrolli.

## Agent teeb kliendi nimel tehingu, mis läheb valesti (`tehing`)

- [ ] **Tsiviilseadustiku üldosa seadus (TsÜS)**, § 115 jj (esindus) (kehtib)
  - Väide: Esindaja teeb tehingu esindatava nimel ja see seob esindatavat, kui esindajal oli esindusõigus. Esindajaks saab olla isik. AI-agent ei ole isik.
  - Allikas: https://www.riigiteataja.ee/akt/131122024048
  - **Kontrollida:** Link viitab 1.01.2025 redaktsioonile, kontrolli kehtivat. Kontrolli § 115 ja § 129 (esindusõiguseta tehing) sõnastust.
- [ ] **Võlaõigusseadus (VÕS)**, § 103 (vastutus kohustuse rikkumise eest), § 115 (kahju hüvitamine) (kehtib)
  - Väide: Kui teenuse osutaja rikub lepingut (nt agent ei tee seda, mis kokku lepiti), vastutab ta kliendi ees lepingu alusel. Vastutusest vabaneb ta vaid siis, kui rikkumine on vabandatav.
  - Allikas: https://www.riigiteataja.ee/akt/V%C3%95S
  - **Kontrollida:** Paragrahvide numbrid on mälu järgi, kontrolli. URL on tuletatud Riigi Teataja lühendilingi mustrist (sama muster töötab KüTS-il).
- [ ] **Makseteenuste direktiiv (EL) 2015/2366 (PSD2)**, art 64 (nõusolek), art 69 (makse kasutaja kohustused), art 73 (volitamata makse), art 74 (makse kasutaja vastutus) (kehtib)
  - Väide: Makse on volitatud ainult siis, kui maksja on selleks nõusoleku andnud. Volitamata makse peab makseteenuse pakkuja üldjuhul tagastama. Makse kasutaja peab hoidma maksevahendit ja isikustatud turvaelemente turvaliselt ning teatama nende kaotusest või väärkasutusest viivitamata (art 69). Kui kasutaja rikkus neid kohustusi pettuse eesmärgil või raske hooletuse tõttu, kannab ta volitamata maksest tekkinud kahju ise (art 74).
  - Allikas: https://eur-lex.europa.eu/eli/dir/2015/2366/oj
  - **Kontrollida:** Artiklite numbrid ja art 69/74 sisu (lisatud v0.2 mälu järgi). Eesti ülevõttev säte (VÕS makseteenuste osa). Kas PSD3 / makseteenuste määrus on vahepeal vastu võetud.
- [ ] **Digitaalse tegevuskerksuse määrus (EL) 2022/2554 (DORA)**, art 19 (IKT-intsidendist teatamine) (kehtib)
  - Väide: Kui tehingut teeb finantsasutuse süsteem, kehtivad finantsasutusele IKT-riski ja intsidentidest teatamise nõuded.
  - Allikas: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
  - **Kontrollida:** Artikli number ja kas see stsenaarium üldse kuulub DORA alla.
- [ ] Vastutuse jaotus (`kes_vastutab`):
  - Agendi kasutaja (kelle nimel tehing tehti): Kolmanda isiku ees on lähtekoht, et agendi kaudu tehtud tehing seob kasutajat, sest agent on tema tööriist. Piirid on lahtised.
  - Agendi teenuse osutaja: Vastutab kasutaja ees lepingu alusel, kui agent ei toiminud nii, nagu lubati.
  - Makseteenuse pakkuja: Vastutab volitamata makse eest PSD2 reeglite järgi.
  - Kasutaja, kes andis agendile oma maksevahendi või sisselogimisandmed: See võib olla raske hooletus (PSD2 art 69 ja 74) ja kahju võib jääda kasutajale. Kontrollimata.
- [ ] Teatamine (`kuhu_teatada`):
  - Finantsinspektsioon: Kui tehing puudutab finantsteenust või makset. (https://www.fi.ee)
  - Tarbijakaitse ja Tehnilise Järelevalve Amet (TTJA): Kui kahju sai tarbija. (https://ttja.ee)

## Agent töötleb või lekitab isikuandmeid (`isikuandmed`)

- [ ] **Isikuandmete kaitse üldmäärus (EL) 2016/679 (GDPR)**, art 5, art 24, art 28 (kehtib)
  - Väide: Vastutav töötleja (agenti kasutav organisatsioon) vastutab töötlemise õiguspärasuse eest. Agendi pakkuja on tavaliselt volitatud töötleja ja vajab lepingut (art 28).
  - Allikas: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- [ ] **Isikuandmete kaitse üldmäärus (EL) 2016/679 (GDPR)**, art 33, art 34 (kehtib)
  - Väide: Isikuandmetega seotud rikkumisest tuleb teatada järelevalveasutusele põhjendamatu viivituseta ja võimaluse korral 72 tunni jooksul. Kui risk inimestele on suur, tuleb teavitada ka neid.
  - Allikas: https://www.edpb.europa.eu/sme/assess-the-risks/data-breaches_et
  - **Kontrollida:** Link on EDPB juhend, mitte määruse tekst. Lisa vajadusel ELT link.
- [ ] **Isikuandmete kaitse üldmäärus (EL) 2016/679 (GDPR)**, art 82 (kehtib)
  - Väide: Inimene, kes sai rikkumise tõttu kahju, võib nõuda hüvitist nii vastutavalt kui volitatud töötlejalt.
  - Allikas: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- [ ] **Isikuandmete kaitse seadus (IKS)**, üldsätted, järelevalve (kehtib)
  - Väide: Täpsustab GDPR-i rakendamist Eestis. Järelevalvet teeb Andmekaitse Inspektsioon.
  - Allikas: https://www.riigiteataja.ee/akt/IKS
  - **Kontrollida:** URL on tuletatud lühendilingi mustrist. Kontrolli, milline IKS-i säte on agendi stsenaariumi jaoks asjakohane.
- [ ] Vastutuse jaotus (`kes_vastutab`):
  - Vastutav töötleja (agenti kasutav organisatsioon): Vastutab rikkumise ja teatamise eest.
  - Volitatud töötleja (agendi pakkuja): Vastutab, kui rikkus oma kohustusi või tegutses juhiste vastaselt. Peab vastutavat töötlejat rikkumisest viivitamata teavitama.
- [ ] Teatamine (`kuhu_teatada`):
  - Andmekaitse Inspektsioon: Rikkumisest teadasaamisest 72 tunni jooksul. (https://www.aki.ee)

## Agent osaleb avaliku sektori otsuses (`avalik-sektor`)

- [ ] **Haldusmenetluse seaduse ja avaliku teabe seaduse muutmise seadus**, HMS § 7¹ (automaatne haldusmenetlus) (kohaldub_alates 2027-07-01)
  - Väide: Lubab haldusorganil anda haldusakti või teha toimingu automaatselt, ilma ametniku otsese osaluseta. Kui menetlusosaline kasutab ärakuulamisõigust, jätkub menetlus ametnikuga. Kohaldub menetlustele, mis algavad alates 1.07.2027.
  - Allikas: https://www.riigiteataja.ee/akt/109072026012
  - **Kontrollida:** Seaduse jõustumise säte (§ 3) jäi otsingus nägemata. Kontrolli kaalutlusotsuste piirang ja märgistamise nõue.
- [ ] **Riigivastutuse seadus (RVastS)**, § 7 (kehtib)
  - Väide: Avaliku võimu kandja peab hüvitama õigusvastase tegevusega tekitatud kahju. Eelduseks on muu hulgas, et esmased õiguskaitsevahendid (vaie, kaebus) on kasutatud.
  - Allikas: https://www.riigiteataja.ee/akt/RVastS
  - **Kontrollida:** URL on tuletatud lühendilingi mustrist. Tingimused pärinevad kohtulahendist.
- [ ] **Isikuandmete kaitse üldmäärus (EL) 2016/679 (GDPR)**, art 22 (kehtib)
  - Väide: Inimesel on õigus, et tema kohta ei tehtaks ainult automatiseeritud töötlusel põhinevat õiguslikku otsust, välja arvatud seaduses lubatud juhtudel ja kaitsemeetmetega.
  - Allikas: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- [ ] **Tehisintellekti määrus (EL) 2024/1689**, III lisa p 5, art 26, art 27 (kohaldub_alates 2027-12-02)
  - Väide: Avalike hüvitiste ja teenuste saamise hindamiseks kasutatav AI on suure riskiga. Avalik-õiguslikust juurutajast tuleb enne kasutamist teha põhiõiguste mõjuhinnang.
  - Allikas: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
  - **Kontrollida:** Kuupäev omnibusi järgi. Lisa punkti ja artiklite numbrid.
- [ ] Vastutuse jaotus (`kes_vastutab`):
  - Haldusorgan: Vastutab otsuse eest täielikult, sõltumata sellest, kas otsuse tegi ametnik või süsteem.
  - Süsteemi tarnija: Vastutab haldusorgani ees lepingu alusel. Kodaniku ees otse tavaliselt ei vastuta.
- [ ] Teatamine (`kuhu_teatada`):
  - Haldusorgan ise (vaie): Haldusakti vaidlustamise tähtaja jooksul. (https://www.riigiteataja.ee/akt/109072026012)
  - Õiguskantsler: Kui on kahtlus, et põhiõigusi rikuti. (https://www.oiguskantsler.ee)
  - Andmekaitse Inspektsioon: Kui rikuti GDPR art 22 õigusi. (https://www.aki.ee)

## Agent teeb tööalase otsuse inimese kohta (`too`)

- [ ] **Tehisintellekti määrus (EL) 2024/1689**, III lisa p 4, art 26 (kohaldub_alates 2027-12-02)
  - Väide: Värbamiseks, töötajate hindamiseks ja ülesannete jagamiseks kasutatav AI on suure riskiga. Tööandja kui juurutaja peab süsteemi kasutama juhendi järgi, tagama inimjärelevalve ja teavitama töötajaid.
  - Allikas: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
  - **Kontrollida:** Kuupäev omnibusi järgi. Art 26 lõiked (töötajate teavitamine).
- [ ] **Tehisintellekti määrus (EL) 2024/1689**, art 86 (kohaldub_alates 2027-12-02)
  - Väide: Inimesel, kelle kohta tehti suure riskiga AI väljundil põhinev otsus, on õigus saada juurutajalt selgitus AI rolli kohta otsuses.
  - Allikas: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
  - **Kontrollida:** Art 86 tekst ja kohaldumise kuupäev ei tulnud otsingus välja.
- [ ] **Isikuandmete kaitse üldmäärus (EL) 2016/679 (GDPR)**, art 22 (kehtib)
  - Väide: Ainult automatiseeritud otsus, millel on inimesele oluline mõju, on lubatud ainult erandjuhtudel ja inimesel on õigus nõuda inimese sekkumist.
  - Allikas: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- [ ] Vastutuse jaotus (`kes_vastutab`):
  - Tööandja (juurutaja): Vastutab otsuse ja selle põhjendamise eest kandidaadi või töötaja ees.
  - Süsteemi pakkuja: Vastutab suure riskiga süsteemi nõuetele vastavuse eest (andmed, dokumentatsioon, logimine).
- [ ] Teatamine (`kuhu_teatada`):
  - Andmekaitse Inspektsioon: Kui rikuti isikuandmete või art 22 õigusi. (https://www.aki.ee)
  - Soolise võrdõiguslikkuse ja võrdse kohtlemise volinik: Kui otsus võib olla diskrimineeriv. (https://www.volinik.ee)

## Agent tekitab turvaintsidendi (`turvaintsident`)

- [ ] **Küberturvalisuse seadus (KüTS)**, intsidendist teavitamine (kehtib)
  - Väide: NIS2 üle võttes laienes seadus 1.01.2026 umbes 3000 uuele ettevõttele ja asutusele. Olulistest intsidentidest tuleb teavitada Riigi Infosüsteemi Ametit.
  - Allikas: https://www.riigiteataja.ee/akt/130122025004
  - **Kontrollida:** Lisa paragrahvi number ja teavitamise tähtajad KüTS-i kehtivast tekstist. Seadusele lisandus muudatus, mis jõustus 1.10.2026, sisu teadmata.
- [ ] **NIS2 direktiiv (EL) 2022/2555**, art 23 (kehtib)
  - Väide: Olulisest intsidendist tuleb anda varajane hoiatus 24 tunni jooksul, teade 72 tunni jooksul ja lõpparuanne ühe kuu jooksul.
  - Allikas: https://eur-lex.europa.eu/eli/dir/2022/2555/oj
  - **Kontrollida:** Tähtajad on mälu järgi, kontrolli art 23 tekstist.
- [ ] **Küberkerksuse määrus (EL) 2024/2847 (CRA)**, art 14 (teavitamiskohustus) (kehtib)
  - Väide: Digitaalsete elementidega toodete (sh tarkvara) tootjad peavad teatama aktiivselt ära kasutatud haavatavustest ja tõsistest intsidentidest. Teavitamiskohustus kohaldub alates 11.09.2026, muud nõuded hiljem.
  - Allikas: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
  - **Kontrollida:** Artikli number ja kuupäevad on mälu järgi, kontrolli.
- [ ] Vastutuse jaotus (`kes_vastutab`):
  - Agenti kasutav organisatsioon: Kui on KüTS-i subjekt, vastutab riskijuhtimise ja teavitamise eest. Volituste andmine agendile on tema otsus.
  - Agendi või tööriista tootja: Vastutab CRA järgi turvanõuete ja haavatavustest teavitamise eest ning tootevastutuse kaudu puudusega toote eest.
- [ ] Teatamine (`kuhu_teatada`):
  - RIA / CERT-EE: KüTS-i subjektid NIS2 tähtaegade järgi. Teised vabatahtlikult. (https://www.ria.ee/uudised/uuest-aastast-laienes-kuberturvalisuse-seadus)
  - Andmekaitse Inspektsioon: Kui intsident puudutas isikuandmeid, 72 tunni jooksul. (https://www.aki.ee)

## Agent annab vale info, millele klient tugineb (`vale-info`)

- [ ] **Tehisintellekti määrus (EL) 2024/1689**, art 50 (kehtib)
  - Väide: Inimestega suhtlev AI-süsteem peab olema kujundatud nii, et inimene teab, et suhtleb AI-ga, kui see pole ilmne.
  - Allikas: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
  - **Kontrollida:** Kas art 50 lg 1 kohaldub alates 2.08.2026 muutmata kujul.
- [ ] **Võlaõigusseadus (VÕS)**, lepingueelsed kohustused ja lepingu rikkumine (kehtib)
  - Väide: Ettevõtja vastutab oma esindajate ja abiliste antud teabe eest. Agendi antud lubadus võib siduda ettevõtjat.
  - Allikas: https://www.riigiteataja.ee/akt/V%C3%95S
  - **Kontrollida:** Täpsed paragrahvid puuduvad, lisa need. URL on tuletatud lühendilingi mustrist.
- [ ] **Tootevastutuse direktiiv (EL) 2024/2853**, art 4, art 6 (kohaldub_alates 2026-12-09)
  - Väide: Kui vale info põhjustas tervisekahju või asja kahju, võib tarkvara tootja vastutada puudusega toote eest. Puhas varaline kahju ei ole direktiiviga kaetud.
  - Allikas: https://eur-lex.europa.eu/eli/dir/2024/2853/oj
  - **Kontrollida:** Artikli numbrid ja kahjuliikide loetelu.
- [ ] Vastutuse jaotus (`kes_vastutab`):
  - Agenti kasutav ettevõtja: Kliendi ees vastutab ettevõtja, kelle nimel agent suhtleb. Ta ei saa vastutust lükata agendile kui "eraldi üksusele".
  - Agendi tarnija: Vastutab ettevõtja ees lepingu alusel.
- [ ] Teatamine (`kuhu_teatada`):
  - Tarbijakaitse ja Tehnilise Järelevalve Amet (TTJA): Kui kahju sai tarbija või puudub AI-märgistus. (https://ttja.ee/ariklient/ohutus/tooted-teenused/tehisintellektisusteemid)
  - Finantsinspektsioon: Kui vale info puudutas finantsteenust. (https://www.fi.ee)

## Agent tegutseb inimese volitusel riigi e-teenustes (`e-teenused`)

- [ ] **Tsiviilseadustiku üldosa seadus (TsÜS)**, § 115 jj (esindus ja volitus) (kehtib)
  - Väide: Esindaja teeb tehingu esindatava nimel ja see seob esindatavat, kui esindajal oli esindusõigus. Volituse ulatus määrab, mida esindaja teha tohib. AI-agent ei ole isik.
  - Allikas: https://www.riigiteataja.ee/akt/131122024048
  - **Kontrollida:** Link viitab 1.01.2025 redaktsioonile, kontrolli kehtivat. Kas esinduse sätted kohalduvad avalik-õiguslikele toimingutele.
- [ ] **Maksukorralduse seadus (MKS)**, maksukohustuslase esindamine ja deklaratsiooni esitamine (kehtib)
  - Väide: Reguleerib maksudeklaratsiooni esitamist ja maksukohustuslase esindamist. Lähtekoht on, et maksukohustus jääb maksukohustuslasele ka siis, kui deklaratsiooni esitas esindaja.
  - Allikas: https://www.riigiteataja.ee/akt/MKS
  - **Kontrollida:** Väide ja säte on mälu järgi, paragrahvid puuduvad. URL on tuletatud lühendilingi mustrist. Kontrolli MKS-ist esinduse ja deklaratsiooni sätted.
- [ ] **eIDAS-määrus (EL) nr 910/2014, muudetud määrusega (EL) 2024/1183**, e-identimine, usaldusteenused, Euroopa digitaalse identiteedi rahakott (kehtib)
  - Väide: Reguleerib e-identimist ja usaldusteenuseid. Muudatus (EL) 2024/1183 lisab Euroopa digitaalse identiteedi rahakoti, mille liikmesriigid peavad kodanikele pakkuma.
  - Allikas: https://eur-lex.europa.eu/eli/reg/2014/910/oj
  - **Kontrollida:** Kas rahakott toetab volituste andmist (nt agendile) ja millal liikmesriigid peavad rahakoti pakkuma. Muutva määruse link: https://eur-lex.europa.eu/eli/reg/2024/1183/oj
- [ ] **Isikuandmete kaitse üldmäärus (EL) 2016/679 (GDPR)**, art 22 (kehtib)
  - Väide: Inimesel on õigus, et tema kohta ei tehtaks ainult automatiseeritud töötlusel põhinevat õiguslikku otsust, välja arvatud seaduses lubatud juhtudel ja kaitsemeetmetega.
  - Allikas: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- [ ] Vastutuse jaotus (`kes_vastutab`):
  - Volituse andja: Agendi kaudu tema nimel tehtud toimingud, nt esitatud deklaratsioon, on lähtekohana tema toimingud. Kontrollimata.
  - Agendi pakkuja: Vastutab volituse andja ees lepingu alusel, kui agent ei toiminud kokkulepitult.
  - Teenust osutav asutus: Vastutab oma e-teenuse ja otsuste eest. Kas ta peab kontrollima volituse ulatust iga toimingu juures, on lahtine.
- [ ] Teatamine (`kuhu_teatada`):
  - Teenust osutav asutus (nt Maksu- ja Tolliamet): Kohe, kui avastad vea, et seda parandada või toimingut tühistada. (https://www.emta.ee)
  - Riigi Infosüsteemi Amet (RIA): Kui volitust või e-identiteeti kuritarvitati. (https://www.ria.ee)
  - Politsei: Identiteedivarguse korral. (https://www.politsei.ee)

## Juurutaja kontrollnimekiri

- [ ] Nimeta, kes otsustab intsidendist teatamise üle ja teatab (AKI 72 tunni jooksul, RIA, Finantsinspektsioon). (https://www.edpb.europa.eu/sme/assess-the-risks/data-breaches_et)
- [ ] Kui agent töötleb isikuandmeid, sõlmi tarnijaga GDPR art 28 kohane leping. (https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [ ] Märgista, kui inimene suhtleb AI-ga (AI-määrus art 50). (https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [ ] Taga inimjärelevalve suure riskiga otsustes, nt töö ja avalikud teenused (AI-määrus art 26, GDPR art 22). (https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [ ] Ära anna agendile kasutaja maksevahendit ega sisselogimisandmeid ilma selge volituse ja piiranguteta (PSD2 art 69). (https://eur-lex.europa.eu/eli/dir/2015/2366/oj)
