#!/usr/bin/env python3
"""Bouwt de HTML van de Fonske-week van 2 nov 2026 (tekeningen inline, zodat de recepten zonder externe SVG werken).
Gebruik: python3 build.py  (in deze map). Daarna: node ../../../../shared/render.mjs . en recipe.mjs."""
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

# ---------- MA: carrousel "Leuven like a local" (template guide-carousel-blue, nieuw) ----------
BLUE = """
body.v-blue { background: radial-gradient(90% 60% at 50% 0%, rgba(244,164,52,.16) 0%, transparent 65%), linear-gradient(180deg,#132036 0%,#0E1626 100%); }
.count { position:absolute; right:var(--pad); top:70px; font-size:24px; font-weight:700; letter-spacing:.2em; color:var(--mute); }
.num { font-family:"Bebas Neue"; font-size:230px; line-height:.8; color:transparent; -webkit-text-stroke:3px var(--amber); }
"""
NOTE_G = "Carrousel mini-gids (Leuven by night). Feiten van fonskecrawl.com/leuven-nightlife: Oude Markt = 'the longest bar in Europe', elke crawl eindigt daar; bars lopen pas vol na 22:00; Leuven draait op de studentenkalender, weekavonden drukker dan je denkt. Geen cafénamen."

files["carousel-ma-01-cover.html"] = page(
    "Leuven like a local, cover", "1080x1350", NOTE_G + " Cover: straatfoto 61c22281 (regen, toren, groep van achteren, geen gezichten).",
    BLUE + """
.photo { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 58%; }
.shade { position:absolute; inset:0; background:linear-gradient(180deg, rgba(14,22,38,.55) 0%, rgba(14,22,38,0) 18%, rgba(14,22,38,0) 40%, rgba(14,22,38,.9) 70%, #0E1626 100%); }
.swipe { font-size:26px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; color:var(--amber); }
""",
    """  <img class="photo" src="../../photos/2026-10-24/61c22281-5d73-40bd-a5ec-82c8acd154fb.jpg" alt="">
  <div class="shade"></div>
  <div class="brandrow" style="left:56px; top:50px"><img src="../../logo-mark.png" alt=""><span class="wordmark">The Fonske Crawl</span></div>
  <div style="position:absolute; left:var(--pad); right:var(--pad); bottom:90px; display:flex; flex-direction:column; gap:24px">
    <div class="kicker" data-slot="kicker" data-label="Kicker" data-max="30">Leuven by night</div>
    <h1 class="display d-xl" data-slot="titel" data-label="Titel" data-max="34">Go out like<br><span class="gold">a local.</span></h1>
    <p class="lead" data-slot="sub" data-label="Ondertitel" data-max="60">Three things to know before your first night out.</p>
    <div class="swipe">Swipe &rarr;</div>
  </div>""", "v-blue")

tips = [
    ("02", "01", "The Oude Markt", "A square in the old centre lined with bars. Locals call it the longest bar in Europe. Every Fonske Crawl ends here.",
     svg("oude-markt", "position:absolute; left:40px; right:40px; bottom:40px; width:1000px; height:560px")),
    ("03", "02", "Start late", "Most bars only really fill up after 22:00. Dinner, then out. No need to be first.",
     svg("last-call", "position:absolute; left:190px; bottom:40px; width:700px; height:630px", replace={"#B9473E": "#1A2A45"})),
    ("04", "03", "Weeknights count", "Leuven runs on the student calendar. In term time, a weeknight can be busier than you'd expect.",
     svg("fonske", "position:absolute; left:250px; bottom:30px; width:580px; height:640px", replace={'stroke="#110C08"': 'stroke="#F4A434"', 'fill="#110C08"': 'fill="#1A2A45"'})),
]
for n, (cnt, num, title, body, art) in enumerate(tips, start=2):
    files[f"carousel-ma-0{n}-tip.html"] = page(
        f"Leuven like a local, tip {num}", "1080x1350", NOTE_G,
        BLUE,
        f"""  <div class="grain"></div>
  <div class="count">{cnt} / 05</div>
  <div style="position:absolute; left:var(--pad); right:var(--pad); top:80px; display:flex; flex-direction:column; gap:22px">
    <div class="num">{num}</div>
    <h1 class="display d-l" data-slot="titel" data-label="Titel" data-max="22">{title}</h1>
    <p class="lead" data-slot="tekst" data-label="Tekst" data-max="130" data-multiline="true">{body}</p>
  </div>
{art}""", "v-blue")

files["carousel-ma-05-crawl.html"] = page(
    "Leuven like a local, crawl", "1080x1350", NOTE_G + " Slot: wat de crawl is (site): 21:00 Ladeuzeplein, lokale gids, 4 cafés, shot per stop (alcoholvrij op aanvraag), finale Oude Markt, 18+. Geen datum: er staat geen crawl gepland in SellQo.",
    BLUE + """
.facts div { display:flex; gap:24px; align-items:baseline; padding:22px 0; border-top:2px solid var(--line); font-size:32px; color:rgba(244,241,236,.9); }
.facts div:last-child { border-bottom:2px solid var(--line); }
.facts b { font-family:"Bebas Neue"; font-weight:400; font-size:46px; color:var(--amber); min-width:150px; }
""",
    """  <div class="grain"></div>
  <div class="count">05 / 05</div>
  <div style="position:absolute; left:var(--pad); right:var(--pad); top:110px; display:flex; flex-direction:column; gap:22px">
    <div class="kicker" data-slot="kicker" data-label="Kicker" data-max="30">Or skip the guesswork</div>
    <h1 class="display d-l" data-slot="titel" data-label="Titel" data-max="36">Let a local<br><span class="gold">show you.</span></h1>
  </div>
  <div class="facts" style="position:absolute; left:var(--pad); right:400px; top:520px">
    <div><b>21:00</b><span data-slot="f1" data-label="Feit 1" data-max="30">Ladeuzeplein, at the Totem</span></div>
    <div><b>4 bars</b><span data-slot="f2" data-label="Feit 2" data-max="30">with a local host</span></div>
    <div><b>1 shot</b><span data-slot="f3" data-label="Feit 3" data-max="34">per stop, alcohol-free on request</span></div>
    <div><b>Finale</b><span data-slot="f4" data-label="Feit 4" data-max="30">on the Oude Markt. 18+</span></div>
  </div>
""" + svg("totem", "position:absolute; right:20px; bottom:50px; width:400px; height:800px") + """
  <div class="small" style="position:absolute; left:var(--pad); bottom:70px">fonskecrawl.com</div>""", "v-blue")

# ---------- DI: pollstory (template poll-story-cream, nieuw) ----------
files["story-di-poll.html"] = page(
    "Leuven poll", "1080x1920", "Story met pollsticker (handwerk). Vrije zone voor de sticker: y 880-1330. Tekening route.svg (crème). Geen feitelijke claim: enkel een vraag.",
    """
body.v-cream { background: #F4F1EC; }
.v-cream .display, .v-cream .lead { color:#110C08 } .v-cream .kicker { color:#C4650F }
.zone { position:absolute; left:120px; right:120px; top:880px; height:450px; border:4px dashed rgba(17,12,8,.22); border-radius:40px; display:flex; align-items:center; justify-content:center; font-size:26px; letter-spacing:.2em; text-transform:uppercase; color:rgba(17,12,8,.0); }
""",
    """  <div class="brandrow" style="top:250px; left:var(--pad)"><img src="../../logo-mark.png" alt="" style="filter:brightness(.2)"><span class="wordmark" style="color:#110C08">The Fonske Crawl</span></div>
  <div style="position:absolute; left:var(--pad); right:var(--pad); top:380px; display:flex; flex-direction:column; gap:26px">
    <div class="kicker" data-slot="kicker" data-label="Kicker" data-max="26">Leuven poll</div>
    <h1 class="display d-l" data-slot="titel" data-label="Titel" data-max="40">Best night<br>to go out?</h1>
  </div>
  <div class="zone"></div>
""" + svg("route", "position:absolute; left:140px; bottom:200px; width:800px; height:370px"), "v-cream")

# ---------- DO: vergelijking teambuilding (template versus-amber, nieuw) ----------
files["post-do-teambuilding.html"] = page(
    "Four bars, one invoice", "1080x1350", "Vergelijking, typografisch. Alles van fonskecrawl.com/teambuilding-leuven: geen vier zaken reserveren, geen rekeningen splitsen bij elke stop; factuur met bedrijfsnaam en btw-nummer; lokale gids; alcoholvrij aan dezelfde prijs; eindejaarsdrink genoemd. Prijs €19.99 p.p., minimum €239.88 (site/README). Tekening tie.svg (nieuw).",
    """
body.v-amber { background: #F4A434; }
.v-amber .display, .v-amber .lead, .v-amber .body { color:#110C08 } .v-amber .kicker { color:#110C08; opacity:.7 }
.vs { position:absolute; left:var(--pad); right:var(--pad); top:470px; display:grid; grid-template-columns:1fr 1fr; column-gap:36px; }
.vs .h { font-size:22px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; padding-bottom:16px; border-bottom:3px solid #110C08; color:#110C08; }
.vs .h.no { opacity:.55; }
.vs .c { font-size:29px; line-height:1.3; padding:20px 0; border-bottom:2px solid rgba(17,12,8,.2); color:#110C08; font-weight:500; min-height:116px; }
.vs .c.no { color:rgba(17,12,8,.55); font-weight:400; }
.price { position:absolute; left:var(--pad); bottom:84px; right:330px; }
.price .p { font-family:"Bebas Neue"; font-size:96px; line-height:.9; color:#110C08; }
""",
    """  <div class="grain"></div>
  <div style="position:absolute; left:var(--pad); right:var(--pad); top:90px; display:flex; flex-direction:column; gap:20px">
    <div class="kicker" data-slot="kicker" data-label="Kicker" data-max="40">Teambuilding &amp; end-of-year drinks</div>
    <h1 class="display d-l" data-slot="titel" data-label="Titel" data-max="30">Four bars.<br>One invoice.</h1>
  </div>
  <div class="vs">
    <div class="h no">Doing it yourself</div><div class="h">A private Fonske Crawl</div>
    <div class="c no" data-slot="n1" data-label="Zelf 1" data-max="40">Book four venues</div><div class="c" data-slot="y1" data-label="Crawl 1" data-max="40">One request, you pick the date</div>
    <div class="c no" data-slot="n2" data-label="Zelf 2" data-max="40">Split the bill at every stop</div><div class="c" data-slot="y2" data-label="Crawl 2" data-max="44">One invoice, company name and VAT</div>
    <div class="c no" data-slot="n3" data-label="Zelf 3" data-max="40">Somebody plans the route</div><div class="c" data-slot="y3" data-label="Crawl 3" data-max="40">A local host who knows it</div>
    <div class="c no" data-slot="n4" data-label="Zelf 4" data-max="40">Colleagues who don't drink?</div><div class="c" data-slot="y4" data-label="Crawl 4" data-max="40">Alcohol-free, same price</div>
  </div>
  <div class="price">
    <div class="p" data-slot="prijs" data-label="Prijs" data-max="20">&euro;19.99 p.p.</div>
    <p class="body" style="font-weight:500" data-slot="min" data-label="Minimum" data-max="50">Minimum &euro;239.88 &middot; 18+ &middot; Leuven</p>
  </div>
""" + svg("tie", "position:absolute; right:40px; bottom:40px; width:320px; height:290px"), "v-amber")

# ---------- VR: beeld eerst (template photo-frame, nieuw) ----------
files["post-vr-exhibit-a.html"] = page(
    "Exhibit A", "1080x1350", "Beeld eerst: crawlfoto e60ef123 (crawl 01, 24 okt; twee crawlers aan tafel, krijtbord). Amber lijnkader + logo als tekening. Geen claim behalve de datum van de foto.",
    """
.photo { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:50% 62%; }
.shade { position:absolute; inset:0; background:linear-gradient(180deg, rgba(17,12,8,.5) 0%, rgba(17,12,8,0) 16%, rgba(17,12,8,0) 66%, rgba(17,12,8,.88) 100%); }
.frame { position:absolute; inset:34px; border:5px solid var(--amber); border-radius:6px; }
.frame-gap { position:absolute; left:110px; bottom:22px; width:560px; height:30px; background:transparent; }
.stamp { font-size:24px; font-weight:700; letter-spacing:.22em; text-transform:uppercase; color:var(--cream); opacity:.9; }
""",
    """  <img class="photo" src="../../photos/2026-10-24/e60ef123-6c16-4f66-87e3-e733d223de54.jpg" alt="">
  <div class="shade"></div>
  <div class="frame"></div>
  <img src="../../logo-mark.png" alt="" style="position:absolute; right:84px; bottom:90px; width:120px">
  <div style="position:absolute; left:84px; right:84px; bottom:84px; display:flex; flex-direction:column; gap:14px">
    <h1 class="display d-l" data-slot="titel" data-label="Titel" data-max="16">Exhibit <span class="gold">A</span></h1>
    <div class="stamp" data-slot="stempel" data-label="Stempel" data-max="40">Crawl 01 &middot; Leuven &middot; 24.10.2026</div>
  </div>""")

# ---------- ZA: story aanvraag (template request-story-night, nieuw) ----------
files["story-za-pick-your-night.html"] = page(
    "You pick the night", "1080x1920", "Story met link-sticker naar /crawls (formulier 'Date not listed?'). Site: 'Tell us when you want to crawl and we'll try to make it happen.' Strook y 1300-1560 vrij voor de sticker. Tekening totem.svg. Geen datum beweren (geen crawl scheduled in SellQo).",
    """
""",
    """  <div class="grain"></div>
  <div class="brandrow" style="top:250px; left:var(--pad)"><img src="../../logo-mark.png" alt=""><span class="wordmark">The Fonske Crawl</span></div>
  <div style="position:absolute; left:var(--pad); right:var(--pad); top:370px; display:flex; flex-direction:column; gap:26px">
    <div class="kicker" data-slot="kicker" data-label="Kicker" data-max="26">Date not listed?</div>
    <h1 class="display d-xl" data-slot="titel" data-label="Titel" data-max="30">You pick<br><span class="gold">the night.</span></h1>
    <p class="lead" data-slot="tekst" data-label="Tekst" data-max="90" data-multiline="true">Tell us when you want to crawl and we'll try to make it happen.</p>
  </div>
""" + svg("totem", "position:absolute; left:290px; top:920px; width:500px; height:370px") + """
  <div class="small" style="position:absolute; left:0; right:0; top:1620px; text-align:center">fonskecrawl.com/crawls</div>""")

for name, html in files.items():
    (HERE / name).write_text(html)
    print("✓", name)
