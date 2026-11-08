#!/usr/bin/env python3
"""Bouwt de HTML van de Fonske-week van 9 nov 2026 (crawl 02 op vr 27 nov staat 'scheduled' in SellQo).
Feiten: SellQo event_details (27-11-2026, 21:00, Ladeuzeplein; ticket €9.95, early bird €6.95, geen deadline ingevuld)
en fonskecrawl.com (Totem = reuzennaald met de kever, amber polsbandjes, 4 cafés, shot per stop, alcoholvrij op aanvraag,
finale Oude Markt, 18+). Geen cafénamen, geen aantallen, geen deadline.
Gebruik: python3 build.py  (in deze map). Daarna render.mjs en recipe.mjs; reels: reels/build.py en reel-find-us/."""
import re, pathlib

HERE = pathlib.Path(__file__).parent
ILL = HERE / ".." / ".." / "illustrations"


def svg(name, style, prefix=None, replace=None):
    s = (ILL / f"{name}.svg").read_text()
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    for a, b in (replace or {}).items():
        s = s.replace(a, b)
    p = prefix or name.replace("-", "")
    s = re.sub(r'id="([^"]+)"', lambda m: f'id="{p}-{m.group(1)}"', s)
    s = re.sub(r"url\(#([^)]+)\)", lambda m: f"url(#{p}-{m.group(1)})", s)
    return s.replace("<svg ", f'<svg style="{style}" preserveAspectRatio="xMidYMid meet" ', 1)


def page(title, size, note, css, body, cls=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="nx-size" content="{size}">
<title>{title}</title>
<link rel="stylesheet" href="../../brand.css">
<!-- {note} -->
<style>
{css}
</style>
</head>
<body class="{cls}">
{body}
</body>
</html>
"""


files = {}

# ---------- MA: aankondiging met foto (template announce-photo-date, nieuw) ----------
files["post-ma-crawl-02.html"] = page(
    "Crawl 02 is on", "1080x1350",
    "Aankondiging crawl 02 (SellQo: 27-11-2026 21:00, Ladeuzeplein, scheduled). Achtergrond: still uit crawlvideo cdd717dc (t=16,8 s; groep in de regen van achteren, geen gezichten).",
    """
.photo { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 30%; filter:saturate(1.05) contrast(1.05); }
.shade { position:absolute; inset:0; background:linear-gradient(180deg, rgba(17,12,8,.82) 0%, rgba(17,12,8,.25) 30%, rgba(17,12,8,0) 46%, rgba(17,12,8,.78) 66%, #110C08 92%); }
.date { display:flex; align-items:flex-end; gap:26px; }
.date .d { font-family:"Bebas Neue"; font-size:330px; line-height:.76; }
.date .m { display:flex; flex-direction:column; gap:6px; padding-bottom:14px; }
.date .m b { font-family:"Bebas Neue"; font-weight:400; font-size:120px; line-height:.8; color:var(--cream); }
.date .m span { font-size:28px; font-weight:700; letter-spacing:.22em; text-transform:uppercase; color:var(--amber); }
.line { display:flex; gap:18px; flex-wrap:wrap; }
""",
    """  <img class="photo" src="../../photos/2026-10-24/still-cdd717dc-t16-8.jpg" alt="">
  <div class="shade"></div>
  <div class="brandrow" style="left:var(--pad); top:70px"><img src="../../logo-mark.png" alt=""><span class="wordmark">The Fonske Crawl</span></div>
  <div class="kicker" style="position:absolute; right:var(--pad); top:86px" data-slot="kicker" data-label="Kicker" data-max="20">Crawl 02 is on</div>
  <div style="position:absolute; left:var(--pad); right:var(--pad); bottom:84px; display:flex; flex-direction:column; gap:30px">
    <div class="date">
      <div class="d gold" data-slot="dag" data-label="Dag" data-max="2">27</div>
      <div class="m"><span data-slot="weekdag" data-label="Weekdag" data-max="12">Friday</span><b data-slot="maand" data-label="Maand" data-max="10">November</b></div>
    </div>
    <div class="line">
      <span class="pill amber" data-slot="uur" data-label="Uur" data-max="8">21:00</span>
      <span class="pill ghost" data-slot="plek" data-label="Plek" data-max="34">The Totem &middot; Ladeuzeplein</span>
      <span class="pill ghost" data-slot="leeftijd" data-label="Leeftijd" data-max="6">18+</span>
    </div>
  </div>""")

# ---------- DI: story met countdown-sticker (template countdown-story-blue, nieuw) ----------
files["story-di-countdown.html"] = page(
    "Countdown to crawl 02", "1080x1920",
    "Story met Instagram-countdownsticker (handwerk, manual_reason sticker): zet hem in de lege zone y 860-1240, einddatum 27 nov 21:00. Tekening totem.",
    """
body.v-blue { background: radial-gradient(90% 55% at 50% 100%, rgba(244,164,52,.18) 0%, transparent 65%), linear-gradient(180deg,#0E1626 0%,#132036 100%); }
.zone { position:absolute; left:140px; right:140px; top:860px; height:380px; border:3px dashed rgba(244,164,52,.45); border-radius:36px; display:flex; align-items:center; justify-content:center; }
.zone span { font-size:24px; font-weight:700; letter-spacing:.24em; text-transform:uppercase; color:rgba(244,241,236,.35); }
""",
    """  <div class="grain"></div>
  <div class="brandrow" style="top:250px; left:var(--pad)"><img src="../../logo-mark.png" alt=""><span class="wordmark">The Fonske Crawl</span></div>
  <div style="position:absolute; left:var(--pad); right:var(--pad); top:370px; display:flex; flex-direction:column; gap:24px">
    <div class="kicker" data-slot="kicker" data-label="Kicker" data-max="30">Fri 27 Nov &middot; 21:00</div>
    <h1 class="display d-xl" data-slot="titel" data-label="Titel" data-max="30">Who's<br><span class="gold">coming?</span></h1>
  </div>
""" + svg("totem", "position:absolute; left:300px; top:1260px; width:480px; height:360px") + """
  <div class="small" style="position:absolute; left:0; right:0; top:1600px; text-align:center" data-slot="voet" data-label="Voet" data-max="50">Tap the countdown. We'll remind you.</div>""", "v-blue")

# ---------- DO: aanbod, groot cijfer op goud (template ticket-gold, nieuw) ----------
files["post-do-early-bird.html"] = page(
    "Early bird crawl 02", "1080x1350",
    "Aanbod crawl 02. Prijzen live uit SellQo op 8-11: early_bird_price 6.95, price 9.95, early_bird_deadline leeg (dus geen einddatum vermelden). Geen doorstreepte prijs. Inhoud van de site.",
    """
body.v-gold { background: linear-gradient(150deg, #F6CB6A 0%, #F4A434 55%, #E58A2A 100%); color:#110C08; }
.v-gold .kicker { color:#110C08; }
.ticket { position:absolute; left:70px; right:70px; top:300px; height:470px; background:#110C08; border-radius:34px; display:flex; overflow:hidden; }
.ticket::before, .ticket::after { content:""; position:absolute; left:640px; width:64px; height:64px; border-radius:50%; background:#F4A434; }
.ticket::before { top:-32px; } .ticket::after { bottom:-32px; }
.ticket .l { width:672px; padding:46px 54px; display:flex; flex-direction:column; justify-content:space-between; border-right:4px dashed rgba(244,164,52,.5); }
.ticket .r { flex:1; padding:46px 30px; display:flex; flex-direction:column; justify-content:center; align-items:center; gap:14px; text-align:center; }
.big { font-family:"Bebas Neue"; font-size:250px; line-height:.8; }
.reg { font-family:"Bebas Neue"; font-size:84px; line-height:.9; color:var(--cream); }
.list { position:absolute; left:var(--pad); right:360px; top:830px; display:flex; flex-direction:column; gap:16px; font-size:32px; font-weight:500; line-height:1.3; }
.list div { padding-left:40px; position:relative; }
.list div::before { content:""; position:absolute; left:0; top:14px; width:18px; height:18px; border-radius:50%; background:#110C08; }
""",
    """  <div class="brandrow" style="left:var(--pad); top:80px"><img src="../../logo-mark.png" alt="" style="filter:brightness(0)"><span class="wordmark" style="color:#110C08">The Fonske Crawl</span></div>
  <div class="kicker" style="position:absolute; left:var(--pad); top:190px" data-slot="kicker" data-label="Kicker" data-max="36">Crawl 02 &middot; Friday 27 November</div>
  <div class="ticket">
    <div class="l">
      <div class="kicker" style="color:var(--amber)" data-slot="label1" data-label="Label" data-max="16">Early bird</div>
      <div class="big gold" data-slot="prijs" data-label="Prijs" data-max="8">&euro;6.95</div>
      <div class="small" style="color:var(--mute)" data-slot="sub" data-label="Onder prijs" data-max="40">per ticket &middot; 21:00 &middot; Ladeuzeplein</div>
    </div>
    <div class="r">
      <div class="kicker" style="color:var(--mute)" data-slot="label2" data-label="Label 2" data-max="10">Regular</div>
      <div class="reg" data-slot="prijs2" data-label="Gewone prijs" data-max="8">&euro;9.95</div>
    </div>
  </div>
  <div class="list">
    <div data-slot="l1" data-label="Punt 1" data-max="40">4 bars with a local host</div>
    <div data-slot="l2" data-label="Punt 2" data-max="44">A shot at every stop, alcohol-free on request</div>
    <div data-slot="l3" data-label="Punt 3" data-max="40">Finale on the Oude Markt</div>
    <div data-slot="l4" data-label="Punt 4" data-max="40">18+ &middot; tickets via the link in bio</div>
  </div>
""" + svg("cheers", "position:absolute; right:40px; bottom:40px; width:330px; height:420px", replace={'stroke="#F4A434"': 'stroke="#110C08"', 'stroke="#F4F1EC"': 'stroke="#110C08"'}), "v-gold")

# ---------- ZA: story dit-of-dat met linksticker (template this-or-that-cream, nieuw) ----------
files["story-za-friday-plans.html"] = page(
    "Friday plans", "1080x1920",
    "Story met link-sticker naar /crawls (strook y 1300-1560 vrij). Contrast: zelfde vrijdagavond, twee plannen. Feiten site: 4 bars, finale Oude Markt ('the longest bar in Europe'), lokale gids. Tekening oude-markt.",
    """
body.v-cream { background:#F4F1EC; color:#110C08; }
.v-cream .kicker { color:#B5651D; }
.opt { display:flex; align-items:center; gap:30px; padding:34px 0; border-top:3px solid rgba(17,12,8,.14); }
.opt .ab { font-family:"Bebas Neue"; font-size:120px; line-height:.8; min-width:90px; }
.opt .t { font-family:"Bebas Neue"; font-size:74px; line-height:.92; text-transform:uppercase; }
.opt.no .t { color:rgba(17,12,8,.38); }
.opt.no .ab { color:rgba(17,12,8,.25); }
.opt.yes .ab { color:#E58A2A; }
""",
    """  <div class="brandrow" style="top:250px; left:var(--pad)"><img src="../../logo-mark.png" alt="" style="filter:brightness(0)"><span class="wordmark" style="color:#110C08">The Fonske Crawl</span></div>
  <div style="position:absolute; left:var(--pad); right:var(--pad); top:370px; display:flex; flex-direction:column; gap:10px">
    <div class="kicker" data-slot="kicker" data-label="Kicker" data-max="30">Friday 27 November</div>
    <h1 class="display d-l" style="margin-bottom:30px" data-slot="titel" data-label="Titel" data-max="24">Pick your Friday.</h1>
    <div class="opt no"><div class="ab">A</div><div class="t" data-slot="a" data-label="Optie A" data-max="40">Sofa, series, <br>“one more episode”</div></div>
    <div class="opt yes" style="border-bottom:3px solid rgba(17,12,8,.14)"><div class="ab">B</div><div class="t" data-slot="b" data-label="Optie B" data-max="44">4 bars, a local host,<br>the longest bar in Europe</div></div>
  </div>
""" + svg("oude-markt", "position:absolute; left:40px; top:1560px; width:1000px; height:300px; opacity:.9", replace={'stroke="#F4A434"': 'stroke="#110C08"', 'stroke="#F4F1EC"': 'stroke="#E58A2A"'}) + """
  <div class="small" style="position:absolute; left:0; right:0; top:1250px; text-align:center; color:rgba(17,12,8,.55)">B? Tickets below &darr;</div>""", "v-cream")

for name, html in files.items():
    (HERE / name).write_text(html)
    print("✓", name)
