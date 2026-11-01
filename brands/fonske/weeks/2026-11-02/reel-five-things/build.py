#!/usr/bin/env python3
"""Reel 'Five things in one ticket' (reel-slideshow: foto's + tekeningen op de beat). Muziek: Pub Stomp, 112 BPM -> scène = 4 tellen = 2,143 s.
Inhoud letterlijk van fonskecrawl.com ('What's included'): local host, 4 shots (alcoholvrij op aanvraag), new friends, photos, safe way home (night bus); finale Oude Markt."""
import importlib.util, pathlib
HERE = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("b", HERE.parent / "build.py")
# enkel de svg()-helper hergebruiken, zonder de week opnieuw te schrijven
src = (HERE.parent / "build.py").read_text().split("files = {}")[0]
ns = {"__file__": str(HERE.parent / "build.py")}
exec(src, ns)
svg = ns["svg"]

SC = 4 * 60 / 112
scenes = [
 ("night", "", "<div class='kicker'>The Fonske Crawl</div><h1 class='display' style='font-size:190px'>5 things<br><span class='gold'>in one ticket</span></h1>",
  svg("totem", "position:absolute; left:240px; top:960px; width:600px; height:560px", prefix="s0")),
 ("cream", "", "<div class='num'>01</div><h1 class='display' style='font-size:170px'>A local host</h1><p class='lead'>Not a Google Maps pin.</p>",
  svg("route", "position:absolute; left:100px; top:1000px; width:880px; height:560px", prefix="s1")),
 ("photo", "../../../photos/2026-10-24/31e6b7bd-3de6-426a-a6bd-748c937ed86f.jpg", "<div class='num'>02</div><h1 class='display' style='font-size:170px'>Four shots</h1><p class='lead'>One per bar. Alcohol-free on request.</p>", ""),
 ("photo", "../../../photos/2026-10-24/68287ecb-066a-4065-bbb4-25a0cf291352.jpg", "<div class='num'>03</div><h1 class='display' style='font-size:170px'>New friends</h1><p class='lead'>Students, Erasmus crowd, locals and lost tourists.</p>", ""),
 ("blue", "", "<div class='num'>04</div><h1 class='display' style='font-size:170px'>Photos</h1><p class='lead'>The evidence lands in the Crawl Log.</p>",
  svg("camera", "position:absolute; left:90px; top:1000px; width:900px; height:600px", prefix="s4")),
 ("amber", "", "<div class='num'>05</div><h1 class='display' style='font-size:170px'>A safe way home</h1><p class='lead'>We'll point you to the right night bus.</p>",
  svg("nightbus", "position:absolute; left:90px; top:1010px; width:900px; height:580px", prefix="s5")),
 ("night", "", "<div class='kicker'>And the finale</div><h1 class='display' style='font-size:170px'>The Oude Markt.</h1><p class='lead'>New dates at fonskecrawl.com &middot; 18+</p>",
  svg("oude-markt", "position:absolute; left:40px; top:1040px; width:1000px; height:560px", prefix="s6")),
]
DUR = round(SC * len(scenes), 2)
parts = []
for i, (bg, photo, text, art) in enumerate(scenes):
    ph = f"<img class='ph' src='{photo}' alt=''><div class='shade'></div>" if photo else ""
    top = "bottom:330px" if photo else "top:300px"
    parts.append(f"<section class='s {bg}' id='s{i}'><div class='grain'></div>{ph}{art}<div class='txt' style='{top}'>{text}</div></section>")

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="nx-reel" content="1080x1920" data-duration="{DUR}" data-fps="30">
<title>Reel: five things in one ticket</title>
<link rel="stylesheet" href="../../../brand.css">
<!-- reel-slideshow (vorige week reel-montage met video). Foto's crawl 01: 31e6b7bd, 68287ecb. Tekeningen: totem, route, camera, nightbus (nieuw), oude-markt. Scène {SC:.3f} s (Pub Stomp, 112 BPM). -->
<style>
.s {{ position:absolute; inset:0; opacity:0; overflow:hidden; }}
.night {{ background: radial-gradient(110% 70% at 50% 0%, rgba(150,95,30,.38) 0%, transparent 62%), linear-gradient(180deg,#17110B 0%,#110C08 100%); }}
.cream {{ background:#F4F1EC; }} .cream .display, .cream .lead {{ color:#110C08 }}
.blue {{ background: linear-gradient(180deg,#132036 0%,#0E1626 100%); }}
.amber {{ background:#F4A434; }} .amber .display, .amber .lead {{ color:#110C08 }} .amber .num {{ -webkit-text-stroke-color:#110C08 }}
.ph {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }}
.shade {{ position:absolute; inset:0; background:linear-gradient(180deg, rgba(17,12,8,.35) 0%, rgba(17,12,8,0) 25%, rgba(17,12,8,0) 45%, rgba(17,12,8,.92) 82%, #110C08 100%); }}
.txt {{ position:absolute; left:var(--pad); right:var(--pad); display:flex; flex-direction:column; gap:22px; }}
.num {{ font-family:"Bebas Neue"; font-size:150px; line-height:.8; color:transparent; -webkit-text-stroke:3px var(--amber); }}
.lead {{ font-size:44px; }}
.logo {{ position:absolute; right:var(--pad); top:240px; width:96px; z-index:5; }}
</style>
</head>
<body>
{chr(10).join(parts)}
<img class="logo" id="logo" src="../../../logo-mark.png" alt="">
<script>
const SC = {SC}, N = {len(scenes)};
const S = [...document.querySelectorAll('.s')];
const imgs = [...document.images];
const ready = Promise.all(imgs.map(im => im.complete ? 1 : new Promise(r => im.addEventListener('load', r, {{ once: true }}))));
window.setT = async (t) => {{
  await ready;
  const i = Math.min(N - 1, Math.floor(t / SC));
  const local = (t - i * SC) / SC;
  S.forEach((s, k) => {{
    s.style.opacity = k === i ? 1 : 0;
    if (k === i) {{
      const pop = local < .08 ? 1.04 - .5 * local : 1;
      const ph = s.querySelector('.ph'); if (ph) ph.style.transform = `scale(${{1.03 + .07 * local}})`;
      const tx = s.querySelector('.txt'); tx.style.transform = `scale(${{pop}})`; tx.style.transformOrigin = 'left center';
      tx.style.opacity = Math.min(1, local / .07);
    }}
  }});
  const fade = i === N - 1 ? Math.max(0, 1 - (t - (DUR - 1.2)) / 1.2) : 1;
  document.body.style.opacity = 1;
}};
const DUR = {DUR};
</script>
</body>
</html>
"""
(HERE / "index.html").write_text(html)
print("ok", DUR)
