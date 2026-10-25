import subprocess, os, json, sys
O=os.environ['O']; V=os.environ['V']
vid={'v1':'3e8a2ecd-5bd3-4475-8346-206c6a3f41e1.mov','v2':'011ba278-394c-405c-b2b3-a844fe1dee1f.mov','v3':'cdd717dc-e529-4bbf-94ed-ad6862fae326.mov','v4':'c607e920-cc9f-4d11-96bf-c72fc304146f.mov','v5':'f3f4f5c4-bf79-479a-a5b8-a8f0d61fbf29.mov','v6':'3e7b98d1-85ae-4f46-a2bd-e1bcfa2000c9.mov'}
END=2.5
reels={
 'r1':{'segs':[('v3',2.0,3.0,1),('v5',4.5,3.5,1),('v3',9.0,2.5,1),('v4',13.5,2.0,1),('v4',26.0,2.0,1)],
       'texts':[('r1-t1',0.2,3.0),('r1-t2',3.2,6.6),('r1-t3',7.0,12.8)]},
 'r2':{'segs':[('v2',0.0,3.0,1),('v1',8.0,3.0,1),('v6',2.0,3.0,1),('v3',12.0,2.5,1)],
       'texts':[('r2-t1',0.2,3.0),('r2-t2',3.1,6.0),('r2-t3',6.1,9.0),('r2-t4',9.1,11.5)]},
 'r3':{'segs':[('v4',0.0,30.0,2.5)],
       'texts':[('r3-t1',0.3,12.0)]},
 'r4':{'segs':[('v5',1.2,3.8,1),('v3',4.0,4.0,1),('v5',12.0,3.0,1)],
       'texts':[('r4-t1',0.3,5.5),('r4-t2',6.0,11.0)]},
}
def run(cmd):
    r=subprocess.run(cmd,capture_output=True,text=True)
    if r.returncode: print(r.stderr[-1500:]); sys.exit(1)
VF="scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p"
for name,cfg in reels.items():
    parts=[]
    for i,(v,s,d,sp) in enumerate(cfg['segs']):
        out=f'{O}/{name}_s{i}.mp4'
        vf=VF+(f",setpts=PTS/{sp}" if sp!=1 else "")
        run(['ffmpeg','-v','error','-y','-ss',str(s),'-t',str(d),'-i',f'{V}/{vid[v]}','-vf',vf,'-an','-c:v','libx264','-preset','veryfast','-crf','16','-r','30',out])
        parts.append(out)
    endv=f'{O}/{name}_end.mp4'
    run(['ffmpeg','-v','error','-y','-loop','1','-t',str(END),'-i',f'{O}/{name}-end.png','-vf','scale=1080:1920,fps=30,format=yuv420p,fade=t=in:st=0:d=0.3','-c:v','libx264','-preset','veryfast','-crf','16','-r','30',endv])
    parts.append(endv)
    lst=f'{O}/{name}_list.txt'; open(lst,'w').write(''.join(f"file '{p}'\n" for p in parts))
    base=f'{O}/{name}_base.mp4'
    run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',lst,'-c','copy',base])
    dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',base],capture_output=True,text=True).stdout)
    cmd=['ffmpeg','-v','error','-y','-i',base]
    for t,a,b in cfg['texts']: cmd+=['-loop','1','-t',str(dur),'-i',f'{O}/{t}.png']
    fc=[]; last='[0:v]'
    for k,(t,a,b) in enumerate(cfg['texts'],1):
        fc.append(f"[{k}:v]format=rgba,fade=t=in:st={a}:d=0.25:alpha=1,fade=t=out:st={b-0.25}:d=0.25:alpha=1[o{k}]")
        fc.append(f"{last}[o{k}]overlay=0:0:enable='between(t,{a},{b})'[x{k}]"); last=f'[x{k}]'
    final=f'{O}/fonske-reel-{name}.mp4'
    cmd+=['-filter_complex',';'.join(fc),'-map',last,'-an','-c:v','libx264','-preset','veryfast','-crf','24','-maxrate','5M','-bufsize','10M','-pix_fmt','yuv420p','-movflags','+faststart','-t',str(dur),final]
    run(cmd)
    run(['ffmpeg','-v','error','-y','-ss','1.6','-i',final,'-frames:v','1','-q:v','3',f'{O}/fonske-reel-{name}-cover.jpg'])
    sz=os.path.getsize(final)/1e6
    print(name, f'{dur:.1f}s', f'{sz:.2f}MB')
