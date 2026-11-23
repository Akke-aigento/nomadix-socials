# Film: een (nieuw) merk opnemen in de AI-filmmachine

Akke 23-11: "per merk typisch, en als er ooit merken bijkomen hier gewoon op doorpakken, met research op de websites zelf en een brede research-bar."

Voor elk merk (ook nieuwe) staat dit klaar in `brands/<slug>/film/`:

1. **`ideeen.md` — ideeënbank uit research**
   - De eigen site lezen (WebFetch), plus concurrenten en vergelijkbare makers.
   - Trends en formats in de niche van dit jaar: wat gedeeld en bewaard wordt.
   - Resultaat:
     - merkessentie in 5 regels;
     - 6–8 vaste reeksen (hook-patroon, shotstructuur, stijl, stem, bron);
     - 30 losse ideeën;
     - seizoenshaken;
     - bronnen.
   - Elke 3 maanden vernieuwen, of zodra de scores dalen.
2. **`cast/` — castbladen.** Elk vast personage, dier of voorwerp (een auto, mascotte of product) krijgt een castblad, gemaakt met nano-banana-pro en het echte beeld als referentie. Een product wordt nooit verzonnen: het echte product komt altijd als referentie mee.
3. **`stijl.md` — beste stijl en model per reeks.** Komt uit de lab-experimenten (`shared/LAB.md`): stijl × model × aanpak, met juryscores in `shared/FILM-SCORES.csv`.
4. **`stemmen.md` — vaste stemmen.** Per personage een ElevenLabs-voice_id, en een voice-overstem per merk.

**Wekelijks** kiest de weektaak:
- een idee uit `ideeen.md`, afwisselend uit de reeksen en de losse ideeën, en nooit hetzelfde binnen 6 weken;
- het recept uit `stijl.md`.

Daarna maakt de weektaak de film en laat hem door de JURY gaan. Onder 8/10 maakt ze hem opnieuw; pas dan gaat hij naar SellQo als "te keuren".

**Leren:**
- Juryscores en, zodra beschikbaar, Instagram-cijfers (views, sends, saves, kijkduur) komen per film in `FILM-SCORES.csv`.
- Reeksen en recepten die winnen, krijgen meer beurten; wat zwak scoort, valt af.
- Elke terugkerende fout wordt een regel in `FILM-LESSEN.md`.
