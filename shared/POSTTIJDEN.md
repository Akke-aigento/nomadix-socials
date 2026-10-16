# Posttijden — verplicht voor alle merken

Akke heeft dit op 16 okt 2026 beslist. Er bestaat geen standaarduur meer: nooit "18:00 omdat het moet". Elk merk post op het moment dat **zijn** publiek scrolt, en elk tijdstip wordt gemotiveerd.

Dit bestand is de bron voor de weektaken, "Opnieuw maken" en de skill "post op aanvraag". De Loveke-repo verwijst hiernaar.

## Regels

1. **Geen vaste uren.**
   - Nooit twee posts in dezelfde week op hetzelfde uur.
   - Geen ronde reeksen zoals 18:00, 18:05 en 19:00.
   - Kies minuten zoals :10, :20, :35 of :45. Op :00 en :30 posten de meeste accounts, dus daar is de concurrentie het grootst.
2. **Per merk een venster, niet één tijd.** Kies elke week binnen het venster van dat merk (zie hieronder) en wissel ochtend, middag en avond af.
3. **Stories horen bij een ander piekmoment dan de post van die dag.** Een story komt nooit 5 minuten na de post. Een story met sticker staat liefst op het drukste uur van de dag, want daar zijn de meeste reacties te halen.
4. **De reel krijgt het sterkste slot van de week.** Dat is het slot met de meeste kijkers volgens de tabel hieronder, en later volgens de data.
5. **Eén testslot per week.**
   - Plaats één post buiten het vaste venster, op een uur dat we nog niet probeerden, en zet `(test)` in `log.md`.
   - Zodra SellQo resultaten heeft (SOCIAL-5), beslis je zo: wint het testslot, dan komt het in het venster; scoort het zwak, dan valt het weg.
6. **Schrijf bij elk item het uur en de reden in `log.md`**, bijvoorbeeld "wo 12:20 — middagpauze ondernemers".
7. **De data gaat voor.** Staan er resultaten in SellQo, dan gaan die boven deze tabel:
   - de beste uren van het merk zelf;
   - `online_followers` (Instagram geeft die pas vanaf 100 volgers).
   De tabel is het startpunt, geen wet.
8. **SellQo publiceert elke 5 minuten.** Elk uur dat je kiest is dus ook het echte uur (±5 min).

Alle tijden zijn in Brusselse tijd. `scheduled_for` gaat altijd als `'<datum> <uur> Europe/Brussels'`, zodat de wissel naar winteruur vanzelf goed gaat.

## Vensters per merk

### Loveke — streetwear voor koppels, BE, 18–35

| Moment | Waarom | Typisch |
| --- | --- | --- |
| Avond 19:30–21:00 | Na het eten op de zetel, samen scrollen. Dit is het sterkste slot. | posts, reel (zo 20:30) |
| Middag 12:10–12:40 | Lunchpauze | product-post |
| Ochtend 08:15–08:45 | Pendelen (trein, tram) | verhaal of strip |
| Story 20:45–21:30 | Avondpiek, stickers krijgen dan de meeste reacties | sticker-stories |

Vrijdag- en zaterdagavond na 21:30: dan zijn mensen weg, dus niet posten.

### SellQo — ondernemers met een webshop, kassa of horecazaak, BE/NL

| Moment | Waarom | Typisch |
| --- | --- | --- |
| Ochtend 07:35–08:30 | Vóór de zaak opengaat: koffie en telefoon | tip, post (ma/vr) |
| Middag 12:10–12:45 | Lunch, rustig moment | story, korte tip |
| Avond 20:30–21:30 | Na sluiting: administratietijd | carrousel (wordt bewaard), reel |
| Horecadal 14:30–15:30 | Tussen lunch- en avondservice | test voor horeca-onderwerpen |

Zaterdag kort en vroeg (09:00–09:30). Zondagavond 20:00–20:45 mag: dan plannen ondernemers hun week.

### Studio Akke — zelfstandigen en kmo's die een site willen, BE/NL

| Moment | Waarom | Typisch |
| --- | --- | --- |
| Ochtend 08:00–08:45 | Start van de werkdag, mail en Instagram | post, story |
| Middag 12:15–12:45 | Lunch | carrousel (ma), story |
| Avond 20:15–21:00 | "Ik moet eens werk maken van mijn site": thuis denken ondernemers aan hun zaak | reel, zondagpost |
| Zaterdag 10:00–11:00 | Rustig, tijd om iets te lezen | info-story |

### VanXcel — campervanbouwers en overlanders, internationaal, Engels

| Moment | Waarom | Typisch |
| --- | --- | --- |
| Avond 20:00–21:30 | Na het werk: builds bekijken, plannen | carrousel, reel, sticker-story |
| Weekendochtend 09:30–10:30 | Bouwdag aan de van, koffie | post, story |
| Vrijdag 18:45–19:30 | Weekendtrip in voorbereiding | post |
| Middag 12:15–12:45 | Lunch, kort | info-story |

Het publiek zit ook in het VK (−1 u) en in Duitsland en Nederland (zelfde uur). 20:00–21:00 Brussel is overal de avond.

### The Fonske Crawl — studenten, expats en toeristen in Leuven, Engels

| Moment | Waarom | Typisch |
| --- | --- | --- |
| Late namiddag 16:30–17:45 | Na de les of het museum: plannen voor de avond | sticker-story, post |
| Avond 20:00–22:15 | Studenten en uitgaanspubliek. Di/wo/do zijn de grote uitgaansavonden in Leuven. | posts, stories |
| Middag 12:15–12:45 | Laatste oproep, tickets | post richting het weekend |
| Op de dag van de crawl | ±15:00 "tonight", ±19:30 "2 hours to go" | stories |

Vlak vóór een crawl telt het event meer dan het venster: tel af naar de crawl.

## Controle vóór de insert

Draai deze query voor de week van het merk. Komt een uur meer dan één keer voor, of zitten alle items in hetzelfde dagdeel, dan pas je dat eerst aan:

```sql
select to_char(scheduled_for at time zone 'Europe/Brussels','HH24:MI') uur, count(*)
from social_posts where tenant_id = '<tenant>' and scheduled_for >= '<maandag> Europe/Brussels'
  and scheduled_for < '<maandag> Europe/Brussels'::timestamptz + interval '7 days'
group by 1 having count(*) > 1;
```
