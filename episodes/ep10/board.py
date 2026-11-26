# Episode 10 boards. Runs inside engine/build.py (exec), so it uses the engine's helpers:
# Page, fact_page, G, GX, ell, squiggle, cue, op, sfx, greg, pages, SEC, fit and the colour constants.
import math

def popin(pg, d, color, w, fill, t, tr=''):
    i = pg.path(d, color, w, fill, tr)
    op('set', '#'+i, t, {'opacity': 1, 'strokeDashoffset': 0, 'fillOpacity': 1})
    op('fromTo', '#'+i, t, {'scale': 1, 'duration': 0.28, 'ease': 'back.out(3)'}, {'scale': 0.2, 'transformOrigin': '50% 50%'})
    return i

SKIN = '#ffd9b3'

def wedge(cx, cy, r1, r2, a0, a1):
    p = lambda r, a: (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
    x0, y0 = p(r1, a0); x1, y1 = p(r2, a0); x2, y2 = p(r2, a1); x3, y3 = p(r1, a1)
    return (f'M{x0:.1f} {y0:.1f} L {x1:.1f} {y1:.1f} A {r2} {r2} 0 0 1 {x2:.1f} {y2:.1f} '
            f'L {x3:.1f} {y3:.1f} A {r1} {r1} 0 0 0 {x0:.1f} {y0:.1f} Z')

# ---------------------------------------------------------------- page 0: intro (already drawn at frame 0)
pg = Page(0)
pg.text("TODAY'S LESSON:", PW/2, 150, 82, BLUE, rot=-2)
pg.text('USELESS', PW/2, 318, 176, RED, rot=-1.5)
pg.text('FACTS', PW/2, 482, 176, RED, rot=1)
pg.static(G([(squiggle(215, 735, 520, 9, 6), RED, 9)]))
pg.static(G([
    ('M70 400 C 70 362, 128 362, 128 400 C 128 430, 98 426, 98 456', BLUE, 9), ('M98 484 l 0 3', BLUE, 12),
    ('M822 392 C 822 356, 876 356, 876 392 C 876 420, 848 418, 848 446', GREEN, 9), ('M848 474 l 0 3', GREEN, 12),
    ('M868 70 l 9 22 l 23 6 l -21 12 l -3 24 l -15 -18 l -24 4 l 13 -20 l -11 -22 l 23 8 Z', AMBER, 6),
    ('M66 76 l 7 17 l 18 5 l -16 9 l -2 19 l -12 -14 l -19 3 l 10 -16 l -9 -17 l 18 6 Z', AMBER, 6),
]))
pg.text('(100% true. 0% useful.)', PW/2, 602, 50, GREEN, at=cue('intro', 0, 'bananas'), rot=-1)
greg.append((cue('intro', 0, 'radioactive'), 'tap', (PX + 300, PY + 500)))
pages.append((pg, 'intro'))

# ---------------------------------------------------------------- page 1: bananas are radioactive
pg, S = fact_page(1, 'banana', 'FACT #1', 'BANANAS CONTAIN RADIOACTIVE', 'POTASSIUM-40', cue('banana', 0, 'bananas'), cue('banana', 0, 'potassium'))
BAN = '#ffd23f'; GLOW = '#39d353'
tb = cue('banana', 0, 'bananas')
banana = G([('M110 230 C 140 360, 360 390, 450 260 C 400 320, 200 330, 150 220 Z', INK, 7, BAN, 1),
            ('M110 230 l -14 -10 l 10 -12 l 14 12', INK, 6, '#6b4a1f', 0.2),        # stem
            ('M450 260 l 10 6', INK, 9, None, 0.1),                                    # black tip
            ('M230 300 l 0 1 M290 306 l 0 1', INK, 12, None, 0.1),                     # eyes
            ('M248 330 q 14 10 28 0', INK, 4, None, 0.1)], 0, 0)                       # smile
pg.draw(banana, tb - 0.1, 0.9)
tr = cue('banana', 0, 'radioactive')
for k, (x, y, dx, dy) in enumerate([(90, 300, -30, 10), (150, 180, -14, -30), (300, 230, 0, -34), (460, 210, 24, -24), (480, 310, 34, 6)]):
    popin(pg, f'M{x} {y} l {dx} {dy}', GLOW, 7, None, tr + 0.05 * k)               # glow lines
popin(pg, ell(720, 220, 110), INK, 6, BAN, tr + 0.1)                                  # radiation sign
for k, a in enumerate((-90, 30, 150)):
    popin(pg, wedge(720, 220, 24, 92, a - 30, a + 30), INK, 3, INK, tr + 0.2 + 0.05 * k)
popin(pg, ell(720, 220, 14), INK, 3, INK, tr + 0.35)
te = cue('banana', 0, 'every')
pg.text('CLICK', 560, 120, 36, GREEN, at=te, rot=-10, pop=False)
pg.text('CLICK', 600, 380, 36, GREEN, at=te + 0.25, rot=8, pop=False)
pg.text('x 1,000,000', 300, 140, 46, PURPLE, at=cue('banana', 1, 'millions'), rot=-5)
pg.text('calm down', 860, 380, 34, BLUE, at=cue('banana', 1, 'calm'), rot=-8, pop=False)

# ---------------------------------------------------------------- page 2: Franklin: turkey more respectable than eagle
pg, S = fact_page(2, 'turkey', 'FACT #2', 'BEN FRANKLIN CALLED THE TURKEY', 'A MORE RESPECTABLE BIRD', cue('turkey', 0, 'franklin'), cue('turkey', 0, 'respectable'))
BROWN = '#8b5a2b'; LBROWN = '#c08a52'
tt = cue('turkey', 0, 'turkey')
fan = [(wedge(250, 300, 60, 150, 190 + 32 * k, 190 + 32 * (k + 1)), INK, 5, [RED, AMBER, LBROWN, AMBER, RED][k], 0.3) for k in range(5)]
turkey = G(fan + [
    (ell(250, 310, 72, 62), INK, 6, BROWN, 1),
    ('M226 368 l -6 26 M274 368 l 6 26 M206 394 l 28 0 M266 394 l 28 0', INK, 6, None, 0.3),   # legs
    (ell(250, 222, 30), INK, 5, LBROWN, 0.5),
    ('M240 214 l 0 1 M262 214 l 0 1', INK, 10, None, 0.1),
    ('M248 226 l 20 6 l -20 6 Z', INK, 3, AMBER, 0.1),                                         # beak
    ('M246 238 q -6 24 6 30 q 8 -14 2 -30 Z', INK, 3, RED, 0.2)], 0, 0)                       # wattle
pg.draw(turkey, tt - 0.2, 1.0)
trs = cue('turkey', 0, 'respectable')
popin(pg, 'M222 196 L 278 196 L 270 186 L 270 130 L 230 130 L 230 186 Z', INK, 5, INK, trs)  # top hat
popin(pg, ell(262, 214, 12), INK, 3, None, trs + 0.1)                                         # monocle
popin(pg, 'M274 214 q 8 20 0 40', INK, 2, None, trs + 0.12)
te = cue('turkey', 0, 'eagle')
eagle = G([(ell(720, 300, 70, 80), INK, 6, '#4a3020', 1),
           (ell(720, 200, 42, 38), INK, 6, WHITE, 0.6),
           ('M700 190 l 30 6 M724 188 l 30 -4', INK, 5, None, 0.1),                         # angry brows
           ('M712 202 l 0 1 M744 200 l 0 1', INK, 10, None, 0.1),
           ('M756 208 q 30 4 20 26 q -8 -12 -22 -10 Z', INK, 4, AMBER, 0.2),                # hooked beak
           ('M700 380 l -6 14 M740 380 l 6 14', INK, 6, AMBER, 0.2)], 0, 0)
pg.draw(eagle, te - 0.1, 0.8)
tm = cue('turkey', 1, 'moral')
pg.text('BAD MORAL', 720, 110, 40, RED, at=tm, rot=-4)
pg.text('CHARACTER', 720, 152, 40, RED, at=tm + 0.1, rot=-4)
pg.text('$$', 820, 300, 40, GREEN, at=tm + 0.4, rot=10, pop=False)                          # shady eagle
tg = cue('turkey', 1, 'thanksgiving')
popin(pg, 'M410 210 L 410 390 M396 210 l 0 40 M410 210 l 0 40 M424 210 l 0 40 M396 250 q 14 14 28 0', INK, 5, None, tg)  # fork
popin(pg, 'M460 390 L 460 270 q 0 -60 18 -60 L 478 300 L 460 300', INK, 5, '#d8dde3', tg + 0.1)                      # knife
pg.text('uh oh', 150, 150, 40, PURPLE, at=tg + 0.3, rot=-10, pop=False)

# ---------------------------------------------------------------- page 3: Reno is west of Los Angeles
pg, S = fact_page(3, 'reno', 'FACT #3', 'RENO, NEVADA IS FARTHER WEST', 'THAN LOS ANGELES', cue('reno', 0, 'reno'), cue('reno', 0, 'los'))
CA = '#fff1b8'; NV = '#d9ecff'
tr0 = cue('reno', 0, 'reno')
ca = ('M110 80 L 248 80 L 248 179 L 427 311 L 430 387 L 344 394 L 301 351 L 229 328 '
      'L 186 258 L 166 219 L 123 153 Z')
nv = 'M248 80 L 446 80 L 446 275 L 427 311 L 248 179 Z'
pg.draw(G([(ca, INK, 6, CA, 1), (nv, INK, 6, NV, 0.8)], 0, 0), S + 0.05, 0.9)
popin(pg, ell(255, 162, 10), INK, 3, RED, tr0)
pg.text('RENO', 300, 150, 30, RED, at=tr0, rot=0, pop=False, anchor='start')
tl = cue('reno', 0, 'los')
popin(pg, ell(307, 342, 10), INK, 3, BLUE, tl)
pg.text('L.A.', 330, 330, 30, BLUE, at=tl, rot=0, pop=False, anchor='start')
tw = cue('reno', 0, 'west')
for k, x in enumerate((255, 307)):
    popin(pg, ' '.join(f'M{x} {y} l 0 14' for y in range(96, 380, 26)), [RED, BLUE][k], 4, None, tw + 0.1 * k)
compass = G([(ell(720, 230, 100), INK, 6, WHITE, 1),
             ('M720 150 L 736 230 L 720 310 L 704 230 Z', INK, 4, None, 0.4),
             ('M720 150 L 736 230 L 704 230 Z', INK, 3, RED, 0.2)], 0, 0)
pg.draw(compass, tl + 0.2, 0.7)
pg.text('N', 720, 118, 34, INK, at=tl + 0.6, rot=0, pop=False)
pg.text('W', 596, 242, 34, INK, at=tl + 0.6, rot=0, pop=False)
tm = cue('reno', 1, 'map')
popin(pg, 'M580 340 L 470 340 M496 318 L 466 340 L 496 362', RED, 8, None, tm)               # big "west" arrow
pg.text('NO JOKE', 860, 380, 34, PURPLE, at=tm + 0.2, rot=-8)

# ---------------------------------------------------------------- page 4: giraffes and humans both have 7 neck bones
pg, S = fact_page(4, 'neck', 'FACT #4', 'GIRAFFES AND HUMANS BOTH HAVE', '7 NECK BONES', cue('neck', 0, 'giraffes'), cue('neck', 0, 'seven'))
GIR = '#f2b84b'; SPOT = '#9a5a1e'
tg = cue('neck', 0, 'giraffes')
giraffe = G([
    ('M596 296 L 640 282 L 528 120 L 498 132 Z', INK, 6, GIR, 1),                                # neck
    (ell(680, 316, 104, 44), INK, 6, GIR, 1),                                                     # body
    ('M612 352 l 0 42 M646 356 l 0 38 M720 356 l 0 38 M754 350 l 0 44', INK, 9, None, 0.4),      # legs
    ('M784 300 q 30 10 26 50', INK, 5, None, 0.1),                                                # tail
    (ell(494, 112, 44, 24), INK, 6, GIR, 0.5),                                                    # head
    ('M494 90 l -6 -26 M512 92 l 4 -26', INK, 6, None, 0.1),                                      # ossicones
    ('M480 106 l 0 1', INK, 10, None, 0.1),
    (ell(650, 306, 16, 10), SPOT, 1, SPOT, 0.1), (ell(704, 326, 14, 9), SPOT, 1, SPOT, 0.1),
    (ell(740, 302, 12, 8), SPOT, 1, SPOT, 0.1)], 0, 0)
pg.draw(giraffe, tg - 0.2, 1.0)
ts = cue('neck', 0, 'seven')
for k in range(1, 7):                                                                           # 7 segments
    f = k / 7
    x0, y0 = 498 + (596 - 498) * f, 132 + (296 - 132) * f
    x1, y1 = 528 + (640 - 528) * f, 120 + (282 - 120) * f
    popin(pg, f'M{x0:.0f} {y0:.0f} L {x1:.0f} {y1:.0f}', INK, 4, None, ts + 0.05 * k)
pg.text('7', 420, 230, 64, RED, at=ts + 0.3, rot=-6)
tu = cue('neck', 0, 'you')
human = G([(ell(240, 250, 30), INK, 5, SKIN, 0.4),
           ('M240 280 L 240 286', INK, 6, None, 0.1),
           ('M240 286 L 240 344 M240 344 L 218 392 M240 344 L 262 392 M212 304 L 268 304', INK, 6, None, 0.6),
           ('M228 244 l 0 1 M252 244 l 0 1', INK, 8, None, 0.1)], 0, 0)
pg.draw(human, tu - 0.3, 0.6)
pg.text('7', 300, 290, 48, RED, at=tu + 0.2, rot=6)
popin(pg, 'M290 280 L 250 283', RED, 4, None, tu + 0.25)
tb = cue('neck', 1, 'bigger')
pg.text('SHOW-OFF', 150, 140, 42, PURPLE, at=tb, rot=-8)
popin(pg, 'M226 236 q 14 -8 28 0', INK, 3, None, cue('neck', 1, 'short'))                       # human frowning up

# ---------------------------------------------------------------- page 5: outro
pg = Page(5); S = SEC['outro']['start']
pg.text('HOMEWORK:', PW/2, 150, 96, BLUE, at=cue('outro', 0, 'class'), rot=-2)
s1, _ = fit('WHICH FRUIT IS', 840, 150)
pg.text('WHICH FRUIT IS', PW/2, 310, s1, RED, at=cue('outro', 1, 'which'), rot=-1.5)
s2, _ = fit('RADIOACTIVE?', 820, 150)
pg.text('RADIOACTIVE?', PW/2, 458, s2, RED, at=cue('outro', 1, 'radioactive'), rot=1)
u = pg.path(squiggle(110, 840, 492, 9, 10), RED, 9)
tc = cue('outro', 1, 'comment')
op('set', '#'+u, tc, {'opacity': 1}); op('to', '#'+u, tc, {'strokeDashoffset': 0, 'duration': 0.3, 'ease': 'none'})
pg.text('answer in the comments', PW/2, 596, 52, GREEN, at=tc + 0.1, rot=-1)
greg.append((cue('outro', 1, 'radioactive'), 'tap', (PX + 270, PY + 478)))
pages.append((pg, 'outro'))
