# Episode 7 boards. Runs inside engine/build.py (exec), so it uses the engine's helpers:
# Page, fact_page, G, GX, ell, squiggle, cue, op, sfx, greg, pages, SEC, fit and the colour constants.
def popin(pg, d, color, w, fill, t, tr=''):
    i = pg.path(d, color, w, fill, tr)
    op('set', '#'+i, t, {'opacity': 1, 'strokeDashoffset': 0, 'fillOpacity': 1})
    op('fromTo', '#'+i, t, {'scale': 1, 'duration': 0.28, 'ease': 'back.out(3)'}, {'scale': 0.2, 'transformOrigin': '50% 50%'})
    return i

def star(x, y, r):
    return f'M{x} {y-r} l {r*0.3} {r*0.7} l {r*0.7} {r*0.1} l {-r*0.55} {r*0.45} l {r*0.2} {r*0.75} l {-r*0.65} {-r*0.4} l {-r*0.65} {r*0.4} l {r*0.2} {-r*0.75} l {-r*0.55} {-r*0.45} l {r*0.7} {-r*0.1} Z'

SKIN = '#ffd9b3'

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
pg.text('(100% true. 0% useful.)', PW/2, 602, 50, GREEN, at=cue('intro', 0, 'guillotine'), rot=-1)
greg.append((cue('intro', 0, 'france'), 'tap', (PX + 300, PY + 500)))
pages.append((pg, 'intro'))

# ---------------------------------------------------------------- page 1: guillotine in 1977
pg, S = fact_page(1, 'guillotine', 'FACT #1', "FRANCE'S LAST GUILLOTINING WAS IN", '1977, THE YEAR OF STAR WARS', cue('guillotine', 0, 'france'), cue('guillotine', 0, 'star'))
STEEL = '#b8c2cc'
guil = G([
    ('M120 400 L 120 110 M260 400 L 260 110', BROWN, 16, None, 1),                   # posts
    ('M104 100 L 276 100 L 276 122 L 104 122 Z', INK, 5, BROWN, 0.5),                # top beam
    ('M80 390 L 300 390 L 300 404 L 80 404 Z', INK, 5, BROWN, 0.4),                  # base
    ('M128 140 L 252 170 L 252 210 L 128 210 Z', INK, 5, STEEL, 0.8),                # slanted blade
    ('M190 122 L 190 140', INK, 4, None, 0.1),                                       # rope
    ('M128 300 L 252 300 L 252 330 L 128 330 Z', INK, 5, BROWN, 0.4),                # lunette
    (ell(190, 315, 18, 14), INK, 4, WHITE, 0.2),
], 0, 0)
pg.draw(guil, S + 0.05, 1.1)
tg = cue('guillotine', 0, 'guillotined')
basket = G([('M300 340 L 400 340 L 386 400 L 314 400 Z', INK, 5, '#c79a5b', 0.6),
            ('M300 356 L 400 356 M306 374 L 394 374', INK, 3, None, 0.2)], 0, 0)
pg.draw(basket, tg, 0.4)
popin(pg, ell(350, 330, 30, 22), INK, 4, '#5cb85c', tg + 0.4)                         # watermelon "volunteer"
pg.text('practice melon', 380, 280, 28, GREEN, at=tg + 0.6, rot=-6, pop=False)
tsw = cue('guillotine', 0, 'star')
screen = G([('M520 110 L 900 110 L 900 330 L 520 330 Z', INK, 6, '#1d2340', 1),
            ('M560 330 L 540 380 M860 330 L 880 380', INK, 6, None, 0.3)], 0, 0)
pg.draw(screen, tsw - 0.4, 0.6)
pg.text('NOW SHOWING', 710, 160, 34, AMBER, at=tsw + 0.2, rot=0, pop=False)
tls = cue('guillotine', 1, 'lightsabers')
pg.draw(G([('M600 290 L 820 200', '#7fd3ff', 16, None, 1), ('M600 290 L 572 302', INK, 14, None, 0.3)], 0, 0), tls, 0.4)
tbl = cue('guillotine', 1, 'blades')
pg.draw(G([('M120 230 L 260 230', RED, 6, None, 1), ('M190 200 l 0 20 M180 210 l 10 12 l 10 -12', RED, 5, None, 0.5)], 0, 0), tbl, 0.3)
pg.text('1977!!', 710, 400, 48, RED, at=cue('guillotine', 1, 'holy'), rot=-4)

# ---------------------------------------------------------------- page 2: sea otters hold hands
pg, S = fact_page(2, 'otters', 'FACT #2', 'SEA OTTERS HOLD HANDS', 'WHILE THEY SLEEP', cue('otters', 0, 'sea'), cue('otters', 0, 'sleep'))
OTTER = '#8a5a2b'; BELLY = '#d9b48a'; WATER = '#7fb2e5'
pg.draw(G([('M30 300 ' + ' '.join('q 30 -16 60 0' for _ in range(15)) + ' L 930 404 L 30 404 Z', INK, 5, WATER, 1)], 0, 0), S + 0.05, 0.6)
def otter(cx, flip):
    s = -1 if flip else 1
    return [
        (ell(cx, 270, 110, 34), INK, 6, OTTER, 1),                                   # body floating
        (ell(cx, 262, 80, 20), INK, 4, BELLY, 0.5),                                  # belly
        (ell(cx - s * 120, 252, 32, 28), INK, 6, OTTER, 0.6),                        # head
        (ell(cx - s * 120, 262, 18, 12), INK, 4, BELLY, 0.3),                        # muzzle
        (f'M{cx - s*132} 244 q 6 6 12 0', INK, 4, None, 0.1),                         # closed eye
        (f'M{cx + s*104} 272 q {s*40} 10 {s*60} -14', INK, 10, None, 0.3),            # tail
    ]
to = cue('otters', 0, 'otters')
pg.draw(G(otter(300, False), 0, 0), to - 0.1, 0.8)
pg.draw(G(otter(640, True), 0, 0), to + 0.5, 0.8)
th = cue('otters', 0, 'hold')
pg.draw(G([('M380 240 Q 470 200 560 240', OTTER, 14, None, 1), (ell(470, 222, 16, 12), INK, 4, OTTER, 0.4)], 0, 0), th, 0.4)
tz = cue('otters', 0, 'sleep')
pg.text('z', 170, 190, 40, BLUE, at=tz + 0.1, pop=False)
pg.text('z', 196, 160, 50, BLUE, at=tz + 0.25, pop=False)
pg.text('Z', 228, 124, 62, BLUE, at=tz + 0.4, pop=False)
pg.draw(G([('M680 110 L 910 110 L 910 170 L 680 170 Z', INK, 4, WHITE, 1), ('M795 170 L 795 200', BROWN, 6, None, 0.2)], 0, 0), cue('otters', 0, 'drift'), 0.4)
pg.text('DO NOT DISTURB', 795, 150, 22, RED, at=cue('otters', 0, 'drift') + 0.35, pop=False)
heart = 'M470 150 C 440 110, 400 140, 470 190 C 540 140, 500 110, 470 150 Z'
popin(pg, heart, INK, 4, RED, cue('otters', 1, 'cuter'))
pg.text('awww', 470, 100, 40, PURPLE, at=cue('otters', 1, 'family'), rot=-4)

# ---------------------------------------------------------------- page 3: Alaska is the most western and eastern state
pg, S = fact_page(3, 'alaska', 'FACT #3', 'ALASKA IS THE MOST WESTERN AND', 'MOST EASTERN U.S. STATE', cue('alaska', 0, 'alaska'), cue('alaska', 0, 'eastern'))
LAND = '#9ccc65'; SEA = '#cfe6f7'
pg.draw(G([('M40 90 L 900 90 L 900 404 L 40 404 Z', INK, 5, SEA, 1)], 0, 0), S + 0.05, 0.4)
ak = 'M520 140 L 640 120 L 760 130 L 760 330 L 720 300 L 690 330 L 650 300 L 600 320 L 560 300 L 540 260 L 500 240 L 510 190 Z'
ta = cue('alaska', 0, 'alaska')
pg.draw(G([(ak, INK, 6, LAND, 1), ('M760 330 L 800 370 L 790 380 L 750 340', INK, 5, LAND, 0.3)], 0, 0), ta, 0.8)
pg.text('ALASKA', 640, 230, 40, INK, at=ta + 0.6, pop=False)
tdl = cue('alaska', 1, 'line')
pg.draw(G([('M300 96 L 300 400', RED, 6, None, 1)], 0, 0), cue('alaska', 0, 'western') - 0.1, 0.4)
pg.text('180°', 345, 136, 32, RED, at=cue('alaska', 0, 'western') + 0.2, rot=0, pop=False)
pg.text('<- EAST', 170, 200, 34, BLUE, at=cue('alaska', 0, 'eastern') + 0.1, rot=0, pop=False)
pg.text('WEST ->', 420, 200, 34, BLUE, at=cue('alaska', 0, 'western') + 0.3, rot=0, pop=False)
ti = cue('alaska', 1, 'islands')
for k, (x, y) in enumerate([(480, 300), (430, 322), (380, 338), (330, 350), (276, 360), (220, 366)]):
    popin(pg, ell(x, y, 14, 9), INK, 3, LAND, ti + 0.07 * k)
pg.text('?!', 110, 330, 64, PURPLE, at=cue('alaska', 1, 'map'), rot=-10)

# ---------------------------------------------------------------- page 4: can't hum with nose pinched
pg, S = fact_page(4, 'hum', 'FACT #4', "YOU CAN'T KEEP HUMMING", 'WITH YOUR NOSE PINCHED', cue('hum', 0, 'humming'), cue('hum', 0, 'pinched'))
face = G([
    (ell(400, 240, 120, 140), INK, 6, SKIN, 1),
    ('M350 210 l 0 1 M450 210 l 0 1', INK, 12, None, 0.1),
    ('M370 316 L 430 316', INK, 6, None, 0.2),                                       # sealed lips
    ('M400 220 Q 384 262 404 274', INK, 5, None, 0.2),                               # nose
], 0, 0)
pg.draw(face, S + 0.05, 0.9)
tm = cue('hum', 0, 'humming')
for k, (x, y) in enumerate([(600, 150), (680, 210), (760, 140)]):
    popin(pg, ell(x, y + 40, 16, 12) + f' M{x+16} {y+40} L {x+16} {y-10} l 18 8', INK, 5, INK, tm + 0.12 * k)
tp = cue('hum', 0, 'pinched')
pg.draw(G([('M300 380 Q 330 300 386 262 M420 262 Q 470 300 500 380', SKIN, 22, None, 1),
           ('M300 380 Q 330 300 386 262 M420 262 Q 470 300 500 380', INK, 4, None, 0.6)], 0, 0), tp - 0.3, 0.4)
pg.draw(G([('M570 110 L 820 270 M820 110 L 570 270', RED, 12, None, 1)], 0, 0), tp + 0.3, 0.3)
tt = cue('hum', 1, 'try')
popin(pg, ell(310, 280, 28, 18), INK, 3, '#f59a8a', tt)                              # puffed red cheeks
popin(pg, ell(490, 280, 28, 18), INK, 3, '#f59a8a', tt + 0.08)
pg.text('TRY IT', 160, 160, 52, GREEN, at=tt, rot=-8)
tb = cue('hum', 1, 'bastard')
popin(pg, 'M540 300 q 14 24 0 32 q -14 -8 0 -32 Z', INK, 3, '#7fd3ff', tb)          # sweat drops
popin(pg, 'M560 240 q 12 20 0 26 q -12 -6 0 -26 Z', INK, 3, '#7fd3ff', tb + 0.1)
pg.text('mmmMMF—', 720, 360, 40, PURPLE, at=tb + 0.2, rot=-4, pop=False)

# ---------------------------------------------------------------- page 5: outro
pg = Page(5); S = SEC['outro']['start']
pg.text('HOMEWORK:', PW/2, 150, 96, BLUE, at=cue('outro', 0, 'class'), rot=-2)
s1, _ = fit('WHEN DID FRANCE', 840, 150)
pg.text('WHEN DID FRANCE', PW/2, 310, s1, RED, at=cue('outro', 1, 'when'), rot=-1.5)
s2, _ = fit('DROP THE BLADE?', 820, 150)
pg.text('DROP THE BLADE?', PW/2, 458, s2, RED, at=cue('outro', 1, 'guillotine'), rot=1)
u = pg.path(squiggle(170, 780, 492, 9, 8), RED, 9)
tc = cue('outro', 1, 'comment')
op('set', '#'+u, tc, {'opacity': 1}); op('to', '#'+u, tc, {'strokeDashoffset': 0, 'duration': 0.3, 'ease': 'none'})
pg.text('answer in the comments', PW/2, 596, 52, GREEN, at=tc + 0.1, rot=-1)
greg.append((cue('outro', 1, 'guillotine'), 'tap', (PX + 270, PY + 478)))
pages.append((pg, 'outro'))
