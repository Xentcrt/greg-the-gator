# Greg the Gator — automated TikTok episodes

Greg is a small 3D crocodile figurine in glasses and a crown who teaches a classroom of "useless facts", swearing constantly. Each episode is a ~35–50 s vertical (1080×1920, 30 fps) video: Greg stands by a whiteboard, each fact's doodle draws itself, two lines of board text pop in on key words, Greg taps them with his pointer, and an eraser wipes the board between facts. Yellow one-word captions run at the top.

TikTok account: **@greg.the.gator3**, posted through the **Metricool** connector (brand blogId `8073640`, timezone America/New_York).

## Repo layout
- `assets/` — Greg's rig layers (body, arm, jaw PNGs), fonts, GSAP. Don't change these.
- `engine/make_episode.sh episodes/epNN` — whole pipeline: voice (Kokoro `am_adam` via `hyperframes tts`) → timing/mouth (`voice.py`) → composition + audio mix (`build.py`) → render. Writes `episodes/epNN/greg-epNN.mp4`. Takes ~5 min.
- `episodes/epNN/script.json` — the lines Greg says, grouped into sections.
- `episodes/epNN/board.py` — what's drawn on the whiteboard for each section. Copy `episodes/ep02/board.py` as the model.
- `EPISODES.md` — log of every episode and every fact used. Never reuse a fact.

## Growth rules (from TikTok algorithm research, Nov 2026)
TikTok ranks mostly on **completion rate and watch time**, then rewatches, shares and saves; likes matter less. Videos are tested on a small pool first (first 30–90 min), and roughly 70% completion is the bar for wider push. So:
- **Short:** target 25–35 s of speech. Use **4 facts**, not 6. One line per fact plus one punchline line.
- **Hook in the first 2 seconds:** no slow intro. Greg's very first line is the most shocking fact as a one-liner or a rude tease ("Australia lost a war to birds. Sit the fuck down."). Page 0 still shows the lesson title so the first frame works as a thumbnail.
- **No dead air:** keep gaps tight; every section should change the board.
- **Loop / rewatch ending:** the outro line should be short and flow back into the opening (e.g. ends on a question the hook answers), and include a reason to comment.
- **Share/save bait:** pick facts people want to send to a friend; end the caption with a question.
- Always set `firstCommentText` to a question that invites replies (e.g. "which one did you NOT know? 🐊").

## When to post
Metricool's best-time data for this account (America/New_York) peaks at 10 AM, 12 PM and **6 PM** every day, strongest Wed–Thu, then Fri, Tue, Mon; weekends are weakest. The audience for a swearing cartoon skews young, so post at **6:00 PM ET** (after school/work).
- Schedule the post for 6:00 PM ET on the day of the run. Before scheduling, call `getScheduledPosts` for that day: if a Greg post is already scheduled within 12 h of that slot, use 6:00 PM on the next day that has none.
- Every ~4 weeks, check post performance with Metricool analytics and shift the slot/day if a different time is clearly winning.

## Making a new episode (what a scheduled run does)
1. Read `EPISODES.md`. Pick the next number NN.
2. Pick **4 new, true, absurd facts** not in the log. Mix animals, history, science, food, geography, the human body. Verify each with a web search before using it; skip anything that turns out to be a myth. If a fact is a joke or exaggeration in Greg's line, make sure the board text itself stays true.
3. Write `episodes/epNN/script.json` in the same shape as ep02: sections `intro` (one-line hook), four fact sections, `outro`; short lines. Follow the Growth rules above. Greg's voice: rude, deadpan teacher, **lots of swearing** (fuck, shit, ass, goddamn, bitch, bastard…), short punchy sentences. Never slurs, never jokes about real private people, nothing sexual. Total ≈ 25–35 s of speech.
4. Write `episodes/epNN/board.py` modelled on ep02:
   - `fact_page(idx, sec_id, 'FACT #n', line1, line2, cue1, cue2)` for each fact, then `pg.draw(G([...]), start, seconds)` doodles.
   - Doodle style: whiteboard-marker cartoons with ink outlines and flat colour fills (`(path, stroke, width, fill, weight)`), with a small visual joke in each. Keep drawings in the page area x 20–920, y 80–400 (text sits at y 488 and 592). No brand logos or trademarked mascots.
   - Every `cue(sec, sentence_index, 'prefix')` must match a word that is actually in that sentence of script.json (first word starting with that prefix).
   - Keep page 0 (intro) and the last page (outro) like ep02, updating the text to fit.
5. Run `engine/make_episode.sh episodes/epNN`. Then check it: grab frames at 4–6 moments with ffmpeg and look at them (text not overflowing the board, drawings not overlapping text, Greg's pointer on the red line). Fix and re-render if needed.
6. `git add` the episode folder (including the mp4) and `EPISODES.md`, commit, push to `main`.
7. Post with Metricool `createScheduledPost`:
   - blogId `8073640`; date: 6:00 PM ET as described in **When to post**
   - media: `https://raw.githubusercontent.com/Xentcrt/greg-the-gator/main/episodes/epNN/greg-epNN.mp4` (wait until the push is done; check the URL returns 200 with curl first)
   - providers `[{"network":"tiktok"}]`, `tiktokData`: `{"privacyOption":"PUBLIC_TO_EVERYONE","isAigc":false,"title":"<short title, required>","disableComment":false,"disableDuet":false,"disableStitch":false,"commercialContentThirdParty":false,"commercialContentOwnBrand":false,"autoAddMusic":false}`
   - text: one short funny caption + `#uselessfacts #funfacts #didyouknow #greg #comedy` and 1–2 topic hashtags. Keep swear words in the caption censored (f*ck) to avoid TikTok suppression.
   - `isAigc` is **false** by the user's choice (2026-11-14): Greg is a stylized cartoon on a whiteboard with a generic TTS voice, which TikTok's rules don't require labelling. If TikTok ever flags or removes a post for missing the AI label, stop setting it to false and tell the user.
   - Metricool copies the video to its own storage when the post is created, so the GitHub link only has to work at that moment.
8. Add the episode to `EPISODES.md` (date, facts, caption, Metricool planner URL), commit and push.
9. Report back with the video file and a one-line summary of the facts.

If any step fails (TTS, render, push, Metricool), stop before posting and report what failed. Never post a video you haven't looked at.
