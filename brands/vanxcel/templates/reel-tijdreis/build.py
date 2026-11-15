"""Vult FRAMES in index.html met N gelijkmatig over de reis verspreide foto's uit media.json.
Gebruik: python3 build.py [N=56] [--seed S] → schrijft build.html naast index.html (render die met shared/reel.mjs).
Wissel --seed elke keer dat je het format opnieuw gebruikt, zodat het nooit dezelfde reeks foto's is."""
import json, random, sys, pathlib

here = pathlib.Path(__file__).parent
args = [a for a in sys.argv[1:] if not a.startswith("--")]
n = int(args[0]) if args else 56
seed = int(sys.argv[sys.argv.index("--seed") + 1]) if "--seed" in sys.argv else 1
media = json.loads((here / "../../media.json").read_text())["items"]
# Niet gebruiken (14 nov 2026): fles alcohol prominent in beeld, botst met de selectieregel in brand-vanxcel §8.
EXCLUDE = {"vx-2022-06-13-kazakhstan-0762"}
photos = sorted([m for m in media if m.get("kind") == "photo" and m.get("country") and m["id"] not in EXCLUDE
                 and not {"alcohol", "exclude"} & set(m.get("tags", []))], key=lambda m: (m["date"], m["id"]))
rnd = random.Random(seed)
picked = []
for k in range(n):
    lo, hi = len(photos) * k // n, max(len(photos) * (k + 1) // n, len(photos) * k // n + 1)
    picked.append(rnd.choice(photos[lo:hi]))
frames = [{"file": p["file"], "day": p["day"], "country": p["country"], "place": p.get("place", "")} for p in picked]
html = (here / "index.html").read_text().replace("/*FRAMES*/[]", json.dumps(frames))
(here / "build.html").write_text(html)
print(f"{len(frames)} foto's, dag {frames[0]['day']} tot {frames[-1]['day']} → build.html")
