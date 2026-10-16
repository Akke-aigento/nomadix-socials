// Rendert elke .html in een map naar een JPG op het formaat uit <meta name="nx-size" content="BxH">.
// Gebruik: node shared/render.mjs brands/<slug>/weeks/<maandag> [uitvoermap]
// Werkt voor alle merken; de huisstijl komt uit brands/<slug>/brand.css (relatief gelinkt in de HTML).
// Oude Loveke-templates met <meta name="loveke-size"> werken ook.
import fs from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";

const pwPath = process.env.PLAYWRIGHT_MODULE ?? "playwright";
const { chromium } = await import(pwPath);

const [srcDir, outDirArg] = process.argv.slice(2).filter((a) => !a.startsWith("--"));
if (!srcDir) {
  console.error("Gebruik: node shared/render.mjs <map-met-html> [uitvoermap]");
  process.exit(1);
}
const outDir = path.resolve(outDirArg ?? path.join(srcDir, "..", "..", "out", path.basename(srcDir)));
fs.mkdirSync(outDir, { recursive: true });

const browser = await chromium.launch();
const files = fs.readdirSync(srcDir).filter((f) => f.endsWith(".html")).sort();
let n = 0;
for (const f of files) {
  const file = path.resolve(srcDir, f);
  const html = fs.readFileSync(file, "utf8");
  const m = html.match(/name="(?:nx|loveke)-size" content="(\d+)x(\d+)"/);
  if (!m) { console.warn(`overgeslagen (geen nx-size): ${f}`); continue; }
  const [w, h] = [Number(m[1]), Number(m[2])];
  const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
  await page.goto(pathToFileURL(file).href, { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);
  // Beelden die niet laden zijn een fout, geen leeg vak.
  const broken = await page.evaluate(() => [...document.images].filter((i) => !i.complete || !i.naturalWidth).map((i) => i.src));
  if (broken.length) { console.error(`✗ ${f}: beeld niet geladen: ${broken.join(", ")}`); process.exitCode = 1; await page.close(); continue; }
  const out = path.join(outDir, f.replace(/\.html$/, ".jpg"));
  await page.screenshot({ path: out, type: "jpeg", quality: 92, clip: { x: 0, y: 0, width: w, height: h } });
  await page.close();
  n++;
  console.log(`✓ ${path.relative(process.cwd(), out)} (${w}x${h})`);
}
await browser.close();
console.log(`${n} beeld(en) gerenderd naar ${path.relative(process.cwd(), outDir)}`);
