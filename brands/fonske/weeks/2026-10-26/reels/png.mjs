import fs from "node:fs"; import path from "node:path"; import { pathToFileURL } from "node:url";
const { chromium } = await import(process.env.PLAYWRIGHT_MODULE);
const [src, out] = process.argv.slice(2);
const b = await chromium.launch(); 
for (const f of fs.readdirSync(src).filter(f=>f.endsWith('.html')).sort()) {
  const p = await b.newPage({ viewport:{width:1080,height:1920}, deviceScaleFactor:1 });
  await p.goto(pathToFileURL(path.resolve(src,f)).href, { waitUntil:'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const transparent = !f.includes('-end');
  await p.screenshot({ path: path.join(out, f.replace('.html','.png')), omitBackground: transparent });
  await p.close();
}
await b.close();
