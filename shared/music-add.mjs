// Voegt een nummer toe aan de muziekbibliotheek van een merk (MUZIEK.md).
//
// Gebruik:
//   node shared/music-add.mjs <music-map> <bestand> --title "<titel>" --mood warm,akoestisch --bpm 96 [--prompt "<prompt>"] [--date JJJJ-MM-DD]
//
// Doet: luidheid gelijk trekken (-14 LUFS, piek -1,5 dB), omzetten naar mp3 192 kbps,
// duur en best_start (einde van de stilte vooraan) meten, en een regel in tracks.json zetten.
// Weigert bestanden boven 5 MB en dubbele namen.

import fs from "node:fs";
import path from "node:path";
import { execFileSync, spawnSync } from "node:child_process";

const args = process.argv.slice(2);
const flag = (name) => {
  const i = args.indexOf(name);
  return i >= 0 ? args[i + 1] : undefined;
};
const [dir, input] = args;
const title = flag("--title");
const mood = (flag("--mood") ?? "").split(",").map((s) => s.trim()).filter(Boolean);
const bpm = Number(flag("--bpm"));
if (!dir || !input || !title || mood.length === 0 || !bpm) {
  console.error('Gebruik: node shared/music-add.mjs <music-map> <bestand> --title "<titel>" --mood a,b --bpm <n> [--prompt "<tekst>"] [--date JJJJ-MM-DD]');
  process.exit(1);
}
if (!fs.existsSync(input)) {
  console.error(`Niet gevonden: ${input}`);
  process.exit(1);
}

const slug = (s) => s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
const file = `${slug(mood[0])}-${slug(title)}.mp3`;
const out = path.join(dir, file);
const listPath = path.join(dir, "tracks.json");
const list = fs.existsSync(listPath) ? JSON.parse(fs.readFileSync(listPath, "utf8")) : [];
if (list.some((t) => t.file === file) || fs.existsSync(out)) {
  console.error(`Bestaat al: ${file}`);
  process.exit(1);
}

fs.mkdirSync(dir, { recursive: true });
execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-i", input, "-vn",
  "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "44100", "-b:a", "192k", out]);

const size = fs.statSync(out).size;
if (size > 5 * 1024 * 1024) {
  fs.unlinkSync(out);
  console.error(`Te groot na omzetten (${(size / 1048576).toFixed(1)} MB > 5 MB): maak het nummer korter.`);
  process.exit(1);
}

const duration = Number(execFileSync("ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out]).toString().trim());
let bestStart = 0;
try {
  const log = spawnSync("ffmpeg", ["-hide_banner", "-i", out, "-af", "silencedetect=n=-45dB:d=0.2", "-f", "null", "-"]).stderr.toString();
  const m = log.match(/silence_start: (-?[\d.]+)[\s\S]*?silence_end: ([\d.]+)/);
  if (m && Number(m[1]) <= 0.05) bestStart = Math.round(Number(m[2]) * 10) / 10;
} catch {
  // geen meting: start vooraan
}

const entry = {
  file,
  title,
  artist: "ElevenLabs Music (gegenereerd voor Nomadix BV)",
  source_url: "https://elevenlabs.io/music",
  license: "ElevenLabs Music, betaald plan: commercieel gebruik incl. social media",
  attribution_required: false,
  generated_on: flag("--date") ?? new Date().toISOString().slice(0, 10),
  prompt: flag("--prompt") ?? null,
  mood,
  bpm,
  duration: Math.round(duration * 10) / 10,
  best_start: bestStart,
  used: [],
};
list.push(entry);
fs.writeFileSync(listPath, JSON.stringify(list, null, 2) + "\n");
console.log(JSON.stringify(entry, null, 2));
