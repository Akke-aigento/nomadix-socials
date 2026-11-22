#!/usr/bin/env python3
"""FILM-1 kwaliteitscontrole per shot of per film (Akke 22-11: "zo'n AI-fouten mogen er niet in").
Gebruik: filmcheck.py <video.mp4> <uitmap> [--from s] [--to s]
Maakt:
  - grids van 3x2 frames per 0,25 s op 360 px breed (om elk frame echt te bekijken),
  - een sprongenlijst: frames waar het beeld plots verspringt (verschil t.o.v. vorig frame >> mediaan),
  - zooms van de sprongen (frame ervoor / erna naast elkaar).
Alles moet daarna met het oog nagekeken worden op de checklist in FILM.md §5.
"""
import subprocess, sys, os, json, statistics
from PIL import Image, ImageChops, ImageStat
src, out = sys.argv[1], sys.argv[2]
a = sys.argv[3:]; t0 = float(a[a.index('--from')+1]) if '--from' in a else 0.0
dur = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src]).decode())
t1 = float(a[a.index('--to')+1]) if '--to' in a else dur
os.makedirs(out, exist_ok=True)
fd = os.path.join(out, 'frames'); os.makedirs(fd, exist_ok=True)
subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t0),'-to',str(t1),'-i',src,'-vf','fps=12,scale=360:-2',os.path.join(fd,'f%05d.jpg')], check=True)
files = sorted(os.listdir(fd)); ims = [Image.open(os.path.join(fd,f)).convert('L').resize((90,160)) for f in files]
diffs = [0.0] + [ImageStat.Stat(ImageChops.difference(ims[i], ims[i-1])).mean[0] for i in range(1,len(ims))]
med = statistics.median(diffs[1:]) if len(diffs) > 2 else 1
jumps = [(round(t0+i/12,2), round(d,1)) for i,d in enumerate(diffs) if i and d > max(6*med, 8)]
# grids van 6 frames, om de 3 frames (0,25 s)
pick = list(range(0, len(files), 3)); grids = []
for g in range(0, len(pick), 6):
    sel = pick[g:g+6]; tiles = [Image.open(os.path.join(fd, files[i])) for i in sel]
    w, h = tiles[0].size; G = Image.new('RGB', (w*3, h*2), 'white')
    for k, im in enumerate(tiles): G.paste(im, ((k%3)*w, (k//3)*h))
    p = os.path.join(out, f'grid_{t0+sel[0]/12:05.2f}s.jpg'); G.save(p, quality=85); grids.append(p)
for t, d in jumps:
    i = int(round((t-t0)*12)); A = Image.open(os.path.join(fd, files[i-1])); B = Image.open(os.path.join(fd, files[i]))
    J = Image.new('RGB', (A.width*2, A.height)); J.paste(A,(0,0)); J.paste(B,(A.width,0)); J.save(os.path.join(out, f'jump_{t:05.2f}s.jpg'))
json.dump({'src': src, 'from': t0, 'to': t1, 'median_diff': round(med,2), 'jumps': jumps, 'grids': grids}, open(os.path.join(out,'report.json'),'w'), indent=1)
print(json.dumps({'median_diff': round(med,2), 'jumps': jumps, 'grids': len(grids)}))
