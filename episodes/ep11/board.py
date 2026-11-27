# Episode 11 boards. Runs inside engine/build.py (exec), so it uses the engine's helpers:
# Page, fact_page, G, GX, ell, squiggle, cue, op, sfx, greg, pages, SEC, fit and the colour constants.
import math

def popin(pg, d, color, w, fill, t, tr=''):
    i = pg.path(d, color, w, fill, tr)
    op('set', '#'+i, t, {'opacity': 1, 'strokeDashoffset': 0, 'fillOpacity': 1})
    op('fromTo', '#'+i, t, {'scale': 1, 'duration': 0.28, 'ease': 'back.out(3)'}, {'scale': 0.2, 'transformOrigin': '50% 50%'})
    return i

SKIN = '#ffd9b3'
MOL = '#5a3210'

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
pg.text('(100% true. 0% useful.)', PW/2, 602, 50, GREEN, at=cue('intro', 0, 'boston'), rot=-1)
greg.append((cue('intro', 0, 'molasses'), 'tap', (PX + 300, PY + 500)))
pages.append((pg, 'intro'))

# ---------------------------------------------------------------- page 1: Boston molasses flood, 1919
pg, S = fact_page(1, 'molasses', 'FACT #1', 'IN 1919 BOSTON WAS HIT BY', 'A WAVE OF MOLASSES', cue('molasses', 0, 'boston'), cue('molasses', 0, 'molasses'))
tt = cue('molasses', 0, 'tank')
tank = G([('M70 160 L 210 160 L 210 390 L 70 390 Z', INK, 6, '#b9c2cc', 1),
          (ell(140, 160, 70, 18), INK, 6, '#d8dde3', 0.4),
          ('M70 230 L 210 230 M70 310 L 210 310', INK, 3, None, 0.2)], 0, 0)
pg.draw(tank, S + 0.05, 0.8)
house = G([('M700 300 L 760 250 L 820 300 L 820 390 L 700 390 Z', INK, 5, '#f4d9a8', 1),
           ('M730 330 L 760 330 L 760 360 L 730 360 Z', INK, 4, '#bfe3ff', 0.2),
           ('M840 330 L 900 330 L 900 390 L 840 390 Z M840 330 L 870 300 L 900 330', INK, 5, '#f7c1c1', 0.6)], 0, 0)
pg.draw(house, tt, 0.6)
tb = cue('molasses', 0, 'burst')
popin(pg, 'M150 190 l -14 30 l 18 20 l -16 30 l 14 26', RED, 6, None, tb)                        # crack
popin(pg, 'M80 120 l -24 -24 M140 112 l 0 -30 M200 120 l 24 -24', RED, 6, None, tb + 0.08)       # boom lines
tw = cue('molasses', 0, 'wave')
popin(pg, 'M210 390 L 210 330 C 260 300, 300 170, 420 160 C 520 150, 580 230, 540 262 '
          'C 600 236, 640 300, 700 330 L 900 360 L 900 396 L 210 396 Z', INK, 6, MOL, tw)          # molasses wave
popin(pg, 'M560 262 q -40 -30 -10 -60', '#a9672a', 5, None, tw + 0.15)                            # shine curl
tm = cue('molasses', 0, 'molasses')
pancakes = G([(ell(370, 128, 60, 12), INK, 5, '#e8b25e', 0.3), (ell(370, 112, 60, 12), INK, 5, '#e8b25e', 0.3),
              (ell(370, 96, 60, 12), INK, 5, '#e8b25e', 0.3), ('M340 92 l 0 1 M398 92 l 0 1', INK, 9, None, 0.1),
              ('M356 100 q 14 10 28 0', INK, 3, None, 0.1)], 0, 0)
pg.draw(pancakes, tm + 0.1, 0.5)                                                                  # pancakes riding the wave
pg.text('finally.', 520, 100, 36, PURPLE, at=tm + 0.5, rot=-6, pop=False)
ts = cue('molasses', 1, 'thirty')
pg.text('35 MPH', 760, 140, 56, RED, at=ts, rot=-5)
popin(pg, 'M600 200 l -60 0 M610 224 l -80 0 M600 248 l -60 0', RED, 5, None, ts + 0.15)          # speed lines
tk = cue('molasses', 1, 'sticky')
pg.text('STICKY', 760, 220, 40, MOL, at=tk, rot=6, pop=False)

# ---------------------------------------------------------------- page 2: crows remember faces and hold grudges
pg, S = fact_page(2, 'crows', 'FACT #2', 'CROWS REMEMBER HUMAN FACES', 'AND HOLD GRUDGES', cue('crows', 0, 'crows'), cue('crows', 0, 'grudge'))
tc = cue('crows', 0, 'crows')
CROW = '#2a2a33'
crow = G([('M600 380 L 900 380', '#7a4b22', 12, None, 0.3),                                       # branch
          (ell(720, 300, 70, 56), INK, 6, CROW, 1),
          ('M770 290 L 860 340 L 780 330 Z', INK, 5, CROW, 0.3),                                   # tail
          (ell(660, 236, 42, 38), INK, 6, CROW, 0.6),
          ('M624 232 L 584 246 L 626 254 Z', INK, 4, AMBER, 0.2),                                  # beak
          ('M640 214 l 26 10', WHITE, 5, None, 0.1),                                               # angry brow
          ('M652 232 l 0 1', WHITE, 10, None, 0.1),
          ('M700 356 l -6 24 M736 356 l 6 24', AMBER, 6, None, 0.2)], 0, 0)
pg.draw(crow, tc - 0.1, 0.9)
tf = cue('crows', 0, 'face')
poster = G([('M100 110 L 330 110 L 330 390 L 100 390 Z', INK, 6, '#fff4d6', 1),
            (ell(215, 250, 60, 70), INK, 5, SKIN, 0.6),
            ('M180 236 l 0 1 M250 236 l 0 1', INK, 10, None, 0.1),
            ('M196 288 q 19 -10 38 0', INK, 4, None, 0.1)], 0, 0)
pg.draw(poster, tf - 0.2, 0.8)
pg.text('WANTED', 215, 160, 40, RED, at=tf + 0.4, rot=-2, pop=False)
tg = cue('crows', 0, 'grudge')
popin(pg, 'M160 230 L 200 230 M230 230 L 270 230 M200 230 L 230 230', INK, 8, None, tg - 0.3)     # disguise glasses
popin(pg, 'M190 270 q 25 -14 50 0 q -25 8 -50 0 Z', INK, 3, INK, tg - 0.2)                         # fake moustache
pg.text('NICE TRY', 215, 370, 32, PURPLE, at=tg + 0.2, rot=-4, pop=False)
tt = cue('crows', 1, 'teach')
for k, (x, y) in enumerate(((470, 180), (520, 330))):
    popin(pg, f'{ell(x, y, 34, 26)} M{x - 30} {y - 8} l -24 8 l 24 6', INK, 4, CROW, tt + 0.12 * k)
pg.text('HIM.', 840, 170, 50, RED, at=cue('crows', 1, 'hate'), rot=8)
popin(pg, 'M380 250 L 340 250 M356 236 L 338 250 L 356 264', RED, 6, None, cue('crows', 1, 'hate') + 0.1)

# ---------------------------------------------------------------- page 3: Point Nemo
pg, S = fact_page(3, 'nemo', 'FACT #3', 'AT POINT NEMO THE NEAREST HUMANS', 'ARE OFTEN ASTRONAUTS', cue('nemo', 0, 'point'), cue('nemo', 0, 'astronauts'))
SEA = '#9fd3f5'
tp = cue('nemo', 0, 'point')
sea = G([('M20 330 q 40 -20 80 0 t 80 0 t 80 0 t 80 0 t 80 0 t 80 0 t 80 0 t 80 0 t 80 0 t 80 0 t 80 0 L 900 396 L 20 396 Z',
          INK, 5, SEA, 1)], 0, 0)
pg.draw(sea, S + 0.05, 0.7)
popin(pg, 'M300 300 l 30 30 M330 300 l -30 30', RED, 8, None, tp)                                 # X marks the spot
buoy = G([('M420 330 L 440 270 L 460 330 Z', INK, 5, RED, 0.6),
          ('M440 270 L 440 200 M440 200 L 520 200 L 520 240 L 440 240', INK, 5, '#fff4d6', 0.6)], 0, 0)
pg.draw(buoy, tp + 0.3, 0.6)
pg.text('NEAREST', 480, 228, 18, INK, at=tp + 0.8, rot=0, pop=False)
ta = cue('nemo', 0, 'astronauts')
iss = G([('M640 110 L 760 110 L 760 140 L 640 140 Z', INK, 5, '#d8dde3', 1),
         ('M590 96 L 636 96 L 636 154 L 590 154 Z M764 96 L 810 96 L 810 154 L 764 154 Z', INK, 4, BLUE, 1),
         ('M690 140 l 0 1 M710 140 l 0 1', INK, 1, None, 0.1)], 0, 0)
pg.draw(iss, ta - 0.1, 0.7)
popin(pg, 'M520 214 L 620 150 M600 148 L 622 148 L 614 168', RED, 5, None, ta + 0.3)               # sign points up
pg.text('~400 km', 860, 220, 34, RED, at=ta + 0.4, rot=-4)
popin(pg, 'M700 170 L 700 300', RED, 4, None, ta + 0.35)
te = cue('nemo', 1, 'everybody')
pg.text('LAND: ~2,700 km', 200, 160, 34, GREEN, at=te, rot=-4)
popin(pg, 'M290 220 L 40 220 M64 204 L 40 220 L 64 236', GREEN, 5, None, te + 0.1)
pg.text('hello?', 300, 260, 32, PURPLE, at=cue('nemo', 1, 'lonely'), rot=-8, pop=False)

# ---------------------------------------------------------------- page 4: pineapple takes up to 2 years
pg, S = fact_page(4, 'pineapple', 'FACT #4', 'A PINEAPPLE CAN TAKE UP TO', '2 YEARS TO GROW', cue('pineapple', 0, 'pineapple'), cue('pineapple', 0, 'two'))
PINE = '#f5c542'; LEAF = '#3f9b4a'
tp = cue('pineapple', 0, 'pineapple')
pine = G([('M220 160 L 190 90 L 228 140 L 240 80 L 254 140 L 292 92 L 262 162 Z', INK, 5, LEAF, 0.6),  # leaves
          (ell(240, 260, 72, 100), INK, 6, PINE, 1),
          ('M184 210 L 290 330 M200 180 L 306 300 M176 260 L 260 356 M290 200 L 184 320 M300 250 L 210 352 M270 170 L 176 280',
           '#b0801c', 3, None, 0.4),
          ('M222 250 l 0 1 M262 250 l 0 1', INK, 10, None, 0.1)], 0, 0)
pg.draw(pine, tp - 0.1, 0.9)
tu = cue('pineapple', 0, 'two')
popin(pg, 'M212 280 q 28 70 56 0 q -10 30 -28 30 q -18 0 -28 -30 Z', INK, 3, WHITE, tu + 0.2)      # old-man beard
popin(pg, 'M330 390 L 330 250 q 0 -24 24 -24', '#7a4b22', 8, None, tu + 0.3)                       # cane
cal = G([('M560 120 L 760 120 L 760 330 L 560 330 Z', INK, 6, WHITE, 1),
         ('M560 120 L 760 120 L 760 170 L 560 170 Z', INK, 6, RED, 0.4),
         ('M600 104 l 0 30 M720 104 l 0 30', INK, 8, None, 0.2)], 0, 0)
pg.draw(cal, tu - 0.2, 0.6)
pg.text('MONTH', 660, 216, 34, INK, at=tu + 0.2, rot=0, pop=False)
pg.text('24', 660, 300, 76, RED, at=tu + 0.4, rot=-3)
tg = cue('pineapple', 0, 'grow')
pg.text('zzz', 360, 140, 40, BLUE, at=tg, rot=-10, pop=False)
tf = cue('pineapple', 1, 'five')
pg.text('5 MIN', 850, 160, 44, PURPLE, at=tf, rot=8)
popin(pg, 'M800 380 q 50 22 100 0 L 900 372 L 800 372 Z', INK, 5, '#d8dde3', tf + 0.15)           # empty plate
pg.text('RUDE', 850, 310, 40, RED, at=cue('pineapple', 1, 'greedy'), rot=-8)

# ---------------------------------------------------------------- page 5: outro
pg = Page(5); S = SEC['outro']['start']
pg.text('HOMEWORK:', PW/2, 150, 96, BLUE, at=cue('outro', 0, 'class'), rot=-2)
s1, _ = fit('WHAT HIT', 840, 150)
pg.text('WHAT HIT', PW/2, 310, s1, RED, at=cue('outro', 1, 'what'), rot=-1.5)
s2, _ = fit('BOSTON?', 820, 150)
pg.text('BOSTON?', PW/2, 458, s2, RED, at=cue('outro', 1, 'boston'), rot=1)
u = pg.path(squiggle(200, 750, 492, 9, 10), RED, 9)
tc = cue('outro', 1, 'comment')
op('set', '#'+u, tc, {'opacity': 1}); op('to', '#'+u, tc, {'strokeDashoffset': 0, 'duration': 0.3, 'ease': 'none'})
pg.text('answer in the comments', PW/2, 596, 52, GREEN, at=tc + 0.1, rot=-1)
greg.append((cue('outro', 1, 'boston'), 'tap', (PX + 270, PY + 478)))
pages.append((pg, 'outro'))
