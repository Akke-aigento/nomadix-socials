import React from 'react';
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig, Easing} from 'remotion';
import {THEMES, Theme} from './themes';
import {useBrandFonts} from './fonts';

// FILM-1 (22-11): echte korte films i.p.v. slideshows. Zie shared/FILM.md.
// Shots zijn bewegende video (AI-geanimeerd of echt gefilmd) met hun eigen geluid (sfeer, dialoog).
// Daaronder: optionele voice-over met tijd per woord (ondertitels lopen exact mee) en muziek die wegduikt onder stem.

export type Shot = {
  src: string;              // mp4 (of jpg/png voor een still met lichte beweging)
  dur: number;              // seconden in de film
  from?: number;            // starttijd in de bron
  speed?: number;
  volume?: number;          // eigen geluid van de shot (0 = stil), standaard 1
  fadeIn?: number;          // crossfade vanaf de vorige shot, seconden (0 = harde knip)
  fit?: 'cover' | 'contain';
  focus?: string;           // object-position, bv. '50% 30%'
};
export type Word = {text: string; start: number; end: number};
export type Line = {text: string; start: number; end: number; who?: string; kind?: 'sub' | 'msg'; side?: 'in' | 'out'}; // ondertitel, of gsm-bericht (kind 'msg': ballon, in = ontvangen links, out = verstuurd rechts)
export type FilmProps = {
  brand: string;
  shots: Shot[];
  voice?: {src: string; words: Word[]; at?: number; volume?: number}; // words = alignment-JSON van media-compose
  lines?: Line[];
  music?: string;
  musicVolume?: number;     // standaard 0.55
  duck?: number;            // muziekvolume terwijl iemand spreekt (fractie van musicVolume), standaard 0.3
  hook?: {text: string; dur?: number};      // grote tekst bovenaan in de eerste seconden
  end?: {title: string; sub?: string; dur: number; logo?: boolean};
  grade?: 'none' | 'warm' | 'film';
};

const fr = (s: number, fps: number) => Math.round(s * fps);
export const filmDuration = (p: FilmProps, fps: number) =>
  fr(p.shots.reduce((a, s) => a + s.dur - (s.fadeIn ?? 0), 0) + (p.end?.dur ?? 0), fps);

// Woorden groeperen tot ondertitels van max. 4 woorden / 26 tekens, knippen bij pauzes en leestekens.
export const chunkWords = (words: Word[], at = 0): Line[] => {
  const out: Line[] = []; let cur: Word[] = [];
  const push = () => { if (cur.length) out.push({text: cur.map((w) => w.text).join(' '), start: cur[0].start + at, end: cur[cur.length - 1].end + at}); cur = []; };
  words.forEach((w, i) => {
    const prev = words[i - 1];
    if (cur.length && (prev && w.start - prev.end > 0.3 || cur.length >= 4 || (cur.map((x) => x.text).join(' ') + ' ' + w.text).length > 26)) push();
    cur.push(w);
    if (/[.!?…,:;]$/.test(w.text)) push();
  });
  push();
  // ondertitel blijft staan tot net voor de volgende (geen geflikker)
  return out.map((l, i) => ({...l, end: Math.min(out[i + 1]?.start ?? l.end + 0.6, l.end + 0.6)}));
};

const Sub: React.FC<{line: Line; t: Theme}> = ({line, t}) => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const s = spring({frame: f, fps, config: {damping: 18, mass: 0.5}});
  return <AbsoluteFill style={{justifyContent: 'flex-end', alignItems: 'center', paddingBottom: 400, paddingLeft: 80, paddingRight: 80}}>
    {line.who ? <div style={{fontFamily: t.text, fontWeight: 700, fontSize: 30, letterSpacing: '.12em', textTransform: 'uppercase', color: t.accent2, marginBottom: 10, opacity: s}}>{line.who}</div> : null}
    <div style={{fontFamily: t.title, fontWeight: t.titleWeight, textTransform: t.titleUpper ? 'uppercase' : 'none', fontSize: t.titleUpper ? 78 : 62, lineHeight: 1.1,
      color: '#fff', textAlign: 'center', maxWidth: 920, opacity: s, transform: `translateY(${(1 - s) * 16}px)`,
      textShadow: '0 3px 0 rgba(0,0,0,.6), 0 0 24px rgba(0,0,0,.65)'}}>{line.text}</div>
  </AbsoluteFill>;
};


const Msg: React.FC<{line: Line; t: Theme; row: number}> = ({line, t, row}) => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const s = spring({frame: f, fps, config: {damping: 14, mass: 0.6}});
  const out = line.side === 'out';
  return <AbsoluteFill style={{justifyContent: 'flex-start', alignItems: out ? 'flex-end' : 'flex-start', paddingTop: 300 + row * 150, paddingLeft: 90, paddingRight: 90}}>
    <div style={{maxWidth: 760, background: out ? t.accent : '#FFFFFF', color: out ? '#fff' : '#1A1A1A', fontFamily: t.text, fontWeight: 700, fontSize: 52, lineHeight: 1.2,
      padding: '26px 38px', borderRadius: 44, borderBottomRightRadius: out ? 12 : 44, borderBottomLeftRadius: out ? 44 : 12,
      boxShadow: '0 10px 30px rgba(0,0,0,.25)', transform: `scale(${0.6 + 0.4 * s}) translateY(${(1 - s) * 30}px)`, transformOrigin: out ? 'right bottom' : 'left bottom', opacity: s}}>{line.text}</div>
  </AbsoluteFill>;
};

const ShotView: React.FC<{s: Shot; fps: number; first: boolean}> = ({s, fps, first}) => {
  const f = useCurrentFrame(); const d = fr(s.dur, fps);
  const fi = fr(s.fadeIn ?? 0, fps);
  const op = first || !fi ? 1 : interpolate(f, [0, fi], [0, 1], {extrapolateRight: 'clamp'});
  const isVid = /\.(mp4|mov|webm)$/i.test(s.src);
  const style: React.CSSProperties = {width: '100%', height: '100%', objectFit: s.fit ?? 'cover', objectPosition: s.focus ?? '50% 50%'};
  if (isVid) return <AbsoluteFill style={{opacity: op, background: '#000'}}>
    <OffthreadVideo src={staticFile(s.src)} startFrom={fr(s.from ?? 0, fps)} playbackRate={s.speed ?? 1}
      volume={(x) => (s.volume ?? 1) * interpolate(x, [0, Math.max(1, fi), d - 6, d], [fi ? 0 : 1, 1, 1, 0.6], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})} style={style} />
  </AbsoluteFill>;
  const p = interpolate(f, [0, d], [0, 1], {easing: Easing.inOut(Easing.quad)});
  return <AbsoluteFill style={{opacity: op, background: '#000'}}><Img src={staticFile(s.src)} style={{...style, transform: `scale(${1.04 + 0.08 * p})`}} /></AbsoluteFill>;
};

const Hook: React.FC<{text: string; t: Theme; dur: number}> = ({text, t, dur}) => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const s = spring({frame: f, fps, config: {damping: 14}});
  const out = interpolate(f, [fr(dur, fps) - 8, fr(dur, fps)], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return <AbsoluteFill style={{justifyContent: 'flex-start', paddingTop: 290, paddingLeft: 80, paddingRight: 80, opacity: out}}>
    <div style={{fontFamily: t.title, fontWeight: t.titleWeight, textTransform: t.titleUpper ? 'uppercase' : 'none', fontSize: t.titleUpper ? 120 : 92, lineHeight: 1,
      color: '#fff', textShadow: '0 4px 0 rgba(0,0,0,.55), 0 0 40px rgba(0,0,0,.6)', transform: `translateY(${(1 - s) * 40}px)`, opacity: s, whiteSpace: 'pre-line'}}>{text}</div>
  </AbsoluteFill>;
};

const End: React.FC<{e: NonNullable<FilmProps['end']>; t: Theme}> = ({e, t}) => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const s = spring({frame: f, fps, config: {damping: 16}});
  return <AbsoluteFill style={{background: t.bg, justifyContent: 'center', alignItems: 'center', padding: '0 90px', opacity: interpolate(f, [0, 8], [0, 1], {extrapolateRight: 'clamp'})}}>
    <div style={{fontFamily: t.title, fontWeight: t.titleWeight, textTransform: t.titleUpper ? 'uppercase' : 'none', fontSize: t.titleUpper ? 130 : 100, lineHeight: 1, color: t.fg, textAlign: 'center', transform: `scale(${0.9 + 0.1 * s})`, whiteSpace: 'pre-line'}}>{e.title}</div>
    {e.sub ? <div style={{fontFamily: t.text, fontWeight: 600, fontSize: 42, color: t.accent, marginTop: 36, textAlign: 'center', opacity: spring({frame: f - 8, fps})}}>{e.sub}</div> : null}
    {e.logo !== false && t.logo ? <Img src={staticFile(t.logo)} style={{position: 'absolute', bottom: 400, width: 360, height: 100, objectFit: 'contain', opacity: spring({frame: f - 14, fps})}} /> : null}
  </AbsoluteFill>;
};

export const Film: React.FC<FilmProps> = (p) => {
  const {fps, durationInFrames} = useVideoConfig();
  const t = THEMES[p.brand]; useBrandFonts(p.brand);
  let at = 0;
  const seqs = p.shots.map((s, i) => {
    const start = at - fr(s.fadeIn ?? 0, fps) * (i ? 1 : 0);
    at = start + fr(s.dur, fps);
    return {s, start, i};
  });
  const shotsEnd = at;
  const vAt = p.voice?.at ?? 0;
  const lines = [...(p.lines ?? []), ...(p.voice ? chunkWords(p.voice.words, vAt) : [])];
  const speaking = lines.filter((l) => l.kind !== 'msg').map((l) => [fr(l.start, fps), fr(l.end, fps)] as const);
  const mv = p.musicVolume ?? 0.55; const duck = p.duck ?? 0.3;
  const musicVol = (x: number) => {
    const talk = speaking.some(([a, b]) => x >= a - 6 && x <= b + 6);
    const env = interpolate(x, [0, 10, durationInFrames - fps * 1.5, durationInFrames - 1], [0, 1, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
    return mv * env * (talk ? duck : 1);
  };
  const grade = p.grade === 'warm' ? 'saturate(1.08) sepia(.08) contrast(1.04)' : p.grade === 'film' ? 'contrast(1.06) saturate(.92)' : 'none';
  return <AbsoluteFill style={{background: '#000'}}>
    <AbsoluteFill style={{filter: grade}}>
      {seqs.map(({s, start, i}) => <Sequence key={i} from={start} durationInFrames={fr(s.dur, fps)}><ShotView s={s} fps={fps} first={i === 0} /></Sequence>)}
    </AbsoluteFill>
    <AbsoluteFill style={{background: 'linear-gradient(180deg,rgba(0,0,0,.28),transparent 22%,transparent 60%,rgba(0,0,0,.55))', pointerEvents: 'none'}} />
    {lines.map((l, i) => <Sequence key={'l' + i} from={fr(l.start, fps)} durationInFrames={Math.max(1, fr(l.end - l.start, fps))}>{l.kind === 'msg' ? <Msg line={l} t={t} row={lines.filter((x, j) => j < i && x.kind === 'msg' && x.end > l.start).length} /> : <Sub line={l} t={t} />}</Sequence>)}
    {p.hook ? <Sequence from={0} durationInFrames={fr(p.hook.dur ?? 2.2, fps)}><Hook text={p.hook.text} t={t} dur={p.hook.dur ?? 2.2} /></Sequence> : null}
    {p.end ? <Sequence from={shotsEnd} durationInFrames={fr(p.end.dur, fps)}><End e={p.end} t={t} /></Sequence> : null}
    {p.voice ? <Sequence from={fr(vAt, fps)}><Audio src={staticFile(p.voice.src)} volume={p.voice.volume ?? 1} /></Sequence> : null}
    {p.music ? <Audio src={staticFile(p.music)} volume={musicVol} /> : null}
  </AbsoluteFill>;
};
