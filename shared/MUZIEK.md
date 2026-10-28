# Muziek voor reels (alle merken)

Stand: 28 okt 2026. Beslissing Akke: reels met muziek gaan **volledig automatisch**, net als posts en stories zonder sticker. Daarvoor zit de muziek al in de MP4 (`-muziek.mp4` → `video_url`). Muziek uit de Instagram-bibliotheek kan via de API niet; trending audio blijft dus handwerk ("Ik kies zelf muziek").

## Waar

| Merk | Map |
|---|---|
| Loveke | repo `Akke-aigento/loveke`, `marketing/music/` |
| VanXcel, SellQo, Studio Akke, Fonske | `brands/<slug>/music/` in deze repo |

Elke map heeft `tracks.json` (formaat hieronder). Een nummer zonder regel in `tracks.json` wordt niet gebruikt.

## Bron: ElevenLabs Music

- ElevenLabs Music (betaald plan). Commercieel gebruik op social media mag; geen naamsvermelding nodig.
- **Zo maak je nieuwe nummers** (bijvullen kan elke chat of taak met de Lovable-connector): Watchtower heeft de route `/api/public/music-compose` met de eigen sleutel `ELEVENLABS_MUSIC_API_KEY` (enkel Music Generation). Roep ze aan vanuit SQL op het Watchtower-project (`b9945398-c9e9-49cc-bc0b-97a3b0757531`), zodat het secret nooit in een chat komt:
  ```sql
  select net.http_post(url := 'https://watchtower.studioakke.com/api/public/music-compose',
    headers := jsonb_build_object('Content-Type','application/json','x-cron-secret', public.get_cron_secret()),
    body := jsonb_build_object('name','<merk>/<sfeer>-<titel>','length_ms',30000,'prompt','<prompt>'),
    timeout_milliseconds := 280000);
  -- ±60 s later: select status_code, content from net._http_response where id = <request_id>;
  ```
  Het nummer staat dan op `https://xlidgtxgqmsxxreghpdg.supabase.co/storage/v1/object/public/social-music/<merk>/<naam>.mp3` (domein toegelaten in de sandbox). Max **2 tegelijk** (ElevenLabs geeft anders 429). Daarna `music-add.mjs` hieronder.
- Eerste reeks: 28 okt 2026, 30 nummers (6 per merk), model `music_v2_5`.
- Altijd **instrumentaal**, 30 seconden (reels zijn 12–25 s).
- Nooit een artiest, band of bestaand nummer in de prompt (geen "in de stijl van …").
- Deze repo is publiek: de losse nummers zijn dus te downloaden. Dat is aanvaard (28 okt): de reels met de muziek staan sowieso publiek.

## Toevoegen

```
node shared/music-add.mjs brands/<slug>/music <bestand> --title "<titel>" --mood <sfeer1,sfeer2> --bpm <bpm uit de prompt> --prompt "<prompt>"
```

Het script zet de luidheid gelijk (-14 LUFS), maakt er mp3 192 kbps van (max 5 MB), meet duur en `best_start` en schrijft de regel. Luister of bekijk de golfvorm: klinkt het niet goed (vervormd, rare overgang, zang erin), niet toevoegen.

## Kiezen in de weektaak

1. Kies in `tracks.json` van het merk een nummer met de sfeer van de reel dat **het langst niet gebruikt** is. Nooit hetzelfde nummer als de vorige reel van dat merk; liefst niet vaker dan eens per maand.
2. Zet de scèneduur op de beat: `SCENE = 4 * 60 / bpm` (4 tellen).
3. Render met `--music <map>/<file> --music-start <best_start>` → `-stil.mp4` en `-muziek.mp4`.
4. In SellQo: `video_url` = `-muziek.mp4`, `video_silent_url` = `-stil.mp4`, `music_hint.track` = `{ "title", "source": "ElevenLabs Music", "license" }`, en status zoals een post: Instagram gekoppeld = `pending_approval` (gaat na "Week goedkeuren" vanzelf online), niet gekoppeld = `manual` + `other`.
5. `music_hint.songs` (3 trending nummers) is dan **optioneel**: enkel als je een goede actuele bron hebt, voor wie toch zelf muziek wil kiezen.
6. Voeg `"<maandag> reel-<onderwerp>"` toe aan `used` en noteer het nummer in `log.md`.
7. Geen passend nummer (lege bibliotheek of geen enkele sfeer past): zoals vroeger `manual` + `music`, en meld het aan Akke ("bibliotheek <merk> aanvullen: <sfeer>").

## Prompts (eerste reeks, 6 per merk)

Instelling in ElevenLabs: Instrumental aan, duur 30 s. Kopieer de prompt letterlijk.

### Loveke (warm, grappig, streetwear, liefdesverhaal)
| Titel | Sfeer | BPM | Prompt |
|---|---|---|---|
| Zachte Ochtend | warm, akoestisch | 96 | Warm acoustic guitar and soft hand percussion with a gentle ukulele, cozy and romantic, sunny morning, 96 BPM, instrumental, clean ending |
| Sticker Pop | vrolijk, pop | 118 | Upbeat indie pop with bright electric guitar, hand claps and a bouncy bass line, playful and happy, 118 BPM, instrumental, clean ending |
| Nachttrein | lo-fi, chill | 84 | Lo-fi hip hop with mellow Rhodes piano, soft vinyl crackle and relaxed boom-bap drums, nostalgic night train, 84 BPM, instrumental |
| Straatfunk | funk, energiek | 108 | Light funk groove with slap bass, wah guitar and tight drums, confident streetwear swagger, 108 BPM, instrumental, clean ending |
| Perron | emotioneel, piano | 72 | Emotional solo piano with soft strings slowly swelling, bittersweet goodbye at a train station, 72 BPM, instrumental |
| Samen Sterk | energiek, pop | 124 | Energetic electro pop with punchy drums and bright synth stabs, joyful and confident, 124 BPM, instrumental, clean ending |

### VanXcel (filmisch, avontuur, techniek; Engels merk)
| Titel | Sfeer | BPM | Prompt |
|---|---|---|---|
| Open Steppe | filmisch, rustig | 90 | Cinematic ambient road trip with wide warm pads and slowly building drums, sense of distance and open plains, 90 BPM, instrumental |
| Long Road | indie, avontuur | 110 | Driving indie folk with strummed acoustic guitar and a steady kick drum, adventurous and free, 110 BPM, instrumental, clean ending |
| Clean Current | techniek, elektronisch | 120 | Minimal electronic pulse with a clean synth arpeggio and tight hi-hats, precise and technical, 120 BPM, instrumental |
| Mountain Dawn | rustig, gitaar | 80 | Warm ambient electric guitar with light delay, dawn in the mountains, calm and hopeful, 80 BPM, instrumental |
| Gravel | rock, energiek | 100 | Gritty blues rock riff with stomping drums, rugged off-road energy, 100 BPM, instrumental, clean ending |
| Workbench | lo-fi, chill | 88 | Chill lo-fi beat with soft keys and mellow bass, focused workshop build session, 88 BPM, instrumental |

### SellQo (helder, nuchter, knipoog; ondernemers)
| Titel | Sfeer | BPM | Prompt |
|---|---|---|---|
| Open Voor Zaken | vrolijk, pop | 116 | Friendly modern pop with marimba, plucked synths and hand claps, optimistic small business vibe, 116 BPM, instrumental, clean ending |
| Focus | lo-fi, chill | 85 | Lo-fi beat with warm electric piano and soft drums, focused and calm, 85 BPM, instrumental |
| Kassa Groove | house, energiek | 122 | Light deep house groove with clean piano chords and a smooth bass line, modern and positive, 122 BPM, instrumental |
| Knipoog | speels | 104 | Playful pizzicato strings and glockenspiel with light percussion, a wink of humor, 104 BPM, instrumental, clean ending |
| Bouwlog | elektronisch, opbouw | 112 | Indie electronic with a steady kick and rising synth arpeggios, a sense of progress and building, 112 BPM, instrumental |
| Eerlijk Werk | warm, akoestisch | 96 | Warm acoustic guitar with a soft shaker, honest and human, 96 BPM, instrumental, clean ending |

### Studio Akke (technisch, rustig, modern)
| Titel | Sfeer | BPM | Prompt |
|---|---|---|---|
| Nachtcode | synthwave, rustig | 98 | Calm synthwave with soft analog pads and a gentle arpeggio, city at night, 98 BPM, instrumental |
| Strak | minimal, techniek | 120 | Minimal tech beat with crisp percussion and a subtle bass line, precise and clean, 120 BPM, instrumental |
| Regen Op Het Raam | lo-fi, chill | 82 | Lo-fi beat for coding with mellow keys and a soft rain texture, 82 BPM, instrumental |
| Luchtig | garage, modern | 130 | Future garage with airy chords and shuffled drums, modern and calm, 130 BPM, instrumental |
| Opbouw | ambient, opbouw | 100 | Ambient electronic with slowly rising pads and pulses, something coming together step by step, 100 BPM, instrumental |
| Live | elektronisch, energiek | 118 | Upbeat electro pop with bright synths and a confident beat, launch day energy, 118 BPM, instrumental, clean ending |

### The Fonske Crawl (pubcrawl Leuven; Engels merk)
| Titel | Sfeer | BPM | Prompt |
|---|---|---|---|
| Brass Night | feest, koper | 120 | Festive brass band party groove with trumpets and tuba, lively European street celebration, 120 BPM, instrumental, clean ending |
| Old Market | indie, energiek | 128 | Indie rock with jangly guitars and driving drums, a night out with friends, 128 BPM, instrumental, clean ending |
| Pub Stomp | folk, feest | 112 | Upbeat pub folk with accordion and fiddle, stomping and clapping, 112 BPM, instrumental, clean ending |
| Disco Round | disco, funk | 118 | Disco funk with a four-on-the-floor beat, funky rhythm guitar and strings, 118 BPM, instrumental |
| Swing By | swing, speels | 124 | Electro swing with brass and a modern beat, playful and cheeky, 124 BPM, instrumental, clean ending |
| Morning After | chill, nostalgisch | 92 | Warm nostalgic indie pop with soft guitars, the morning after a great night, 92 BPM, instrumental |
