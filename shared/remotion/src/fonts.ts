import {useState} from 'react';
import {continueRender, delayRender, staticFile} from 'remotion';
import {loadFont} from '@remotion/fonts';
import {THEMES} from './themes';
const loaded: Record<string, Promise<unknown>> = {};
export const useBrandFonts = (brand: string) => {
  const [h] = useState(() => {
    const id = delayRender('fonts ' + brand);
    loaded[brand] ??= Promise.all(THEMES[brand].fonts.map((f) => loadFont({family: f.family, url: staticFile(f.url), weight: f.weight})));
    loaded[brand].then(() => continueRender(id)).catch((e) => { console.error(e); continueRender(id); });
    return id;
  });
  return h;
};
