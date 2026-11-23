# FILMLAB — experimenten (stijl × model × aanpak)

Doel (Akke 23-11): ontdekken hoever AI-video kan gaan en een systeem bouwen dat elke film beter maakt. Elk experiment: één vaste testscène, meerdere modellen/stijlen, de jury (JURY.md) scoort, winnaars worden recepten.

## Modellen via imgeditor (`ie_video`, kosten 23-11)
| Model | id | Kosten | Duur | Beeld als start | Bijzonder |
|---|---|---|---|---|---|
| Veo 3.1 Fast | veo-3.1-fast | 35 (8 s 1080p) | 8 | image_url e.a. | volgt startbeeld slecht, gezichten drijven (lab 23-11) |
| Veo 3.1 | veo-3.1 | 120 (4 s 720p) · 180 (6 s 720p) · 260 (8 s 1080p) | 4/6/8 | image_url e.a. | stabiel, zegt exact de dialoog |
| Seedance 1.5 Pro | seedance-1.5 | 50 (4 s 720p) · 95 (8 s 720p) | 4/8/12 | image_url e.a. | verzint extra dialoog (lab 23-11) |
| Seedance 2.5 | seedance-2.5 | 120 (4 s 480p) · 175 (6 s 480p) · 330 (5 s 720p) · 935 (8 s 1080p) | 4–30 | NIET via image_url: geef `first_frame_image`/`image`/`reference_image_urls` mee (anders negeert hij het startbeeld) | audio-referentie (`reference_audio_urls`, 2–30 s) werkt: zegt de zin met onze stem; tot 30 beeld- en 10 audioreferenties |
| MiniMax H3 | minimax-h3 | 130 (6 s 768p) | 4–15 | idem Seedance 2.5 (omni) | resolutie 768p/2k |
| Kling O3 Pro | kling-o3-pro | 340 (5 s 720p) | 5/10 | alleen image_url (omni-velden → fout) | |
| Kling O3 | kling-o3-std | 270 (5 s 720p) | 5/10 | | |

- `name` mag geen punt bevatten (`hug-veo31`, niet `hug-veo-3.1`).
- Kosten vooraf: `ie_cost` met `{type:'video', model_id, duration, resolution, generate_audio}`.

## Stijlen (beginbeelden met nano-banana-pro + castblad)
comic (huidige strip) · real (filmisch fotorealistisch) · 3d (animatiefilm) · paint (geschilderd).
Realistische weergave van Akke en Nastya: enkel intern tot beiden akkoord geven.

## Experiment 1 — perron "You came!" (23-11)
Beelden: `social-media/loveke/lab/perron-<stijl>.jpg`, clips `perron-<stijl>-<model>.mp4`. Juryscores: zie FILM-SCORES.csv.

### Uitslag experiment 1 (jury, 23-11)
Winnaar: **3D + Veo 3.1 = 8,4** (enige boven de poort). Real: Veo 3.1 en Seedance 2.5 7,4 · comic: Seedance 2.5 7,2 / Veo 3.1 7,0 · paint: Veo 3.1 7,2. Kling 3,8–4,6, Seedance 1.5 4,4–6,0.

Recept-regels:
1. Seedance 1.5 verzint altijd extra tekst → alleen zonder eigen audio gebruiken, stem en geluid apart.
2. Kling O3 Pro: geen audio, verdubbelt voorwerpen → niet voor overdrachten.
3. MiniMax H3: 1–2 s bevroren bij de start → eerste seconde wegknippen of een startactie geven.
4. Seedance 2.5: herkadreert, 480p → voor emotie en knuffels, daarna upscalen.
5. Veo 3.1: betrouwbaarste audio (exact de zin + ruimte); man laat voorwerpen niet los → prompt "he lets go, she holds it alone".
6. Knuffel met voorwerp: voorwerp achter de rug van de ander houden (anders geklemd of opgeslokt).
7. Startbeeld = rustpositie: personages volledig in de scène (niet met een voet in de trein).
