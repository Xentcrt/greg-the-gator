# Greg the Gator — automated TikTok episodes

Greg is a small 3D crocodile figurine in glasses and a crown who teaches a classroom of "useless facts", swearing constantly. Each episode is a ~35–50 s vertical (1080×1920, 30 fps) video: Greg stands by a whiteboard, each fact's doodle draws itself, two lines of board text pop in on key words, Greg taps them with his pointer, and an eraser wipes the board between facts. Yellow one-word captions run at the top.

TikTok account: **@greg.the.gator3**, posted through the **Metricool** connector (brand blogId `8073640`, timezone America/New_York).

## Repo layout
- `assets/` — Greg's rig layers (body, arm, jaw PNGs), fonts, GSAP. Don't change these.
- `engine/make_episode.sh episodes/epNN` — whole pipeline: voice (Kokoro `am_adam` via `hyperframes tts`) → timing/mouth (`voice.py`) → composition + audio mix (`build.py`) → render. Writes `episodes/epNN/greg-epNN.mp4`. Takes ~5 min.
- `episodes/epNN/script.json` — the lines Greg says, grouped into sections.
- `episodes/epNN/board.py` — what's drawn on the whiteboard for each section. Copy `episodes/ep02/board.py` as the model.
- `EPISODES.md` — log of every episode and every fact used. Never reuse a fact.

## Making a new episode (what a scheduled run does)
1. Read `EPISODES.md`. Pick the next number NN.
2. Pick **6 new, true, absurd facts** not in the log. Mix animals, history, science, food, geography, the human body. Verify each with a web search before using it; skip anything that turns out to be a myth. If a fact is a joke or exaggeration in Greg's line, make sure the board text itself stays true.
3. Write `episodes/epNN/script.json` in the same shape as ep02: sections `intro`, six fact sections, `outro`; two short lines each. Greg's voice: rude, deadpan teacher, **lots of swearing** (fuck, shit, ass, goddamn, bitch, bastard…), short punchy sentences. Never slurs, never jokes about real private people, nothing sexual. Total ≈ 40–50 s of speech.
4. Write `episodes/epNN/board.py` modelled on ep02:
   - `fact_page(idx, sec_id, 'FACT #n', line1, line2, cue1, cue2)` for each fact, then `pg.draw(G([...]), start, seconds)` doodles.
   - Doodle style: whiteboard-marker cartoons with ink outlines and flat colour fills (`(path, stroke, width, fill, weight)`), with a small visual joke in each. Keep drawings in the page area x 20–920, y 80–400 (text sits at y 488 and 592). No brand logos or trademarked mascots.
   - Every `cue(sec, sentence_index, 'prefix')` must match a word that is actually in that sentence of script.json (first word starting with that prefix).
   - Keep page 0 (intro) and the last page (outro) like ep02, updating the text to fit.
5. Run `engine/make_episode.sh episodes/epNN`. Then check it: grab frames at 4–6 moments with ffmpeg and look at them (text not overflowing the board, drawings not overlapping text, Greg's pointer on the red line). Fix and re-render if needed.
6. `git add` the episode folder (including the mp4) and `EPISODES.md`, commit, push to `main`.
7. Post with Metricool `createScheduledPost`:
   - blogId `8073640`; date: ~10 minutes from now (or the next good slot from `getBestTimeToPostByNetwork` for tiktok, within the next 6 hours)
   - media: `https://raw.githubusercontent.com/Xentcrt/greg-the-gator/main/episodes/epNN/greg-epNN.mp4` (wait until the push is done; check the URL returns 200 with curl first)
   - providers `[{"network":"tiktok"}]`, `tiktokData`: `{"privacyOption":"PUBLIC_TO_EVERYONE","isAigc":true,"title":"<short title, required>","disableComment":false,"disableDuet":false,"disableStitch":false,"commercialContentThirdParty":false,"commercialContentOwnBrand":false,"autoAddMusic":false}`
   - text: one short funny caption + `#uselessfacts #funfacts #didyouknow #greg #comedy` and 1–2 topic hashtags. Keep swear words in the caption censored (f*ck) to avoid TikTok suppression.
   - Metricool copies the video to its own storage when the post is created, so the GitHub link only has to work at that moment.
8. Add the episode to `EPISODES.md` (date, facts, caption, Metricool planner URL), commit and push.
9. Report back with the video file and a one-line summary of the facts.

If any step fails (TTS, render, push, Metricool), stop before posting and report what failed. Never post a video you haven't looked at.
