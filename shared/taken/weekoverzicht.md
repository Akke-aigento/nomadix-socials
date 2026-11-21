# Weekoverzicht en lessen (SOCIAL-6 + Insights)

Elke maandag om 08:12.

Merken met hun site in Akke Insights (`sites.name`):
- **Loveke:** lessen in `/home/user/loveke/marketing/instagram/` (log.md, lessen.md); Insights 'Loveke'.
- **VanXcel:** `brands/vanxcel/`; Insights 'VanXcel'.
- **SellQo:** `brands/sellqo/`; Insights 'SellQo'.
- **Studio Akke:** `brands/studio-akke/`; Insights 'Studio Akke'.
- **The Fonske Crawl:** `brands/fonske/`; Insights 'The Fonske Crawl'.

0. Lees `shared/LEREN.md` (ook §5 en §6) en `shared/POSTTIJDEN.md` volledig: die regels gelden.

1. Labels achteraf, enkel waar ze ontbreken. Per merk:
   ```
   select id, media_type, status, (scheduled_for at time zone 'Europe/Brussels') lokaal, left(post_text,300) tekst from social_posts where tenant_id='<t>' and source='content_task' and content_tags is null and scheduled_for > now() - interval '60 days';
   ```
   Bepaal per rij de labels uit LEREN.md §1, met het log.md van het merk (zelfde dag en soort) en de tekst. Zet ze met precies:
   ```
   update social_posts set content_tags = '<json>'::jsonb where id = '<id>' and content_tags is null;
   ```
   Twijfel je over één sleutel, laat die sleutel dan weg; verzin niets. Raak geen andere kolommen aan.

2. Cijfers per merk, voor de laatste 7 dagen en de laatste 90 dagen (queries in LEREN.md §2):
   - `social_post_performance` per uur/dagdeel, per pillar, format, hook, caption_length, cta en bucket (score_48h, anders score; zonder bereik: likes + comments);
   - `social_post_events` van de laatste 30 dagen (removed, edited, regenerate_requested met note, image_changed);
   - volgers: `select captured_on, followers_count from social_account_stats where tenant_id='<t>' order by captured_on desc limit 30`.

2b. Wat Instagram oplevert op de site (LEREN.md §6):
   - Draai per merk de Insights-query uit §6 voor de laatste 7 dagen, en voor de lessen ook met interval '90 days'. Dat is `query_database` op project `f639dfa8-ad8f-4c7f-9b35-9672dd0fefbc`, ALLEEN LEZEN: enkel select, nooit iets schrijven in Insights.
   - Koppel rijen aan posts via `utm_campaign <merk>-<JJJJMMDD>` (zeker) of, zonder campagne, aan de post(s) van die dag en de dag ervoor (waarschijnlijk).
   - Weektotalen per merk: bezoekers, aanvragen, bestellingen en omzet via Instagram.
   - Minder dan 10 Instagram-bezoekers in de week: cijfers noemen, geen les trekken.

3. `lessen.md` per merk bijwerken volgens LEREN.md §4 en §6:
   - **Wat telt als les:** enkel lessen met minstens 3 posts per waarde, of twee keer hetzelfde signaal van Akke, met datum, bewijs en status. Bezoekers, aanvragen en bestellingen via Instagram wegen zwaarder dan likes.
   - **Wat niet terug mag:** doorstreepte regels of "(Akke: nee)" nooit terugzetten.
   - **Maximum:** 15 actieve lessen; vervallen lessen naar "Vervallen".
   - **Te weinig data:** laat "Actief" leeg en zet er één regel onder met hoeveel gemeten posts er al zijn.
   - **Posttijden:** noteer het beste dagdeel/uur als dat minstens 3 posts heeft.
   - **Commit en push naar main:** nomadix-socials `brands/*/lessen.md`; loveke `marketing/instagram/lessen.md`. Raak geen andere bestanden aan.

4. Zet een melding in SellQo per merk dat de voorbije 7 dagen minstens één geposte post had (status posted):
   ```
   insert into notifications (tenant_id, category, type, priority, title, message, action_url, data) values ('<t>','marketing','social_posts_ready','low','Weekoverzicht social','<2-3 korte zinnen: wat werkte (met cijfer), wat niet, wat de weektaak daardoor anders doet, plus één zin "Instagram bracht deze week X bezoekers, Y aanvragen, Z bestellingen naar je site" (echte getallen uit stap 2b, ook als het 0 is; laat de zin weg als er geen Insights-site is)>','/admin/marketing/social?tab=results', jsonb_build_object('kind','weekly_report','ig_site', jsonb_build_object('visitors',X,'leads',Y,'orders',Z)));
   ```
   Geen geposte posts: geen melding voor dat merk.

5. Bericht aan Akke:
   - per merk 1-2 regels: de beste post van de week met score, wat Instagram opleverde op de site (bezoekers/aanvragen/bestellingen), één les of "nog te weinig data", en wat er deze week anders gaat;
   - hoeveel rijen labels kregen;
   - of een account nog "basic" cijfers geeft (dan: Instagram opnieuw koppelen voor statistieken).

Schrijf in SellQo niets anders dan `content_tags` (waar null) en de meldingen uit stap 4. In Insights schrijf je nooit iets. Wijzig nooit de status, tijd of tekst van posts. Lukt iets niet (repo, connector, Insights-query), meld dat en ga verder met de andere merken.
