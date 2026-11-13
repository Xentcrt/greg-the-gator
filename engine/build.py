# Greg engine: builds a HyperFrames project (index.html + mixed audio) for one episode.
# usage: python3 build.py EPISODE_DIR WORK_DIR
#   EPISODE_DIR has script.json and board.py; WORK_DIR has voice/, assets/ and timing.json (from voice.py).
import json, math, re, html
import numpy as np, soundfile as sf
from PIL import ImageFont

import sys, os
EP = os.path.abspath(sys.argv[1]) + '/'
P = os.path.abspath(sys.argv[2]) + '/'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
T = json.load(open(P + 'timing.json'))
DUR = T['duration']; FPS = 30
SEC = {s['id']: s for s in T['sections']}
ORDER = [s['id'] for s in T['sections']]
PM = ROOT + 'assets/PermanentMarker.ttf'

def cue(sec, si, prefix):
    for w in SEC[sec]['sentences'][si]['words']:
        if re.sub(r"[^a-z']", '', w['w'].lower()).startswith(prefix):
            return w['s']
    raise KeyError((sec, si, prefix))

def fit(text, maxw, maxsize):
    w100 = ImageFont.truetype(PM, 100).getlength(text)
    size = min(maxsize, maxw / w100 * 100)
    return round(size, 1), w100 * size / 100

# ---------------------------------------------------------------- layout
BX, BY, BW, BH = 50, 320, 980, 685            # whiteboard outer
PX, PY, PW, PH = 66, 336, 948, 653            # page area on the board
GS = 0.68; GX0, GY0 = 440, 1040               # Greg scale and box corner (mirrored)
PIV = (645.0, 405.0); HAND = (726.0, 605.0)   # shoulder and palm, crop units
A_LEN = math.hypot(HAND[0]-PIV[0], HAND[1]-PIV[1])
TH0 = math.degrees(math.atan2(HAND[1]-PIV[1], HAND[0]-PIV[0]))
B_LEN = 640.0
INK = '#1f1f24'; BLUE = '#1c53c7'; RED = '#d42d27'; GREEN = '#178a4a'; AMBER = '#e09a00'; PURPLE = '#7a3cc2'; BROWN = '#8a5a2b'

def ik(sx, sy):
    """screen target -> (arm rotation, pointer rotation) in degrees."""
    tx = 798 - (sx - GX0) / GS; ty = (sy - GY0) / GS
    dx, dy = tx - PIV[0], ty - PIV[1]
    d = min(max(math.hypot(dx, dy), abs(B_LEN - A_LEN) + 5), A_LEN + B_LEN - 6)
    phi = math.atan2(dy, dx)
    al = math.acos((A_LEN**2 + d**2 - B_LEN**2) / (2 * A_LEN * d))
    th = phi + al
    hx, hy = PIV[0] + A_LEN * math.cos(th), PIV[1] + A_LEN * math.sin(th)
    psi = math.atan2(PIV[1] + d * math.sin(phi) - hy, PIV[0] + d * math.cos(phi) - hx)
    return round(math.degrees(th) - TH0, 2), round(math.degrees(psi - th), 2)

REST = (-20.0, round(-90 - (TH0 - 20), 2))

ops = []          # timeline operations, replayed by the page script
def op(kind, sel, at, vars, frm=None):
    o = {'k': kind, 's': sel, 't': round(at, 3), 'v': vars}
    if frm is not None: o['f'] = frm
    ops.append(o)

uid = [0]
def nid(p='e'):
    uid[0] += 1; return f'{p}{uid[0]}'

sfx = []          # (time, kind)

class Page:
    def __init__(self, idx):
        self.idx = idx; self.els = []
    def path(self, d, color=INK, w=7, fill=None, tr='', hidden=True):
        i = nid('p')
        st = 'stroke-dasharray:1.02 1.02;stroke-dashoffset:1.02;opacity:0' if hidden else ''
        fa = f' fill="{fill}" fill-opacity="{0 if hidden else 1}"' if fill else ' fill="none"'
        self.els.append(f'<path id="{i}" d="{d}" pathLength="1" stroke="{color}" stroke-width="{w}"{fa} '
                        f'stroke-linecap="round" stroke-linejoin="round" transform="{tr}" style="{st}"/>')
        return i
    def draw(self, items, t0, total):
        """items: [(d, color, w, fill, weight)] drawn one after another across `total` seconds."""
        tw = sum(it[4] for it in items); t = t0
        for d, color, w, fill, wt, tr in items:
            i = self.path(d, color, w, fill, tr)
            du = max(total * wt / tw, 0.05)
            op('set', '#'+i, t, {'opacity': 1})
            op('to', '#'+i, t, {'strokeDashoffset': 0, 'duration': round(du, 3), 'ease': 'none'})
            if fill: op('to', '#'+i, t + du * 0.7, {'fillOpacity': 1, 'duration': 0.15})
            t += du
    def static(self, items):
        for d, color, w, fill, wt, tr in items:
            self.path(d, color, w, fill, tr, hidden=False)
    def text(self, s, x, y, size, color, at=None, anchor='middle', rot=0, pop=True, ls=0):
        i = nid('t')
        hid = 'opacity:0' if at is not None else ''
        self.els.append(f'<g id="{i}" style="{hid}"><text x="{x}" y="{y}" font-size="{size}" fill="{color}" '
                        f'text-anchor="{anchor}" letter-spacing="{ls}" transform="rotate({rot} {x} {y})">{html.escape(s)}</text></g>')
        if at is not None:
            op('fromTo', '#'+i, at, {'opacity': 1, 'scale': 1, 'duration': 0.24, 'ease': 'back.out(2.4)'},
               {'opacity': 0, 'scale': 0.55, 'transformOrigin': '50% 50%'})
            if pop: sfx.append((at, 'pop'))
        return i
    def svg(self):
        vis = '' if self.idx == 0 else 'opacity:0'
        return (f'<div class="page" id="pg{self.idx}" style="{vis}"><svg viewBox="0 0 {PW} {PH}" width="{PW}" height="{PH}">'
                + '\n'.join(self.els) + '</svg></div>')

def G(items, ox=0, oy=0, sc=1):
    tr = f'translate({ox} {oy}) scale({sc})'
    out = []
    for it in items:
        d, color = it[0], it[1]
        w = it[2] if len(it) > 2 else 7
        fill = it[3] if len(it) > 3 else None
        wt = it[4] if len(it) > 4 else 1
        out.append((d, color, w, fill, wt, tr))
    return out

def squiggle(x0, x1, y, amp=7, n=None):
    n = n or max(int((x1 - x0) / 60), 3)
    step = (x1 - x0) / n; d = f'M{x0:.0f} {y:.0f}'
    for k in range(n):
        d += f' q {step/2:.1f} {(-amp if k % 2 == 0 else amp):.1f} {step:.1f} 0'
    return d

pages = []
greg = []          # (time, kind, payload)

def fact_page(idx, sec, tag, l1, l2, l1cue, l2cue):
    pg = Page(idx); S = SEC[sec]['start']
    pg.text(tag, 22, 58, 46, RED, at=S - 0.02, anchor='start', rot=-3, pop=False)
    i = pg.path(squiggle(20, 196, 74, 4, 4), RED, 5)
    op('set', '#'+i, S + 0.1, {'opacity': 1}); op('to', '#'+i, S + 0.1, {'strokeDashoffset': 0, 'duration': 0.25, 'ease': 'none'})
    s1, w1 = fit(l1, 800, 60); s2, w2 = fit(l2, 800, 96); w1 *= 1.08; w2 *= 1.08
    pg.text(l1, PW/2, 488, s1, BLUE, at=l1cue, rot=-1)
    pg.text(l2, PW/2, 592, s2, RED, at=l2cue, rot=1)
    ux0, ux1 = PW/2 - w2/2 + 6, PW/2 + w2/2 - 6
    u = pg.path(squiggle(ux0, ux1, 622, 6), RED, 7)
    op('set', '#'+u, l2cue + 0.12, {'opacity': 1}); op('to', '#'+u, l2cue + 0.12, {'strokeDashoffset': 0, 'duration': 0.3, 'ease': 'none'})
    tx = min(max(ux0 + 0.22 * (ux1 - ux0), 150), 330)
    greg.append((l2cue, 'tap', (PX + tx, PY + 604)))
    pages.append((pg, sec)); return pg, S

# ---------------------------------------------------------------- drawing helpers
def ell(cx, cy, rx, ry=None):
    ry = rx if ry is None else ry
    return f'M{cx-rx} {cy} A {rx} {ry} 0 1 0 {cx+rx} {cy} A {rx} {ry} 0 1 0 {cx-rx} {cy} Z'

def GX(items, ox, oy, sx, sy):
    tr = f'translate({ox} {oy}) scale({sx} {sy})'
    return [(it[0], it[1], it[2] if len(it) > 2 else 7, it[3] if len(it) > 3 else None,
             it[4] if len(it) > 4 else 1, tr) for it in items]

WHITE = '#ffffff'

# ---------------------------------------------------------------- episode boards (episode's board.py)
exec(open(EP + 'board.py').read())
pages.sort(key=lambda p: p[0].idx)

# ---------------------------------------------------------------- page changes (eraser wipe)
for k in range(1, len(pages)):
    S = SEC[pages[k][1]]['start']
    w0 = S - 0.44
    prev = f'#pg{k-1}'
    op('fromTo', prev, w0, {'clipPath': 'inset(0% 0% 0% 100%)', 'duration': 0.30, 'ease': 'power1.inOut', 'immediateRender': False},
       {'clipPath': 'inset(0% 0% 0% 0%)'})
    op('set', prev, w0 + 0.31, {'opacity': 0})
    op('set', f'#pg{k}', w0 + 0.32, {'opacity': 1})
    op('set', '#eraser', w0 - 0.02, {'opacity': 1, 'x': 0, 'y': 0})
    op('to', '#eraser', w0, {'x': PW - 40, 'duration': 0.30, 'ease': 'power1.inOut'})
    op('to', '#eraser', w0, {'y': 46, 'duration': 0.075, 'ease': 'sine.inOut', 'yoyo': True, 'repeat': 3})
    op('set', '#eraser', w0 + 0.32, {'opacity': 0})
    sfx.append((w0, 'whoosh'))
    greg.append((w0 - 0.05, 'rest', None))

# ---------------------------------------------------------------- Greg: pointer, eyes, body
greg.sort(key=lambda g: g[0])
op('set', '#arm', 0, {'rotation': REST[0], 'transformOrigin': f'{PIV[0]}px {PIV[1]}px'})
op('set', '#ptr', 0, {'rotation': REST[1], 'transformOrigin': '0px 0px'})
for t, kind, tgt in greg:
    if kind == 'tap':
        ar, pr = ik(*tgt)
        op('to', '#arm', t - 0.32, {'rotation': ar, 'duration': 0.30, 'ease': 'power2.out'})
        op('to', '#ptr', t - 0.32, {'rotation': pr - 9, 'duration': 0.26, 'ease': 'power2.out'})
        for k in range(2):
            tt = t - 0.05 + k * 0.24
            op('to', '#ptr', tt, {'rotation': pr, 'duration': 0.06, 'ease': 'power2.in'})
            op('to', '#ptr', tt + 0.06, {'rotation': pr - 7, 'duration': 0.12, 'ease': 'power2.out'})
            sfx.append((tt + 0.06, 'tap'))
        op('to', '#ptr', t + 0.45, {'rotation': pr - 2, 'duration': 0.15, 'ease': 'power1.out'})
        op('to', '.pupil', t - 0.3, {'x': 7, 'y': -5, 'duration': 0.15})
        op('to', '#gregWrap', t - 0.04, {'scaleY': 1.035, 'scaleX': 0.985, 'duration': 0.09, 'ease': 'power2.out', 'transformOrigin': '50% 100%'})
        op('to', '#gregWrap', t + 0.05, {'scaleY': 1, 'scaleX': 1, 'duration': 0.22, 'ease': 'back.out(3)'})
    else:
        op('to', '#arm', t, {'rotation': REST[0], 'duration': 0.34, 'ease': 'power2.inOut'})
        op('to', '#ptr', t, {'rotation': REST[1], 'duration': 0.34, 'ease': 'power2.inOut'})
        op('to', '.pupil', t, {'x': 0, 'y': 0, 'duration': 0.15})
# end: back to rest and look at the camera
tend = SEC['outro']['end'] + 0.35
op('to', '#arm', tend, {'rotation': REST[0], 'duration': 0.4, 'ease': 'power2.inOut'})
op('to', '#ptr', tend, {'rotation': REST[1], 'duration': 0.4, 'ease': 'power2.inOut'})
op('to', '.pupil', tend, {'x': 0, 'y': 0, 'duration': 0.15})
# idle bob for the whole film
nb = int(DUR / 0.8)
op('to', '#gregBob', 0, {'y': -7, 'duration': 0.8, 'ease': 'sine.inOut', 'yoyo': True, 'repeat': nb})
# blinks
for t in [1.7, 5.3, 8.1, 11.4, 14.6, 16.9, 20.4, 22.9, 26.0, 28.6, 31.3, 34.4]:
    if t < DUR - 0.3:
        op('to', '.eye', t, {'scaleY': 0.08, 'duration': 0.07, 'ease': 'power1.in'})
        op('to', '.eye', t + 0.09, {'scaleY': 1, 'duration': 0.08, 'ease': 'power1.out'})
# mouth: jaw drop per frame from the voice loudness
JAW = 19
last = None
for f, v in enumerate(T['mouth']):
    if v != last:
        op('set', '#jaw', f / FPS, {'y': round(v * JAW, 2)}); last = v

# ---------------------------------------------------------------- captions (one word at a time)
caps = []
def capword(w):
    w = re.sub(r"[^A-Za-z0-9'?!\-]", '', w).upper()
    for x, y in (('FUCK', 'F*CK'), ('SHIT', 'SH*T'), ('BITCH', 'B*TCH')): w = w.replace(x, y)
    return w
for s in T['sections']:
    for sen in s['sentences']:
        ws = sen['words']
        for k, w in enumerate(ws):
            e = ws[k+1]['s'] if k + 1 < len(ws) else sen['e'] + 0.12
            i = nid('c'); txt = capword(w['w'])
            e_ = html.escape(txt)
            caps.append(f'<svg class="cap" id="{i}" viewBox="0 0 1080 170" width="1080" height="170">'
                        f'<text x="540" y="128" fill="#14110f" stroke="#14110f" stroke-width="22">{e_}</text>'
                        f'<text x="540" y="120" fill="#ffe11a" stroke="#14110f" stroke-width="20" paint-order="stroke fill">{e_}</text></svg>')
            op('set', '#'+i, w['s'], {'opacity': 1})
            op('fromTo', '#'+i, w['s'], {'scale': 1, 'duration': 0.1, 'ease': 'back.out(3)'}, {'scale': 0.72})
            op('set', '#'+i, e, {'opacity': 0})

# ---------------------------------------------------------------- audio: voice + small sound effects
y, sr = sf.read(P + 'assets/greg-voice.wav', dtype='float32')
rng = np.random.default_rng(7)
def add(sig, t, g):
    a = int(t * sr); b = min(a + len(sig), len(y))
    if a < len(y): y[a:b] += sig[:b-a] * g
tt = np.arange(int(0.09 * sr)) / sr
tap = (np.sin(2*np.pi*820*tt) + 0.6*np.sin(2*np.pi*1730*tt)) * np.exp(-tt*70); tap[:int(0.004*sr)] += rng.normal(0, 0.6, int(0.004*sr))
tt = np.arange(int(0.08 * sr)) / sr
pop = np.sin(2*np.pi*(420*tt + 3600*tt**2)) * np.sin(np.pi*tt/0.08)**2
n = int(0.32 * sr); wn = rng.normal(0, 1, n); wn = np.convolve(wn, np.ones(9)/9, 'same'); wn = np.diff(wn, prepend=0) * 3
who = wn * np.hanning(n)
for t, k in sfx:
    if k == 'tap': add(tap, t, 0.16)
    elif k == 'pop': add(pop, t, 0.10)
    else: add(who / np.abs(who).max(), t, 0.10)
y = np.clip(y, -0.98, 0.98)
sf.write(P + 'assets/ep2-audio.wav', y, sr, subtype='PCM_16')

# ---------------------------------------------------------------- HTML
pages_html = '\n'.join(p.svg() for p, _ in pages)
W, H = 1080, 1920
tray_y = BY + BH
HTML = f'''<!doctype html>
<html lang="en" data-resolution="portrait">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width={W}, height={H}" />
<script src="assets/gsap.min.js"></script>
<style>
@font-face {{ font-family: "Permanent Marker"; src: url("assets/PermanentMarker.woff2") format("woff2"); font-display: block; }}
@font-face {{ font-family: "Luckiest Guy"; src: url("assets/LuckiestGuy.woff2") format("woff2"); font-display: block; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: {W}px; height: {H}px; overflow: hidden; background: #7fb3ab; }}
#root {{ position: relative; width: {W}px; height: {H}px; overflow: hidden; }}
#scene {{ position: absolute; inset: 0; }}
#bg {{ position: absolute; inset: 0; }}
.page {{ position: absolute; left: {PX}px; top: {PY}px; width: {PW}px; height: {PH}px; }}
.page svg {{ overflow: visible; display: block; }}
.page text {{ font-family: "Permanent Marker", cursive; }}
#eraser {{ position: absolute; left: {PX - 20}px; top: {PY + 250}px; width: 64px; height: 150px; opacity: 0;
  border-radius: 10px; background: linear-gradient(90deg, #2f3640 0 46%, #1c53c7 46% 100%); box-shadow: 0 6px 10px rgba(0,0,0,.25); transform-origin: 50% 50%; rotate: 9deg; }}
#gregWrap {{ position: absolute; left: {GX0}px; top: {GY0}px; width: {798*GS:.1f}px; height: {1240*GS:.1f}px; }}
#gregBob {{ position: absolute; inset: 0; }}
#gregFlip {{ position: absolute; left: 0; top: 0; width: 798px; height: 1240px; transform-origin: 0 0; transform: translateX({798*GS:.2f}px) scale(-{GS}, {GS}); }}
#gregFlip img {{ position: absolute; left: 0; top: 0; width: 798px; height: 1240px; }}
#arm {{ position: absolute; left: 0; top: 0; width: 798px; height: 1240px; }}
#ptrBase {{ position: absolute; left: {HAND[0]}px; top: {HAND[1]}px; width: 0; height: 0; transform-origin: 0 0; transform: rotate({TH0:.2f}deg); }}
#ptr {{ position: absolute; left: 0; top: 0; width: 0; height: 0; }}
#ptr svg {{ position: absolute; left: -70px; top: -30px; overflow: visible; }}
#face {{ position: absolute; left: 0; top: -140px; overflow: visible; }}
#shadow {{ position: absolute; left: {GX0 + 30}px; top: {GY0 + 1240*GS - 52:.0f}px; width: {798*GS - 60:.0f}px; height: 56px; border-radius: 50%; background: rgba(40,25,10,.28); filter: blur(6px); }}
#caps {{ position: absolute; left: 0; top: 140px; width: {W}px; height: 170px; }}
.cap {{ position: absolute; left: 0; top: 0; opacity: 0; overflow: visible; transform-origin: 50% 60%; }}
.cap text {{ font-family: "Luckiest Guy", sans-serif; font-size: 108px; letter-spacing: 2px; text-anchor: middle; stroke-linejoin: round; stroke-linecap: round; }}
#fontwarm {{ position: absolute; left: -2000px; top: 0; opacity: 0.01; }}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="{W}" data-height="{H}" data-fps="{FPS}">
 <div id="scene" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0">
  <svg id="bg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
   <defs>
    <linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8ebfb7"/><stop offset="1" stop-color="#73a69e"/></linearGradient>
    <linearGradient id="floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c99a62"/><stop offset="1" stop-color="#a97a45"/></linearGradient>
    <linearGradient id="sheen" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="0.5" stop-color="#f6f7f3"/><stop offset="1" stop-color="#eceee9"/></linearGradient>
    <radialGradient id="vig" cx="0.5" cy="0.45" r="0.75"><stop offset="0.6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.28"/></radialGradient>
   </defs>
   <rect width="{W}" height="1400" fill="url(#wall)"/>
   <rect y="1400" width="{W}" height="320" fill="#4f837c"/>
   <rect y="1392" width="{W}" height="18" fill="#3d6a64"/>
   <g stroke="#467670" stroke-width="5">{''.join(f'<line x1="{x}" y1="1410" x2="{x}" y2="1700"/>' for x in range(90, 1080, 180))}</g>
   <rect y="1700" width="{W}" height="220" fill="url(#floor)"/>
   <rect y="1690" width="{W}" height="22" fill="#e9e3d6"/>
   <g stroke="#8f6436" stroke-width="4" opacity=".55"><line x1="0" y1="1772" x2="{W}" y2="1772"/><line x1="0" y1="1846" x2="{W}" y2="1846"/><line x1="260" y1="1712" x2="230" y2="1772"/><line x1="700" y1="1712" x2="720" y2="1772"/><line x1="480" y1="1772" x2="460" y2="1846"/><line x1="900" y1="1772" x2="930" y2="1846"/><line x1="160" y1="1846" x2="120" y2="1920"/><line x1="640" y1="1846" x2="650" y2="1920"/></g>
   <!-- whiteboard -->
   <rect x="{BX+8}" y="{BY+12}" width="{BW}" height="{BH+24}" rx="16" fill="#000" opacity=".18"/>
   <rect x="{BX}" y="{BY}" width="{BW}" height="{BH}" rx="14" fill="#c3c7cd" stroke="#8e939b" stroke-width="4"/>
   <rect x="{BX+16}" y="{BY+16}" width="{BW-32}" height="{BH-32}" rx="4" fill="url(#sheen)" stroke="#a7acb3" stroke-width="2"/>
   <rect x="{BX+40}" y="{tray_y-4}" width="{BW-80}" height="26" rx="6" fill="#aeb3ba" stroke="#8e939b" stroke-width="3"/>
   <g>
    <rect x="130" y="{tray_y-16}" width="92" height="16" rx="7" fill="#d42d27"/><rect x="130" y="{tray_y-16}" width="24" height="16" rx="6" fill="#8f1c18"/>
    <rect x="240" y="{tray_y-16}" width="92" height="16" rx="7" fill="#1c53c7"/><rect x="240" y="{tray_y-16}" width="24" height="16" rx="6" fill="#123a8c"/>
    <rect x="350" y="{tray_y-16}" width="92" height="16" rx="7" fill="#178a4a"/><rect x="350" y="{tray_y-16}" width="24" height="16" rx="6" fill="#0e5e31"/>
   </g>
   <!-- desk -->
   <g>
    <rect x="54" y="1560" width="26" height="250" fill="#6f4420"/><rect x="352" y="1560" width="26" height="250" fill="#6f4420"/>
    <rect x="40" y="1520" width="352" height="150" rx="6" fill="#8f5d2e"/>
    <rect x="70" y="1556" width="292" height="84" rx="6" fill="#7d4f25" stroke="#6a411c" stroke-width="3"/><circle cx="216" cy="1598" r="10" fill="#e3c27a"/>
    <rect x="22" y="1492" width="388" height="34" rx="8" fill="#b47a3f"/><rect x="22" y="1492" width="388" height="10" rx="5" fill="#c98f52"/>
    <rect x="200" y="1452" width="170" height="40" rx="5" fill="#1c53c7"/><rect x="200" y="1462" width="170" height="8" fill="#f1ede2"/>
    <rect x="214" y="1416" width="150" height="36" rx="5" fill="#e0a100"/><rect x="214" y="1425" width="150" height="7" fill="#f1ede2"/>
    <path d="M110 1440 C 80 1436, 70 1474, 86 1490 C 98 1500, 124 1500, 136 1490 C 152 1474, 142 1436, 110 1440 Z" fill="#d42d27"/>
    <path d="M110 1440 C 108 1428, 112 1420, 120 1414" stroke="#5a3a18" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path d="M118 1424 C 132 1412, 146 1418, 148 1426 C 138 1434, 126 1432, 118 1424 Z" fill="#178a4a"/>
    <ellipse cx="96" cy="1458" rx="7" ry="11" fill="#fff" opacity=".45"/>
   </g>
   <rect width="{W}" height="{H}" fill="url(#vig)"/>
  </svg>
{pages_html}
  <div id="eraser"></div>
  <div id="shadow"></div>
  <div id="gregWrap"><div id="gregBob"><div id="gregFlip">
   <img src="assets/greg-body-noarm.png" alt="" />
   <img id="jaw" src="assets/greg-jaw.png" alt="" />
   <svg id="face" viewBox="0 -140 798 1380" width="798" height="1380">
    <g class="eye"><circle cx="287" cy="66" r="31" fill="#fff" stroke="#1b1b1b" stroke-width="4"/><g class="pupil"><circle cx="287" cy="68" r="14" fill="#16130f"/><circle cx="282" cy="62" r="5" fill="#fff"/></g></g>
    <g class="eye"><circle cx="501" cy="66" r="31" fill="#fff" stroke="#1b1b1b" stroke-width="4"/><g class="pupil"><circle cx="501" cy="68" r="14" fill="#16130f"/><circle cx="496" cy="62" r="5" fill="#fff"/></g></g>
    <g fill="rgba(255,255,255,.10)" stroke="#111" stroke-width="9" stroke-linecap="round"><circle cx="287" cy="66" r="41"/><circle cx="501" cy="66" r="41"/><path d="M328 60 Q 394 38 460 60" fill="none"/><path d="M246 62 L 230 72 M542 62 L 558 72" fill="none"/></g>
    <g stroke="#a8780f" stroke-width="5" stroke-linejoin="round"><path d="M330 40 L 318 -48 L 360 -6 L 394 -70 L 428 -6 L 470 -48 L 458 40 Z" fill="#f6c543"/><path d="M328 18 L 460 18" fill="none"/>
     <circle cx="318" cy="-50" r="8" fill="#f6c543"/><circle cx="394" cy="-72" r="8" fill="#f6c543"/><circle cx="470" cy="-50" r="8" fill="#f6c543"/>
     <circle cx="356" cy="30" r="8" fill="#ff6b5e"/><circle cx="394" cy="30" r="8" fill="#ff6b5e"/><circle cx="432" cy="30" r="8" fill="#ff6b5e"/></g>
   </svg>
   <div id="arm">
    <div id="ptrBase"><div id="ptr"><svg width="800" height="60" viewBox="-70 -30 800 60">
      <line x1="-52" y1="0" x2="{B_LEN-40:.0f}" y2="0" stroke="#6e431b" stroke-width="17" stroke-linecap="round"/>
      <line x1="-52" y1="0" x2="{B_LEN-40:.0f}" y2="0" stroke="#b9803f" stroke-width="11" stroke-linecap="round"/>
      <line x1="{B_LEN-52:.0f}" y1="0" x2="{B_LEN-6:.0f}" y2="0" stroke="#b3382e" stroke-width="17" stroke-linecap="round"/>
      <line x1="{B_LEN-52:.0f}" y1="0" x2="{B_LEN-6:.0f}" y2="0" stroke="#ff6b5e" stroke-width="11" stroke-linecap="round"/>
    </svg></div></div>
    <img src="assets/greg-arm.png" alt="" />
   </div>
  </div></div></div>
  <div id="caps">
{chr(10).join(caps)}
  </div>
  <div id="fontwarm"><span style="font-family:'Permanent Marker'">a</span><span style="font-family:'Luckiest Guy'">a</span></div>
 </div>
 <audio id="voice" class="clip" data-start="0" data-duration="{DUR}" data-track-index="1" data-volume="1" src="assets/ep2-audio.wav"></audio>
</div>
<script>
const OPS = {json.dumps(ops, separators=(',', ':'))};
const tl = gsap.timeline({{ paused: true }});
for (const o of OPS) {{
  if (o.k === "set") tl.set(o.s, o.v, o.t);
  else if (o.k === "to") tl.to(o.s, o.v, o.t);
  else tl.fromTo(o.s, o.f, o.v, o.t);
}}
tl.set({{}}, {{}}, {DUR});
window.__timelines = window.__timelines || {{}};
window.__timelines["main"] = tl;
tl.seek(0);
</script>
</body>
</html>
'''
open(P + 'index.html', 'w').write(HTML)
json.dump({'duration': DUR, 'ops': len(ops), 'taps': [(round(t, 2), k) for t, k, _ in greg]}, open(P + 'build_report.json', 'w'))
print('ops', len(ops), 'captions', len(caps), 'duration', DUR)
print('rest', REST, 'a', round(A_LEN, 1), 'th0', round(TH0, 2))
for t, k, tgt in greg:
    if k == 'tap': print(round(t, 2), tgt, ik(*tgt))
