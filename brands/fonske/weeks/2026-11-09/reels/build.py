#!/usr/bin/env python3
"""Twee reels uit echte crawlvideo (crawl_media, crawl 01 van 24-10), enkel fragmenten die nog in geen enkele reel zaten.
Gebruik: V=<map met .mov> O=<uitvoermap> python3 build.py   (vereist ffmpeg en Playwright; PLAYWRIGHT_MODULE optioneel)
- reel-crawl-02 (reel-tekst, Old Market 128 BPM, scène 1,875 s): aankondiging crawl 02.
- reel-pov-crew (reel-pov, Disco Round 118 BPM, scène 2,034 s): POV, je kent niemand in Leuven.
Niet gebruikt (zoals eerder): 83db3e21 en 1dd508c6 (shots in de mond gegoten), aec25cb2 (wazig)."""
import subprocess, os, sys, json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
FONSKE = HERE.parents[2]
O = pathlib.Path(os.environ['O']); V = pathlib.Path(os.environ['V']); O.mkdir(parents=True, exist_ok=True)
vid = {'v1': '3e8a2ecd-5bd3-4475-8346-206c6a3f41e1.mov', 'v2': '011ba278-394c-405c-b2b3-a844fe1dee1f.mov',
       'v3': 'cdd717dc-e529-4bbf-94ed-ad6862fae326.mov', 'v4': 'c607e920-cc9f-4d11-96bf-c72fc304146f.mov',
       'v5': 'f3f4f5c4-bf79-479a-a5b8-a8f0d61fbf29.mov', 'v6': '3e7b98d1-85ae-4f46-a2bd-e1bcfa2000c9.mov'}
CSS = (FONSKE / 'brand.css').as_uri()
LOGO = (FONSKE / 'logo-mark.png').as_uri()

A = 4 * 60 / 128
B = 4 * 60 / 118
reels = {
    'reel-crawl-02': {
        'scene': A, 'music': 'indie-old-market.mp3', 'start': 0,
        'segs': [('v5', 8.0), ('v3', 14.5), ('v2', 3.2), ('v5', 14.8), ('v4', 30.2), ('v4', 33.6)],
        'texts': [("<div class='k'>Crawl 01 was a storm.</div><h1>Remember<br><span class='gold'>that night?</span></h1>", 0, 2),
                  ("<h1>Round<br><span class='gold'>two.</span></h1>", 2, 3),
                  ("<div class='k'>Crawl 02</div><h1>Friday<br><span class='gold'>27 November</span></h1>", 3, 5),
                  ("<h1>21:00<br><span class='gold'>The Totem</span></h1><div class='k'>Ladeuzeplein</div>", 5, 6)],
        'end': ("Crawl 02", "Fri 27 Nov &middot; 21:00", "The Totem &middot; Ladeuzeplein", "Tickets: link in bio &middot; 18+"),
        'endscenes': 2, 'cover': 3,
    },
    'reel-pov-crew': {
        'scene': B, 'music': 'disco-disco-round.mp3', 'start': 0,
        'segs': [('v6', 0.0), ('v1', 11.0), ('v6', 5.0), ('v2', 11.0), ('v6', 8.0)],
        'texts': [("<div class='k'>POV</div><h1>You moved to Leuven.<br><span class='gold'>You know nobody.</span></h1>", 0, 1),
                  ("<h1>Hour one:<br><span class='gold'>small talk.</span></h1>", 1, 2),
                  ("<h1>Hour two:<br><span class='gold'>inside jokes.</span></h1>", 2, 3),
                  ("<h1>Next bar?<br><span class='gold'>Together.</span></h1>", 3, 4),
                  ("<h1>End of the night:<br><span class='gold'>a crew.</span></h1>", 4, 5)],
        'end': ("Next crawl", "Fri 27 Nov &middot; 21:00", "The Totem &middot; Ladeuzeplein", "Bring nobody. Leave with a crew. 18+"),
        'endscenes': 2, 'cover': 0,
    },
}

OVL = """<!doctype html><html><head><meta charset='utf-8'><link rel='stylesheet' href='{css}'>
<style>html,body{{background:transparent!important}} body{{width:1080px;height:1920px}}
.box{{position:absolute;left:70px;right:70px;bottom:420px;padding:44px 50px;background:rgba(17,12,8,.78);border-left:10px solid #F4A434;border-radius:8px;display:flex;flex-direction:column;gap:18px}}
h1{{font-family:'Bebas Neue';font-weight:400;font-size:132px;line-height:.9;text-transform:uppercase;color:#F4F1EC}}
.k{{font-size:30px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:#F4A434}}
.logo{{position:absolute;right:80px;top:250px;width:96px}}</style></head>
<body><img class='logo' src='{logo}'><div class='box'>{t}</div></body></html>"""
END = """<!doctype html><html><head><meta charset='utf-8'><link rel='stylesheet' href='{css}'>
<style>body{{width:1080px;height:1920px}} .w{{position:absolute;left:80px;right:80px;top:420px;display:flex;flex-direction:column;gap:34px}}
.rows .row .v{{font-size:72px}}</style></head>
<body><div class='grain'></div>
<div class='brandrow' style='left:80px;top:250px'><img src='{logo}'><span class='wordmark'>The Fonske Crawl</span></div>
<div class='w'><div class='kicker'>{a}</div><h1 class='display' style='font-size:210px'>{b0}<br><span class='gold'>{b1}</span></h1>
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
        f = O / f'{name}-t{i}.html'; f.write_text(OVL.format(css=CSS, logo=LOGO, t=t)); pngjobs.append((str(f), str(O / f'{name}-t{i}.png'), True))
    a, b, cc, d = c['end']; b0, b1 = b.split(' &middot; ')
    f = O / f'{name}-end.html'; f.write_text(END.format(css=CSS, logo=LOGO, a=a, b0=b0, b1=b1, c=cc, d=d)); pngjobs.append((str(f), str(O / f'{name}-end.png'), False))
js = O / 'shots.mjs'
js.write_text("""const {chromium}=await import(process.env.PLAYWRIGHT_MODULE??'playwright');
const jobs=%s; const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1920}});
for (const [h,o,t] of jobs){ await p.goto('file://'+h,{waitUntil:'networkidle'}); await p.evaluate(()=>document.fonts.ready); await p.screenshot({path:o,omitBackground:t}); }
await b.close();""" % json.dumps(pngjobs))
run(['node', str(js)])

VF = "transpose=1,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p"
for name, c in reels.items():
    S = c['scene']; parts = []
    for i, (v, s) in enumerate(c['segs']):
        out = O / f'{name}_s{i}.mp4'
        # ffmpeg roteert .mov automatisch; transpose enkel als het beeld liggend uitkomt
        run(['ffmpeg', '-v', 'error', '-y', '-ss', str(s), '-t', f'{S:.4f}', '-i', str(V / vid[v]), '-vf', VF.replace('transpose=1,', ''),
             '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-r', '30', str(out)])
        parts.append(out)
    endd = S * c['endscenes']; endv = O / f'{name}_end.mp4'
    run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-t', f'{endd:.4f}', '-i', str(O / f'{name}-end.png'), '-vf',
         'scale=1080:1920,fps=30,format=yuv420p,fade=t=in:st=0:d=0.25', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-r', '30', str(endv)])
    parts.append(endv)
    lst = O / f'{name}_list.txt'; lst.write_text(''.join(f"file '{p}'\n" for p in parts))
    base = O / f'{name}_base.mp4'
    run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', str(lst), '-c', 'copy', str(base)])
    dur = S * (len(c['segs']) + c['endscenes'])
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', str(base)]
    for i, _ in enumerate(c['texts']):
        cmd += ['-loop', '1', '-t', f'{dur:.3f}', '-i', str(O / f'{name}-t{i}.png')]
    fc = []; last = '[0:v]'
    for k, (t, a, b) in enumerate(c['texts'], 1):
        ta, tb = a * S, b * S
        fc.append(f"[{k}:v]format=rgba,fade=t=in:st={ta:.3f}:d=0.15:alpha=1[o{k}]")
        fc.append(f"{last}[o{k}]overlay=0:0:enable='between(t,{ta:.3f},{tb - 0.02:.3f})'[x{k}]"); last = f'[x{k}]'
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
    run(['ffmpeg', '-v', 'error', '-y', '-ss', f"{S * c['cover'] + 0.8:.2f}", '-i', str(music), '-frames:v', '1', '-q:v', '3', str(O / f'{name}-cover.jpg')])
    for f in (silent, music):
        print(name, f.name, f'{dur:.2f}s', f'{f.stat().st_size / 1e6:.2f} MB')
