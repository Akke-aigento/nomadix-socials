# Muziek voor reels (alle merken)

## v2 (14 nov 2026): geluid met karakter

Beslissing Akke: "muziek is wat saai nu, maak er echt iets van." De eerste reeks was veilig: per merk zes sferen
(akoestisch, lo-fi, pop, funk). Vanaf nu:

1. **Genrewiel voor muziek.** Elk merk krijgt naast de bestaande sferen een reeks verrassende genres (tabel "Reeks 2" onderaan).
   Regel: nooit twee reels na elkaar in hetzelfde genre, minstens 3 verschillende genres per maand per merk, en het genre
   van de muziek past bij het genre van de reel (`GENRES.md` §5): een `ping`-reel krijgt percussie, een `tijdreis` iets dat bouwt.
2. **Structuur in de prompt.** Vraag om wat de montage nodig heeft: "quiet intro for 2 seconds, then the full beat",
   "big hit at 15 seconds, then a clean ending". Zet daarna de knippen op de beat (`SCENE = 60 / bpm` per tel).
3. **Geluidseffecten (SFX) als tweede laag.** `shared/reel.mjs` mengt nu `--sfx <bestand>@<seconde>[@<volume>]` over de muziek
   (meermaals mogelijk), of zonder muziek voor een reel die enkel op geluid draait (ping van een bestelling, bon die print,
   camera-flits, trein, de motor van Sandy). SFX-bestanden in `brands/<slug>/sfx/` of `shared/sfx/` met een `sfx.json` (bron, licentie).
   Bron: zie "SFX-bron" hieronder.
4. **Klankhandtekening (sting).** Per merk één kort herkenbaar slot van ±2 s (bv. Loveke: ukelele + handklap, VanXcel: diepe
   drone + metalen tik, SellQo: kassabel, Studio Akke: toetsenbordtik + synthblip, Fonske: koperstoot). Altijd hetzelfde,
   op het einde van elke reel via `--sfx sting.mp3@<duur−2>`. Zo herken je het merk met je ogen dicht.
5. **Echte stem of echt geluid van Akke** (optioneel): een spraakmemo of een opname uit de zaak maakt een reel meteen echter
   dan om het even welk nummer.
6. Trending audio uit de Instagram-app blijft handwerk (API kan het niet).

### SFX-bron (voorstel WATCHTOWER-SFX-1, wacht op go van Akke)

- ElevenLabs heeft naast Music ook **Sound Effects** (geluid uit een korte omschrijving, 0,5 tot 22 s, commercieel bruikbaar).
  De huidige sleutel `ELEVENLABS_MUSIC_API_KEY` mag enkel Music Generation. Nodig:
  1. Akke: in ElevenLabs een sleutel `nomadix-sfx` met enkel **Sound Effects**, als secret `ELEVENLABS_SFX_API_KEY` in Watchtower.
  2. Watchtower: route `/api/public/sfx-compose` naar het model van `music-compose` (zelfde `x-cron-secret`, zelfde bucket
     `social-music`, map `sfx/<merk>/`), body `{ name, prompt, duration_s }`.
  3. Eerste set per merk (±10 per merk): pint tappen, glazen klinken, kassabel, bonprinter, gsm-tik, trein op de rails, envelop
     openen, polaroid-flits, motor van een oude 4x4, grind onder banden, toetsenbord, muisklik, menigte die juicht.
- Tot dan: geen SFX uit willekeurige sites halen (licentie). Wel toegelaten: geluid dat Akke zelf opneemt.

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

## Reeks 2 (14 nov 2026): verrassende genres + stings

Gemaakt via Watchtower, model `music_v2_5`, 30 s, in `tracks.json` met de volledige prompt. De stings staan als `sting.mp3`
in de muziekmap (niet in `tracks.json`, ze zijn geen nummer): max 3,5 s, eindigt in stilte.

| Merk | Titel | Genre | BPM | Past bij reelformat |
|---|---|---|---|---|
| Loveke | Balkan Trein | accordeonfolk, treinritme | 132 | `parallax`, `zoom-uit` (de treinreis) |
| Loveke | Hartje | 8-bit chiptune | 140 | `stop-motion`, `fotohokje`, `quiz` |
| VanXcel | Steppe Strings | getokkelde luit + drone, bouwt op | 100 | `tijdreis`, `kaart-tekent` |
| VanXcel | Nachtrit | jaren-80 synthwave | 108 | `rauwe-clip` bij nacht, `slot` |
| SellQo | Kassa Percussie | funk met kassabel en bonprinter als drums | 112 | `ping`, `bon-print`, `pov-tik` |
| SellQo | Terras | bossa nova | 92 | horeca, `dag-in-het-leven` |
| Studio Akke | Typemachine | hiphop uit typemachine en muisklikken | 90 | `bouwwerf`, `scroll` |
| Studio Akke | Glitch | glitch-pop met drop | 140 | `glitch` (404) |
| Fonske | Straatfanfare | Belgische straatfanfare | 126 | `kaartflip`, `aftellen` |
| Fonske | Nachtjacht | surfrock | 150 | `kaart-tekent`, `rauwe-clip` |

Ideeën voor reeks 3 (telkens 2 per merk, nooit een artiest in de prompt): Loveke: Franse musette-wals, lo-fi bossa voor twee,
kinderliedjes-glockenspiel (bodysuit); VanXcel: Georgische meerstemmige zang als instrumentale bewerking (strijkers), desert blues-gitaar,
industriële percussie uit gereedschap; SellQo: swing big band "openingsuur", minimal techno uit scannerbiepjes, schlager-polka (knipoog);
Studio Akke: ambient piano, drum and bass, vaporwave; Fonske: ska met blazers, Ierse pubfolk, middeleeuwse luit en trommel (Leuven Lore 1225).

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
