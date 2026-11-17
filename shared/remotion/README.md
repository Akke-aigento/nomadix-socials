# Remotion-motor (POSTS-2)

Reels en carrouselslides voor alle Nomadix-merken, met echte motion design in plaats van zelfgeschreven HTML-animaties.
Licentie: Remotion Free License (individuen en bedrijven tot 3 personen; Nomadix BV valt daaronder). Wordt dit ooit een
geautomatiseerde dienst voor SellQo-klanten (SOCIAL-ENGINE-1), dan is een Company License nodig ("Remotion for Automators").

## Gebruik

    shared/remotion/render.sh reel  props.json uit.mp4     # 1080x1920, 30 fps, h264
    shared/remotion/render.sh slide props.json uit.jpg     # carrouselslide 1080x1350
    shared/remotion/render.sh story props.json uit.jpg     # story 1080x1920

- Eerste keer installeert het script zelf (`npm ci`). Het gebruikt de Chromium uit /opt/pw-browsers (of `REMOTION_BROWSER`).
- Paden in de props zijn relatief: `brands/<slug>/...` en, voor Loveke, `loveke/...` (zet `LOVEKE_DIR=/pad/naar/loveke-repo`).
- Een reel van 12 s rendert in ± 80 s.
- Officiële Remotion-skills (best practices, captions, maps, transitions): `git clone --depth 1 https://github.com/remotion-dev/skills /tmp/remotion-skills` en lees `skills/remotion-best-practices/SKILL.md` en `skills/remotion-markup/`. Nieuwe composities horen in `src/`, met een voorbeeld-JSON in `examples/`.

## Reel-props (`src/Reel.tsx`)

| veld | wat |
|---|---|
| `brand` | vanxcel, fonske, sellqo, studio-akke, loveke (huisstijl in `src/themes.ts`) |
| `hook` | korte tekst die de eerste 1,8 s groot in beeld springt (verplicht) |
| `scenes[]` | `clip` (echte video, `from` = startseconde, `caption`), `image` (Ken Burns: `move` in/out/left/right/up), `title` (kicker/title/sub, `\n` = nieuwe regel, laatste regel in accentkleur), `end` (title/sub/cta + logo) |
| `transition` | slide (standaard), fade, wipe of cut |
| `music`, `sting` | bibliotheeknummer en merksting (`brands/<slug>/music/…`) |
| `captionStyle` | pop (standaard, woord per woord) of bar |

Ondertitels staan altijd in de veilige zone (boven 250 px en onder 340 px vrij).
**Kies `from` pas nadat je frames van de clip bekeken hebt**: het begin van een clip is vaak niet het beste stuk.

## Slide-props (`src/Slide.tsx`)

`layout`: photo (beeld vult alles, titel onderaan), split (beeld boven, tekst onder), statement, list (`items[]`), cta.
`title` met `*woord*` = accentkleur. `tone`: dark, accent of light. `page` ("2/6"), `swipe` (op slide 1).

Voorbeelden: `examples/`.
