# JURY — vaste beoordeling van elke AI-film (Akke 23-11: "zelflerend, tot 100% perfect")

Elke film (en elke testshot in het lab) gaat langs deze jury vóór Akke hem ziet. De jury heeft de film niet gemaakt (aparte subagents). Zelfde schaal, altijd, zodat scores vergelijkbaar zijn over weken.

## Jury (3 rollen, elk een aparte subagent)
1. **Verhaal & social** — hook in 1 s, spanning/pointe, begrijpbaar zonder geluid, deelbaar, merk, CTA.
2. **Beeld & AI** — 6 fps contactsheets: AI-fouten (vervormen, opduiken, drift van gezicht/kleren/props), bewegingskwaliteit (acteert het of wiebelt het), shotvariatie, kadrering, ondertitels.
3. **Geluid & montage** — stemmen (acteren of vlakke TTS), lipsync, sfeer/foley, muziek en mix, loudness (doel −14 LUFS, −1 dBTP), shotlengtes, ritme, ondertiteltiming.

## Schaal (elke rol, 0–10)
- 9–10: niet van echt/studio te onderscheiden, je wil het delen.
- 7–8: goed, één zichtbare zwakte.
- 5–6: oké, maar je ziet dat het AI/goedkoop is.
- ≤4: niet posten.

**Poort:** gemiddelde ≥ 8 én geen enkele AI-fout → naar Akke. Anders: de zwakste punten oplossen en opnieuw jureren.

## Na elke jurering
- Score + datum + film + werkwijze (model, shotlengte, geluid) in `shared/FILM-SCORES.csv`.
- Elke terugkerende fout → regel in `FILM-LESSEN.md`.
- Elk lab-experiment: één variabele tegelijk; winnaar wordt standaard in `FILM.md`.
- Akke's eigen oordeel telt als vierde stem en overrulet de jury.
