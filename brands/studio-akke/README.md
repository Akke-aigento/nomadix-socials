# Studio Akke Instagram — werkwijze en weekroutine

Instagram @studio.akke (gekoppeld in SellQo sinds 16 okt) · Nederlands · tenant `c96fb1b2-ddac-44d1-a638-72dd54efd31e` · SellQo-project `9932a7fe-43a1-42de-9c64-168968599600`.
Een geplande taak ("Studio Akke IG: weekcontent") voert de **weekroutine** hieronder elke zondag uit.
De brand bible staat in het claude.ai-project "Nomadix Socials" (`claude/brand-studio-akke.md`); bij verschil over
de werkwijze is dit bestand leidend, voor feiten over het merk de bible.

## Wat waar staat

| Pad | Wat |
| --- | --- |
| `brand.css`, `fonts/`, `mark.svg` | Huisstijl: navy → violet verloop, teal/cyaan-accent, koraal max. één element; Inter (800/900 titels) + JetBrains Mono (kleine `// labels`). Woordmerk = HTML-tekst `Studio <b>Akke</b>` naast `mark.svg`. |
| `logo-white.svg`, `logo-color.svg` | Originele logo's van de site (tekst in systeemfont; voor beelden `mark.svg` + HTML-tekst gebruiken). |
| `templates/` | Donker: `cover` (stelling/carrousel-slide 1), `case` (site in browservenster), `tip` (genummerd), `offer` (pakket + prijs), `compare` (twee kolommen), `story` (vraag/poll/link), `question` (carrousel: vraag + antwoordkaart). Fel: `story-fel` (groot cijfer). Licht: `myth` (mythe vs. feit, `body.paper`). Fel: `statement` (één zin op teal-cyaan verloop). Kopieer en varieer de layout; kleuren, fonts en logo-regels blijven. Nieuwe varianten zijn welkom (zie `../../shared/VARIATIE.md`). |
| `media/` + `media.json` | Schermafbeeldingen van de 8 portfolio-sites (uit de repo `studioakke`, `src/assets/portfolio/`), met `used`. |
| `weeks/<maandag>/` | HTML-bronnen + `.recipe.json` + `reel-<onderwerp>/index.html`. |
| `published/<maandag>/` | Wat online gaat (publiek; SellQo haalt het op via de raw-URL). |
| `log.md` | Wat al gepost is. Lees dit eerst: geen onderwerp of case herhalen binnen 4 weken. |

Raw-URL: `https://raw.githubusercontent.com/Akke-aigento/nomadix-socials/main/brands/studio-akke/<pad>`.

## Bron van alle feiten: de site

Clone de privé-repo `Akke-aigento/studioakke` (add_repo, read) en haal alles daar:

- **Prijzen en pakketten**: `src/components/home/Pricing.tsx`, `src/pages/Prijzen.tsx`, `src/pages/Mail.tsx`, `src/pages/Insights.tsx`, `src/pages/diensten/*.tsx`.
- **Teksten** (NL): `src/contexts/LanguageContext.tsx`, blok `nl:` (sleutels `hero.*`, `process.*`, `pricing.*`, `faq.*`, `mail.*`, `insights.*`, `logoDesign.*`, `photo.*`, `copy.*`, `overAkkePage.*`, `portfolio.*`).
- **Portfolio**: `src/components/home/PortfolioCarousel.tsx` (naam, URL, categorie) + `portfolio.<slug>.*` in de vertalingen.
- Wijkt een prijs af van wat in een eerdere week stond: volg de site en meld het in de weekmelding.

Stand 16 okt 2026 (excl. btw): Landing Page €895 (1 pagina, 5–7 werkdagen), Business Starter €1.795 (3–5 pagina's, 7–10), Professional €2.995 (6–10 pagina's, 10–14). Onderhoud €69 en €119/maand. Mail vanaf €10/maand, Insights vanaf €15/maand. Logo €395, copywriting €65/pagina, fotografie €65–€95/product. Extra pagina €200–400, spoed €300–500.

## Wat we wel en niet zeggen

- **Altijd "excl. btw"** bij een prijs. Geen doorstreepte prijzen, geen kortingen of acties die niet op de site staan.
- Snelheid altijd met de voorwaarde: de termijn start zodra de materialen (logo, teksten, foto's) binnen zijn. "Werkdagen", niet "dagen".
- "Acht sites live" mag (staat op de site). Nooit klantaantallen, "tevreden klanten", reviews, sterren, quotes of resultaten (bezoekers, omzet, "+40% leads") die niet aantoonbaar zijn.
- Cases: enkel wat de site zelf zegt (categorie, omschrijving, kenmerken). Wat een klant van de site vindt, is niet gekend: niet invullen. Yeketi-klant heet altijd "Baram Maro" (nooit een familienaam).
- AI en tools mogen genoemd worden zoals op de site ("moderne tools zoals Lovable"), zonder te overdrijven.
- **Geen foto van Akke** tot hij bevestigt welke foto mag (de bureaufoto op "Over Akke" of een nieuwe). De ongebruikte `akke-photo.jpg` in de site-repo (man in pak) nooit gebruiken.
- Geen "duurzaam/eco/groen". Geen emoji in beelden, wel in captions. Insights: "cookieloos" mag (staat op de site), geen juridische garanties.
- Studio Akke is los van Akke's werkgever: daar nooit naar verwijzen.

## Contentpijlers

| Pijler | Aandeel | Template |
| --- | --- | --- |
| Werk (één case, portfolio-overzicht, voor/na als Akke het aanlevert) | 30% | `case`, reel door de sites |
| Tips (vindbaarheid, mail bij je domein, wat een site nodig heeft, onderhoud) | 30% | `tip`, story |
| Aanbod (pakketten, onderhoud, Mail, Insights, gratis scan, logo/copy/foto) | 20% | `offer`, `cover` |
| Ondernemers (vragen, polls, "wat houdt je tegen?") | 20% | `story` met sticker (handwerk) |

## Ritme (Brusselse tijd)

Uren: **geen vaste uren**. Volg `shared/POSTTIJDEN.md` (venster van dit merk, uur en reden in `log.md`, één testslot per week). Dit is het ritme van de dagen:

| Dag | Wat |
| --- | --- |
| ma | post (meestal carrousel) |
| di | story |
| wo | reel |
| do | story |
| vr | post |
| za | story |
| zo | post |

## Leren (verplicht)

Volg `shared/LEREN.md` (SOCIAL-6): elke post krijgt `content_tags` (pijler, format, template, hook, captionlengte, cta, bucket), lees vóór je iets bedenkt `lessen.md` van dit merk en de resultaten in `social_post_performance`, kies volgens 70/20/10, en zet UTM-parameters op elke link.

## Variatie (verplicht)

Volg `shared/VARIATIE.md` (beslissing Akke, 16 okt 2026): elke post uniek, per week minstens 5 formats, nooit twee dagen na elkaar dezelfde template, minstens één lichte/felle post, één beeld-eerst-post en één typografische post, hooks en captionlengtes wisselen, en per item format/template/hook in `log.md`. Volstaat een template niet, maak een nieuwe variant in de huisstijl.

## Weekroutine (elke zondag, voor de week vanaf maandag)

1. **Lees** `log.md`, de laatste week in `weeks/`, de bible en de README. Kies items volgens het ritme, uit verschillende pijlers.
2. **Feiten**: clone `studioakke` en controleer elke prijs en elke zin tegen de bronnen hierboven.
   Koppeling: `select is_active from social_connections where tenant_id='c96fb1b2-ddac-44d1-a638-72dd54efd31e' and platform='instagram';`
3. **Maak** de HTML in `weeks/<maandag>/` (`post-ma-1.html` …, `story-di.html`, `reel-<onderwerp>/index.html`) naar de templates, met `<meta name="nx-size" content="1080x1350">` (story `1080x1920`) en `<link rel="stylesheet" href="../../brand.css">`; beelden via `../../media/…`, merkteken `../../mark.svg`. Stories: tekst binnen `.story-safe`. Stickerstories: `.sticker-slot` leeg laten (onzichtbaar).
3b. **Tekstvakken** markeren met `data-slot`/`data-label`/`data-max`.
4. **Render**: `node shared/render.mjs brands/studio-akke/weeks/<maandag> out/studio-akke/<maandag>` en bekijk elk beeld.
4b. **Recept**: `node shared/recipe.mjs brands/studio-akke/weeks/<maandag>/*.html`.
5. **Publiceer** naar `published/<maandag>/`, commit + push naar `main`, controleer elke raw-URL met `curl -sI` (200).
6. **In SellQo** (één insert, nooit update/delete op bestaande rijen, nooit `approved`):
   - Instagram **gekoppeld**: posts `pending_approval`; stories zonder sticker `story` + `pending_approval`; stickerstories `manual` + `sticker`; reel zonder bibliotheekmuziek `manual` + `music`.
   - **Niet gekoppeld** (nu): alles `manual`, reden `other` (stickers `sticker`, reels `music`). SellQo stuurt ±1 u vooraf een push.
   - Carrousel: `media_type` `carousel`, `image_urls` in volgorde, één recept per slide (of `null`).
   - Caption: Nederlands, je-vorm, max 2200 tekens, 3–5 hashtags, CTA met "link in bio" (studioakke.com/contact of de juiste pagina). Controleer met een `select`.
7. **Herinneringen** doet SellQo zelf. Geen losse herinneringstaken.
8. **Log en git**: week in `log.md`, `used` in `media.json` aanvullen, commit naar `main`.
9. **Meld**: `insert into notifications (tenant_id, category, type, priority, title, message, action_url, data) values ('c96fb1b2-ddac-44d1-a638-72dd54efd31e','marketing','social_posts_ready','medium','Week van <d mmm> klaar: <n> items','<onderwerpen>. Bekijk ze in de Social planning.','/admin/marketing/social','{}'::jsonb);`

## Reels

Eén per week (woensdag, op het sterkste slot uit `shared/POSTTIJDEN.md`). Formats afwisselen: sites in een browservenster (portfolio), "pakket in 15 seconden",
tip in 3 stappen, het proces in 4 stappen, schermopname die Akke aanlevert. `weeks/<maandag>/reel-<onderwerp>/index.html` met
`<meta name="nx-reel" content="1080x1920" data-duration="<s>" data-fps="30">` en `window.setT(t)`.
Wissel beelden door ze allemaal vooraf te laden en `display` te schakelen (nooit `src` veranderen in `setT`).
Noem een eigen voortgangsbalk niet `.bar` (botst met het browservenster).
Render: `node shared/reel.mjs <index.html> out/studio-akke/<maandag>/reel-<onderwerp>` (< 9,5 MB), cover = één frame (`ffmpeg -ss <t> -frames:v 1`).
In SellQo: `media_type` `reel`, `video_silent_url`, `image_urls` = cover, `music_hint` met 3 concrete songs uit een actuele bron; zonder bibliotheekmuziek `manual` + `music`.

## Opnieuw maken

Verzoeken uit de Social planning (`regenerate_requested`, en vanaf SOCIAL-SEC-1 `social_content_requests`) verwerkt de taak
"Social: opnieuw maken" volgens dezelfde regels als bij Loveke en VanXcel, met de paden van deze map.
