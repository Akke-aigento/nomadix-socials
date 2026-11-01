# SellQo Instagram — log

Wat er gepost is, per week (maandag). Lees dit vóór je een nieuwe week maakt: geen onderwerp, scène of changelog-item herhalen.

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
