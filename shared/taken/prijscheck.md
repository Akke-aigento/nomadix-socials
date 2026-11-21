# Prijscheck: kloppen geplande posts nog met de live prijzen, plannen en data?

Elke dag om 07:43 (Akke, 19-10: "houdt de generator rekening met prijs- en planwijzigingen?").

Bron per merk:
- **Loveke en VanXcel:** `products` (name, price, compare_at_price, stock) van de tenant.
- **The Fonske Crawl:** events van de tenant (`event_details` e.d., enkel status 'scheduled'; datum, uur, plek, ticketprijzen, einde early bird).
- **SellQo:** `pricing_plans` (name, monthly_price, yearly_price, active, limieten) én de landingcopy in `/home/user/sellqo/src/i18n/locales/landing.nl.json`: proefperiode, gratis plan, wat er in een plan zit. NOOIT `landing.pricing.plans` als bron.
- **Studio Akke:** de repo `/home/user/studioakke` (`Pricing.tsx`, `Prijzen.tsx`, `Mail.tsx`, `Insights.tsx`, `diensten/*`, `LanguageContext.tsx` blok nl).

1. Haal de posts op die nog moeten komen:
   ```
   select p.id, p.tenant_id, p.status, p.media_type, (p.scheduled_for at time zone 'Europe/Brussels') lokaal, p.post_text, p.image_recipes::text recepten, p.video_url from social_posts p where p.source='content_task' and p.status in ('pending_approval','approved','manual') and p.scheduled_for > now() and p.scheduled_for < now() + interval '8 days' order by p.scheduled_for;
   ```
   Lees per post de caption én de tekst in beeld: de HTML in `image_recipes`, of de bron van de reel/slides in de repo (log van het merk → weekmap). Zoek feitelijke claims die kunnen verouderen:
   - bedragen (€), kortingen, "gratis";
   - proefperiodes ("14 dagen");
   - plannamen en wat erin zit, limieten;
   - data en uren van events, early-bird-deadlines;
   - "op voorraad"/beschikbaarheid, productnamen.
2. Vergelijk elke claim met de live bron. Een claim klopt als de bron hem vandaag letterlijk of eenduidig bevestigt. Voorraad: een product met stock 0 mag niet gepromoot worden, tenzij het duidelijk print-on-demand is (Loveke). Bij twijfel: melden, niet aanpassen.
3. Klopt een post niet en is hij meer dan 2 uur van nu gepland? Vraag dan "Opnieuw maken" aan, precies zoals de knop in SellQo:
   ```
   update social_posts set status='regenerate_requested', regenerate_from=status, regenerate_note='Prijscheck <datum>: <wat staat er> → <wat is het nu> (bron: <tabel of bestand>)', regenerate_language=null, regenerate_requested_at=now(), updated_at=now() where id='<id>' and status in ('pending_approval','approved','manual');
   ```
   Staat hij binnen 2 uur gepland: wijzig niets, enkel melden met "dringend". Wijzig verder NIETS: geen tekst, geen tijd, geen status naar approved of posted, geen andere kolommen of tabellen.
   Was de post al **approved**, zeg dat dan duidelijk in de melding. Na het opnieuw maken moet Akke hem opnieuw goedkeuren, anders gaat hij niet online.
4. Was er minstens één afwijking? Zet één melding per betrokken merk:
   ```
   insert into notifications (tenant_id, category, type, priority, title, message, action_url, data) values ('<t>','marketing','social_posts_ready','medium','Prijscheck: <n> post(s) opnieuw gemaakt','<per post: dag + uur, wat niet meer klopte, wat het nu is>','/admin/marketing/social', jsonb_build_object('kind','price_check'));
   ```
   Stuur ook een bericht aan Akke met dezelfde lijst, plus de posts die je enkel meldde (binnen 2 uur of twijfel).
5. Klopt alles: antwoord "Niets te doen." en maak geen melding.

Lukt een bron niet (repo of connector onbereikbaar)? Pas dan niets aan voor dat merk, meld het kort en ga verder met de andere merken.
