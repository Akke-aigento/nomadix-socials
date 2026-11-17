import React from 'react';
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig, Easing} from 'remotion';
import {TransitionSeries, linearTiming, springTiming} from '@remotion/transitions';
import {slide} from '@remotion/transitions/slide';
import {fade} from '@remotion/transitions/fade';
import {wipe} from '@remotion/transitions/wipe';
import {THEMES, Theme} from './themes';
import {useBrandFonts} from './fonts';

// Eén scène = één beeld of clip met (optioneel) ondertitel. Alles in seconden.
export type Scene =
  | {type: 'clip'; src: string; dur: number; from?: number; caption?: string; zoom?: boolean; muted?: boolean}
  | {type: 'image'; src: string; dur: number; caption?: string; move?: 'in' | 'out' | 'left' | 'right' | 'up'; fit?: 'cover' | 'contain'; bg?: string}
  | {type: 'title'; dur: number; kicker?: string; title: string; sub?: string; bg?: 'brand' | 'accent' | 'light'}
  | {type: 'end'; dur: number; title: string; sub?: string; cta?: string};
export type ReelProps = {
  brand: string;
  hook?: string;              // tekst die in de eerste 1,5 s groot in beeld staat (verplicht volgens POSTS-2)
  scenes: Scene[];
  transition?: 'cut' | 'slide' | 'fade' | 'wipe';
  music?: string;             // pad in public-map
  musicVolume?: number;
  sting?: string;             // merksting, speelt op het einde
  captionStyle?: 'pop' | 'bar';
};

const sec = (s: number, fps: number) => Math.max(1, Math.round(s * fps));
export const TRANS = 10; // frames per overgang

export const reelDuration = (p: ReelProps, fps: number) => {
  const total = p.scenes.reduce((a, s) => a + sec(s.dur, fps), 0);
  const n = (p.transition ?? 'slide') === 'cut' ? 0 : Math.max(0, p.scenes.length - 1) * TRANS;
  return total - n;
};

// Ondertitels: woord per woord, groot, in de veilige zone (niet boven 250 px, niet onder 340 px).
const Caption: React.FC<{text: string; t: Theme; style: 'pop' | 'bar'}> = ({text, t, style}) => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const words = text.split(' ');
  const per = Math.max(3, Math.round(fps * 0.16));
  return (
    <AbsoluteFill style={{justifyContent: 'flex-end', alignItems: 'center', paddingBottom: 420, paddingLeft: 70, paddingRight: 70}}>
      <div style={{display: 'flex', flexWrap: 'wrap', justifyContent: 'center', gap: '6px 18px', maxWidth: 940,
        ...(style === 'bar' ? {background: 'rgba(0,0,0,.55)', padding: '20px 30px', borderRadius: t.radius} : {})}}>
        {words.map((w, i) => {
          const s = spring({frame: f - i * per, fps, config: {damping: 14, mass: 0.6}});
          const on = f >= i * per;
          return <span key={i} style={{fontFamily: t.title, fontWeight: t.titleWeight, textTransform: t.titleUpper ? 'uppercase' : 'none',
            fontSize: t.titleUpper ? 92 : 70, lineHeight: 1.05, color: i === words.length - 1 && words.length > 2 ? t.accent2 : '#fff',
            opacity: on ? 1 : 0, transform: `scale(${0.6 + 0.4 * s}) translateY(${(1 - s) * 30}px)`,
            textShadow: style === 'pop' ? '0 4px 0 rgba(0,0,0,.55), 0 0 30px rgba(0,0,0,.5)' : 'none'}}>{w}</span>;
        })}
      </div>
    </AbsoluteFill>
  );
};

const Move: React.FC<{children: React.ReactNode; move?: string; dur: number}> = ({children, move, dur}) => {
  const f = useCurrentFrame();
  const p = interpolate(f, [0, dur], [0, 1], {extrapolateRight: 'clamp', easing: Easing.inOut(Easing.quad)});
  const tr = move === 'out' ? `scale(${1.18 - 0.18 * p})` : move === 'left' ? `scale(1.15) translateX(${40 - 80 * p}px)` : move === 'right' ? `scale(1.15) translateX(${-40 + 80 * p}px)` : move === 'up' ? `scale(1.15) translateY(${50 - 100 * p}px)` : `scale(${1 + 0.15 * p})`;
  return <AbsoluteFill style={{transform: tr}}>{children}</AbsoluteFill>;
};

const SceneView: React.FC<{s: Scene; t: Theme; fps: number; cs: 'pop' | 'bar'}> = ({s, t, fps, cs}) => {
  const d = sec(s.dur, fps);
  if (s.type === 'clip') return (
    <AbsoluteFill style={{background: '#000'}}>
      <Move move={s.zoom ? 'in' : 'none'} dur={d}><OffthreadVideo src={staticFile(s.src)} startFrom={Math.round((s.from ?? 0) * fps)} muted={s.muted ?? true} style={{width: '100%', height: '100%', objectFit: 'cover'}} /></Move>
      <AbsoluteFill style={{background: 'linear-gradient(180deg,rgba(0,0,0,.35),transparent 25%,transparent 55%,rgba(0,0,0,.6))'}} />
      {s.caption ? <Caption text={s.caption} t={t} style={cs} /> : null}
    </AbsoluteFill>);
  if (s.type === 'image') return (
    <AbsoluteFill style={{background: s.bg ?? t.bg}}>
      <Move move={s.move} dur={d}><Img src={staticFile(s.src)} style={{width: '100%', height: '100%', objectFit: s.fit ?? 'cover'}} /></Move>
      <AbsoluteFill style={{background: 'linear-gradient(180deg,rgba(0,0,0,.3),transparent 25%,transparent 55%,rgba(0,0,0,.55))'}} />
      {s.caption ? <Caption text={s.caption} t={t} style={cs} /> : null}
    </AbsoluteFill>);
  if (s.type === 'title') {
    const bg = s.bg === 'accent' ? t.accent : s.bg === 'light' ? t.accent2 : t.bg;
    const fg = s.bg === 'light' ? t.bg : '#fff';
    return <AbsoluteFill style={{background: bg, justifyContent: 'center', padding: '0 80px'}}><TitleBlock t={t} kicker={s.kicker} title={s.title} sub={s.sub} fg={fg} /></AbsoluteFill>;
  }
  return <AbsoluteFill style={{background: t.bg, justifyContent: 'center', padding: '0 80px'}}>
    <TitleBlock t={t} title={s.title} sub={s.sub} fg={t.fg} />
    {s.cta ? <div style={{marginTop: 50, alignSelf: 'flex-start', background: t.accent, color: '#fff', fontFamily: t.text, fontWeight: 700, fontSize: 40, padding: '18px 34px', borderRadius: 99}}>{s.cta}</div> : null}
    {t.logo ? <Img src={staticFile(t.logo)} style={{position: 'absolute', left: 80, bottom: 380, width: 320, height: 90, objectFit: 'contain', objectPosition: 'left center'}} /> : null}
  </AbsoluteFill>;
};

const TitleBlock: React.FC<{t: Theme; kicker?: string; title: string; sub?: string; fg: string}> = ({t, kicker, title, sub, fg}) => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const lines = title.split('\n');
  return <div style={{display: 'flex', flexDirection: 'column'}}>
    {kicker ? <div style={{fontFamily: t.text, fontWeight: 700, fontSize: 30, letterSpacing: '.18em', textTransform: 'uppercase', color: t.accent2, marginBottom: 18, opacity: spring({frame: f, fps})}}>{kicker}</div> : null}
    {lines.map((l, i) => { const s = spring({frame: f - 4 - i * 5, fps, config: {damping: 13}}); return (
      <div key={i} style={{overflow: 'hidden'}}><div style={{fontFamily: t.title, fontWeight: t.titleWeight, textTransform: t.titleUpper ? 'uppercase' : 'none', fontSize: t.titleUpper ? 170 : 118, lineHeight: t.titleUpper ? 0.88 : 1, letterSpacing: t.titleUpper ? 0 : '-.03em', color: i === lines.length - 1 && lines.length > 1 ? t.accent2 === '#FFF7F2' ? t.accent : t.accent2 : fg, transform: `translateY(${(1 - s) * 110}%)`}}>{l}</div></div>); })}
    {sub ? <div style={{fontFamily: t.text, fontWeight: 500, fontSize: 40, lineHeight: 1.35, color: fg, opacity: 0.85 * spring({frame: f - 14, fps}), marginTop: 30, maxWidth: 900}}>{sub}</div> : null}
  </div>;
};

const Hook: React.FC<{text: string; t: Theme}> = ({text, t}) => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const s = spring({frame: f, fps, config: {damping: 11}});
  const out = interpolate(f, [fps * 1.6, fps * 1.9], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return <AbsoluteFill style={{justifyContent: 'flex-start', paddingTop: 280, paddingLeft: 70, paddingRight: 70, opacity: out}}>
    <div style={{alignSelf: 'flex-start', background: t.accent, color: '#fff', fontFamily: t.title, fontWeight: t.titleWeight, textTransform: t.titleUpper ? 'uppercase' : 'none', fontSize: t.titleUpper ? 110 : 80, lineHeight: 1, padding: '18px 30px 14px', borderRadius: t.radius / 2, transform: `rotate(-2deg) scale(${0.7 + 0.3 * s})`, boxShadow: '0 12px 0 rgba(0,0,0,.35)'}}>{text}</div>
  </AbsoluteFill>;
};

export const Reel: React.FC<ReelProps> = (p) => {
  const {fps, durationInFrames} = useVideoConfig();
  const t = THEMES[p.brand]; useBrandFonts(p.brand);
  const tr = p.transition ?? 'slide';
  const pres = tr === 'fade' ? fade() : tr === 'wipe' ? wipe({direction: 'from-left'}) : slide({direction: 'from-right'});
  return <AbsoluteFill style={{background: t.bg}}>
    {tr === 'cut' ? (() => { let at = 0; return p.scenes.map((s, i) => { const d = sec(s.dur, fps); const el = <Sequence key={i} from={at} durationInFrames={d}><SceneView s={s} t={t} fps={fps} cs={p.captionStyle ?? 'pop'} /></Sequence>; at += d; return el; }); })()
      : <TransitionSeries>{p.scenes.flatMap((s, i) => {
        const el = [<TransitionSeries.Sequence key={'s' + i} durationInFrames={sec(s.dur, fps)}><SceneView s={s} t={t} fps={fps} cs={p.captionStyle ?? 'pop'} /></TransitionSeries.Sequence>];
        if (i < p.scenes.length - 1) el.push(<TransitionSeries.Transition key={'t' + i} presentation={pres as any} timing={springTiming({config: {damping: 200}, durationInFrames: TRANS})} />);
        return el; })}</TransitionSeries>}
    {p.hook ? <Sequence from={0} durationInFrames={Math.round(fps * 2)}><Hook text={p.hook} t={t} /></Sequence> : null}
    {p.music ? <Audio src={staticFile(p.music)} volume={(f) => (p.musicVolume ?? 0.9) * interpolate(f, [0, 8, durationInFrames - fps * 1.2, durationInFrames], [0, 1, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})} /> : null}
    {p.sting ? <Sequence from={Math.max(0, durationInFrames - Math.round(fps * 2.4))}><Audio src={staticFile(p.sting)} volume={0.9} /></Sequence> : null}
  </AbsoluteFill>;
};
