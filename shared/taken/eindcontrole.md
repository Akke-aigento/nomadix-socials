# Eindcontrole week: onafhankelijke controle van de Instagram-weken

Elke zondag om 11:13, na de vijf weektaken. Akke, 17-11-2026: "het moet gewoon in orde zijn zonder dat ik mij er zorgen rond moet maken." Jij hebt de items NIET gemaakt: wees streng en ga uit van niets.

1. Bepaal de eerstvolgende maandag (Europe/Brussels). Haal per merk alle items van die week op:
   ```
   select p.id, p.tenant_id, p.status, p.media_type, (p.scheduled_for at time zone 'Europe/Brussels') lokaal, p.post_text, p.image_urls, p.video_url, p.content_tags::text from social_posts p where p.source='content_task' and p.status in ('pending_approval','manual') and p.scheduled_for >= '<maandag> 00:00 Europe/Brussels' and p.scheduled_for < '<maandag> 00:00 Europe/Brussels'::timestamptz + interval '7 days' order by p.tenant_id, p.scheduled_for;
   ```
   Heeft een merk 0 items, dan is de weektaak van dat merk mislukt. Meld dat bovenaan.
2. Lees `shared/POSTS-2.md` (vooral §2, §4 en §6) en per merk de sectie "wat we wel en niet zeggen" van de README (Loveke: `/home/user/loveke/marketing/instagram/README.md`), plus de sectie van het merk in `shared/taken/weektaak.md`.
3. Controleer ELK item zelf, met de echte bestanden (curl de raw-URL's naar /tmp):
   - **Beelden:** bekijk elk beeld (Read). Controleer:
     - niets afgesneden of overlappend;
     - tekst leesbaar op een gsm, geen tikfouten, juiste taal;
     - geen emoji in het beeld;
     - veilige zones vrij (story/reel: boven 250 px, onder 340 px).
   - **Reels:** haal één frame per 0,5 s uit de video (`ffmpeg -vf fps=2`) en bekijk ze allemaal als contactsheet. Controleer:
     - elke ondertitel klopt met wat er op dat moment in beeld is (17-11: "a river in full flow" stond op een brugdek);
     - geen zwarte of bevroren stukken, eindkaart leesbaar;
     - geluid aanwezig (ffprobe: audiostream);
     - grootte max. 9,5 MB.
   - **Feiten:** vergelijk elke prijs, datum, uur, plek, spec en claim in caption én beeld met de live bron. De bronnen staan per merk in `shared/taken/prijscheck.md` (Fonske: early bird enkel als de deadline in de toekomst ligt). Geen verzonnen anekdotes, klantaantallen, reviews, doorstreepte prijzen of greenwashing.
   - **Kwaliteit:** score 0–2 op de zes punten van POSTS-2 §6. Vraag je eerlijk af: zou een mens dit doorsturen?
4. Beslis per item:
   - **In orde** (score minstens 9 en geen fout): niets doen.
   - **Een fout of score onder 9.** Fouten zijn: een feit, een ondertitel die niet klopt met het beeld, afgesneden tekst, een tikfout, emoji in beeld.
     - Meer dan 3 uur van nu gepland: vraag "Opnieuw maken" aan:
       ```
       update social_posts set status='regenerate_requested', regenerate_from=status, regenerate_note='Eindcontrole <datum>: <wat er precies mis is, met tijdstip in de reel of slidenummer> → <wat het moet worden>', regenerate_language=null, regenerate_requested_at=now(), updated_at=now() where id='<id>' and status in ('pending_approval','manual');
       ```
     - Binnen 3 uur: wijzig niets, enkel melden als "dringend".
   - **Verder:** wijzig NIETS. Geen tekst, geen tijd, geen andere kolommen of tabellen; nooit 'approved' of 'posted'.
5. Zet per merk één melding in SellQo:
   ```
   insert into notifications (tenant_id, category, type, priority, title, message, action_url, data) values ('<t>','marketing','social_posts_ready','medium','Eindcontrole week: <n> ok, <m> teruggestuurd','<per teruggestuurd item: dag + uur + wat er mis was>','/admin/marketing/social', jsonb_build_object('kind','final_check'));
   ```
6. Bericht aan Akke:
   - per merk "x items gecontroleerd, y in orde, z teruggestuurd (waarom, in één regel)", plus wat dringend is;
   - is alles in orde, zeg dat in één zin: dan kan hij met een gerust hart "Week goedkeuren";
   - "Social: opnieuw maken" (elk uur 8–22 u) maakt de teruggestuurde items opnieuw; hij keurt die pas goed als ze opnieuw klaarstaan.

Lukt een stap niet (repo, connector, download), meld dat en ga verder met de rest.
