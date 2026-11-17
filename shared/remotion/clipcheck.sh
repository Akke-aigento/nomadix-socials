#!/bin/bash
# Verplicht vóór een clip in een reel gaat: toont het EXACTE fragment dat in beeld komt.
# Gebruik: shared/remotion/clipcheck.sh <clip.mp4> <from_s> <dur_s> [speed] [uit.jpg]
# (speed zoals in de reel-props; het fragment in de clip is dur × speed seconden)
# Maakt een strip van 6 frames verspreid over [from, from+dur]. Bekijk hem (Read) en controleer
# dat ELK frame past bij de ondertitel. Eén frame dat niet klopt = ander fragment of kortere dur.
set -e
CLIP=$1; FROM=$2; SPEED=${4:-1}; DUR=$(python3 -c "print($3*$SPEED)"); OUT=${5:-/tmp/clipcheck.jpg}
LEN=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$CLIP")
python3 - "$CLIP" "$FROM" "$DUR" "$OUT" "$LEN" <<'PY'
import sys,subprocess,tempfile,os
from PIL import Image,ImageDraw
clip,frm,dur,out,ln=sys.argv[1],float(sys.argv[2]),float(sys.argv[3]),sys.argv[4],float(sys.argv[5])
if frm+dur>ln+0.01: print(f"FOUT: fragment {frm}+{dur}s is langer dan de clip ({ln:.2f}s)"); sys.exit(1)
d=tempfile.mkdtemp();ims=[]
for i in range(6):
    t=frm+dur*i/5 if i<5 else frm+dur-0.05
    p=f"{d}/{i}.jpg";subprocess.run(['ffmpeg','-loglevel','error','-y','-ss',f'{t:.2f}','-i',clip,'-frames:v','1','-vf','scale=200:-1',p],check=True)
    im=Image.open(p);ImageDraw.Draw(im).text((6,6),f"{t:.1f}s",fill='yellow');ims.append(im)
W=sum(i.width+6 for i in ims);H=max(i.height for i in ims);s=Image.new('RGB',(W,H),'white');x=0
for im in ims: s.paste(im,(x,0));x+=im.width+6
s.save(out);print(f"✓ {out}  (clip {ln:.2f}s, fragment {frm}–{frm+dur}s)")
PY
