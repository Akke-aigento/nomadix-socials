# POSTS-2 — betere posts (vanaf week 23 nov 2026)

Beslist door Akke op 17-11-2026 na een week die "niet zo geweldig" was. **Bij verschil met een README, VARIATIE.md of GENRES.md gaat dit document voor.**
Achtergrond en bronnen: projectdoc `claude/voorstel-betere-posts.md`.

## 0. Wat Instagram beloont (2026)

1. **Kijktijd**, dan **sends per bereik** (doorsturen via DM weegt 3–5× zwaarder dan een like voor niet-volgers), dan likes per bereik.
2. **Origineel en menselijk** boven gepolijst. Een "mooi kaartje" is goedkoop en wordt overgeslagen.
3. **Reels = bereik, carrousels = diepgang.** Carrousels halen het meeste engagement per bereikte persoon en de meeste saves.
4. Reel-basis: hook in de eerste seconde, ondertitels, audio, geen watermerk, max. 3 min (wij: 8–25 s).

## 1. Week per merk: 4 items, niet meer

| # | Soort | Doel | Regel |
|---|---|---|---|
| 1 | **Reel** | bereik, sends | echt beeld (clip, foto's, schermopname), gemaakt met `shared/remotion` (geen HTML-animatie meer) |
| 2 | **Carrousel** 5–8 slides | saves, diepgang | één van de vijf structuren (§3), slides met `shared/remotion` (Slide) of een eigen template met echte foto |
| 3 | **Post** (1 beeld) | gesprek | echte foto of één sterke zin; geen ontwerp om het ontwerp |
| 4 | **Story** | band met volgers | rauw: foto of korte clip + 1 regel, of een sticker-vraag/poll (`manual`) |

Uitzondering: een event (Fonske crawlweek) of een productlaunch mag 1 item extra.
Uren volgens `shared/POSTTIJDEN.md` (de beste slots uit de eigen data).

## 2. Voor je iets maakt: de drie vragen

Schrijf per item in `log.md`:
1. **Naar wie stuurt iemand dit door, en waarom?** ("naar mijn lief, want dat zijn wij", "naar mijn maat die zijn camper bouwt, want hij doet dat fout"). Geen goed antwoord = ander idee.
2. **Wat is de hook in 1 seconde?** Beeld + tekst in beeld (+ gesproken zin als er stem is) moeten samen hetzelfde zeggen.
3. **Wat is het ene idee?** Eén item = één idee. Twee ideeën = twee items (of één ervan schrappen).

Hookvormen (marketingskills `social`): nieuwsgierigheid ("Niemand vertelt je dit over…"), verhaal ("Dag 83. De weg hield op."), waarde ("3 fouten in elke camperbouw"), tegendraads ("Duurdere accu's zijn niet beter"). Altijd gevuld met een **echt feit, getal of moment** uit de bronnen: nooit een lege formule.

## 3. Carrouselstructuren (kies er één, noteer welke)

- **Value-Stack**: belofte → 4–6 concrete stappen/tips → samenvatting → CTA "bewaar dit".
- **Problem-Proof**: herkenbaar probleem → waarom het misgaat → bewijs/voorbeeld → oplossing → CTA.
- **Hack List**: "X dingen die…" → één per slide, elk met een echt detail.
- **Rant Callout**: een mythe in de niche → waarom ze niet klopt (met bron) → wat wel.
- **Demo Walkthrough**: stap voor stap door iets echts (bestelling, installatie, scherm) met echte beelden.

Slide 1 is de hook (groot, kort, swipe-reden). Laatste slide = één CTA. Tekst op slides min. 34 px, max. ±25 woorden per slide.

## 4. Echt beeld eerst

- VanXcel: `brands/vanxcel/clips/` (41 clips) en `media/` (342 foto's).
- **Elke clip door `shared/remotion/clipcheck.sh <clip> <from> <dur> [speed]`** en de strip bekijken: elk frame van het fragment moet kloppen met de ondertitel. Eén frame dat niet klopt = ander fragment, kortere `dur` of `speed` 0,5. (17-11: "A river in full flow" liep 1,5 s door op een brugdek. Akke zag het meteen.)
- Fonske: Crawl Log-foto's en -video (enkel gepubliceerde avonden), getekende scènes enkel als aanvulling.
- Loveke: strip 1 en 2, productfoto's, en elke clip/foto die Akke in de mediabibliotheek zet (map `brand`, hartje = voorkeur).
- SellQo en Studio Akke: schermopnames/screenshots van de echte app of sites (demowinkels, portfolio), nooit klanttenants.
- **Nieuw materiaal van Akke gaat altijd voor** (mediabibliotheek, laatste 14 dagen, `is_favorite` eerst).
- Wat níet: AI-gegenereerde foto's van mensen of producten, stockbeelden.

## 5. Gereedschap

- Reels en slides: `shared/remotion/` (README). Ondertitels altijd aan (woord per woord), hook-tekst in de eerste 1,8 s, merksting op het einde, bibliotheekmuziek.
- Skills (lees ze bij elke weektaak):
  - `git clone --depth 1 https://github.com/coreyhaines31/marketingskills /tmp/mskills` → `skills/social/SKILL.md`, `references/carousel-frameworks.md`, `references/short-form-video.md`, `references/reverse-engineering.md` (MIT).
  - `git clone --depth 1 https://github.com/remotion-dev/skills /tmp/remotion-skills` → `skills/remotion-best-practices/`, `remotion-markup/`, `remotion-captions/`.
  - Skill `frontend-design` (als die in de sessie zit) voor typografie en compositie.
- Referenties per merk: `brands/<slug>/referenties.md` (Loveke: `loveke/marketing/instagram/referenties.md`). Gebruik ze als maatstaf: "zou dit item tussen hun beste posts passen?"

## 6. Kwaliteitspoort (verplicht vóór iets in SellQo komt)

Score elk item 0–2 op: **hook in 1 s · sendbaar (vraag 1) · één idee · echt beeld · leesbaar op gsm (tekst ≥ 34 px, contrast) · merkregels en feiten**. Max. 12.
- **< 9 = opnieuw maken of schrappen.** Liever 3 sterke items dan 4 met één zwakke.
- Daarna een **tweede, onafhankelijke review**: als de Agent-tool beschikbaar is, laat een subagent (zonder de maakgeschiedenis) de contactsheet + captions beoordelen op dezelfde 6 punten en op "zou een mens dit doorsturen?". Zonder Agent-tool: zelf de contactsheet opnieuw bekijken alsof je hem voor het eerst ziet, en de zwakste eruit halen.
- Noteer de scores in `log.md`.

## 7. Wat blijft gelden

Spelregels uit het masterplan (niets verzinnen, prijzen live, geen greenwashing, geen ongeverifieerde reviews, geen emoji in beelden), veilige zones, `content_tags` volgens `LEREN.md` (+ `genre` = de carrouselstructuur of het reelformat, `quality` = score), UTM-links, nooit `approved`/`posted` zetten.
GENRES.md en VARIATIE.md blijven bruikbaar als **ideeënbron**, niet als verplichting: variatie komt uit verschillende ideeën en echte beelden, niet uit trucjes.
