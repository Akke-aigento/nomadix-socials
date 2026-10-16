# VanXcel Instagram — werkwijze en weekroutine

@vanxcel.shop · Engels · tenant `54f6b480-280b-42e1-b843-d5beb2831acd` · SellQo-project `9932a7fe-43a1-42de-9c64-168968599600`.
Een geplande taak ("VanXcel IG: weekcontent") voert de **weekroutine** hieronder elke zondag uit.
De brand bible staat in het claude.ai-project "Nomadix Socials" (`claude/brand-vanxcel.md`); bij verschil over
de werkwijze is dit bestand leidend, voor feiten over het merk de bible.

## Wat waar staat

| Pad | Wat |
| --- | --- |
| `brand.css`, `fonts/`, `logo-white.svg`, `logo-black.svg` | Huisstijl (zwart, petrol `#008894`, amber `#F59E0B` max. één element; Bebas Neue + Inter). |
| `templates/` | Voorbeelden: `journey-cover` (reisfoto), `tip` (know-how), `spec` (product). Kopieer, pas aan, verander de stijl niet. |
| `media/` + `media.json` | 342 geselecteerde reisfoto's (2048 px) met datum, dag, land, plaats, tags (`sandy`, `road`, `landscape`, `people`, `cat`, `camp`, `tech`) en `used`. |
| `clips/` | 41 rijbeelden/clips (≤9 s, 1080p, zonder geluid) voor reels. Ook in `media.json` (`kind: clip`). |
| `products/` | Vrijstaande productfoto's (PNG). Ontbreekt een product: meld het, gebruik geen stock. |
| `weeks/<maandag>/` | HTML-bronnen + `.recipe.json` van die week. |
| `published/<maandag>/` | De beelden die online gaan (publiek, SellQo haalt ze op via de raw-URL). |
| `log.md` | Wat al gepost is. Lees dit eerst: geen beeld of onderwerp herhalen. |
| `../../shared/render.mjs`, `reel.mjs`, `recipe.mjs` | Gedeelde scripts voor alle merken. |

Raw-URL: `https://raw.githubusercontent.com/Akke-aigento/nomadix-socials/main/brands/vanxcel/<pad>`.

## Het verhaal (feiten, niets bijverzinnen)

- 1984 Toyota Land Cruiser **"Sandy"** (geen bus, geen van). Elektrische installatie in België gebouwd vóór vertrek: LiFePO4 120Ah, omvormer 2500W, zonnepaneel.
- Vertrek 2 april 2022 (dag 1, België), terug 5 augustus 2022. 17 landen in de foto's: BE, DE, AT, SI, HR, BA, ME, AL, GR, TR, GE, AZ, KZ, KG, TJ, UZ, BG.
- Verste punt: Kirgizië (Naryn/Osh), aan de Chinese grens. **Mongolië is niet bereikt**: de enige weg liep door een strook Rusland van ±70 km, onbegaanbaar door de oorlog.
- Duur in posts: **"6 months"** (beslissing Akke, 16 okt 2026). Nooit "in a van" of "in a bus": het is een Land Cruiser. De dagteller op beelden (`day` uit media.json) blijft de echte dag van de foto.
- Een kitten stapte in Kirgizië in en reed mee tot thuis (foto's met tag `cat`, juni–augustus).
- Plaats, land en dag van een foto komen uit `media.json`. Geen kilometers, temperaturen of anekdotes verzinnen die nergens staan.

## Wat we wel en niet zeggen

- Prijzen, voorraad en specs **live uit SellQo** (stap 2). Voorraad 0 = niet promoten. Producten die er niet zijn (zonnepanelen, 3000W-converter, 100Ah) nooit tonen.
- Know-how alleen uit de teksten van vanxcel.com (installatiegids, calculators, FAQ). 230V: altijd "laat keuren door een erkend elektricien".
- Geen reviews of sterren (niet geverifieerd). Geen klantaantallen ("hundreds of builders").
- Geen "cheaper than X" zonder gedocumenteerde concurrentieprijs; wel onze prijs en wat erin zit. Geen doorstreepte prijs.
- Geen "duurzaam/eco/groen" (ook niet de verpakking). Geen emoji in beelden, wel in captions.
- Niet tonen: paspoorten, papieren, chats, sigaretten/alcohol als onderwerp, kinderen, merknamen van derden in beeld.
- Nieuwsbriefkorting (10% op de eerste bestelling) mag als CTA.

## Contentpijlers

| Pijler | Aandeel | Template |
| --- | --- | --- |
| Journey (Sandy, route, plekken, de kat, wat werkte en wat niet) | 30% | `journey-cover`, carousel van 3–6 foto's van één land of etappe |
| Know-how (kabeldikte, zekering < 18 cm, LiFePO4 vs AGM, smart alternator, vorst) | 30% | `tip`, altijd met link naar de calculator of configurator |
| Product (één product, echte foto, live prijs, één concreet detail) | 25% | `spec` |
| Builders (vraag, poll, "show us your build") | 15% | story met sticker (handwerk) |

## Ritme

Om de twee dagen een post of reel, stories op de tussendagen (Brusselse tijd):

| Dag | Wat | Uur |
| --- | --- | --- |
| ma | post | 18:00 |
| di | story | 18:05 |
| wo | reel | 19:00 |
| do | story | 18:05 |
| vr | post | 18:00 |
| za | story | 18:05 |
| zo | post (of reel, afwisselen per week) | 18:00 |

## Variatie (verplicht)

Volg `shared/VARIATIE.md` (beslissing Akke, 16 okt 2026): elke post uniek, per week minstens 5 formats, nooit twee dagen na elkaar dezelfde template, minstens één lichte/felle post, één beeld-eerst-post en één typografische post, hooks en captionlengtes wisselen, en per item format/template/hook in `log.md`. Volstaat een template niet, maak een nieuwe variant in de huisstijl.

## Weekroutine (elke zondag, voor de week vanaf maandag)

1. **Lees** `log.md`, de laatste week in `weeks/`, en de bible. Kies de items volgens het ritme, uit verschillende pijlers. Kies foto's uit `media.json` met de minste `used`, en voorkeur voor beelden die Akke in SellQo een hartje gaf (`media_assets.is_favorite`, map `brand`, zodra die rijen bestaan).
2. **Live data** via `query_database`:
   `select p.name, p.slug, p.price, p.stock, left(regexp_replace(coalesce(p.description,''),'<[^>]+>','','g'),600) txt from products p where p.tenant_id='54f6b480-280b-42e1-b843-d5beb2831acd' and p.is_active order by p.price desc;`
   Koppeling: `select is_active from social_connections where tenant_id='54f6b480-280b-42e1-b843-d5beb2831acd' and platform='instagram';`
3. **Maak** de HTML in `weeks/<maandag>/` (`post-ma.html`, `story-di.html`, `reel-<onderwerp>/index.html`, …) naar de templates, met `<meta name="nx-size" content="1080x1350">` (story `1080x1920`) en `<link rel="stylesheet" href="../../brand.css">`; foto's via `../../media/<id>.jpg`. Stories: tekst binnen de veilige zone (boven 250 px, onder 340 px vrij).
3b. **Tekstvakken** markeren met `data-slot`/`data-label`/`data-max` (zie templates).
4. **Render**: `node shared/render.mjs brands/vanxcel/weeks/<maandag> out/vanxcel/<maandag>` en bekijk elk beeld.
4b. **Recept**: `node shared/recipe.mjs brands/vanxcel/weeks/<maandag>/*.html`.
5. **Publiceer**: kopieer naar `published/<maandag>/` (`post-ma-<onderwerp>.jpg`, …), commit + push naar `main`, controleer elke raw-URL met `curl -sI` (200).
6. **In SellQo** (één insert, nooit update/delete op bestaande rijen, nooit `approved`):
   - Instagram **gekoppeld**: posts `pending_approval`; stories zonder sticker `story` + `pending_approval`; stories met sticker `manual` + `sticker`; reel zoals hieronder.
   - Instagram **niet gekoppeld** (nu): alles `manual` met `manual_reason` `other` (sticker-stories `sticker`, reels zonder bibliotheekmuziek `music`). SellQo stuurt ±1 u vooraf een push; Akke post zelf via "Beeld openen" en klikt "Gepost".
   ```sql
   insert into social_posts (tenant_id, platform, media_type, status, source, manual_reason, language, post_text, image_urls, image_recipes, scheduled_for) values
   ('54f6b480-280b-42e1-b843-d5beb2831acd','instagram','image','manual','content_task','other','en','<caption>',
    array['<raw-url>'], jsonb_build_array($r$<recipe>$r$::jsonb), '<JJJJ-MM-DD> 18:00 Europe/Brussels');
   ```
   Caption: Engels, max 2200 tekens, 3–5 hashtags uit de bible, CTA met link in bio. Controleer met een `select`.
7. **Herinneringen** doet SellQo zelf (±1 u vooraf, push). Geen losse herinneringstaken.
8. **Log en git**: week in `log.md` (onderwerp, gebruikte media-id's), `used` in `media.json` aanvullen met de maandag, commit naar `main`.
9. **Meld**: `insert into notifications (tenant_id, category, type, priority, title, message, action_url, data) values ('54f6b480-280b-42e1-b843-d5beb2831acd','marketing','social_posts_ready','medium','Week van <d mmm> klaar: <n> items','<onderwerpen>. Bekijk ze in de Social planning.','/admin/marketing/social','{}'::jsonb);`

## Reels

Eén per week (woensdag 19:00). Formats afwisselen: rijbeelden-montage op de beat (clips), "day X in <land>"-slideshow,
know-how in 3 stappen, product in actie, de kat. `weeks/<maandag>/reel-<onderwerp>/index.html` met
`<meta name="nx-reel" content="1080x1920" data-duration="<s>" data-fps="30">` en `window.setT(t)`; clips via
`<video src="../../../clips/<id>.mp4" muted>` en in `setT` `video.currentTime = …` (wacht op `seeked`).
Render: `node shared/reel.mjs <index.html> out/vanxcel/<maandag>/reel-<onderwerp>` (elk < 9,5 MB).
In SellQo zoals bij Loveke (`media_type` `reel`, `video_url`/`video_silent_url`, `music_hint` met 3 concrete songs uit een actuele bron); zonder bibliotheekmuziek `manual` + `music`.

## Opnieuw maken

Verzoeken uit de Social planning (`regenerate_requested`, en vanaf SOCIAL-SEC-1 ook `social_content_requests`) worden
door de taak "Social: opnieuw maken" verwerkt volgens dezelfde regels als bij Loveke (README Loveke, sectie "Opnieuw maken"),
met de paden van deze map.
