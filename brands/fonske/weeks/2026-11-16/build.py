#!/usr/bin/env python3
"""Bouwt de HTML van de Fonske-week van 16 nov 2026 (week vóór crawl 02; vr 27 nov 21:00 staat 'scheduled' in SellQo).
Feiten: SellQo event_details (27-11-2026, 21:00, Ladeuzeplein; ticket €9.95, early bird €6.95, geen deadline ingevuld)
en fonskecrawl.com (Totem, 4 cafés van ±45 min, shot per stop, alcoholvrij op aanvraag, finale Oude Markt, 18+ met ID,
standaard Engels). Geen cafénamen, geen aantallen, geen deadline.
Foto's: still uit crawlvideo f3f4f5c4 (t=10,4 s) en crawlfoto b1323f66 (beide crawl 01, 24-10, gepubliceerd).
Gebruik: python3 build.py (in deze map). Daarna render.mjs en recipe.mjs; reels: reels/build.py en reel-checklist/."""
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

# ---------- MA: beeld eerst, straatfoto (template street-photo-band, nieuw) ----------
files["post-ma-rain.html"] = page(
    "Wet cobbles, warm bars", "1080x1350",
    "Beeld-eerst. Still uit crawlvideo f3f4f5c4 (t=10,4 s): groep met paraplu's op een zebrapad in Leuven, regen, crawl 01 (24-10). Geen close-up, geen nummerplaten of schermen.",
    """
.photo { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 62%; filter:saturate(1.08) contrast(1.04); }
.shade { position:absolute; inset:0; background:linear-gradient(180deg, rgba(17,12,8,.0) 0%, rgba(17,12,8,0) 58%, rgba(17,12,8,.82) 80%, #110C08 100%); }
.band { position:absolute; left:0; right:0; bottom:0; padding:0 var(--pad) 70px; display:flex; align-items:flex-end; justify-content:space-between; gap:30px; }
.band h1 { font-size:132px; }
.tag { position:absolute; left:var(--pad); top:76px; padding:14px 24px; background:rgba(17,12,8,.72); border-radius:999px; }
""",
    """  <img class="photo" src="../../photos/2026-10-24/still-f3f4f5c4-t10-4.jpg" alt="">
  <div class="shade"></div>
  <div class="tag kicker" data-slot="kicker" data-label="Kicker" data-max="24">Leuven by night</div>
  <img src="../../logo-mark.png" alt="" style="position:absolute; right:var(--pad); top:64px; width:84px">
  <div class="band">
    <h1 class="display" data-slot="titel" data-label="Titel" data-max="34">Wet cobbles.<br><span class="gold">Warm bars.</span></h1>
    <div class="small" style="text-align:right; padding-bottom:12px; color:rgba(244,241,236,.75)" data-slot="voet" data-label="Voet" data-max="30">Crawl 01<br>Sat 24 Oct</div>
  </div>""")

# ---------- DI: story met vraagsticker (template ask-story-night, nieuw) ----------
files["story-di-ask.html"] = page(
    "Ask us anything", "1080x1920",
    "Story met Instagram-vraagsticker (handwerk, manual_reason sticker): zet hem in de lege zone y 880-1240. Tekening speech (nieuw).",
    """
.zone { position:absolute; left:140px; right:140px; top:880px; height:360px; border:3px dashed rgba(244,164,52,.45); border-radius:36px; display:flex; align-items:center; justify-content:center; }
.zone span { font-size:24px; font-weight:700; letter-spacing:.24em; text-transform:uppercase; color:rgba(244,241,236,.35); }
.chips { display:flex; flex-wrap:wrap; gap:14px; margin-top:16px; }
.chips span { padding:14px 24px; border:2px solid rgba(244,164,52,.5); border-radius:999px; font-size:26px; font-weight:500; color:rgba(244,241,236,.85); }
""",
    """  <div class="grain"></div>
  <div class="brandrow" style="top:250px; left:var(--pad)"><img src="../../logo-mark.png" alt=""><span class="wordmark">The Fonske Crawl</span></div>
  <div style="position:absolute; left:var(--pad); right:var(--pad); top:360px; display:flex; flex-direction:column; gap:20px">
    <div class="kicker" data-slot="kicker" data-label="Kicker" data-max="30">Crawl 02 &middot; in 10 days</div>
    <h1 class="display" style="font-size:180px" data-slot="titel" data-label="Titel" data-max="24">Ask us<br><span class="gold">anything.</span></h1>
    <div class="chips"><span data-slot="c1" data-label="Voorbeeld 1" data-max="16">First crawl?</span><span data-slot="c2" data-label="Voorbeeld 2" data-max="16">Coming solo?</span><span data-slot="c3" data-label="Voorbeeld 3" data-max="16">Not drinking?</span></div>
  </div>
  <div class="zone"><span>Question sticker</span></div>
""" + svg("speech", "position:absolute; left:290px; top:1270px; width:500px; height:400px"))

# ---------- DO: foto + tekening op crème (template snapshot-cream, nieuw) ----------
files["post-do-between-bars.html"] = page(
    "Between bar one and the finale", "1080x1350",
    "Foto + tekening. Crawlfoto b1323f66 (crawl 01, 24-10, gepubliceerd): twee crawlers aan de bar, lachend, glas in de hand (geen close-up van drinken). Lijntekening cheers in donkere lijn.",
    """
body.v-cream { background:#F4F1EC; color:#110C08; }
.v-cream .kicker { color:#B5651D; }
.snap { position:absolute; left:120px; top:250px; width:620px; height:860px; background:#fff; padding:26px 26px 110px; box-shadow:0 30px 60px rgba(17,12,8,.22); transform:rotate(-3.5deg); }
.snap img { width:100%; height:100%; object-fit:cover; object-position:50% 58%; display:block; }
.snap .cap { position:absolute; left:30px; right:30px; bottom:30px; font-family:"Bebas Neue"; font-size:48px; color:#110C08; letter-spacing:.03em; }
.side { position:absolute; left:640px; right:60px; top:560px; display:flex; flex-direction:column; gap:22px; transform:rotate(2deg); }
.side h1 { font-size:108px; color:#110C08; }
""",
    """  <div class="brandrow" style="left:var(--pad); top:80px"><img src="../../logo-mark.png" alt="" style="filter:brightness(0)"><span class="wordmark" style="color:#110C08">The Fonske Crawl</span></div>
  <div class="kicker" style="position:absolute; right:var(--pad); top:100px" data-slot="kicker" data-label="Kicker" data-max="20">Crawl 01 &middot; 24 Oct</div>
  <div class="snap"><img src="../../photos/2026-10-24/b1323f66-591c-4966-876e-a1e9fdd71fae.jpg" alt=""><div class="cap" data-slot="onderschrift" data-label="Onderschrift" data-max="26">Leuven, 24 October</div></div>
  <div class="side" style="background:#F4F1EC; padding:34px 30px; border-radius:24px; box-shadow:0 20px 40px rgba(17,12,8,.12)">
    <div class="kicker" data-slot="k2" data-label="Boven titel" data-max="18">Somewhere</div>
    <h1 class="display" data-slot="titel" data-label="Titel" data-max="40">Between<br>bar one<br>and the<br><span style="color:#E58A2A">finale.</span></h1>
  </div>
""" + svg("cheers", "position:absolute; left:560px; top:1090px; width:420px; height:240px", replace={'fill="#F4F1EC"': 'fill="#FFFFFF"'}), "v-cream")

# ---------- VR: aanbod, groot cijfer op amber (template price-amber-stack, nieuw) ----------
files["post-vr-ticket.html"] = page(
    "One Friday, 9.95", "1080x1350",
    "Aanbod crawl 02 (exploit: aanbod + cta profiel + middag). Prijzen live uit SellQo op 15-11: price 9.95, early_bird_price 6.95, early_bird_deadline leeg (geen einddatum vermelden). Geen doorstreepte prijs. Inhoud van de site. Tekening early-bird.",
    """
body.v-amber { background:#F4A434; color:#110C08; }
.v-amber .kicker { color:#110C08; }
.huge { font-family:"Bebas Neue"; font-size:400px; line-height:.78; letter-spacing:-.01em; }
.huge small { font-size:200px; vertical-align:top; line-height:1; }
.lines { display:flex; flex-direction:column; border-top:4px solid #110C08; }
.lines div { font-family:"Bebas Neue"; font-size:62px; line-height:1; padding:18px 0; border-bottom:3px solid rgba(17,12,8,.25); text-transform:uppercase; }
.lines div em { display:block; font-style:normal; font-family:"Space Grotesk"; font-size:28px; font-weight:500; text-transform:none; margin-top:8px; }
.eb { display:inline-flex; gap:16px; align-items:center; padding:16px 26px; background:#110C08; color:#F4F1EC; border-radius:999px; font-size:28px; font-weight:700; }
""",
    """  <div class="brandrow" style="left:var(--pad); top:80px"><img src="../../logo-mark.png" alt="" style="filter:brightness(0)"><span class="wordmark" style="color:#110C08">The Fonske Crawl</span></div>
  <div style="position:absolute; left:var(--pad); right:var(--pad); top:200px; display:flex; flex-direction:column; gap:26px">
    <div class="kicker" data-slot="kicker" data-label="Kicker" data-max="40">Crawl 02 &middot; next Friday, 27 Nov &middot; 21:00</div>
    <div class="huge" data-slot="prijs" data-label="Prijs" data-max="8"><small>&euro;</small>9.95</div>
    <div class="lines" style="margin-right:300px">
      <div data-slot="l1" data-label="Regel 1" data-max="24">4 bars, 1 local host</div>
      <div data-slot="l2" data-label="Regel 2" data-max="60">A shot at every stop <em>alcohol-free on request</em></div>
      <div data-slot="l3" data-label="Regel 3" data-max="30">Finale: the Oude Markt</div>
    </div>
    <div><span class="eb" data-slot="eb" data-label="Early bird" data-max="30">Early bird &euro;6.95 &middot; 18+</span></div>
  </div>
""" + svg("early-bird", "position:absolute; right:30px; bottom:60px; width:420px; height:340px", replace={'>€19<': '>€6.95<', 'font-size="78" fill="#110C08">': 'font-size="64" fill="#110C08">'}), "v-amber")

# ---------- ZA: story met pollsticker + linksticker (template poll-story-blue, nieuw) ----------
files["story-za-poll.html"] = page(
    "Who's with you", "1080x1920",
    "Story met pollsticker (zone y 820-1180) en link-sticker naar /crawls (strook y 1300-1560 vrij). Handwerk, manual_reason sticker. Tekening route onderaan.",
    """
body.v-blue { background: radial-gradient(90% 55% at 50% 100%, rgba(244,164,52,.16) 0%, transparent 65%), linear-gradient(180deg,#0E1626 0%,#132036 100%); }
.zone { position:absolute; left:140px; right:140px; top:820px; height:360px; border:3px dashed rgba(244,164,52,.45); border-radius:36px; display:flex; align-items:center; justify-content:center; }
.zone span { font-size:24px; font-weight:700; letter-spacing:.24em; text-transform:uppercase; color:rgba(244,241,236,.35); }
""",
    """  <div class="grain"></div>
  <div class="brandrow" style="top:250px; left:var(--pad)"><img src="../../logo-mark.png" alt=""><span class="wordmark">The Fonske Crawl</span></div>
  <div style="position:absolute; left:var(--pad); right:var(--pad); top:360px; display:flex; flex-direction:column; gap:22px">
    <div class="kicker" data-slot="kicker" data-label="Kicker" data-max="34">POV &middot; Fri 27 Nov &middot; 20:55</div>
    <h1 class="display" style="font-size:118px" data-slot="titel" data-label="Titel" data-max="44">You're walking<br>to the Totem.<br><span class="gold">Who's with you?</span></h1>
  </div>
  <div class="zone"><span>Poll sticker</span></div>
  <div class="small" style="position:absolute; left:0; right:0; top:1220px; text-align:center">Tickets below &darr;</div>
""" + svg("route", "position:absolute; left:150px; top:1570px; width:780px; height:330px; opacity:.9", replace={'stroke="#110C08"': 'stroke="#F4F1EC"'}), "v-blue")

for name, html in files.items():
    (HERE / name).write_text(html)
    print("✓", name)
