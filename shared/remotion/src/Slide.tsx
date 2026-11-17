import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {THEMES, Theme} from './themes';
import {useBrandFonts} from './fonts';

// Carrouselslide (1080x1350) of losse post. Eén idee per slide, tekst groot genoeg voor een gsm (min. 34 px).
export type SlideProps = {
  brand: string;
  layout: 'photo' | 'split' | 'statement' | 'list' | 'cta';
  photo?: string; photoPos?: string;       // pad in public-map, object-position
  kicker?: string; title: string; body?: string; items?: string[];
  tone?: 'dark' | 'accent' | 'light';
  page?: string;                           // bv. "2/6"
  swipe?: boolean;                         // "swipe →" op de eerste slide
};

const Title: React.FC<{t: Theme; text: string; size?: number; color: string; hi: string}> = ({t, text, size, color, hi}) => {
  // *woord* = accentkleur
  const parts = text.split(/(\*[^*]+\*)/g);
  return <div style={{fontFamily: t.title, fontWeight: t.titleWeight, textTransform: t.titleUpper ? 'uppercase' : 'none', fontSize: size ?? (t.titleUpper ? 150 : 104), lineHeight: t.titleUpper ? 0.9 : 1.02, letterSpacing: t.titleUpper ? 0 : '-.025em', color, whiteSpace: 'pre-line'}}>
    {parts.map((p, i) => p.startsWith('*') ? <span key={i} style={{color: hi}}>{p.slice(1, -1)}</span> : <span key={i}>{p}</span>)}
  </div>;
};

export const Slide: React.FC<SlideProps> = (p) => {
  const t = THEMES[p.brand]; useBrandFonts(p.brand);
  const tone = p.tone ?? 'dark';
  const bg = tone === 'accent' ? t.accent : tone === 'light' ? (p.brand === 'loveke' ? t.bg : '#F4F1EC') : t.bg;
  const fg = tone === 'light' ? (p.brand === 'loveke' ? t.fg : '#111') : '#fff';
  const hi = tone === 'accent' ? (p.brand === 'loveke' ? t.fg : '#111') : t.accent2 === '#FFF7F2' ? t.accent : (tone === 'light' ? t.accent : t.accent2);
  const K = p.kicker ? <div style={{fontFamily: t.text, fontWeight: 700, fontSize: 28, letterSpacing: '.16em', textTransform: 'uppercase', color: hi, marginBottom: 20}}>{p.kicker}</div> : null;
  const B = p.body ? <div style={{fontFamily: t.text, fontWeight: 500, fontSize: 38, lineHeight: 1.38, color: fg, opacity: 0.9, marginTop: 28, whiteSpace: 'pre-line'}}>{p.body}</div> : null;
  const foot = <div style={{position: 'absolute', left: 72, right: 72, bottom: 54, display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontFamily: t.text, fontWeight: 700, fontSize: 26, color: fg, opacity: 0.75}}>
    <span>{p.page ?? ''}</span>{p.swipe ? <span>swipe →</span> : (tone !== 'light' && t.logo ? <Img src={staticFile(t.logo)} style={{height: 40}} /> : (t.logoDark ? <Img src={staticFile(t.logoDark)} style={{height: 40}} /> : <span />))}</div>;

  if (p.layout === 'photo') return <AbsoluteFill style={{background: '#000'}}>
    {p.photo ? <Img src={staticFile(p.photo)} style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: p.photoPos ?? 'center'}} /> : null}
    <AbsoluteFill style={{background: 'linear-gradient(180deg,rgba(0,0,0,.15) 0%,transparent 35%,rgba(0,0,0,.82) 100%)'}} />
    <div style={{position: 'absolute', left: 72, right: 72, bottom: 130}}>{K}<Title t={t} text={p.title} color="#fff" hi={t.accent2 === '#FFF7F2' ? t.accent : t.accent2} />{p.body ? <div style={{fontFamily: t.text, fontWeight: 500, fontSize: 36, lineHeight: 1.38, color: '#fff', marginTop: 24, whiteSpace: 'pre-line'}}>{p.body}</div> : null}</div>
    <div style={{position: 'absolute', left: 72, right: 72, bottom: 54, display: 'flex', justifyContent: 'space-between', fontFamily: t.text, fontWeight: 700, fontSize: 26, color: '#fff', opacity: 0.8}}><span>{p.page ?? ''}</span><span>{p.swipe ? 'swipe →' : ''}</span></div>
  </AbsoluteFill>;
  if (p.layout === 'split') return <AbsoluteFill style={{background: bg}}>
    {p.photo ? <div style={{position: 'absolute', left: 0, right: 0, top: 0, height: 760, overflow: 'hidden'}}><Img src={staticFile(p.photo)} style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: p.photoPos ?? 'center'}} /></div> : null}
    <div style={{position: 'absolute', left: 72, right: 72, top: 820}}>{K}<Title t={t} text={p.title} size={t.titleUpper ? 110 : 76} color={fg} hi={hi} />{B}</div>{foot}
  </AbsoluteFill>;
  if (p.layout === 'list') return <AbsoluteFill style={{background: bg, padding: '120px 72px'}}>
    {K}<Title t={t} text={p.title} size={t.titleUpper ? 120 : 84} color={fg} hi={hi} />
    <div style={{marginTop: 50, display: 'flex', flexDirection: 'column', gap: 30}}>{(p.items ?? []).map((it, i) => <div key={i} style={{display: 'flex', gap: 26, alignItems: 'baseline'}}>
      <span style={{fontFamily: t.title, fontWeight: t.titleWeight, fontSize: 70, color: hi, minWidth: 70}}>{i + 1}</span>
      <span style={{fontFamily: t.text, fontWeight: 600, fontSize: 40, lineHeight: 1.3, color: fg}}>{it}</span></div>)}</div>{foot}
  </AbsoluteFill>;
  return <AbsoluteFill style={{background: bg, justifyContent: 'center', padding: '0 72px'}}>
    {K}<Title t={t} text={p.title} size={p.layout === 'cta' ? undefined : (t.titleUpper ? 170 : 116)} color={fg} hi={hi} />{B}{foot}
  </AbsoluteFill>;
};
