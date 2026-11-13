#!/usr/bin/env bash
# Makes one Greg episode end to end.
# usage: engine/make_episode.sh episodes/epNN
# Needs: python3 (numpy, soundfile, pillow, opencv not needed), node/npx, ffmpeg, Chrome.
# Output: episodes/epNN/greg-epNN.mp4
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
EP="$(cd "$1" && pwd)"
NAME="$(basename "$EP")"
WORK="${WORK_DIR:-/tmp/greg-work/$NAME}"
rm -rf "$WORK"; mkdir -p "$WORK/voice" "$WORK/assets"

pip install --break-system-packages -q kokoro-onnx soundfile numpy pillow fonttools >/dev/null 2>&1 || true
cp "$ROOT"/assets/* "$WORK/assets/"

# 1. voice: one file per sentence
python3 - "$EP" "$WORK" <<'PY'
import json, subprocess, sys
ep, work = sys.argv[1], sys.argv[2]
for sec in json.load(open(ep + '/script.json')):
    for i, line in enumerate(sec['lines']):
        subprocess.run(['npx', '--yes', 'hyperframes@0.9.40', 'tts', line, '--voice', 'am_adam',
                        '-o', f"{work}/voice/{sec['id']}_{i}.wav"], check=True, capture_output=True)
print('voice ok')
PY

# 2. timing + mouth, 3. composition + audio mix
python3 "$ROOT/engine/voice.py" "$EP" "$WORK"
python3 "$ROOT/engine/build.py" "$EP" "$WORK"

# 4. HyperFrames project files
cat > "$WORK/hyperframes.json" <<'J'
{ "$schema": "https://hyperframes.heygen.com/schema/hyperframes.json",
  "paths": { "blocks": "compositions", "components": "compositions/components", "assets": "assets" },
  "media": { "autoProxy": true } }
J
echo "{\"id\":\"greg-$NAME\",\"name\":\"greg-$NAME\"}" > "$WORK/meta.json"

# 5. render (writes to a temp name, renamed only on success)
if [ -z "${HYPERFRAMES_BROWSER_PATH:-}" ] && [ -x /usr/bin/google-chrome ]; then export HYPERFRAMES_BROWSER_PATH=/usr/bin/google-chrome; fi
( cd "$WORK" && npx --yes hyperframes@0.9.40 render -o "$WORK/tmp_render.mp4" --quiet )
mv "$WORK/tmp_render.mp4" "$EP/greg-$NAME.mp4"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$EP/greg-$NAME.mp4"
echo "done: $EP/greg-$NAME.mp4"
