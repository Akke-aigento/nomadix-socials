# Nomadix Socials

De contentmachine voor de Instagram (en later andere kanalen) van de Nomadix-merken.

- `shared/` — scripts voor alle merken: `render.mjs` (HTML → JPG), `reel.mjs` (HTML-animatie → MP4), `recipe.mjs` (recept voor "Tekst in beeld aanpassen" in SellQo).
- `shared/LEREN.md` — verplicht leren van resultaten: labels per post (`content_tags`), score na 48 uur, 70/20/10 (bewezen / verkennen / test), `lessen.md` per merk, UTM op elke link.
- `shared/POSTTIJDEN.md` — verplichte posttijden per merk: geen vaste uren, venster per publiek, één testslot per week, data gaat voor.
- `shared/MUZIEK.md` — muziekbibliotheek per merk (`brands/<slug>/music/`, Loveke in zijn eigen repo): ElevenLabs-nummers in de reel, zodat reels zonder handwerk online gaan; `shared/music-add.mjs` voegt een nummer toe.
- `shared/VARIATIE.md` — verplichte variatieregels voor alle merken: elke post uniek, wisselende formats, layouts en hooks.
- `brands/<slug>/` — per merk: huisstijl, templates, media, weken, gepubliceerde beelden, log en een README met de weekroutine.

Goedkeuren en publiceren gebeurt in **SellQo → Marketing → Social planning**. Deze repo is enkel bron en transport:
SellQo haalt beelden op via de raw-URL en kopieert ze bij publicatie naar zijn eigen opslag.

Alles in deze repo is publiek. Zet hier geen persoonlijke documenten, papieren of beelden die niet online mogen.

Playwright: `PLAYWRIGHT_MODULE=/opt/npm-tools/node_modules/playwright/index.mjs` (of `npm i playwright`).
