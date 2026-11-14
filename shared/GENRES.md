# Genres — het wiel voor alle merken

Stand: 14 nov 2026. Beslissing Akke: "alles is zowat dezelfde stijl, het moet heel uiteenlopend zijn."
Dit bestand hoort bij `VARIATIE.md`. VARIATIE.md zegt *hoe vaak* er gewisseld wordt. Dit bestand zegt *waartussen*.

## 1. Waarom

Tot nu wisselden we de **layout** (tekst boven of onder, licht of donker, groot cijfer). Elk beeld bleef wel hetzelfde
**genre**: een kaart met merkfonts, een titel, een subtitel en het logo. Op een profielraster zie je dan negen keer "een kaart".

Een genre is een andere *wereld*: een kassabon, een bierviltje, een bovenaanzicht van een cafétafel, een krantenvoorpagina,
een polaroidmuur, een foto zonder één letter tekst. De huisstijl (kleuren, logo, toon, feitenregels) blijft. Het genre wisselt.

## 2. Regels voor elke weektaak, "Opnieuw maken" en "post op aanvraag"

1. **Elk item heeft een genre** uit §3 (of een nieuw genre, zie regel 7). Zet het in `content_tags.genre` en in `log.md`.
2. **Een week = zoveel verschillende genres als items.** Nooit twee keer hetzelfde genre in één week.
3. **Families**: per week hoogstens **2 items uit familie A (Kaart)**, de oude templates. Minstens 4 verschillende families per week.
4. **Minstens 1 item met een echt beeld** (familie D of E, of een object/scène rond een echte foto).
5. **Eén wildcard per week**: een genre dat dit merk nog nooit gebruikt heeft. Lukt het, dan komt het als template in `templates/g-<genre>.html`.
6. **Rotatie**: hetzelfde genre ten vroegste na 3 weken opnieuw bij hetzelfde merk, en dan met een ander onderwerp en een andere compositie.
7. **Nieuw genre bedenken mag altijd.** Voeg het toe aan §3 met een regel uitleg en, als het goed werkt, aan de lijst van het merk in §4.
8. **Feiten blijven heilig.** Een object of scène is vorm, nooit een excuus om iets te verzinnen. Een kassabon toont enkel
   bewezen claims, een ticket heeft geen verzonnen datum of prijs, een krantenkop is enkel echte lore. Geen nep-reviews, geen
   nep-chats van "klanten", geen documenten die voor echt kunnen doorgaan (geen echte spoorwegmaatschappij, geen paspoort, geen echte krantennaam).
9. **Fonts**: de merkfonts blijven de basis. Een genre mag **één accentfont** gebruiken dat bij het object hoort (handschrift op
   een servet, typemachine op een bon), enkel OFL en lokaal in `fonts/`. *(Voorstel, nog te bevestigen door Akke.)*
10. **Leren**: na 4 weken met genres kijkt de weektaak in `social_post_performance` welke genres per merk het best scoren
    (bereik, saves, profielbezoeken, klikken). Die krijgen meer kans (70/20/10 uit `LEREN.md`), maar regel 2 tot 6 blijven gelden.

## 3. De genrebank

### A. Kaart (de bestaande templates)
| Genre | Wat |
|---|---|
| `kaart-tip`, `kaart-cijfer`, `kaart-mythe`, `kaart-citaat` | wat we al hadden. Prima, maar max 2 per week. |

### B. Objecten uit het echte leven
Een herkenbaar ding, gefotografeerd of getekend van dichtbij, met de boodschap erop.
| Genre | Wat | Voorbeeld |
|---|---|---|
| `kassabon` | lange bon met regels en een totaal | SellQo: alles wat erin zit, "TOTAAL: 1 systeem" (gemaakt) |
| `ticket` | ticket, instapkaart, strookje | Loveke: liefdesticket Bratislava → Kyiv (gemaakt) |
| `bagagelabel` | label aan een touwtje met stempel | VanXcel: dag 80, Issyk Kul (gemaakt) |
| `bierviltje` | rond viltje met streepjes en notities | Fonske: 4 bars, 1 shot each (gemaakt) |
| `servet` | snelle schets op een servetje | Studio Akke: wireframe → live site (gemaakt) |
| `kalender` | muurkalender, dagen doorkruist | Studio Akke: werkdag 1 tot 14 (gemaakt) |
| `post-it` | één of meer briefjes op een scherm of koelkast | SellQo: de to-do van een ondernemer om 23 u |
| `etiket` | wasetiket, prijskaartje, verzendlabel | Loveke: wasetiket als liefdesbrief |
| `enveloppe` | brief, ansichtkaart, postzegel | VanXcel: kaartje uit Tbilisi; Loveke: liefdesbrief |
| `menukaart` | menu, krijtbord, prijslijst | SellQo: pakketten als "menu van de dag" (prijzen live) |
| `bordje` | deurbordje, uithangbord, "open/gesloten" | SellQo: "Gesloten. Online wel open." |
| `speelkaart` | ruilkaart, speelkaart met eigenschappen | Fonske: Leuven Lore-kaarten (Fonske, Margriet, de Totem) |
| `sticker-vel` | vel met stickers om af te pellen | Loveke: producten als stickers |
| `polsbandje` | festivalbandje, toegangsbandje | Fonske / SellQo Events |
| `visitekaartje` | kaartje met naam en mail | Studio Akke: jij@jouwzaak.be vs. jouwzaak123@… |
| `formulier` | papieren formulier, half ingevuld | Studio Akke: het onboardingformulier, met handschrift |
| `handleiding` | bouwinstructie met pictogrammen en stappen | VanXcel: accu aansluiten in 4 tekeningen |

### C. Scènes en POV
Een moment waarin het product gebruikt wordt, getekend of nagebouwd. De kijker zit erin.
| Genre | Wat | Voorbeeld |
|---|---|---|
| `pov-tafel` | bovenaanzicht van een tafel, hand met gsm | SellQo: "Tafel 7 wil nog 2 pintjes" (gemaakt) |
| `pov-toonbank` | over de schouder van de uitbater | SellQo: kassa + keukenscherm tegelijk |
| `pov-frituur` | puntzak, gsm met afhaaltijd | SellQo: afhalen met tijdsloten |
| `pov-deur` | inchecken aan de deur met een gsm | SellQo Events: QR-ticket scannen, ook door crew |
| `pov-werkbank` | bovenaanzicht werkbank, gereedschap, onderdelen | VanXcel: flat lay van een installatie |
| `pov-dashboard` | door de voorruit, met een overlay | VanXcel: echte foto's vanuit Sandy |
| `pov-bureau` | laptop, koffie, schermen | Studio Akke: de site op laptop en gsm tegelijk |
| `straatbeeld` | getekende gevel of winkelstraat | SellQo: de elf demowinkels als etalages in één straat |

### D. Rauw beeld
| Genre | Wat |
|---|---|
| `foto-puur` | één echte foto, geen tekst, geen kader, geen logo. De caption doet het werk. |
| `foto-1-regel` | echte foto met één kleine regel tekst in een hoek |
| `foto-detail` | extreme close-up: een connector, een stiksel, een polsbandje, een scherm |
| `foto-reeks` | carrousel van 6 tot 10 echte foto's, als een fotoboek, zonder ontwerp |
| `schermafbeelding` | een echte screenshot (demowinkel, portfolio), groot, met een pijl of omcirkeling |

### E. Collage
| Genre | Wat | Voorbeeld |
|---|---|---|
| `polaroids` | polaroids op kurk met punaises | VanXcel: Kyrgyzstan (gemaakt) |
| `scrapbook` | kraftpapier, tape, handgeschreven pijlen | Loveke: strip → hoodie (gemaakt) |
| `fotostrip` | vier vakjes zoals een fotohokje | Fonske: Crawl Log-foto's |
| `moodboard` | stalen, kleuren, schetsen naast elkaar | Studio Akke: van moodboard naar site |
| `stempelkaart` | stempels van plaatsen op een kaart | VanXcel: 17 landen als stempels (geen paspoort) |

### F. Typografie extreem
| Genre | Wat | Voorbeeld |
|---|---|---|
| `mega-woord` | één woord of cijfer zo groot dat het van het beeld valt | Studio Akke: 404 (gemaakt) |
| `fluister` | één kleine zin in een lege vlakte | elk merk, voor een stille, sterke zin |
| `poster` | concertaffiche of tourshirt met een lijst | Fonske: "Leuven Tour" met bar 1 tot 4 en de finale |
| `krantenkop` | voorpagina met kop, intro en kaderstukjes | Fonske: "Murder by the Dijle", 1225 (gemaakt) |
| `terminal` | commandoregel, code, log | Studio Akke / SellQo buildlog |
| `typemachine` | getypte brief, met doorhalingen | Loveke: een liefdesbrief aan een trui |

### G. Data en kaarten
| Genre | Wat | Voorbeeld |
|---|---|---|
| `routekaart` | de route als lijn, met pinnen | VanXcel: 17 landen; Fonske: getekende schatkaart (zonder cafénamen) |
| `metrokaart` | een systeem als metrolijnen | VanXcel: zon, dynamo en walstroom komen samen in de 5-in-1 |
| `ware-grootte` | iets op echte schaal tonen | VanXcel: doorsnede 35 vs. 50 mm² op ware grootte |
| `tijdlijn` | van A naar B in stappen | SellQo: een bestelling van mandje tot bol.com |
| `grafiek` | één simpele grafiek met een bron | Studio Akke Insights; enkel met echte cijfers |

### H. Spel en interactie
| Genre | Wat | Voorbeeld |
|---|---|---|
| `zoek-de-fout` | iets klopt niet, antwoord in caption of story | VanXcel: zekering te ver van de accu (gemaakt) |
| `raad-het` | wazig of ingezoomd, antwoord op de volgende slide | Studio Akke: welke sector is deze site? |
| `vul-in` | lege tekstballon of lege regel | Loveke: wat zegt hij in dit stripvakje? |
| `dit-of-dat` | twee keuzes, stem in de comments | elk merk |
| `bingo` | bingokaart met herkenbare situaties | SellQo: ondernemersbingo; VanXcel: vanbuild-bingo |
| `quiz-carrousel` | vraag, swipe, antwoord | elk merk |

### I. Humor
| Genre | Wat | Voorbeeld |
|---|---|---|
| `verwachting-realiteit` | twee panelen | SellQo: webshop vs. alles errond (gemaakt) |
| `profiel` | datingprofiel of "over mij" van een product | Loveke: Classic Hoodie zoekt iemand om te knuffelen |
| `pov-dier` | het verhaal verteld door de kat | VanXcel: de kitten uit Kyrgyzstan (enkel echte foto's) |
| `wanted` / `gezocht` | gezocht-affiche | Fonske: "Wanted: crawlers. Last seen at The Totem, 21:00" |
| `verloren-gevonden` | briefje aan een paal | Fonske: "Lost your group?" |

### J. Docu en proces
| Genre | Wat |
|---|---|
| `achter-de-schermen` | hoe iets gemaakt wordt: een echte foto of schermopname |
| `voor-na` | zelfde ding vroeger en nu (productfoto met de gratis fotobewerker, oude vs. nieuwe site) |
| `dagboek` | handgeschreven notitie van Akke ("dag 3 van de mailmodule"), enkel feiten uit de changelog |
| `fout-van-de-week` | wat er misliep en wat we leerden |

### K. Seizoen en moment
| Genre | Wat |
|---|---|
| `kalendermoment` | Valentijn (Loveke), examens (Fonske), winter en vorst (VanXcel), eindejaar en btw (SellQo), nieuwjaar (Studio Akke) |
| `weerbericht` | weerkaart als drager van een tip ("−5 °C vannacht: zo laad je een LiFePO4"), enkel met bron |

## 4. Per merk: de eerste 15 om uit te kiezen

Elk idee hieronder is een startpunt. De feiten komen altijd uit de bible, SellQo of de site.

### SellQo (Nederlands)
1. `pov-tafel`: tafel 7, twee pintjes, QR aan tafel, keukenscherm *(gemaakt)*
2. `kassabon`: wat er in één systeem zit, "kosten per bestelling €0,00" *(gemaakt)*
3. `verwachting-realiteit`: webshop vs. facturen, OSS, voorraad, bol.com *(gemaakt)*
4. `pov-frituur`: puntzak op de toonbank, gsm met "afhalen 18:30" (tijdsloten)
5. `pov-deur`: event, polsbandje, crewlid scant een QR-ticket met de gsm
6. `menukaart`: de pakketten als krijtbord "menu van de dag" (prijzen live uit `pricing_plans`, excl. btw)
7. `bordje`: deurbordje "Gesloten. De webshop is wel open."
8. `straatbeeld`: de elf demowinkels als etalages in één getekende straat → sellqo.app/voorbeelden
9. `tijdlijn`: één bestelling als lopende band: mandje → betaling → factuur → kassa → bol.com
10. `voor-na`: productfoto voor en na de gratis fotobewerker
11. `bingo`: ondernemersbingo ("Excel met 14 tabbladen", "factuur om middernacht")
12. `dagboek`: Akke's notitieboek met één changelog-regel van die week
13. `terminal`: een buildlog als commandoregel
14. `mega-woord`: "€0" per bestelling, over het hele beeld
15. `foto-puur`: een echte foto van één van onze eigen zaken (VanXcel-pakje, Loveke-hoodie), caption "draait op SellQo"

### VanXcel (Engels)
1. `bagagelabel`: dag 80, Issyk Kul *(gemaakt)*
2. `zoek-de-fout`: zekering te ver van de accu *(gemaakt)*
3. `polaroids`: Kyrgyzstan, waar de kitten instapte *(gemaakt)*
4. `metrokaart`: zon, dynamo en walstroom komen samen in de 5-in-1 converter
5. `ware-grootte`: kabeldoorsnede 35 vs. 50 mm² op echte schaal ("hold your cable against your screen")
6. `handleiding`: accu aansluiten in vier pictogrammen, laatste stap "let a certified electrician check 230V"
7. `pov-dashboard`: echte foto door de voorruit, met één regel
8. `pov-dier`: de reis volgens de kat, enkel foto's met tag `cat`
9. `stempelkaart`: 17 landen als stempels op een kaart
10. `enveloppe`: ansichtkaart uit Tbilisi, achterkant met een tip
11. `pov-werkbank`: flat lay van de vrijstaande producten
12. `weerbericht`: vorst en LiFePO4 (bron: de site)
13. `foto-puur`: Sandy aan de rivier, geen tekst
14. `bingo`: vanbuild-bingo
15. `krantenkop`: "Mongolia: 70 km away. Road closed." (echte reden uit de bible)

### Studio Akke (Nederlands, ik-vorm)
1. `servet`: van schets naar live *(gemaakt)*
2. `mega-woord`: 404 *(gemaakt)*
3. `kalender`: werkdag 1 tot 14 *(gemaakt)*
4. `visitekaartje`: jij@jouwzaak.be naast een gratis mailadres (Mail bij je domein)
5. `formulier`: het onboardingformulier, half ingevuld in handschrift
6. `pov-bureau`: dezelfde site op laptop en gsm
7. `raad-het`: ingezoomd stukje van een portfoliosite, swipe voor de sector
8. `moodboard`: kleuren en fonts → de site
9. `terminal`: `git push` → live, met de echte stappen
10. `menukaart`: pakketten als koffiekaart (prijzen excl. btw uit de site)
11. `bouwwerf`: site achter werfhekken, vier stappen (ook als reel)
12. `schermafbeelding`: één portfoliosite groot, met één omcirkeld detail
13. `fluister`: "Een website hoeft geen maanden te duren."
14. `voor-na`: oude vs. nieuwe site (enkel met toestemming van de klant)
15. `krantenkop`: "Lokale zaak eindelijk vindbaar" als knipoog, zonder echte klantnaam

### The Fonske Crawl (Engels)
1. `bierviltje`: 4 bars, 1 shot each *(gemaakt)*
2. `krantenkop`: Murder by the Dijle, 1225 *(gemaakt)*
3. `speelkaart`: Leuven Lore-kaarten (Fonske, Margriet, The Totem)
4. `wanted`: "Wanted: crawlers. Last seen at The Totem, 21:00"
5. `poster`: Leuven Tour-shirt met Bar 1 tot 4 en de Oude Markt als finale (zonder cafénamen)
6. `routekaart`: schatkaart van Leuven met een X op de Oude Markt
7. `fotostrip`: vier Crawl Log-foto's als fotohokje (enkel gepubliceerde avonden)
8. `polsbandje`: close-up getekend bandje "18+ · ID"
9. `verloren-gevonden`: "Lost your group? Found: The Totem, 21:00"
10. `foto-detail`: een glas alcoholvrij naast een shot ("alcohol-free on request")
11. `ticket`: scheurstrookje "Admit one crawler" (datum en prijs live, of weg)
12. `kalendermoment`: examens voorbij, eerste week van het semester
13. `straatbeeld`: Oude Markt bij nacht, getekend
14. `foto-puur`: de groep aan de Totem
15. `fluister`: "The longest bar in Europe."

### Loveke (Nederlands)
1. `ticket`: liefdesticket Bratislava → Kyiv *(gemaakt)*
2. `scrapbook`: van strip naar hoodie *(gemaakt)*
3. `etiket`: wasetiket met een liefdesbrief in plaats van wasvoorschriften
4. `enveloppe`: liefdesbrief met Loveke-postzegel
5. `vul-in`: stripvakje met lege tekstballon
6. `profiel`: datingprofiel van de Classic Hoodie (feiten uit de productomschrijving)
7. `sticker-vel`: de producten als stickers om af te pellen
8. `typemachine`: getypte brief "Lieve hoodie…"
9. `kalendermoment`: Valentijn (Loveke for Two)
10. `verzendlabel`: pakje met "gemaakt op bestelling, 5 tot 20 werkdagen"
11. `foto-puur`: een echte foto van Akke en Nastya in Loveke (als ze er één geven)
12. `dit-of-dat`: hoodie of sweatshirt?
13. `fotostrip`: vier stripvakjes als fotohokje
14. `mega-woord`: "SAMEN" over het hele beeld, met Loveke for Two (−7% vanaf 2 stuks)
15. `moodboard`: stof, kleuren en strip naast elkaar

## 5. Reels: 20 formats

Per week één reel per merk, nooit twee weken na elkaar hetzelfde format. Muziek en geluid: zie `MUZIEK.md`.

| Format | Wat | Voorbeeld |
|---|---|---|
| `tijdreis` | honderden echte foto's op volgorde, één per halve tel, met een teller | VanXcel: 126 dagen in 19 seconden (`brands/vanxcel/templates/reel-tijdreis/`, gemaakt) |
| `rauwe-clip` | één echte clip, één regel tekst, verder niets | VanXcel `clips/`, Fonske `crawl_media` |
| `ping` | geluid draagt alles: bestelling komt binnen, ping, bon print | SellQo horeca (met SFX) |
| `pov-tik` | duim tikt een bestelling op een gsm, close-up | SellQo: "2 pintjes" in 3 tikken |
| `kaart-tekent` | route tekent zichzelf, pinnen ploppen op de beat | Fonske, VanXcel |
| `parallax` | stripvakje in 2.5D: lagen bewegen, inzoomen, onthulling | Loveke |
| `bouwwerf` | site bouwt zich op in vier stappen, als timelapse | Studio Akke |
| `scroll` | trage scroll door een echte site of demowinkel | Studio Akke, SellQo |
| `stop-motion` | producten schuiven frame per frame in beeld | VanXcel, Loveke |
| `kinetisch` | woorden vallen binnen op de beat, niets anders | elk merk, voor één sterke zin |
| `aftellen` | 3, 2, 1 met per tel een feit | Fonske: 3 dingen voor je eerste crawl |
| `quiz` | vraag, 3 s denken, antwoord, met tik-tak geluid | VanXcel: welke kabeldikte? |
| `split` | links vroeger, rechts nu, tegelijk | SellQo: drie systemen vs. één |
| `kaartflip` | speelkaarten draaien om, één per tel | Fonske: Leuven Lore |
| `fotohokje` | vier foto's flitsen met een camerageluid | Fonske, Loveke |
| `bon-print` | bon rolt uit de printer, regel per regel | SellQo kassabon in beweging |
| `zoom-uit` | start op een detail, zoom uit tot het hele verhaal | Loveke strip, VanXcel polaroidmuur |
| `glitch` | 404, schermfout, dan de oplossing | Studio Akke |
| `slot` | gokautomaat draait, stopt op een land, foto van dat land | VanXcel |
| `dag-in-het-leven` | een dag van een bestelling of van een crawl, in uren | SellQo, Fonske |

## 6. Wat Akke kan aanleveren (maakt het meteen echter)

Niet nodig om te starten. Het meeste kan met wat al in de repo's zit.

- 5 à 10 korte gsm-clips van 5 tot 10 s: een product in je hand, een pakje inpakken, je scherm bij een binnenkomende bestelling, Sandy starten.
- Eén A4 met je eigen handschrift (alfabet + een paar woorden): dan wordt het een echt font voor `servet`, `dagboek` en `formulier`.
- Fonske: na elke crawl 3 clips in "Content · private".
- Loveke: één foto van jullie samen in Loveke, als jullie dat willen.
