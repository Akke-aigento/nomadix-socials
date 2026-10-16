# SellQo Instagram — werkwijze en weekroutine

@sellqo.app (handle te bevestigen) · Nederlands · tenant `d03c63fe-48c6-4ff7-a30b-7506ea3e71ab` · SellQo-project `9932a7fe-43a1-42de-9c64-168968599600`.
Een geplande taak ("SellQo IG: weekcontent") voert de **weekroutine** hieronder elke zondag uit.
De brand bible staat in het claude.ai-project "Nomadix Socials" (`claude/brand-sellqo.md`); bij verschil over
de werkwijze is dit bestand leidend, voor feiten en claims de bible (§8 "Bewezen claims").

## Wat waar staat

| Pad | Wat |
| --- | --- |
| `brand.css`, `fonts/`, `logo-navy.png`, `logo-white.png`, `logo-icon.png` | Huisstijl: navy `#00145B`, koraal `#FD7B5B`, crème `#FFF7F2`, diep navy `#0A1033`; Poppins + Inter. Logo enkel als PNG, niet hertekenen. |
| `templates/` | `feature` (UI-scène + titel), `tip-cover` + `tip-step` + `cta-dark` (carrousel), `buildlog` (changelog, donker), `story-dark`, `poll-story`, `reel-flow/` (geanimeerde UI-flow). Kopieer, pas aan, verander de stijl niet. |
| `weeks/<maandag>/` | HTML-bronnen + `.recipe.json`; `linkedin/` met 1200×1200-versies (iframe van de post). |
| `published/<maandag>/` | Wat online gaat (publiek, raw-URL); `linkedin/` om manueel te posten. |
| `log.md` | Wat al gepost is, welke scènes en changelog-items gebruikt zijn. Lees dit eerst. |

Raw-URL: `https://raw.githubusercontent.com/Akke-aigento/nomadix-socials/main/brands/sellqo/<pad>`.

## Claims: de enige regel die telt

Elke zin over SellQo moet een bron hebben. Toegelaten bronnen, in de repo `Akke-aigento/sellqo` (clone `--depth 20`):

1. Gerenderde landingcopy in `src/i18n/locales/landing.nl.json`: `landing.hero`, `.core`, `.sectors`, `.facts`, `.running`, `.faq`, `.examples`, `.scene`.
   **Niet** `landing.pricing.plans.*`, `.features`, `.comparison`, `.social`: dode copy met foute claims.
2. De publieke changelog: `src/pages/public/PublicChangelog.tsx` + `public.changelog.changes` in `landing.nl.json`.
3. Live `pricing_plans` (prijzen excl. btw, limieten, AI-credits).
4. `.claude/skills/sellqo-claim-audit/SKILL.md` (lijst "waar" / "niet waar").

Nooit: eigen domein koppelen, cadeaubonsaldo, visual editor, meerdere magazijnen, white-label, facturen in meer talen,
klantaantallen, omzet, uptime, verzonnen reviews of citaten, klantnamen buiten onze eigen merken,
"goedkoper dan Shopify". **Social planning / auto-posten is geen klantfeature** (App Review = fase 4): enkel als
build in public ("zo maken wij onze posts"). Fiscale tips: feitelijk, met "vraag je boekhouder".

## Contentpijlers en ritme

| Pijler | Aandeel | Template |
| --- | --- | --- |
| Feature (één functie, getrouwe UI-scène) | 35% | `feature`, `reel-flow` |
| Ondernemerstips (btw/OSS, Peppol, foto's, bol.com, horeca, events) | 30% | carrousel `tip-*` |
| Build in public (changelog van die maand, hoe we bouwen) | 20% | `buildlog`, `story-dark` |
| Bewijs (eigen merken, demowinkels) en Samen (polls) | 15% | `story-dark`, `poll-story` |

| Dag | Wat | Uur |
| --- | --- | --- |
| ma | post | 18:00 |
| di | story | 18:05 |
| wo | carrousel | 12:00 |
| do | reel | 19:00 |
| vr | post | 12:00 |
| za | story (wisselen: poll-sticker of info) | 18:05 |

Minstens drie verschillende templates per week; licht (crème) en donker (navy) afwisselen.
UI-scènes nabouwen met de labels uit `landing.scene` (Atelier Nord, Pizzeria Fiamma, Leuven Pub Crawl) of uit de app;
nooit klantdata, nooit een echt ordernummer of klantnaam.

## Weekroutine (elke zondag, voor de week vanaf maandag)

1. **Lees** `log.md`, de laatste week in `weeks/`, de bible en de sellqo-repo (claims hierboven). Kies per dag een onderwerp
   uit een andere pijler dan de dag ervoor; nieuwe changelog-items van de afgelopen week krijgen voorrang voor de buildlog.
2. **Live data** via `query_database`:
   `select slug, name, monthly_price, yearly_price, limit_products, limit_orders, ticket_fee, ai_credits_monthly from pricing_plans where active order by sort_order;`
   Koppeling: `select is_active from social_connections where tenant_id='d03c63fe-48c6-4ff7-a30b-7506ea3e71ab' and platform='instagram';`
3. **Maak** de HTML in `weeks/<maandag>/` naar de templates (`post-ma.html`, `post-wo-1..n.html`, `story-di.html`, `reel-<onderwerp>/index.html`, …),
   met `<meta name="nx-size">` en `<link rel="stylesheet" href="../../brand.css">`. Stories: tekst binnen de veilige zone. Tekstvakken met `data-slot`.
   LinkedIn: voor de ma- en vr-post een `linkedin/li-<dag>.html` (kopie van `weeks/2026-10-26/linkedin/li-ma.html`).
4. **Render**: `PLAYWRIGHT_MODULE=/opt/npm-tools/node_modules/playwright/index.mjs PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node shared/render.mjs brands/sellqo/weeks/<maandag> out/sellqo/<maandag>`
   (+ `…/linkedin`), bekijk elk beeld. Reel: `node shared/reel.mjs <index.html> out/sellqo/<maandag>/reel-<onderwerp>` + cover (`ffmpeg -ss 1.5 … -frames:v 1`).
4b. **Recept**: `node shared/recipe.mjs brands/sellqo/weeks/<maandag>/post-*.html brands/sellqo/weeks/<maandag>/story-*.html`.
5. **Publiceer** naar `published/<maandag>/` (`post-ma-<onderwerp>.jpg`, `post-wo-<onderwerp>-1.jpg`, …), commit + push naar `main`,
   controleer elke raw-URL met `curl -sI` (200).
6. **In SellQo** (één insert, nooit update/delete op bestaande rijen, nooit `approved`), zoals bij VanXcel:
   - Instagram **niet gekoppeld** (nu): alles `manual`, `manual_reason` `other`; poll-stories `sticker`; reel `music` (`video_silent_url`, cover in `image_urls`, `music_hint` met 3 songs uit een actuele bron).
   - Instagram **gekoppeld**: posts en carrousels `pending_approval`; stories zonder sticker `story` + `pending_approval`; sticker-stories `manual` + `sticker`.
   - `source` `content_task`, `language` `nl`, `scheduled_for` in `Europe/Brussels`. Carrousel: `media_type` `carousel`, alle URL's in volgorde.
   Caption: Nederlands, kort, 3–5 hashtags uit de bible, CTA met "link in bio". Controleer met een `select`.
7. **Herinneringen** doet SellQo zelf (±1 u vooraf). Geen losse herinneringstaken.
8. **Log en git**: week in `log.md` (onderwerp, template, bron, gebruikte scènes/changelog-items), commit naar `main`.
9. **Meld**: `insert into notifications (tenant_id, category, type, priority, title, message, action_url, data) values ('d03c63fe-48c6-4ff7-a30b-7506ea3e71ab','marketing','social_posts_ready','medium','Week van <d mmm> klaar: <n> items','<onderwerpen>. LinkedIn-versies: <raw-url map>. Bekijk ze in de Social planning.','/admin/marketing/social','{}'::jsonb);`

## Opnieuw maken

Verzoeken uit de Social planning (`regenerate_requested`, en na SOCIAL-SEC-1 `social_content_requests`) verwerkt de taak
"Social: opnieuw maken" volgens dezelfde regels als bij Loveke en VanXcel, met de paden van deze map en de claimregel hierboven.
