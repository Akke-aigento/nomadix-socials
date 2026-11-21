# Opnieuw maken: verzoeken "Opnieuw maken" uit de SellQo Social planning

Elk uur van 8 tot 22 u. Schrijf in het Nederlands (Vlaams, casual).

1. Doe eerst precies één read-only query via de Lovable-connector:
   ```
   select id, tenant_id, platform, media_type, language, regenerate_language, regenerate_from, regenerate_note, regenerate_requested_at, (scheduled_for at time zone 'Europe/Brussels') lokaal, post_text, image_urls, image_recipes, video_url, video_silent_url, music_hint, content_tags from social_posts where status = 'regenerate_requested' and source = 'content_task' and scheduled_for > now() + interval '30 minutes' and tenant_id in ('1671a91c-31fe-42ed-8a10-41f3117ceb50','54f6b480-280b-42e1-b843-d5beb2831acd','d03c63fe-48c6-4ff7-a30b-7506ea3e71ab','c96fb1b2-ddac-44d1-a638-72dd54efd31e','95f6685b-3474-42fe-81ad-a5e6ca3d6806') order by scheduled_for limit 5;
   ```
   Posts, stories en reels waarvan het geplande moment al voorbij is (of binnen 30 minuten valt), worden NOOIT opnieuw gemaakt (beslissing Akke, 2 nov 2026). Laat die rijen ongemoeid en meld ze niet.
   Bestaat de tabel social_content_requests (`to_regclass('public.social_content_requests')` is niet null), haal dan ook op: `select * from social_content_requests where status = 'requested' and (wanted_for is null or wanted_for >= current_date) and tenant_id in (dezelfde vijf) order by created_at limit 5;`
   Geen rijen in beide: antwoord "Niets te doen." en stop.

2. Bron per merk: zie de tabel in ALGEMEEN.md en de sectie van het merk in `shared/taken/weektaak.md` ("Per merk"): taal, strikte README-secties en bronnen voor feiten. VanXcel en Fonske zijn altijd Engels. Lees `shared/POSTS-2.md` en `shared/LEREN.md`.
   Test vóór je iets maakt of je kunt pushen: `git push --dry-run origin main` in elke repo die je nodig hebt. Faalt dat, maak dan niets voor de rijen van die repo en laat ze op `regenerate_requested`. Zet per betrokken tenant hooguit één melding per dag (controle zoals in ALGEMEEN.md, kind `regenerate_blocked`):
   ```
   insert into notifications (tenant_id, category, type, priority, title, message, action_url, data) values ('<tenant_id>','marketing','social_posts_ready','high','Opnieuw maken lukt niet','De taak "Social: opnieuw maken" kan niet naar <repo> pushen (<foutmelding in één zin>). Je verzoeken blijven staan; ik meld dit hooguit één keer per dag.','/admin/marketing/social', jsonb_build_object('kind','regenerate_blocked'));
   ```
   Verwerk wel de rijen van repo's die wel werken.

3. Per social_posts-rij (`regenerate_requested`):
   - **Lezen:** de README van dat merk, het log, `lessen.md` en de bron van de huidige versie.
   - **Opmerking van Akke:** `regenerate_note` is leidend. Volg ze, en verwerk een herhaald patroon (bv. twee keer "minder verkoperig") in `lessen.md` volgens LEREN.md §4.
   - **Nieuwe versie:**
     - zelfde soort (post, carrousel, story of reel), zelfde dag en uur;
     - volgens POSTS-2: echt beeld eerst, één idee, hook in 1 s; score op de zes punten van §6, onder 9 = opnieuw;
     - taal: `regenerate_language` als die ingevuld is, anders de huidige `language`;
     - heeft Akke de tekst in het beeld al aangepast (`image_recipes` in SellQo verschilt van de `.recipe.json` in de repo), vertrek dan van de teksten uit SellQo;
     - geen dubbels met het log of met andere rijen van die tenant;
     - prijzen, voorraad, data en specs live, nooit verzonnen;
     - een reel krijgt een bibliotheeknummer + merksting (MUZIEK.md) en een versie zonder muziek;
     - links met UTM volgens LEREN.md §5.
   - **Staat er al een kant-en-klare `-v2` in de published-map, en past ze bij de opmerking?** Controleer ze dan (frames, feiten), gebruik ze en maak niets nieuws. Zie het log van het merk ("opnieuw gemaakt …").
   - **Publiceren:** render, bekijk het resultaat en zet de bestanden met een nieuwe naam (`…-v2`, `-v3`, …) in de map `published/<maandag>/` van het merk. Commit en push naar main, en controleer de raw-URL met `curl -sI` (200).
   - **Database:** werk precies die ene rij bij (de enige update die mag):
     - nieuwe `post_text`, `image_urls`, `image_recipes` (enkel voor beelden met een `.recipe.json`, anders null) en eventueel `video_url`/`video_silent_url`/`music_hint`;
     - `content_tags` volgens LEREN.md §1: oude labels overnemen, format/template/hook/caption_length/cta/genre aanpassen, quality = score;
     - `language` = de taal van de nieuwe versie;
     - `status` = `regenerate_from` als dat 'manual' was, anders 'pending_approval';
     - `regenerate_note`, `regenerate_requested_at`, `regenerate_from`, `regenerate_language`, `reminded_at`, `approved_at`, `approved_by`, `error_message` = null; `publish_attempts` = 0;
     - altijd met `where id = '<id>' and status = 'regenerate_requested' and scheduled_for > now()`.
   - **Log:** pas het log aan (de regel met "(opnieuw gemaakt)", de labels en de score) en commit.
   - **Melding:**
     ```
     insert into notifications (tenant_id, category, type, priority, title, message, action_url, data) values ('<tenant_id>','marketing','social_posts_ready','medium','Nieuwe versie klaar: <onderwerp>','<dag en uur>. Bekijk hem in de Social planning en keur hem goed.','/admin/marketing/social', jsonb_build_object('social_post_id','<id>'));
     ```

4. Per social_content_requests-rij (status `requested`):
   - Zet eerst status 'processing' (`where id = … and status = 'requested'`; geen rij terug = overslaan).
   - Maak met de gekozen beelden een nieuwe post, story of reel (`kind`) volgens POSTS-2 en de README van het merk. De beelden: `media_asset_ids` → `media_assets.file_url`; brand-beelden van VanXcel staan ook in `brands/vanxcel/media/`.
   - **Moment:** op `wanted_for`, of de eerstvolgende vrije dag op het beste uur volgens POSTTIJDEN.md; nooit een moment in het verleden.
   - Zet hem als nieuwe social_posts-rij:
     - `content_tags` volgens LEREN.md;
     - source 'content_task';
     - status zoals de weekroutine van dat merk; zonder Instagram-koppeling 'manual' met `manual_reason` 'other'.
   - Daarna: request op status 'done', `processed_at` = now(), `result_post_id` = de nieuwe id. Lukt het niet: status 'rejected' met error.

5. Andere tenants worden niet verwerkt.
6. Bericht aan Akke (ALGEMEEN.md): welke post(s) opnieuw of nieuw gemaakt zijn, wat er anders is, welke score, en dat hij ze nog moet goedkeuren. Zet nooit iets op approved of posted.

Lukt iets niet (repo, connector, render, URL geen 200)?
- Laat de rij op `regenerate_requested` staan, of de request op `requested`.
- Volg de regel "hooguit één melding per dag".
- Meld kort waarom.
