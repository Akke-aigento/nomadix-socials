# SellQo Instagram — log

Wat er gepost is, per week (maandag). Lees dit vóór je een nieuwe week maakt: geen onderwerp, scène of changelog-item herhalen.

## Week van 2026-11-09

Gemaakt op 08-11 door de weektaak. Instagram **gekoppeld**: alle 7 items `pending_approval` (geen stickers deze week; de drie reels met bibliotheeknummer gaan na "Week goedkeuren" vanzelf online).
**Drie reels** (Akke, 01-11): do-avond op het sterkste slot, di-middag en za-ochtend, elk een ander format en nummer; ze nemen de plaats van de story di en de story za in. Geen vierde reel (geen aparte release-reel nodig: de changelog-items zitten in de reels zelf).
LinkedIn-versies (1200×1200) in `published/2026-11-09/linkedin/`. Meetdata: 13 posts, bereik 0–6, geen signalen van Akke, `lessen.md` leeg.
Toegepast uit de data (nog geen les in `lessen.md`): de drie carrousels (wo-avond, cta `opslaan`) halen score_48h 100, 120 en 50, gemiddeld 90 tegen ±40 voor de rest → carrousel weer wo-avond met cta `opslaan`, als enige `exploit`. Bij dit bereik (4–6 accounts) blijft het een zwak signaal.
Geen eigen links in captions (overal "link in bio"), dus geen UTM nodig. Geen prijzen in beeld of caption (enkel demoprijzen op de menukaart van Pizzeria Fiamma).

| Dag + uur | Wat | Pijler | Onderwerp | Format / template | Hook | Licht/donker | Bron |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ma 09/11 07:40 — vóór de zaak opengaat | post | Feature | "Je kaart op papier. In je eigen kleuren.": A5-boekje van Pizzeria Fiamma (kaft + binnenkant met allergeennummers en QR) | beeld-eerst / feature-print (nieuw) | belofte | licht (crème) | changelog 2026.15k `menu_card_print` |
| di 10/11 12:35 — lunch, het moment uit de reel zelf | reel (23,6 s, Kassa Groove) | Feature | "12:05. Het begint te regenen.": Nu-paneel → terras dicht, QR-menu op het terras gesloten, keuken pauzeren (dranken blijven), dagschotel | reel-ui / reel-tegels (nieuw) | verhaal | donker, lichte eindkaart | changelog 2026.15g `now_panel`, `zone_closed`, `daily_special`, 2026.15h `kitchen_pause_drinks` |
| wo 11/11 12:15 — lunch, ander piekmoment dan de carrousel | story | Bewijs | "Jouw zaak als demowinkel.": 3 stappen (menukaart sturen → wij bouwen → rondklikken en pas daarna beslissen) | lijst / story-steps (nieuw) | statement | licht (crème + koraal) | landing.examples.own_* |
| wo 11/11 20:55 — na sluiting, administratietijd (bewaren) | carrousel (6) | Ondernemerstips | "€10.000. Daarboven verandert de btw op je factuur.": afstandsverkopen aan particulieren in de EU, drempel, btw van de klant, OSS, "vraag je boekhouder" | tip / tip-bigcijfer (nieuw) + tip-step + cta-dark | cijfer | donker + licht | EU-btw-regels e-commerce sinds 1-7-2021; landing.core.invoices_text |
| do 12/11 21:20 — sterkste slot (avond) | reel (23,8 s, Focus) | Feature | "Het internet valt weg.": kassa-noodmodus op het hoofdtoestel (30 s, aantikken + bon op scherm, afrekenen contant/terminal/QR, in volgorde terug) | reel-vraag / reel-vraag (nieuw) | vraag | licht, donkere eindkaart | changelog 2026.15q `kassa_noodmodus_1` |
| vr 13/11 17:35 **(test)** — einde werkdag, pendel naar huis; nog nooit geprobeerd | post | Build in public | "Vier plekken. Eén logo.": voor/na van logo op website, mails, facturen, kassabon (Atelier Nord) | voor-na / buildlog-voorna (nieuw) | contrast | donker | changelog 2026.15d `branding_one_place` |
| za 14/11 09:10 — zaterdag kort en vroeg | reel (23,5 s, Open Voor Zaken) | Ondernemerstips (seizoen) | "POV: Black Friday" (vr 27/11): je kortingscode klaarzetten, 4 vinkjes (kleine letters, tot 23:59, één keer per klant, enkel bepaalde producten) | reel-lijst / reel-lijst (nieuw) | pov | fel (koraal), donkere eindkaart | landing.core.promos_*; changelog `discount_code_case_insensitive`, `discount_dates_scope`, `discount_once_per_customer`, `cart_discount_totals` |

Labels (`content_tags`), alle `bucket: explore` behalve wo-carrousel (`exploit`) en vr (`test`, `experiment: tijd`):
ma `feature/beeld-eerst/feature-print/belofte/kort/link` · di `feature/reel-ui/reel-tegels/verhaal/middel/link` · wo-story `bewijs/lijst/story-steps/statement/kort/profiel` ·
wo `tips/tip/tip-step/cijfer/lang/opslaan` · do `feature/reel-vraag/reel-vraag/vraag/lang/delen` · vr `build/voor-na/buildlog-voorna/contrast/middel/link` · za `tips/reel-lijst/reel-lijst/pov/kort/opslaan`.

Gebruikte changelog-items: `menu_card_print`, `now_panel`, `zone_closed`, `daily_special`, `kitchen_pause_drinks`, `kassa_noodmodus_1`, `branding_one_place`, `discount_code_case_insensitive`, `discount_dates_scope`, `discount_once_per_customer`, `cart_discount_totals`.
Gebruikte scènes: menukaart-boekje (Pizzeria Fiamma), Nu-paneel + QR-menu terras/keuken/dagschotel (Fiamma, "Calzone della casa"), kassa-noodmodus (Fiamma, tafel 4/7), branding voor/na (Atelier Nord), kortingscode VRIJDAG20. Geen foto's gebruikt.
Muziek: di Kassa Groove (122 BPM, 8 tellen = 3,934 s), do Focus (85 BPM, 6 tellen = 4,235 s), za Open Voor Zaken (116 BPM, 8 tellen = 4,138 s); alle drie start 0 s.
Nog niet gebruikt: `table_together` (samen bestellen aan tafel, één mandje), `kassa_offline_state`, `my_business_settings` + `settings_search` ("tik fooi"), `opening_hours` + `website_horeca` + `horeca_themes`, `qr_menu_allergen_filter`, `qr_order_progress`, `qr_staff_call`, `allergens_declared`, `dining_courses` (gangen), `kassa_staff_hours`, `kaart_food_cost`, `kassa_z_to_odoo`, `horeca_reports_admin`, `addon_self_serve`, `printful_auto_forward`, `photo_order`, barscherm, bonprinters, demowinkels (/voorbeelden, elf winkels), overstappen, prijzen per plan.
Bewust niet: `social_ai_post_proposal` ("Post met AI"): social planning is geen klantfeature volgens README/bible.

## Week van 2026-11-02

Gemaakt op 01-11 door de weektaak. Instagram **gekoppeld**: posts, carrousel, story di en reel `pending_approval` (reel met bibliotheeknummer, gaat na "Week goedkeuren" vanzelf online); poll-story za `manual` + `sticker`.
LinkedIn-versies (1200×1200) in `published/2026-11-02/linkedin/`. Meetdata (8 posts, bereik 0–6): te weinig voor een les, dus alles `explore` + één testslot.
Toegepast uit de data (nog geen les, <3 posts): de twee avondcarrousels (wo 20:40 en 21:15) scoorden het hoogst (score_48h 100 en 120) → carrousel en reel weer 's avonds. Geen signalen van Akke in social_post_events. `lessen.md` is nog leeg.
Geen eigen links in captions (overal "link in bio"), dus geen UTM nodig. Geen prijzen in beeld of caption (Events Flex: "vaste kost per betaald ticket", bedrag op /pricing).

| Dag + uur | Wat | Pijler | Onderwerp | Format / template | Hook | Licht/donker | Bron |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ma 02/11 08:10 — vóór de zaak opengaat (café's/horeca) | post | Feature | "Bompa Ré zit altijd aan het raam. Nu ook op je zaalplan.": vaste klant op het zaalplan, rekening op naam | ui-scene / feature-zaalplan (nieuw) | verhaal | licht (crème) | changelog 2026.14o `regulars_1` |
| di 03/11 12:25 — lunch, rustig moment | story | Bewijs | "Deze pub crawl verkoopt zijn tickets op SellQo.": echte foto Fonske Crawl 24/10 (regen, groep van achteren, fonske 0eb2b9b0) | beeld-eerst / story-photo (nieuw) | statement | donker + foto | landing.running.fonske |
| wo 04/11 20:50 — na sluiting, administratietijd (bewaren) | carrousel (6) | Ondernemerstips | "Je eerste tickets online verkopen? Check deze 4 dingen." (datums, tickettypes/early bird, plaatsen, scannen) + SellQo-slide | checklist / tip-cover + check-step (nieuw) + cta-dark | belofte | donker + licht | landing.sectors.events, faq events |
| do 05/11 21:10 — sterkste slot (avond) | reel (20,8 s, muziek Knipoog) | Feature | "POV: vrijdag 17 uur, iemand wil een tafel voor 6": Reserveren → aanvraag oranje → bevestigen + mail → tafel paars (Pizzeria Fiamma, Sam) | reel-pov / reel-pov (nieuw) | pov | licht, donkere eindkaart | changelog 2026.14p `reservations_online`, 2026.14n `reservations_1`, landing.scene.horeca |
| vr 06/11 06:50 **(test)** — vóór het venster, nog nooit geprobeerd (vroege vogels) | post | Build in public | "Geen rapport zoeken. Gewoon vragen.": de assistent kent je cijfers (omzet, winst, lijst zonder foto, CSV) | typografisch / buildlog-chat (nieuw) | contrast | donker | changelog 2026.14t `ai_agent_2` |
| za 07/11 09:05 — zaterdag kort en vroeg | story + poll-sticker | Samen | "Wanneer doe jij je administratie?" (Vroeg / Middag / Na sluiting / Zondag) | poll / poll-story (typografische variant) | vraag | licht (crème + koraal) | geen claim; helpt bij POSTTIJDEN |

Labels (`content_tags`), alle `bucket: explore` behalve vr (`test`, `experiment: tijd`):
ma `feature/ui-scene/feature-zaalplan/verhaal/middel/link` · di `bewijs/foto/story-photo/statement/kort/profiel` (people ja) · wo `tips/checklist/check-step/belofte/lang/opslaan` ·
do `feature/reel-pov/reel-pov/pov/middel/link` · vr `build/typografisch/buildlog-chat/contrast/lang/link` · za `samen/poll/poll-story/vraag/kort/reageren`.

Gebruikte changelog-items: `regulars_1`, `reservations_online`, `reservations_1`, `ai_agent_2`. Gebruikte scènes: zaalplan + rekening op naam (Bompa Ré, Jef), reservatie (Pizzeria Fiamma, Sam), events-checklist. Gebruikt beeld: `fonske/photos/2026-10-24/0eb2b9b0…jpg`.
Muziek reel: Knipoog (ElevenLabs, 104 BPM, start 0 s, scènes van 6 tellen = 3,46 s).
In SellQo gezet op 01-11: 6 rijen (5× `pending_approval`, za `manual` + `sticker`), recepten via net.http_get (md5 gecontroleerd), uurcontrole zonder dubbels, melding `social_posts_ready` verstuurd.
Nog niet gebruikt: `addon_self_serve` (zelf een spoor aanzetten), `printful_auto_forward`, `photo_order`, kassa-snel-tikken (14h/j/m), barscherm (14i), bonprinters (14d), QR-tafelrekening online betalen (14a), keukenscherm, demowinkels (/voorbeelden), "jouw zaak als voorbeeld", overstappen uit Shopify/WooCommerce, prijzen per plan.

## Week van 2026-10-19

Gemaakt op 18-10 door de weektaak (vóór de week van 26-10, die er al stond). Instagram **gekoppeld** (@sellqo.app, sinds 17-10):
posts en carrousel `pending_approval`, story di `story` + `pending_approval`, poll-story en reel `manual` (sticker / music).
LinkedIn-versies (1200×1200) in `published/2026-10-19/linkedin/`. Nog geen meetdata (`social_post_performance` leeg, geen signalen):
alles `explore`, één testslot. Geen eigen links in captions (overal "link in bio"), dus geen UTM nodig deze week.
Bewust **geen prijzen**: pakketten en limieten wijzigden deze week (changelog 2026.12q/t; Free nu 10 producten/20 bestellingen, Events Flex €0,69) → eerst Akke (bible §9).

| Dag + uur | Wat | Pijler | Onderwerp | Format / template | Hook | Licht/donker | Bron |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ma 19/10 07:50 — vóór de zaak opengaat | post | Feature | "Verkocht aan de kassa. Ook weg uit je webshop.": kassabon + webshopkaart, één voorraad (Atelier Nord, Mok Fjord) | ui-scene / feature-split (nieuw) | belofte | licht (crème) | landing.core.pos_text, faq kassa |
| di 20/10 12:20 — lunch, rustig moment | story | Bewijs | "Onze eigen webshop. Ons eigen platform.": echte schermafbeelding vanxcel.be | beeld-eerst / story-screenshot (nieuw) | statement | donker + foto | landing.running.vanxcel, core.orders_text |
| wo 21/10 20:40 — na sluiting, administratietijd (bewaren) | carrousel (6) | Ondernemerstips | "Overstappen: 4 dingen die niet kloppen" (producten opnieuw intikken, geld bij het platform, weken werk, gegevens kwijt) | mythe-feit / tip-cover + myth-fact (nieuw) + cta-dark | contrast | donker + licht | landing.faq (overzetten, betaalmethoden, gegevens), core.shop_text, hero.trust |
| do 22/10 21:05 — sterkste slot (avond) | reel (15 s, stil) | Feature | "Van ticket tot deur. 3 stappen.": kopen → QR per mail → scannen met je gsm (Leuven Pub Crawl) | reel-tekst (3 stappen, nieuw t.o.v. flow) / reel-steps | cijfer | licht, donkere eindkaart | landing.sectors.events, landing.scene.events |
| vr 23/10 14:50 **(test)** — horecadal tussen lunch- en avondservice | post | Build in public | "Diavola op? Eén tik. Overal.": per gerecht waar te bestellen + "Op voor vandaag" | achter-de-schermen / buildlog-ui (variant) | verhaal | donker | changelog 2026.12r `horeca_channels`, labels nl.json admin.storefront.food |
| za 24/10 09:15 — zaterdag kort en vroeg | story + poll-sticker | Samen | "Waar gaat jouw tijd naartoe?" (Facturen / Voorraad / Bestellingen / Social media) | poll / poll-fel (nieuw, koraal, typografisch) | vraag | fel (koraal) | geen claim |

Labels (`content_tags`), allemaal `bucket: explore` behalve vr (`test`, `experiment: tijd`):
ma `feature/ui-scene/feature-split/belofte/kort/link` · di `bewijs/screenshot/story-screenshot/statement/kort/profiel` · wo `tips/mythe-feit/myth-fact/contrast/lang/opslaan` ·
do `feature/reel-tekst/reel-steps/cijfer/middel/link` · vr `build/achter-de-schermen/buildlog-ui/verhaal/lang/link` · za `samen/poll/poll-fel/vraag/kort/reageren`.

Gebruikte changelog-items: `horeca_channels`. Gebruikte scènes: retail-kassa (Atelier Nord), events (Leuven Pub Crawl), horeca-gerecht (Pizzeria Fiamma, Diavola). Gebruikt beeld: `studio-akke/media/site-vanxcel.jpg`.
Muziek reel (SocialPilot, 12–25 okt 2026, niet herhalen): Rikas – Last Train to London, Andrea Vanzo – Autumn Journey, Adrián Berenguer – October.
Nog niet gebruikt: keukenscherm (Fiamma), deurscanner bij slecht bereik, zaalplannen, combitickets/munten, demowinkels (/voorbeelden), "jouw zaak als voorbeeld", homepage-secties, opgeruimde zijbalk.

## Week van 2026-10-26 (eerste week)

Instagram niet gekoppeld: alles op `manual` in SellQo (Akke post zelf). LinkedIn-versies (1200×1200) in `published/2026-10-26/linkedin/`.

| Dag | Wat | Pijler | Onderwerp | Template | Bron |
| --- | --- | --- | --- | --- | --- |
| ma 26/10 18:00 | post | Feature | "Eén bestelling. Drie dingen geregeld.": bestelling, factuur, voorraad (demowinkel Atelier Nord, Mok Fjord) | feature | landing.scene.retail, landing.core |
| di 27/10 18:05 | story | Build in public | "Gebouwd in Oud-Heverlee. Getest op onze eigen zaken.": VanXcel, Fonske Crawl, Loveke | story-dark | landing.facts, landing.running |
| wo 28/10 12:00 | carrousel (6) | Ondernemerstips | "Peppol in 60 seconden": wat, wie (sinds 1 jan 2026, B2B), PDF telt niet, particulieren niet, in SellQo (Odoo, Pro) | tip-cover, tip-step, cta-dark | landing.faq Peppol |
| do 29/10 19:00 | reel (14 s, stil) | Feature | "Eén bestelling. Alles mee.": geanimeerde flow webshop → bestellingen → factuur → voorraad (webshop, kassa, bol.com binnen het half uur) | reel-flow | landing.scene.retail, landing.core |
| vr 30/10 12:00 | post | Build in public | "Je productfoto's, eindelijk op orde.": mediabibliotheek, fotostandaard, bijsnijden zonder AI-credits | buildlog | changelog 2026.12j, 2026.12k |
| za 31/10 18:05 | story + poll-sticker | Samen | "Wat verkoop jij?" (Producten / Horeca / Events) | poll-story | landing.hero.doors |

Gebruikte changelog-items: `media_library_all_photos`, `photo_standard`, `photo_editor_frame`, `media_library_ai_social`.
Gebruikte scènes: retail (Atelier Nord). Nog niet gebruikt: horeca (Pizzeria Fiamma), events (Leuven Pub Crawl / Fonske), kassa, bol.com apart, Events Flex, demowinkels (/voorbeelden), "jouw zaak als voorbeeld", overstappen uit Shopify/WooCommerce, prijzen per plan.
