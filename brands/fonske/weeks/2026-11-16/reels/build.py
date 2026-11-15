#!/usr/bin/env python3
"""Twee reels uit echte crawlvideo (crawl_media, crawl 01 van 24-10). Geen fragment twee keer deze week; f3f4f5c4 niet
(still daarvan staat in de maandagpost). Niet gebruikt (zoals eerder): 83db3e21 en 1dd508c6 (shots in de mond gegoten), aec25cb2 (wazig).
Gebruik: V=<map met .mov> O=<uitvoermap> python3 build.py   (ffmpeg + Playwright; PLAYWRIGHT_MODULE optioneel)
- reel-qa (reel-vraag-antwoord, Swing By 124 BPM; blok = 8 tellen = 3,871 s): 4 vragen van een eerste crawler, antwoorden van de site.
- reel-countdown (reel-aftellen, Pub Stomp 112 BPM; tel = 2 tellen = 1,071 s): 7 → 1 dagen tot crawl 02."""
import subprocess, os, sys, json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
FONSKE = HERE.parents[2]
O = pathlib.Path(os.environ['O']); V = pathlib.Path(os.environ['V']); O.mkdir(parents=True, exist_ok=True)
vid = {'v1': '3e8a2ecd-5bd3-4475-8346-206c6a3f41e1.mov', 'v2': '011ba278-394c-405c-b2b3-a844fe1dee1f.mov',
       'v3': 'cdd717dc-e529-4bbf-94ed-ad6862fae326.mov', 'v4': 'c607e920-cc9f-4d11-96bf-c72fc304146f.mov',
       'v6': '3e7b98d1-85ae-4f46-a2bd-e1bcfa2000c9.mov'}
CSS = (FONSKE / 'brand.css').as_uri()
LOGO = (FONSKE / 'logo-mark.png').as_uri()

QA = 8 * 60 / 124      # 3,871 s
CD = 2 * 60 / 112      # 1,071 s
Q = lambda q, a=None: ("<div class='q'>" + q + "</div>" + (f"<h1>{a}</h1>" if a else ""))
reels = {
    'reel-qa': {
        'music': 'swing-swing-by.mp3', 'start': 0,
        'segs': [('v2', 9.0, QA), ('v1', 4.0, QA), ('v4', 31.9, QA), ('v3', 3.0, QA)],
        'texts': [
            ("<div class='k'>Never done a pub crawl?</div>" + Q("Do I need to speak Dutch?"), 0, QA / 2),
            ("<div class='k'>Never done a pub crawl?</div>" + Q("Do I need to speak Dutch?", "No. <span class='gold'>English by default.</span>"), QA / 2, QA),
            (Q("Do I have to drink alcohol?"), QA, QA * 1.5),
            (Q("Do I have to drink alcohol?", "No. <span class='gold'>Alcohol-free on request.</span>"), QA * 1.5, QA * 2),
            (Q("How long at each bar?"), QA * 2, QA * 2.5),
            (Q("How long at each bar?", "About <span class='gold'>45 minutes.</span> Then we move."), QA * 2.5, QA * 3),
            (Q("Where does it end?"), QA * 3, QA * 3.5),
            (Q("Where does it end?", "The Oude Markt. <span class='gold'>The longest bar in Europe.</span>"), QA * 3.5, QA * 4),
        ],
        'end': ("Crawl 02", "Fri 27 Nov &middot; 21:00", "The Totem &middot; Ladeuzeplein", "18+ with ID &middot; tickets: link in bio"),
        'endlen': QA, 'cover': QA * 0.75,
    },
    'reel-countdown': {
        'music': 'folk-pub-stomp.mp3', 'start': 0,
        'segs': [('v2', 14.0, CD), ('v6', 11.2, CD), ('v4', 36.0, CD), ('v3', 0.3, CD), ('v1', 2.4, CD), ('v2', 16.3, CD), ('v6', 9.0, CD)],
        'texts': [("<div class='k'>Crawl 02 in</div><div class='n'>7</div><div class='k'>days</div>", 0, CD)]
                 + [(f"<div class='n'>{7 - i}</div>", CD * i, CD * (i + 1)) for i in range(1, 7)],
        'end': ("Then this.", "Fri 27 Nov &middot; 21:00", "The Totem &middot; Ladeuzeplein", "Bring your crew. Or come solo. 18+"),
        'endlen': CD * 4, 'cover': CD * 0.5,
    },
}

OVL = """<!doctype html><html><head><meta charset='utf-8'><link rel='stylesheet' href='{css}'>
<style>html,body{{background:transparent!important}} body{{width:1080px;height:1920px}}
.box{{position:absolute;left:70px;right:70px;bottom:420px;padding:44px 50px;background:rgba(17,12,8,.8);border-left:10px solid #F4A434;border-radius:8px;display:flex;flex-direction:column;gap:20px}}
h1{{font-family:'Bebas Neue';font-weight:400;font-size:112px;line-height:.92;text-transform:uppercase;color:#F4F1EC}}
.q{{font-size:50px;font-weight:700;line-height:1.15;color:#F4F1EC}}
.k{{font-size:30px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:#F4A434}}
.cd{{position:absolute;left:0;right:0;top:620px;display:flex;flex-direction:column;align-items:center;gap:6px;text-shadow:0 6px 30px rgba(0,0,0,.55)}}
.n{{font-family:'Bebas Neue';font-size:620px;line-height:.8;color:#F4A434;-webkit-text-stroke:8px #110C08;paint-order:stroke fill;text-shadow:0 10px 40px rgba(0,0,0,.6)}}
.cd .k{{background:rgba(17,12,8,.75);padding:12px 22px;border-radius:999px}}
.logo{{position:absolute;right:80px;top:250px;width:96px}}</style></head>
<body><img class='logo' src='{logo}'>{body}</body></html>"""
END = """<!doctype html><html><head><meta charset='utf-8'><link rel='stylesheet' href='{css}'>
<style>body{{width:1080px;height:1920px}} .w{{position:absolute;left:80px;right:80px;top:420px;display:flex;flex-direction:column;gap:34px}}</style></head>
<body><div class='grain'></div>
<div class='brandrow' style='left:80px;top:250px'><img src='{logo}'><span class='wordmark'>The Fonske Crawl</span></div>
<div class='w'><div class='kicker'>{a}</div><h1 class='display' style='font-size:200px'>{b0}<br><span class='gold'>{b1}</span></h1>
<p class='lead'>{c}</p><p class='lead' style='color:#F4A434'>{d}</p></div>
<img src='{logo}' style='position:absolute;left:390px;top:1180px;width:300px'></body></html>"""


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-2000:]); sys.exit(1)
    return r.stdout


pngjobs = []
for name, c in reels.items():
    for i, (t, a, b) in enumerate(c['texts']):
        body = f"<div class='cd'>{t}</div>" if "class='n'" in t else f"<div class='box'>{t}</div>"
        f = O / f'{name}-t{i}.html'; f.write_text(OVL.format(css=CSS, logo=LOGO, body=body)); pngjobs.append((str(f), str(O / f'{name}-t{i}.png'), True))
    a, b, cc, d = c['end']; b0, b1 = b.split(' &middot; ')
    f = O / f'{name}-end.html'; f.write_text(END.format(css=CSS, logo=LOGO, a=a, b0=b0, b1=b1, c=cc, d=d)); pngjobs.append((str(f), str(O / f'{name}-end.png'), False))
js = O / 'shots.mjs'
js.write_text("""const {chromium}=await import(process.env.PLAYWRIGHT_MODULE??'playwright');
const jobs=%s; const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1920}});
for (const [h,o,t] of jobs){ await p.goto('file://'+h,{waitUntil:'networkidle'}); await p.evaluate(()=>document.fonts.ready); await p.screenshot({path:o,omitBackground:t}); }
await b.close();""" % json.dumps(pngjobs))
run(['node', str(js)])

VF = "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p"
for name, c in reels.items():
    parts = []
    for i, (v, s, d) in enumerate(c['segs']):
        out = O / f'{name}_s{i}.mp4'
        run(['ffmpeg', '-v', 'error', '-y', '-ss', str(s), '-t', f'{d:.4f}', '-i', str(V / vid[v]), '-vf', VF,
             '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-r', '30', str(out)])
        parts.append(out)
    endd = c['endlen']; endv = O / f'{name}_end.mp4'
    run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-t', f'{endd:.4f}', '-i', str(O / f'{name}-end.png'), '-vf',
         'scale=1080:1920,fps=30,format=yuv420p,fade=t=in:st=0:d=0.25', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-r', '30', str(endv)])
    parts.append(endv)
    lst = O / f'{name}_list.txt'; lst.write_text(''.join(f"file '{p}'\n" for p in parts))
    base = O / f'{name}_base.mp4'
    run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', str(lst), '-c', 'copy', str(base)])
    dur = sum(d for _, _, d in c['segs']) + endd
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', str(base)]
    for i, _ in enumerate(c['texts']):
        cmd += ['-loop', '1', '-t', f'{dur:.3f}', '-i', str(O / f'{name}-t{i}.png')]
    fc = []; last = '[0:v]'
    for k, (t, a, b) in enumerate(c['texts'], 1):
        fc.append(f"[{k}:v]format=rgba[o{k}]")
        fc.append(f"{last}[o{k}]overlay=0:0:enable='between(t,{a:.3f},{b - 0.02:.3f})'[x{k}]"); last = f'[x{k}]'
    silent = O / f'{name}-stil.mp4'
    cmd += ['-f', 'lavfi', '-t', f'{dur:.3f}', '-i', 'anullsrc=r=44100:cl=stereo',
            '-filter_complex', ';'.join(fc), '-map', last, '-map', f'{len(c["texts"]) + 1}:a',
            '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '23', '-maxrate', '4M', '-bufsize', '8M', '-pix_fmt', 'yuv420p',
            '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', '-t', f'{dur:.3f}', str(silent)]
    run(cmd)
    music = O / f'{name}-muziek.mp4'
    run(['ffmpeg', '-v', 'error', '-y', '-i', str(silent), '-ss', str(c['start']), '-i', str(FONSKE / 'music' / c['music']),
         '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-af', f'afade=t=in:d=0.2,afade=t=out:st={dur - 1.5:.3f}:d=1.5',
         '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', '-t', f'{dur:.3f}', str(music)])
    run(['ffmpeg', '-v', 'error', '-y', '-ss', f"{c['cover']:.2f}", '-i', str(music), '-frames:v', '1', '-q:v', '3', str(O / f'{name}-cover.jpg')])
    for f in (silent, music):
        print(name, f.name, f'{dur:.2f}s', f'{f.stat().st_size / 1e6:.2f} MB')
