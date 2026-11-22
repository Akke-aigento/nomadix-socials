# FILM-1 — echte korte films in plaats van slideshows (sinds 22-11-2026)

Akke (22-11): "Denk aan echte filmpjes maken, niet gewoon slideshows. Maak de karakters echt, vertel iets nuttigs, laat de strip tot leven komen." De reel van elk merk is voortaan een **film**: bewegende beelden met eigen geluid, personages die bewegen en praten, voice-over waar het helpt, muziek eronder. Geen foto's die schuiven, geen sting.

## 0. Stand 22-11 (avond): imgeditor in plaats van ElevenLabs-video

- **ElevenLabs Image & Video vraagt een Pro-plan; dat nemen we niet** (Akke, 22-11). Video en beelden lopen via **imgeditor.co** op Akkes bestaande credits (±5.700): Nano Banana 2 Pro (beelden, 12 credits in 2K) en **Veo 3.1 Fast** (8 s, 9:16, 1080p, met geluid, 35 credits). Een film van 6 shots kost dus ±300 credits.
- **Nu met de hand via Claude in Chrome**, in meerdere tabs tegelijk. Resultaten staan publiek op `file2.ilovevideo.ai/...` en zijn vanuit de sandbox te downloaden.
- **Automatisch** zodra Akke in imgeditor een API-sleutel maakt, die als secret `IMGEDITOR_API_KEY` in Watchtower zet en Watchtower publiceert: `media-compose` heeft dan `ie_image`, `ie_video`, `ie_status` en `ie_credits` (code staat al op main).
- **Stemmen van Veo zijn onbruikbaar** (Akke: "echo, precies een alien"). Altijd `no speech` in de prompt en `speech, talking, words` in de negatieve prompt. Dialoog komt van een vaste ElevenLabs-stem per personage (`media-compose` `voice`, werkt op het huidige plan na publicatie van Watchtower), of als tekst op het scherm.
- **Personages:** vaste cast met modelblad, expressiebladen en vaste beschrijving. Loveke: `loveke/marketing/films/characters/CAST.md`. Elk begin- en eindbeeld krijgt die bladen als referentie.
- **Tegen drift:** elke shot krijgt een begin- én eindbeeld (imgeditor → Advanced Settings → End Frame), geen inzooms en een negatieve prompt. Zie CAST.md.
- **Controle:** contactsheet per shot (8 frames) naast het modelblad, en spraakherkenning (faster-whisper `small`) op elke shot om te weten wat er echt te horen is. Whisper verzint zinnen op een egale ruis: herhaalt hij dezelfde zin, dan is het ruis.

## 0b. Stand 22-11, 23u30: volledig via de API (dit is de werkwijze)

- **Watchtower EU** (`watchtower.studioakke.com`, Lovable-project `b587da4f-11c6-414a-9136-da44d0e3df93`, repo `Akke-aigento/akke-watchtower-eu`). Het oude project `b9945398…` is niet meer live. SQL-aanroepen gaan altijd naar het EU-project.
- **Resultaten**: `https://c--28cdb60f-f164-4d66-883b-5998725b2d37-prod.lovable.cloud/storage/v1/object/public/social-media/<name>.<ext>` (bereikbaar vanuit de sandbox).
- **Beeld** (`ie_image`, `params`): `{model:'nano-banana-pro', mode:'image', aspect_ratio:'9:16', resolution:'2K', output_format:'jpeg', image_url:<vak>, image_urls:[<vak>, <castblad>, <expressieblad>], prompt}`. Kost 6 credits.
- **Shot** (`ie_video`, `params`): `{model_id:'veo-3.1-fast', aspect_ratio:'9:16', resolution:'1080p', duration:8, generate_audio:true, image_url/start_image_url/first_frame_url:<begin>, end_image_url/last_frame_url/end_frame_url/tail_image_url:<eind>, image_urls:[begin, eind], negative_prompt, prompt}`. Kost 35 credits. Het eindbeeld wordt gerespecteerd (getest: het laatste frame valt samen met het eindbeeld). Laat alle sleutels staan, want de API documenteert niet welke gebruikt wordt.
- **Ophalen**: `ie_status` met `kind` en `name`. Beeld ±60 s, video ±3–4 min.
- **Stem** (`voice`): `voice_id` van de cast (CAST.md), ook stemmen uit de bibliotheek zonder ze toe te voegen. Max. 3 tegelijk (ElevenLabs 429). `voice_search` zoekt in de bibliotheek. `voice_add` werkt niet: de sleutel heeft geen voices_write.
- **Veo verzint dialoog.** Zet het volume van elke shot met spraak op 0 en gebruik spraakherkenning op de shot om te zien wanneer de mond beweegt. Leg de vaste stem (`voices` in de Film-props) op dat moment.
- **Pilot 2 "Pub crawl"** (strip 2 p. 6–7): 9 begin- en eindbeelden, 5 shots, 4 stemmen, ±250 credits. Twee beelden afgekeurd: dubbele rugzak, jeans in plaats van rok.

## 1. De motor

| Stap | Waar | Wat |
|---|---|---|
| Keyframe | Watchtower `media-compose`, `action: image` | Nano Banana Pro (`gemini-3-pro-image`) tekent een 9:16-beginbeeld uit een stripvak, productfoto of reisfoto als referentie, in de stijl van de bron |
| Shot | `action: video` | Veo 3.1 (`veo-3.1-generate-001`) animeert dat beginbeeld (`start_frame.generation_id`) tot 4, 6 of 8 s video **met geluid**: sfeer, effecten en korte dialoog |
| Ophalen | `action: status` + `name` | zet het resultaat in de bucket `social-media` van Watchtower: `https://xlidgtxgqmsxxreghpdg.supabase.co/storage/v1/object/public/social-media/<name>.mp4` (bereikbaar vanuit de sandbox) |
| Stem | `action: voice` | ElevenLabs-stem met tijd per woord → mp3 + JSON (`words`) voor ondertitels die exact meelopen |
| Montage | `shared/remotion/render.sh film <props.json> <uit.mp4>` | compositie `Film`: shots met hun eigen geluid, crossfades, ondertitels (vaste `lines` of uit de stem), muziek die wegduikt onder stem, eindkaart |

De ElevenLabs-sleutel blijft op de server. Elke aanroep gaat vanuit SQL op het Watchtower-project (`b9945398-c9e9-49cc-bc0b-97a3b0757531`) met de Lovable-connector:

```sql
select net.http_post(url := 'https://watchtower.studioakke.com/api/public/media-compose',
  headers := jsonb_build_object('Content-Type','application/json','x-cron-secret', public.get_cron_secret()),
  body := '<JSON>'::jsonb, timeout_milliseconds := 280000);
-- daarna: select status_code, content from net._http_response where id = <request_id>;
```

Bodies:
- beginbeeld: `{"action":"image","model":"gemini-3-pro-image","aspect_ratio":"9:16","resolution":"2K","prompt":"<stijl + beeld>","images":["https://raw.githubusercontent.com/Akke-aigento/…/vak.jpg", …]}` → `{id}`
- shot: `{"action":"video","model":"veo-3.1-generate-001","prompt":"<beweging + geluid>","start_frame":{"generation_id":"<id beginbeeld>"},"duration_secs":6,"aspect_ratio":"9:16","resolution":"1080p","generate_audio":true}` → `{id}`
- ophalen: `{"action":"status","kind":"video","id":"<id>","name":"loveke/films/<film>/<shot>"}` → `{status, url}`. Video: hooguit om de 10 s pollen; een shot duurt 1–4 minuten.
- stem: `{"action":"voice","name":"sellqo/films/<film>/vo","voice_id":"<id>","text":"…","model_id":"eleven_multilingual_v2"}`; stemmen opzoeken met `{"action":"voices"}`.
- Referentiebeelden mogen enkel van `raw.githubusercontent.com/Akke-aigento/…` of de publieke opslag van Watchtower/SellQo komen.

## 2. Een film maken (per merk, per week één)

1. **Idee eerst** (POSTS-2 §2): naar wie stuurt iemand dit door, de hook in 1 s, het ene idee. Een film vertelt iets: een verhaal met een begin en een einde, of een nuttige les.
2. **Schrijf `plan.json`** naast de film (voorbeeld: `loveke/marketing/films/strip2-final-call/plan.json`): stijl, personages, per shot het beginbeeld (`frame`), de beweging en het geluid (`motion`), wie wat zegt (`lines`), en de eindkaart.
3. **Beginbeelden maken en bekijken.** Elk beeld bekijken met Read vóór je het animeert: juiste personages, kleren, geen tekst in beeld, geen extra vingers of gezichten. Fout = opnieuw met een scherpere prompt.
4. **Shots animeren** (Veo 3.1, 6 s, 1080p, met geluid). Bekijk elke shot per 0,5 s (contactsheet) en meet het geluid. Klopt het niet, maak die shot opnieuw. Niet de hele film.
5. **Monteren** met `render.sh film`. Ondertitels: dialoog in `lines`, voice-over via `voice.words`. Muziek uit de bibliotheek van het merk op ±0,5, wegduiken onder stem. **Geen sting.**
6. **Controle**: contactsheet van de hele film, ondertitels naast het beeld, slot fadet uit, grootte ≤ 9,5 MB, en de film in SellQo als `pending_approval`, met de MP4 in `published/` en de video zonder muziek als `video_silent_url`.

## 3. Wat per merk werkt

| Merk | Film | Bron |
|---|---|---|
| Loveke | de strip komt tot leven: Akke en Nastya bewegen, praten, je hoort het station en de wekker | stripvakken (strip 1 en 2) als referentie |
| VanXcel | de reis als film: Sandy rijdt, echte clips + geanimeerde foto's, voice-over met één les ("waarom we 120 Ah meenamen") | `media.json`, `clips/`, feiten uit de bible |
| SellQo | een uitbater met een probleem (fictief personage, getekend) → de echte functie op het scherm → opgelost; voice-over | changelog + echte schermopnames; nooit een echte klant |
| Studio Akke | een ondernemer die zijn eigen site op zijn gsm bekijkt → wat er misloopt → hoe het moet; voice-over in ik-vorm is **niet** Akke's stem (enkel met zijn toestemming) | studioakke.com, echte schermopnames |
| Fonske | de crawl-avond als film: Fonske-tekeningen die bewegen, echte crawlclips | `illustrations/`, Crawl Log |

### 3b. Vaste reeksen (Akke 22-11, 23u57: "goede ideeën, nu zijn we creatief bezig")

Elke film hoort bij een herkenbare reeks (vaste vorm, vaste personages, elke week nieuwe inhoud). Personages krijgen een castblad zoals `loveke/marketing/films/characters/` en blijven altijd dezelfde.

| Merk | Reeks | Vorm | Grens |
|---|---|---|---|
| VanXcel | **Sandy's avonturen** | Sandy (Land Cruiser 1984) als getekend personage in een eigen stijl. Een stroomprobleem (lege accu, koelbox valt uit, te dunne kabel) → het juiste VanXcel-product of de calculator lost het op. Product gemaakt met de echte productfoto als referentie. Nevenreeks: "wat zit er in je van" (onderdelen vliegen samen tot een installatie). | Echte gebeurtenissen alleen als ze in `media.json` of de bible staan. Een probleem dat niet echt gebeurd is, presenteer je als scenario ("What if…"), nooit als reisverhaal. Enkel bestaande producten met voorraad > 0. 230V: altijd keuring door een erkend elektricien. |
| Studio Akke | **Akke legt uit** | Getekende Akke (bestaand castblad) legt in ±20 s één webprobleem uit → echte scan of echte site op een gsm (inset). | Enkel echte scores van eigen of toegestane sites. |
| SellQo | **Maandag 7u** | Vaste getekende winkeliers (bv. bakker, fietsenmaker; fictief) lopen tegen een echt probleem aan → echte SellQo-schermen lossen het op. Nevenreeks: speedrun "van nul tot webwinkel", echt opgenomen met timer. | Enkel functies die live staan; nooit een echte klant nabootsen. |
| Fonske | **Fonske neemt je mee** | Het Fonske-beeldje komt tot leven en leidt je langs de route, in stripstijl. | Cafés, route en uren enkel uit de echte crawlgegevens. |

Volgorde: eerst een pilot per reeks, goedkeuring van Akke, dan pas in de weektaak. Eerste pilot: VanXcel / Sandy.

## 4. Regels

- **Niets verzinnen** blijft gelden: een film vertelt enkel wat in de bible, de strip, `media.json` of de live bron staat. Geanimeerde personages zijn getekend, nooit fotorealistische namaak van echte mensen.
- Geen echte personen nabootsen met AI (stem of gezicht), behalve Akke en Nastya als getekende stripfiguren. Geen stemkloon van Akke zonder zijn uitdrukkelijke go.
- Geen merken van derden, geen tekst in AI-beelden (die wordt gekriebel), geen sigaretten of alcohol aan de mond.
- Kosten: één film = 6 beginbeelden + 6 shots. Niet blind opnieuw genereren: eerst de prompt verbeteren.

## 5. Strenge controle (Akke 22-11: "zo'n AI-fouten mogen er niet in")

Geen enkele film gaat naar SellQo zonder deze controle, per shot én op de eindmontage:

1. `python3 shared/remotion/filmcheck.py <shot.mp4> <map> --from <s> --to <s>` (enkel het stuk dat je gebruikt). Dat geeft grids van een frame per 0,25 s en een lijst met **sprongen** (frames die plots verspringen). Een sprong midden in een shot is bijna altijd een AI-fout. Knips en crossfades in de eindmontage zijn normaal.
2. **Bekijk elke grid** (Read) en zoek actief naar:
   - dubbele of verdwijnende objecten (armsteun, gsm, tas, koffer);
   - extra of samensmeltende ledematen en vingers, vervagende benen;
   - een gezicht of baard dat verandert ten opzichte van het modelblad;
   - een lichaam dat verspringt van houding of plaats;
   - tekst, cijfers of gekriebel op borden en schermen;
   - onlogische actie (de verkeerde kant uitlopen, iets doen dat niet in het verhaal staat).
3. **Geluid**: spraakherkenning op elke shot. Een stem die er niet hoort, gebrabbel of een echo gaat eruit (volume 0) of wordt vervangen door een vaste ElevenLabs-stem.
4. **Eén fout = dat stuk eruit knippen of de shot opnieuw maken.** Nooit "valt niet op".
5. Noteer per shot in het log welk bereik gebruikt is en wat eruit geknipt werd (pilot: vliegtuig enkel 0–3,4 s door een dubbele armsteun vanaf 3,5 s; gate enkel 0,3–4,9 s).
6. Pas daarna de onafhankelijke review (POSTS-2) en dan `pending_approval`.
