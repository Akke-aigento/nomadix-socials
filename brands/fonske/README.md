# The Fonske Crawl Instagram — werkwijze

@the.fonske.crawl · Engels · tenant `95f6685b-3474-42fe-81ad-a5e6ca3d6806` · SellQo-project `9932a7fe-43a1-42de-9c64-168968599600`.
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
Stories met linksticker: laat de strook y 1300–1560 vrij. De link staat als laatste regel in de tekst: `Link-sticker: https://…` met UTM (shared/LEREN.md §5).


## Leren (verplicht)

Volg `shared/LEREN.md` (SOCIAL-6): elke post krijgt `content_tags` (pijler, format, template, hook, captionlengte, cta, bucket), lees vóór je iets bedenkt `lessen.md` van dit merk en de resultaten in `social_post_performance`, kies volgens 70/20/10, en zet UTM-parameters op elke link.

## Variatie (verplicht)

Volg `shared/VARIATIE.md` (beslissing Akke, 16 okt 2026): elke post uniek, per week minstens 5 formats, nooit twee dagen na elkaar dezelfde template, minstens één lichte/felle post, één beeld-eerst-post en één typografische post, hooks en captionlengtes wisselen, en per item format/template/hook in `log.md`. Volstaat een template niet, maak een nieuwe variant in de huisstijl.

## Foto's van de crawl (bron: Crawl Log op fonskecrawl.com)

- Waar: Lovable-project `377b3ca5-a57f-413e-a53a-dc1889be4b40` (eigen Supabase), tabellen `crawl_nights` (night_date, title, crawlers, published, cover_photo_id) en `crawl_photos` (path, thumb_path, width, height, sort); publieke bucket `crawl-photos`.
  URL: `https://mrwiqgrxsyphbxiahule.supabase.co/storage/v1/object/public/crawl-photos/<path>`.
- **Enkel avonden met `published = true`.** Die heeft Akke of een gids via de beheerlogin gekozen. Nooit iets uit niet-gepubliceerde avonden.
- Voorwaarden van de site: foto's mogen op site en socials; wie niet op de foto wil, zegt het aan de gids. Daarbovenop onze regels: geen close-up van één persoon die er dronken of ongemakkelijk uitziet, niemand die overgeeft of op de grond ligt, geen beelden van mensen buiten de groep in close-up, geen herkenbare nummerplaten of schermen.
- Catalogus `photos.json` (zoals `media.json` bij VanXcel): per foto `id` (= crawl_photos.id), `night`, `path`, `type`, `faces` (ja/nee), `note`, `used`. Types: `group` (groep aan de Totem), `shot` (shotmoment), `street` (onderweg, Leuven bij nacht), `bar` (sfeer binnen), `finale` (Oude Markt), `host` (de gids), `detail` (glazen, polsbandjes, handen, tickets). Claude kijkt elke nieuwe foto zelf na en vult de catalogus aan; twijfel = niet opnemen.
- Gebruikte foto's worden een JPG in `published/<maandag>/` (Instagram wil JPEG, de bucket heeft vaak webp).

### Variatie met foto's (nooit enkel feestfoto's)

| Formaat | Wat |
| --- | --- |
| Recap-carrousel (2 dagen na een crawl) | 5–8 foto's in volgorde van de avond: groep aan de Totem → straat → shot → bar → finale; laatste slide = volgende datum (getekend). |
| Detail + verhaal | één `detail`-foto groot, met een korte tekst (wat zit erbij, alcoholvrij kan, 4 cafés, polsbandje). |
| Foto + tekening | foto in een kader met de lijntekeningen (Fonske, Totem) eroverheen; zo blijft het merk herkenbaar. |
| Straat en stad | `street`-foto's voor Leuven Lore en "Leuven by night", zonder partyfocus. |
| Aankondiging | foto van de vorige avond als achtergrond met de nieuwe datum. |
| Reel | 8–12 foto's op de beat (shared/reel.mjs), max 1 per week. |
| Lore en deadlines | blijven getekend (`illustrations/`). |

Regel: per week hoogstens de helft van de beelden met mensen in close-up; afwisselen met detail, straat en tekening.

### Bereikbaarheid

De sandbox moet `mrwiqgrxsyphbxiahule.supabase.co` mogen bereiken (claude.ai → Settings → Capabilities → toegelaten domeinen). Lukt dat niet: catalogus wel bijwerken (de query werkt via de Lovable-connector), beelden niet downloaden, die week getekend werken en het melden.

## Ritme (dagen; uren volgens `shared/POSTTIJDEN.md`, venster Fonske)

| Dag | Wat |
| --- | --- |
| ma | post |
| wo | story (linksticker, of poll/quiz = handwerk) |
| vr | post |
| za | story |

- Crawlweek: aftellen naar het event (POSTTIJDEN: op de dag zelf ±15:00 "tonight" en ±19:30 "2 hours to go"); early bird: dag ervoor een post, laatste dag een story.
- Na een crawl met gepubliceerde foto's: recap-carrousel binnen 2 dagen (vervangt de eerstvolgende post).
- Geen crawl gepland: lore, stad, foto's van vorige avonden, en het aanbod van de site (privécrawls vanaf €35 p.p., min. 12: vrijgezellen, teambuilding). Nooit een datum aankondigen die niet als `scheduled` in SellQo staat.

## Weektaak (elke zondag, voor de week vanaf maandag)

1. Lees `log.md`, `photos.json` en deze README. Geen onderwerp of foto herhalen.
2. SellQo (query_database, project `9932a7fe-43a1-42de-9c64-168968599600`): komende crawls (query bij "Feiten"), Instagram-koppeling (`social_connections`), bestaande `social_posts` van de tenant.
3. Fonske-site (query_database, project `377b3ca5-a57f-413e-a53a-dc1889be4b40`): `select n.id, n.night_date, n.title, n.crawlers, p.id photo_id, p.path, p.width, p.height from crawl_nights n join crawl_photos p on p.night_id=n.id where n.published order by n.night_date desc, p.sort;` Nieuwe foto's downloaden (zie Bereikbaarheid), bekijken, in `photos.json` zetten.
4. HTML in `weeks/<maandag>/` naar de templates; `shared/VARIATIE.md` volgen, uren uit `shared/POSTTIJDEN.md` (controlequery vóór de insert). Render (`shared/render.mjs`), elk beeld bekijken, recepten (`shared/recipe.mjs`).
5. Publiceer naar `published/<maandag>/`, push, raw-URL's 200.
6. SellQo `social_posts` (tenant `95f6685b-3474-42fe-81ad-a5e6ca3d6806`): niet gekoppeld → alles `manual` (`sticker` of `other`); gekoppeld → posts `pending_approval`, stickerstories `manual`. `source` `content_task`, `language` `en`, `image_recipes`. Nooit `approved`/`posted`, geen bestaande rijen wijzigen.
7. `log.md` en `photos.json` (`used`) bijwerken, commit; melding `social_posts_ready`; één korte boodschap aan Akke.
