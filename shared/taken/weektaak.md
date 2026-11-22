# Weektaak: Instagram-content van volgende week voor één merk

De opdracht van de taak noemt het merk. Hieronder staan eerst de stappen voor elk merk, daarna per merk wat anders is. Bij verschil met een README, VARIATIE.md of GENRES.md gaat `shared/POSTS-2.md` voor (sinds 17-11-2026, Akke: de posts waren "niet zo geweldig"; minder, echter, beter).

## Stappen

0. Bepaal de datum van de eerstvolgende maandag (Europe/Brussels). Controleer: `select count(*) from social_posts where tenant_id='<t>' and source='content_task' and scheduled_for >= '<maandag> 00:00 Europe/Brussels' and scheduled_for < '<maandag> 00:00 Europe/Brussels'::timestamptz + interval '7 days'`. Meer dan 0: antwoord "Niets te doen." en stop.
1. Repo's: zie ALGEMEEN.md (verse main). Externe skills: `shared/taken/vendor/marketingskills-social/` en, als het clonen lukt, `/tmp/remotion-skills`.
2. Lees volledig, in deze volgorde: `shared/POSTS-2.md`; de README van het merk (de strikte secties staan hieronder per merk); het log, `lessen.md` en `referenties.md` van het merk; `shared/POSTTIJDEN.md` (venster van het merk), `shared/LEREN.md`, `shared/MUZIEK.md`; `vendor/marketingskills-social/SKILL.md` met `references/carousel-frameworks.md`, `short-form-video.md` en `reverse-engineering.md`; `remotion-skills/skills/remotion-best-practices/SKILL.md` (als die er is); `shared/remotion/README.md`. Is de skill frontend-design beschikbaar, laad die ook.
3. Live data via de Lovable-connector (tenant van het merk): de bron per merk (hieronder). Daarnaast: of Instagram gekoppeld is (`social_connections`), alle bestaande `social_posts` van de tenant (geen dubbels, geen onderwerp herhalen binnen 4 weken), nieuw materiaal van Akke (`media_assets` van de tenant uit de laatste 14 dagen, `is_favorite` eerst) en de queries uit LEREN.md §2 (wat werkte, signalen van Akke).
4. Plan precies 4 items volgens POSTS-2 §1: 1 reel, 1 carrousel van 5–8 slides, 1 post en 1 story (Fonske: +1 in een crawlweek). Schrijf per item eerst de drie antwoorden uit POSTS-2 §2: naar wie doorsturen en waarom, de hook in 1 s, het ene idee. Voor de carrousel noteer je ook welke structuur uit §3. Geen goed antwoord = ander idee. Echt beeld eerst (§4).
5. Maak de items:
   - **Reel en carrouselslides:** met `shared/remotion/render.sh`. De reel krijgt hook-tekst, ondertitels en een bibliotheeknummer uit de muziekmap van het merk, die op het einde uitfadet. Geen merksting (uit sinds 22-11). Slides gebruiken de layouts photo/split/list/statement/cta.
   - **Clips:** kies een fragment pas nadat je er frames van bekeken hebt, en haal elke clip door `shared/remotion/clipcheck.sh`.
   - **Post en story:** mogen ook een eigen HTML-template met een echte foto zijn.
   - **Altijd:** geen emoji in beelden, veilige zones respecteren.
6. Kwaliteitspoort (POSTS-2 §6, verplicht):
   - Bekijk elk beeld en enkele frames van de reel, maak één contactsheet en score elk item 0–2 op de zes punten. Onder 9 van 12: opnieuw maken of een ander idee, **nooit schrappen**. Er gaan altijd minstens 4 items per merk naar SellQo (Akke, 22-11).
   - Is de Agent-tool er, laat dan een subagent zonder de maakgeschiedenis de contactsheet en captions onafhankelijk beoordelen: dezelfde zes punten plus "zou een mens dit doorsturen?". Verwerk wat hij afkeurt.
   - Noteer de scores in het log. Liever 3 sterke items dan 4 met een zwakke.
7. Push naar main van de repo van het merk:
   - de weekmap, de published-map, het log, `media.json`/`photos.json` waar van toepassing en `music/tracks.json`;
   - nooit `node_modules` of `out/`;
   - controleer elke raw-URL met `curl -sI` (200) vóór je iets in SellQo zet. De CDN kan na een push even 404 geven: wacht en probeer tot 3 minuten opnieuw, of test met de commit-hash in de URL.
8. Zet de items in `social_posts`:
   - **Status, Instagram gekoppeld:** posts, carrousels, stories zonder sticker en de reel met bibliotheeknummer op `pending_approval`; stickerstories op `manual` met `manual_reason` `sticker`.
   - **Status, niet gekoppeld:** alles op `manual` met `manual_reason` `other`.
   - **Reel:** met `video_url`, `video_silent_url` (versie zonder muziek) en `music_hint`.
   - **Altijd:**
     - source `content_task`, language van het merk;
     - content_tags volgens LEREN.md §1, plus genre (carrouselstructuur of reelformat) en quality (score);
     - UTM op elke link (LEREN.md §5, `utm_campaign=<campagne>-<JJJJMMDD>`);
     - image_recipes enkel voor beelden met een `.recipe.json` (Remotion-slides hebben er geen: dan null).
   - **Uren** volgens POSTTIJDEN.md; doe een controlequery vóór de insert.
   - **Verboden:** nooit `approved` of `posted`; bestaande rijen niet wijzigen of verwijderen. Raak niets anders in SellQo aan, behalve de ene melding `social_posts_ready`.
9. Geen losse herinneringstaken: SellQo verwittigt zelf. Werk het log bij (per item: dag, uur + reden, soort, structuur/format, hook, de drie antwoorden, score, labels) en commit.
10. Bericht aan Akke (zie ALGEMEEN.md):
    - per item: dag, uur, idee en score;
    - welk echt materiaal je gebruikte;
    - welk materiaal je mist en volgende week graag van hem had (concreet: "een clip van 10 s van …");
    - dat ze klaarstaan in SellQo → Marketing → Social planning ("Week goedkeuren").

Lukt een stap niet, meld dat en stop, en zet niets half in SellQo. Dat geldt voor: repo, connector, render, een URL zonder 200, een reel boven 9,5 MB, een claim zonder bron.

## Per merk

### Loveke
- Tenant `1671a91c-31fe-42ed-8a10-41f3117ceb50`, Instagram @loveke.shop.
- **Taal:** content in het Nederlands (Vlaams, warm, kort); Engels enkel als Akke erom vroeg.
- **Campagne:** `loveke`.
- **Map:** repo `loveke`, `marketing/instagram/` (README = huisstijl, wat we wel en niet zeggen, recepten).
- **Muziek:** `marketing/music/` (`tracks.json`; nooit twee keer hetzelfde nummer na elkaar). Zet bij elke render `LOVEKE_DIR=<repo-map van loveke>`, zodat `loveke/...` in de props werkt.
- **Push** naar loveke: `marketing/instagram/weeks/<maandag>/`, `marketing/instagram/published/<maandag>/`, `marketing/instagram/log.md` en `marketing/music/tracks.json`. Gedeelde bestanden (POSTS-2, remotion) lees je uit nomadix-socials.
- **Bron:** producten (naam, prijs, omschrijving, beelden; nieuwe producten gaan voor).
- **Echt beeld:** strip 1 en 2 (`src/assets/comic/`, `marketing/comic-2/`), productfoto's (`marketing/product-photos/`) en elk nieuw beeld of elke clip van Akke uit de mediabibliotheek.
- **Feiten strikt:**
  - prijzen, materialen en producten enkel live uit SellQo;
  - het verhaal enkel uit de strip of "Ons verhaal";
  - "Belgisch merk" mag, "Made in Belgium" niet;
  - geen duurzaam/eco/groen;
  - gemaakt op bestelling, 5 tot 20 werkdagen.
- **Status:** de reel met bibliotheeknummer op `pending_approval`.

### VanXcel
- Tenant `54f6b480-280b-42e1-b843-d5beb2831acd`, Instagram @vanxcel.shop.
- **Taal:** content in het Engels.
- **Campagne:** `vanxcel`.
- **Map:** nomadix-socials `brands/vanxcel/`. De secties "Het verhaal" en "Wat we wel en niet zeggen" in de README gelden strikt.
- **Bron:** producten met prijs en voorraad (voorraad 0 = niet promoten).
- **Echt beeld:** 41 clips in `clips/`, 342 foto's in `media/` (`media.json`: dag, land, plaats, tags), productfoto's in `products/` en nieuw materiaal van Akke.
- **Feiten strikt:**
  - niets verzinnen: geen kilometers, anekdotes, prijzen of specs die niet in `media.json`, SellQo of op vanxcel.com staan;
  - duur van de reis: "6 months";
  - het voertuig is een Land Cruiser ("Sandy"); Mongolië is niet bereikt;
  - 230V: altijd "laat keuren door een erkend elektricien".

### SellQo
- Tenant `d03c63fe-48c6-4ff7-a30b-7506ea3e71ab`, Instagram @sellqo.app.
- **Taal:** content in het Nederlands, neutraal voor Vlaanderen en Nederland, met "je".
- **Campagne:** `sellqo`.
- **Map:** nomadix-socials `brands/sellqo/`. De sectie "Claims: de enige regel die telt" geldt strikt.
- **Bron voor elke claim:** de repo `<repo-map van sellqo>`:
  - de gerenderde landingcopy `src/i18n/locales/landing.nl.json` (hero/core/sectors/facts/running/faq/examples/scene; NOOIT `landing.pricing.plans`);
  - de publieke changelog;
  - live `pricing_plans`;
  - `.claude/skills/sellqo-claim-audit/SKILL.md`.
  Geen bron = niet zeggen.
- **Nooit:**
  - eigen domein, cadeaubonsaldo, visual editor, meerdere magazijnen, white-label;
  - klantaantallen, cijfers, reviews;
  - klantnamen buiten VanXcel/Loveke/Fonske Crawl;
  - "goedkoper dan".
- **Social planning** is geen klantfeature (enkel build in public). Fiscale tips: feitelijk, met "vraag je boekhouder".
- **Live data:** `pricing_plans` (prijzen en limieten) en de changelog-entries van de voorbije week (die krijgen voorrang).
- **Echt beeld:** schermopnames en screenshots van de echte app en de demowinkels (sellqo.app/voorbeelden), nooit klanttenants; nieuw materiaal van Akke.
- **Extra bij het pushen:** een LinkedIn-versie van 1200×1200 van de post in `published/<maandag>/`.
- **Status:** poll-stories op `manual` (`sticker`).

### Studio Akke
- Tenant `c96fb1b2-ddac-44d1-a638-72dd54efd31e`.
- **Taal:** content in het Nederlands, je-vorm, ik-vorm voor Akke.
- **Campagne:** `studioakke`.
- **Map:** nomadix-socials `brands/studio-akke/`. De secties "Bron van alle feiten" en "Wat we wel en niet zeggen" gelden strikt.
- **Bron:** de repo `<repo-map van studioakke>` is de enige bron voor aanbod, prijzen en teksten (`Pricing.tsx`, `Prijzen.tsx`, `Mail.tsx`, `Insights.tsx`, `diensten/*`, `LanguageContext.tsx` blok nl).
- **Regels:**
  - prijzen altijd met "excl. btw";
  - snelheid in werkdagen, met de voorwaarde dat de termijn start zodra de materialen binnen zijn;
  - geen klantaantallen, reviews, quotes of resultaten;
  - cases enkel met wat de site zegt;
  - geen foto van Akke zolang de README dat niet toelaat;
  - de Yeketi-klant heet Baram Maro.
- **Echt beeld:** portfolio-screenshots in `brands/studio-akke/media/`, schermopnames van echte sites en nieuw materiaal van Akke.

### The Fonske Crawl
- Tenant `95f6685b-3474-42fe-81ad-a5e6ca3d6806`, pubcrawl in Leuven, fonskecrawl.com, Instagram @the.fonske.crawl.
- **Taal:** content in het Engels.
- **Campagne:** `fonske`.
- **Map:** nomadix-socials `brands/fonske/`. De secties "Weektaak", "Foto's van de crawl" en "Feiten (niets bijverzinnen)" in de README gelden strikt.
- **Bron:**
  - datum, uur, plek en prijzen van crawls enkel uit SellQo (`event_details` met status 'scheduled', prijs uit `products`);
  - early bird enkel noemen als de deadline in de toekomst ligt;
  - wat erbij zit enkel van de site;
  - geen cafénamen, geen deelnemersaantallen, geen reviews, geen "sold out".
- **Crawlfoto's en -video:**
  - query_database op project `377b3ca5-a57f-413e-a53a-dc1889be4b40`, enkel avonden met `crawl_nights.published = true`, met de query uit de README;
  - download via `https://mrwiqgrxsyphbxiahule.supabase.co/storage/v1/object/public/crawl-photos/<path>`;
  - bekijk elke foto zelf en zet ze in `photos.json` volgens de README (twijfel = niet opnemen).
  - Lukt het downloaden niet: meld dat. Akke moet dan het domein toelaten in de netwerkinstellingen van de cloudomgeving.
- **Planning:** +1 item in een crawlweek; een gepubliceerde avond zonder recap krijgt een recap-carrousel. Getekende scènes enkel als aanvulling.
