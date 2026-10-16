# The Fonske Crawl Instagram — werkwijze

@fonskecrawl · Engels · tenant `95f6685b-3474-42fe-81ad-a5e6ca3d6806` · SellQo-project `9932a7fe-43a1-42de-9c64-168968599600`.
Site: fonskecrawl.com (repo `Akke-aigento/fonske-crawl-hq`, Lovable-project `377b3ca5-a57f-413e-a53a-dc1889be4b40`).
Brand bible: claude.ai-project "Nomadix Socials", `claude/brand-fonske.md` (volgt na de crawl van 24 okt).

## Wat waar staat

| Pad | Wat |
| --- | --- |
| `brand.css`, `fonts/` | Huisstijl van de site: warm bijna-zwart `#110C08`, amber `#F4A434`, goudverloop `#F6CB6A → #E58A2A`, crème `#F4F1EC`, rood `#D45A4F` enkel voor deadlines. Bebas Neue + Space Grotesk (OFL). |
| `logo-mark.png` | De Fonske-figuur (amber lijn, transparant). `logo-lockup.jpg` = volledige lockup (OG-beeld van de site). |
| `illustrations/` | Getekende scènes in de lijnstijl van het logo: `totem` (kever op de naald + bibliotheek), `fonske` (giet een pint in zijn hoofd), `oude-markt` (trapgevels, terras), `dijle` (Margriet, nacht), `route` (getekende kaart, 4 cafés + ster), `early-bird` (vogel met ticket), `last-call` (klok op 22:00 + shot). Inline in de HTML zetten (dan werken de fonts). |
| `templates/` | `poster-totem`, `lore-story-night`, `lore-story-amber`, `route-map-cream`, `early-bird-amber`, `oude-markt-story`, `last-call-red`, `tonight-story`. |
| `weeks/<maandag>/` | HTML + `.recipe.json` van die week. |
| `published/<maandag>/` | De JPG's die online gaan (SellQo haalt ze via de raw-URL). |
| `log.md` | Wat al gepost is. |

## Variatie (regel)

Nooit twee keer na elkaar dezelfde achtergrond. Kleurvlakken: nacht `#110C08`, amber `#F4A434` (donkere tekst), crème `#F4F1EC` (donkere tekst), Dijleblauw `#0E1626`, rood `#D45A4F` (enkel deadlines). Elk beeld heeft een tekening of (later) een echte crawlfoto, nooit enkel tekst.

## Feiten (niets bijverzinnen)

- Live uit SellQo, per crawl: `select e.event_date, e.start_time, e.location_name, e.meeting_point, e.capacity, e.min_attendees, e.early_bird_price, e.early_bird_deadline, p.price from event_details e join products p on p.id=e.product_id where e.tenant_id='95f6685b-3474-42fe-81ad-a5e6ca3d6806' and e.status='scheduled' and e.event_date >= current_date;`
- Van de site: verzamelen aan The Totem (de grote kever op het boek) op het Ladeuzeplein, 21:00; 4 cafés van ±45 minuten; een shot per stop, alcoholvrij op aanvraag; finale op de Oude Markt ("the longest bar in Europe"); lokale gids; 18+ met ID; standaard Engels; privécrawls vanaf €35 p.p., min. 12 personen.
- Cafénamen en de volgorde staan nergens publiek: niet noemen, behalve "Our first bar is named after a murder victim" (Fiere Margriet, tekst van Akke).
- Leuven Lore: Fiere Margriet (vermoord in 1225 aan de Dijle); Fonske/Fons Sapientiae (geschonken in 1975 voor 550 jaar KU Leuven, giet water over zijn hoofd).
- Geen verzonnen reviews, deelnemersaantallen of "sold out". Geen doorstreepte prijzen. Geen emoji in beelden, wel in captions.
- Alcohol: geen aansporing tot overmatig drinken, altijd 18+, alcoholvrij noemen waar het past.

## Ritme en status in SellQo

Instagram is nog niet gekoppeld in SellQo: alles staat op `manual` (`manual_reason` `sticker` voor stories met linksticker, anders `other`), `source` `content_task`, `language` `en`. SellQo stuurt ±1 u vooraf een push; Akke post zelf via "Beeld openen" en klikt "Gepost". Na het koppelen: posts op `pending_approval`.
Uren: **geen vaste uren**, volg `shared/POSTTIJDEN.md` (venster Fonske; vlak voor een crawl aftellen naar het event).
Stories met linksticker: laat de strook y 1300–1560 vrij.

Een weektaak volgt na de crawl van 24 okt, samen met de brand bible.

## Variatie (verplicht)

Volg `shared/VARIATIE.md` (beslissing Akke, 16 okt 2026): elke post uniek, per week minstens 5 formats, nooit twee dagen na elkaar dezelfde template, minstens één lichte/felle post, één beeld-eerst-post en één typografische post, hooks en captionlengtes wisselen, en per item format/template/hook in `log.md`. Volstaat een template niet, maak een nieuwe variant in de huisstijl.
