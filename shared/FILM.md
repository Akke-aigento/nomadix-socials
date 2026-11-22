# FILM-1 — echte korte films in plaats van slideshows (sinds 22-11-2026)

Akke (22-11): "Denk aan echte filmpjes maken, niet gewoon slideshows. Maak de karakters echt, vertel iets nuttigs, laat de strip tot leven komen." De reel van elk merk is voortaan een **film**: bewegende beelden met eigen geluid, personages die bewegen en praten, voice-over waar het helpt, muziek eronder. Geen foto's die schuiven, geen sting.

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

## 4. Regels

- **Niets verzinnen** blijft gelden: een film vertelt enkel wat in de bible, de strip, `media.json` of de live bron staat. Geanimeerde personages zijn getekend, nooit fotorealistische namaak van echte mensen.
- Geen echte personen nabootsen met AI (stem of gezicht), behalve Akke en Nastya als getekende stripfiguren. Geen stemkloon van Akke zonder zijn uitdrukkelijke go.
- Geen merken van derden, geen tekst in AI-beelden (die wordt gekriebel), geen sigaretten of alcohol aan de mond.
- Kosten: één film = 6 beginbeelden + 6 shots. Niet blind opnieuw genereren: eerst de prompt verbeteren.
