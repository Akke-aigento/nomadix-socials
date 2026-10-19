# Leren van resultaten — verplicht voor alle merken

Beslist door Akke op 16 okt 2026, als SOCIAL-6. Elke week wordt de content beter: niet alleen de **uren** (`POSTTIJDEN.md`), maar ook **wat** we posten. De weektaken, "Opnieuw maken", "post op aanvraag" en de maandagtaak volgen dit bestand. De Loveke-repo verwijst hiernaar.

**De merkregels gaan altijd voor de data.** Een format dat "scoort" maar tegen de brand bible ingaat, gebruiken we niet. Dus geen clickbait, geen verzonnen claims en geen kortingen die niet bestaan.

## 1. Labels bij elke post (verplicht)

Elke nieuwe rij in `social_posts` krijgt `content_tags` (jsonb). Gebruik kleine letters en enkel deze sleutels:

| Sleutel | Waarden | Uitleg |
| --- | --- | --- |
| `pillar` | de pijlers uit de README van het merk (bv. `verhaal`, `product`, `tips`, `bewijs`, `samen`) | waarover de post gaat |
| `format` | `strip`, `productfoto`, `lifestyle`, `typografisch`, `tip`, `lijst`, `quote`, `voor-na`, `poll`, `vraag`, `achter-de-schermen`, `case`, `aanbod`, `reel-montage`, `reel-pov`, `reel-slideshow`, `reel-tekst` (nieuw format? geef het een eigen naam) | hoe het eruitziet |
| `template` | bestandsnaam van de template, bv. `case`, `tip-dark` | om templates te kunnen vergelijken |
| `hook` | `vraag`, `statement`, `cijfer`, `grap`, `pov`, `belofte`, `verhaal`, `contrast` | de eerste regel of de grote tekst in het beeld |
| `caption_length` | `kort` (< 125 tekens), `middel` (125–400), `lang` (> 400) | lengte van de caption |
| `cta` | `geen`, `opslaan`, `reageren`, `delen`, `link`, `dm`, `profiel` | waartoe de post oproept |
| `product` | slug van het product, of weglaten | welk product centraal staat |
| `people` | `ja` / `nee` | is er een persoon of gezicht in beeld |
| `bucket` | `exploit`, `explore`, `test` | waarom deze post er is (zie §3) |
| `experiment` | `tijd`, `inhoud`, of weglaten | wat er getest wordt |

Voorbeeld: `{"pillar":"verhaal","format":"strip","template":"strip-panel","hook":"grap","caption_length":"kort","cta":"opslaan","people":"nee","bucket":"exploit"}`

Zet dezelfde labels per item ook in `log.md`. "Opnieuw maken" past de labels aan als het format of de hook verandert.

## 2. Hoe we meten

- SellQo meet elke 3 uur, en één vaste keer **48 uur na publicatie** (`engagement_48h`). Vergelijk posts altijd met `score_48h`. Is die er nog niet, gebruik dan `score`.
- **Score** = (likes + 2·reacties + 2·story-antwoorden + 3·bewaard + 3·gedeeld + 5·nieuwe volgers) per 100 bereikte accounts. Bewaren, delen en volgen zeggen meer dan een like.
- Is er geen bereik (account nog niet opnieuw gekoppeld met statistieken), vergelijk dan op likes + reacties en zeg dat erbij.
- Een uitspraak ("X werkt beter") mag pas vanaf **3 posts** per waarde.
- **Signalen van Akke** staan in `social_post_events`:

  | Signaal | Betekenis |
  | --- | --- |
  | `removed` | geschrapt |
  | `edited` | tekst aangepast |
  | `regenerate_requested` | opnieuw laten maken, met zijn opmerking in `note` |
  | `image_changed` | tekst in beeld aangepast |
  | `approved` | goedgekeurd zonder aanpassing |

  Twee keer hetzelfde soort schrappen of herschrijven is een les, ook zonder cijfers.

```sql
-- per label, laatste 90 dagen
select format, count(*) posts, round(avg(coalesce(score_48h, score)),2) score, round(avg(saved_48h),1) bewaard
from social_post_performance
where tenant_id = '<tenant>' and posted_at > now() - interval '90 days'
group by 1 order by score desc nulls last;
-- vervang format door pillar, hook, caption_length, cta of bucket

-- signalen van Akke, laatste 30 dagen
select event, content_tags->>'format' format, content_tags->>'hook' hook, note, created_at
from social_post_events where tenant_id = '<tenant>' and created_at > now() - interval '30 days'
  and event in ('removed','edited','regenerate_requested','image_changed') order by created_at desc;
```

## 3. Kiezen: 70 / 20 / 10

Per week, over alle posts en carrousels (stories mogen vrijer):

- **70 % `exploit`**: combinaties van pijler, format en hook die bij dit merk bewezen goed scoren (minstens 3 posts, boven het gemiddelde van het merk).
- **20 % `explore`**: waarden met minder dan 3 posts, zodat we leren wat we nog niet weten.
- **10 % `test`**: één nieuw idee per week, een format, hook of invalshoek die nog nooit gedaan is. Zet `experiment` op `inhoud`.

Zolang er te weinig data is (de eerste 4 tot 6 weken), draai je dit om: vooral `explore`, met de merkregels en `VARIATIE.md` als gids.

Verder:

- **Slijtage.** Scoort een format de laatste 4 weken duidelijk lager dan de 4 weken daarvoor, gebruik het dan minder (maximaal 1× per week) tot het herstelt.
- **Wat wegvalt.** Een `test` of `explore` die na 3 posts onder het merkgemiddelde zit, gaat naar achter: alleen nog af en toe, met een andere hook.
- **Variatie blijft verplicht** (`VARIATIE.md`). Ook als één format wint, posten we het nooit twee dagen na elkaar.

## 4. `lessen.md` per merk

Elk merk heeft een `lessen.md`:

- `brands/<slug>/lessen.md`;
- voor Loveke: `marketing/instagram/lessen.md` in de Loveke-repo.

De maandagtaak werkt het bij. Elke weektaak leest het vóór ze iets bedenkt.

- Per les één regel, met de datum, het bewijs en de status: `- 2026-11-02 · strips scoren 2,1× productfoto's (score_48h 8,4 vs 4,0; 6 vs 5 posts) · actief`.
- **Akke heeft het laatste woord.** Een regel die hij doorstreept (`~~…~~`) of die eindigt op `(Akke: nee)` wordt nooit meer gebruikt of opnieuw voorgesteld.
- Houd het bestand kort: maximaal 15 actieve lessen. Oude of tegengesproken lessen gaan naar een sectie "Vervallen".

## 5. Links meten

Elke link die we zelf maken (linksticker, link in bio-update, URL in een caption) krijgt UTM-parameters:

`?utm_source=instagram&utm_medium=social&utm_campaign=<merk>-<JJJJMMDD>&utm_content=<format>`

`<JJJJMMDD>` is de postdag, zodat een bezoek bij één post hoort.

**Link-sticker (verplicht formaat, Akke 19-10).** Instagram laat geen link in een caption toe, dus de link van een story gaat via een sticker die Akke zelf plakt. Zet in `post_text` van elke story met een link-sticker, op een eigen regel en als laatste regel:

`Link-sticker: https://<domein>/<pad>?utm_source=instagram&utm_medium=social&utm_campaign=<merk>-<JJJJMMDD>&utm_content=story`

Altijd de volledige URL met `https://`, klaar om te kopiëren, en nooit "link naar loveke.be/shop" zonder URL. `<merk>` is `loveke`, `vanxcel`, `sellqo`, `studioakke` of `fonske`. Controleer vóór de insert dat de pagina bestaat (curl -sI geeft 200 of een redirect naar 200). Hetzelfde formaat geldt voor een nieuwe link in bio (`Link in bio: …`). Een link in bio zonder eigen UTM krijgt van Instagram zelf `utm_source=ig`. Akke Insights telt `ig`, `instagram` en doorklikken vanaf instagram.com sinds 16-10 als één kanaal "Instagram" (INSIGHTS-IG-1). Insights bewaart `utm_content` niet; dat is geen probleem, want de campagnenaam volstaat.

## 6. Wat Instagram oplevert op de site (Akke Insights)

Besloten 16-10 (Akke: "die cijfers doorgeven is zeker nuttig"). De maandagtaak leest Insights **alleen-lezen** via de Lovable-connector, `query_database` op project `f639dfa8-ad8f-4c7f-9b35-9672dd0fefbc`. Er is geen API, en schrijven doen we daar nooit.

| Merk | Insights-site (`sites.name`) |
| --- | --- |
| Loveke | `Loveke` |
| VanXcel | `VanXcel` |
| Studio Akke | `Studio Akke` |
| SellQo | `SellQo` |
| The Fonske Crawl | `The Fonske Crawl` |

```sql
-- Bezoekers, aanvragen en bestellingen via Instagram per dag en campagne, laatste 7 dagen (zonder bots)
with site as (select id, coalesce(lead_events,'{}') le from sites where name = '<Insights-site>'),
e as (select h.* from site, public._human_events(site.id, now() - interval '7 days', now()) h),
ig as (
  select distinct on (visitor_id, (ts at time zone 'Europe/Brussels')::date)
         visitor_id, (ts at time zone 'Europe/Brussels')::date dag, coalesce(utm_campaign,'') campagne
    from e
   where kind = 'pageview'
     and (lower(coalesce(utm_source,'')) in ('ig','instagram','instagram.com','insta')
          or lower(coalesce(referrer_host,'')) ~ '(^|\.)instagram\.com$')
   order by visitor_id, (ts at time zone 'Europe/Brussels')::date, ts
),
conv as (
  select e.visitor_id, (e.ts at time zone 'Europe/Brussels')::date dag,
         count(*) filter (where e.name = any(site.le)) aanvragen,
         count(*) filter (where e.name = 'Bestelling') bestellingen,
         coalesce(sum(public._order_value(e.props)) filter (where e.name = 'Bestelling'),0) omzet
    from e, site where e.kind = 'event' group by 1,2
)
select ig.dag, ig.campagne, count(*) bezoekers, coalesce(sum(c.aanvragen),0) aanvragen,
       coalesce(sum(c.bestellingen),0) bestellingen, coalesce(sum(c.omzet),0) omzet
  from ig left join conv c using (visitor_id, dag)
 group by 1,2 order by 1;
```

Hoe je dit gebruikt:

- **Koppelen aan een post.** Heeft een rij `campagne = <merk>-<JJJJMMDD>`, dan hoort ze bij de post van die dag. Zonder campagne (bio-link, `ig`) tel je ze bij de post(s) van die dag en de dag ervoor, als "waarschijnlijk".
- **Les trekken.** Een bezoek, aanvraag of bestelling weegt zwaarder dan likes. Een format dat bezoekers of aanvragen brengt, mag in `lessen.md`, ook met een lagere score. Ook hier geldt: pas een uitspraak vanaf **3 posts**, en noem het bewijs, bv. `5 bezoekers, 1 aanvraag over 4 posts`.
- **Melding en samenvatting.** Eén regel per merk met de weektotalen: "Instagram bracht deze week X bezoekers, Y aanvragen, Z bestellingen". Zijn alle drie 0, zeg dat dan gewoon; nooit afronden naar boven of iets suggereren.
- **Bestellingen.** De bedankpagina's van Loveke (`Bedankt.tsx`) en VanXcel (`ThankYou.tsx`) sturen `akke('Bestelling', {waarde})`, één keer per bestelling. Bestellingen via bol.com lopen niet via de site en tellen dus nooit mee. Op 16-10 stond het op 0, omdat er sinds de start van Insights (11-10) geen webshopbestelling was.
- **Te weinig data** (minder dan 10 Instagram-bezoekers in de week): noem de cijfers, trek geen les.
