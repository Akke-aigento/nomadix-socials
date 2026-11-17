#!/bin/bash
# Gebruik:  shared/remotion/render.sh reel  <props.json> <uit.mp4>
#           shared/remotion/render.sh slide <props.json> <uit.jpg>   (1080x1350)
#           shared/remotion/render.sh story <props.json> <uit.jpg>   (1080x1920)
# Paden in props zijn relatief aan de public-map: brands/... (nomadix-socials/brands) en loveke/... (loveke/marketing, als LOVEKE_DIR gezet is).
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"; ROOT="$(cd "$HERE/../.." && pwd)"
KIND=$1; PROPS=$(realpath "$2"); OUT=$(realpath -m "$3")
[ -d "$HERE/node_modules" ] || (cd "$HERE" && npm ci --silent)
PUB=$(mktemp -d); ln -s "$ROOT/brands" "$PUB/brands"
[ -n "$LOVEKE_DIR" ] && ln -s "$LOVEKE_DIR/marketing" "$PUB/loveke"
BROWSER=${REMOTION_BROWSER:-$(find /opt/pw-browsers -type f -name chrome-headless-shell -path "*headless_shell*" 2>/dev/null | head -1)}
BARG=""; [ -n "$BROWSER" ] && BARG="--browser-executable=$BROWSER"
cd "$HERE"
case $KIND in
  reel)  npx remotion render src/index.ts Reel "$OUT" --props="$PROPS" --public-dir="$PUB" $BARG --codec=h264 --crf=20 --log=error ;;
  slide) npx remotion still src/index.ts Slide "$OUT" --props="$PROPS" --public-dir="$PUB" $BARG --image-format=jpeg --jpeg-quality=90 --log=error ;;
  story) npx remotion still src/index.ts Story "$OUT" --props="$PROPS" --public-dir="$PUB" $BARG --image-format=jpeg --jpeg-quality=90 --log=error ;;
  *) echo "onbekend: $KIND"; exit 1 ;;
esac
rm -rf "$PUB"; echo "✓ $OUT"
