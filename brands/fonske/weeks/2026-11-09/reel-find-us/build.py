#!/usr/bin/env python3
"""Reel 'How to find us' (reel-animatie: lijntekeningen die zich tekenen op de beat). Muziek: Brass Night, 120 BPM -> scène = 4 tellen = 2,0 s.
Feiten letterlijk van fonskecrawl.com: Ladeuzeplein 21:00 sharp; the Totem = 'the giant needle with the beetle on top';
'Look for the amber wristbands'; 'Your host will be wearing something impossible to miss'. Datum uit SellQo (27-11-2026, scheduled).
Gebruik: python3 build.py, daarna node ../../../../../shared/reel.mjs index.html <uitvoer> --music ../../../music/feest-brass-night.mp3 --music-start 0.5"""
import pathlib
HERE = pathlib.Path(__file__).parent
src = (HERE.parent / "build.py").read_text().split("files = {}")[0]
ns = {"__file__": str(HERE.parent / "build.py")}
exec(src, ns)
svg = ns["svg"]

SC = 4 * 60 / 120
scenes = [
 ("night", "<div class='kicker'>Crawl 02 &middot; Fri 27 Nov</div><h1 class='display' style='font-size:200px'>How to<br><span class='gold'>find us</span></h1>",
  svg("route", "position:absolute; left:90px; top:980px; width:900px; height:620px", prefix="s0", replace={'stroke="#110C08"': 'stroke="#F4F1EC"'})),
 ("cream", "<div class='num'>01</div><h1 class='display' style='font-size:170px'>Ladeuzeplein</h1><p class='lead'>21:00 sharp.</p>",
  svg("last-call", "position:absolute; left:220px; top:1000px; width:640px; height:580px", prefix="s1", replace={"#B9473E": "#1A2A45", "M500 440 L366 363": "M500 440 L345 440"})),
 ("blue", "<div class='num'>02</div><h1 class='display' style='font-size:150px'>Look up</h1><p class='lead'>A giant needle with a beetle on top. That's the Totem.</p>",
  svg("totem", "position:absolute; left:190px; top:1000px; width:700px; height:600px", prefix="s2")),
 ("night", "<div class='num'>03</div><h1 class='display' style='font-size:150px'>Amber<br>wristbands</h1><p class='lead'>That's us.</p>",
  svg("wristband", "position:absolute; left:110px; top:1060px; width:860px; height:540px", prefix="s3")),
 ("amber", "<div class='num'>04</div><h1 class='display' style='font-size:150px'>Find the host</h1><p class='lead'>Wearing something impossible to miss.</p>",
  svg("fonske", "position:absolute; left:250px; top:1000px; width:580px; height:600px", prefix="s4", replace={'stroke="#F4A434"': 'stroke="#110C08"'})),
 ("gold", "<div class='kicker' style='color:#110C08'>Then</div><h1 class='display' style='font-size:170px'>4 bars.<br>1 finale.</h1><p class='lead'>Oude Markt. 18+. Tickets: link in bio.</p>",
  svg("oude-markt", "position:absolute; left:40px; top:1080px; width:1000px; height:520px", prefix="s5", replace={'stroke="#F4A434"': 'stroke="#110C08"'})),
]
N = len(scenes)
DUR = round(SC * N + SC, 2)  # laatste scène blijft 2 scènes staan
parts = [f"<section class='s {bg}' id='s{i}'><div class='grain'></div>{art}<div class='txt'>{text}</div></section>" for i, (bg, text, art) in enumerate(scenes)]

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="nx-reel" content="1080x1920" data-duration="{DUR}" data-fps="30">
<title>Reel: how to find us</title>
<link rel="stylesheet" href="../../../brand.css">
<!-- reel-animatie (nieuw format). Tekeningen totem, route, last-call, wristband (nieuw), fonske, oude-markt tekenen zich lijn per lijn. Scène {SC:.3f} s (Brass Night, 120 BPM). -->
<style>
.s {{ position:absolute; inset:0; opacity:0; overflow:hidden; }}
.night {{ background: radial-gradient(110% 70% at 50% 0%, rgba(150,95,30,.38) 0%, transparent 62%), linear-gradient(180deg,#17110B 0%,#110C08 100%); }}
.cream {{ background:#F4F1EC; }} .cream .display, .cream .lead {{ color:#110C08 }}
.blue {{ background: linear-gradient(180deg,#132036 0%,#0E1626 100%); }}
.amber {{ background:#F4A434; }} .amber .display, .amber .lead {{ color:#110C08 }} .amber .num {{ -webkit-text-stroke-color:#110C08 }}
.gold {{ }} section.gold {{ background: linear-gradient(150deg,#F6CB6A 0%,#F4A434 55%,#E58A2A 100%); }} section.gold .display, section.gold .lead {{ color:#110C08 }}
.txt {{ position:absolute; left:var(--pad); right:var(--pad); top:300px; display:flex; flex-direction:column; gap:22px; }}
.num {{ font-family:"Bebas Neue"; font-size:150px; line-height:.8; color:transparent; -webkit-text-stroke:3px var(--amber); }}
.lead {{ font-size:44px; }}
.logo {{ position:absolute; right:var(--pad); top:240px; width:96px; z-index:5; }}
</style>
</head>
<body>
{chr(10).join(parts)}
<img class="logo" src="../../../logo-mark.png" alt="">
<script>
const SC = {SC}, N = {N};
const S = [...document.querySelectorAll('.s')];
const paths = S.map(s => [...s.querySelectorAll('svg path, svg line, svg polyline, svg circle, svg rect, svg ellipse')].map(p => {{
  let L = 0; try {{ L = p.getTotalLength(); }} catch (e) {{}}
  const fill = getComputedStyle(p).fill; return {{ p, L, fill: p.getAttribute('fill') }};
}}));
window.setT = async (t) => {{
  const i = Math.min(N - 1, Math.floor(t / SC));
  const local = Math.min(1, (t - i * SC) / SC);
  S.forEach((s, k) => {{ s.style.opacity = k === i ? 1 : 0; }});
  const draw = Math.min(1, local / 0.7);
  paths[i].forEach(({{p, L}}) => {{
    if (L > 0) {{ p.style.strokeDasharray = L; p.style.strokeDashoffset = L * (1 - draw); }}
    p.style.fillOpacity = Math.max(0, (draw - .6) / .4);
  }});
  const tx = S[i].querySelector('.txt');
  tx.style.opacity = Math.min(1, local / .1);
  tx.style.transform = `translateY(${{Math.max(0, 30 - local * 300)}}px)`;
}};
</script>
</body>
</html>
"""
(HERE / "index.html").write_text(html)
print("ok", DUR)
