# Geplande social-taken: algemene werkwijze

Sinds 21-11-2026 draaien alle social-taken als **Code-taken** (claude.ai/code/scheduled) met de repo's vast ingesteld. De vroegere "Chat"-taken voegden de repo's tijdens de run toe met `add_repo`. Sinds 20-11 weigert een geplande run dat (403), waardoor "Opnieuw maken" 24 keer na elkaar faalde. De oude taken staan uit.

Elke taak heeft een korte opdracht: "Lees en volg `shared/taken/ALGEMEEN.md` en daarna `shared/taken/<taak>.md`". De echte instructies staan dus hier en worden via git aangepast, niet in de taakinstellingen.

## Omgeving

- **Repo's** staan al gecloond in `/home/user/` (`nomadix-socials`, `loveke`, `sellqo`, `studioakke`), elk op een eigen `claude/…`-branch. Voeg nooit zelf een repo toe (`add_repo` bestaat hier niet of werkt niet) en clone deze vier niet opnieuw.
- **Schrijven naar een repo** gebeurt altijd op main:
  ```
  cd /home/user/<repo> && git fetch origin main && git checkout -B main origin/main
  … werk, git add (gericht, nooit node_modules/ of out/), git commit …
  git push origin main   # geweigerd: git fetch origin main && git rebase origin/main && opnieuw pushen
  ```
  Lees ook altijd van een verse main (dezelfde eerste regel), zodat je het werk van andere taken ziet.
- **SellQo-database:** Lovable-connector `query_database`, project `9932a7fe-43a1-42de-9c64-168968599600`. Akke Insights: project `f639dfa8-ad8f-4c7f-9b35-9672dd0fefbc` (enkel lezen).
- **Externe skills:** `shared/taken/vendor/marketingskills-social/` (MIT, coreyhaines31/marketingskills, skill `social` met `references/`). Remotion-skills: probeer `git clone --depth 1 https://github.com/remotion-dev/skills /tmp/remotion-skills`. Lukt dat niet, ga dan verder met `shared/remotion/README.md`; dat is niet fataal.
- **Projects-tool** (brand bible `claude/brand-<slug>.md`) is er meestal niet. Dan volstaan de README's in de repo.
- **Renderen:** `PLAYWRIGHT_MODULE=/opt/npm-tools/node_modules/playwright/index.mjs` en `PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers` voor HTML-templates, `shared/remotion/render.sh` voor reels en slides (Loveke: `LOVEKE_DIR=/home/user/loveke`). Ontbreekt een pad, zoek het (`ls /opt`, `npx playwright`) in plaats van te stoppen.

## Bericht aan Akke

Waar een taak "stuur Akke een boodschap (SendUserMessage)" zegt: gebruik `SendUserMessage` als die tool er is. Anders is je **laatste antwoord** het bericht; dat komt als melding bij Akke. Nederlands (Vlaams), kort, "maat". Is er niets te doen, dan antwoord je enkel "Niets te doen." en verder niets.

## Vaste regels (altijd)

- Nooit iets op `approved` of `posted` zetten; dat doet Akke.
- Niets verzinnen: prijzen, voorraad, data en claims komen live uit SellQo of de bron van het merk. Geen greenwashing, geen ongeverifieerde reviews, geen doorstreepte prijzen, geen emoji in beelden.
- Publieke repo nomadix-socials: nooit paspoorten, papieren, chats of beelden die niet online mogen.
- Wijzig in SellQo enkel wat de taak uitdrukkelijk toelaat.
- **Meldingen bij een blokkade: maximaal één per merk per dag.** Controleer eerst of er al een melding is: `select count(*) from notifications where tenant_id='<t>' and data->>'kind'='<kind>' and created_at > now() - interval '24 hours'`. Is die er al: stil stoppen (Akke, 21-11: 24 dezelfde meldingen op een dag is spam).

## Merken

| Merk | Tenant | Taal content | Map |
|---|---|---|---|
| Loveke | 1671a91c-31fe-42ed-8a10-41f3117ceb50 | nl | loveke: `marketing/instagram/` |
| VanXcel | 54f6b480-280b-42e1-b843-d5beb2831acd | en | nomadix-socials: `brands/vanxcel/` |
| SellQo | d03c63fe-48c6-4ff7-a30b-7506ea3e71ab | nl | nomadix-socials: `brands/sellqo/` |
| Studio Akke | c96fb1b2-ddac-44d1-a638-72dd54efd31e | nl | nomadix-socials: `brands/studio-akke/` |
| The Fonske Crawl | 95f6685b-3474-42fe-81ad-a5e6ca3d6806 | en | nomadix-socials: `brands/fonske/` |
