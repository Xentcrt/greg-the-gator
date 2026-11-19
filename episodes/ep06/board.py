# Episode 6 boards. Runs inside engine/build.py (exec), so it uses the engine's helpers:
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
pg.text('(100% true. 0% useful.)', PW/2, 602, 50, GREEN, at=cue('intro', 0, 'wrestling'), rot=-1)
greg.append((cue('intro', 0, 'lincoln'), 'tap', (PX + 300, PY + 500)))
pages.append((pg, 'intro'))

# ---------------------------------------------------------------- page 1: Lincoln, wrestling hall of famer
pg, S = fact_page(1, 'lincoln', 'FACT #1', 'ABRAHAM LINCOLN IS IN THE', 'WRESTLING HALL OF FAME', cue('lincoln', 0, 'lincoln'), cue('lincoln', 0, 'wrestling'))
abe = G([
    ('M226 236 L 294 236 L 306 356 L 214 356 Z', INK, 6, RED, 1.2),                  # red singlet
    ('M226 252 Q 170 246 172 196 M294 252 Q 350 246 348 196', INK, 12, None, 0.6),  # flexing arms
    (ell(176, 222, 14, 18) + ' ' + ell(344, 222, 14, 18), INK, 5, SKIN, 0.4),       # biceps
    ('M238 356 l -6 34 M282 356 l 6 34', INK, 10, None, 0.3),
    (ell(260, 192, 38, 42), INK, 6, SKIN, 1),                                        # face
    ('M224 200 Q 260 270 296 200 Q 260 226 224 200 Z', INK, 5, '#2a2a2a', 0.6),      # chin beard
    ('M230 152 L 290 152 L 284 74 L 236 74 Z', INK, 6, '#1f1f24', 0.8),              # top hat
    ('M206 154 L 314 154', INK, 10, None, 0.2),
    ('M246 186 l 0 1 M274 186 l 0 1', INK, 9, None, 0.1),
    ('M238 172 l 14 6 M282 172 l -14 6', INK, 5, None, 0.1),                         # serious brows
], 0, 0)
tl = cue('lincoln', 0, 'lincoln')
pg.draw(abe, S + 0.05, max(tl - S + 0.6, 1.0))
tw = cue('lincoln', 0, 'wrestled')
dude = G([
    (ell(690, 372, 120, 18), INK, 6, '#7fb2e5', 1),                                  # flattened opponent
    (ell(552, 364, 24), INK, 6, SKIN, 0.5),
    ('M540 356 l 10 10 M550 356 l -10 10 M556 356 l 10 10 M566 356 l -10 10', INK, 4, None, 0.2),  # X eyes
    ('M800 372 l 30 -6 M800 380 l 30 6', INK, 6, None, 0.2),
], 0, 0)
pg.draw(dude, tw, 0.5)
pg.text('PINNED.', 690, 300, 44, RED, at=tw + 0.5, rot=-5)
th = cue('lincoln', 0, 'hall')
popin(pg, 'M420 190 L 600 190 L 600 222 L 420 222 Z', INK, 5, BROWN, th)           # champ belt
popin(pg, ell(510, 206, 40, 32), INK, 5, AMBER, th + 0.1)
pg.text('CHAMP', 510, 140, 40, AMBER, at=th + 0.25, rot=-4)
tf = cue('lincoln', 1, 'four')
pg.text('4 score + 7 slams', 740, 104, 34, PURPLE, at=tf, rot=4)
tb = cue('lincoln', 1, 'bitch')
for k, (x, y) in enumerate([(530, 320), (580, 304), (630, 322)]):
    popin(pg, star(x, y, 14), INK, 3, AMBER, tb + 0.08 * k)

# ---------------------------------------------------------------- page 2: butterflies taste with their feet
pg, S = fact_page(2, 'butterfly', 'FACT #2', 'BUTTERFLIES TASTE WITH', 'THEIR FEET', cue('butterfly', 0, 'butterflies'), cue('butterfly', 0, 'feet'))
BREAD = '#e8c27a'
sandwich = G([
    ('M280 384 L 660 384 L 660 356 L 280 356 Z', INK, 6, BREAD, 1),
    ('M272 356 q 24 -18 48 0 q 24 -18 48 0 q 24 -18 48 0 q 24 -18 48 0 q 24 -18 48 0 q 24 -18 48 0 q 24 -18 48 0 q 24 -18 48 0 Z', INK, 5, '#5cb85c', 0.8),
    ('M290 340 L 650 340 L 620 360 L 320 360 Z', INK, 5, AMBER, 0.6),                # cheese
    ('M280 336 Q 470 270 660 336 Z', INK, 6, BREAD, 1),                              # top bread
], 0, 0)
pg.draw(sandwich, S + 0.05, 0.9)
fly = G([
    ('M466 196 C 380 100, 300 140, 340 210 C 360 250, 440 240, 466 214 Z', INK, 6, PURPLE, 1),
    ('M474 196 C 560 100, 640 140, 600 210 C 580 250, 500 240, 474 214 Z', INK, 6, PURPLE, 1),
    ('M466 220 C 410 240, 400 290, 450 280 Z M474 220 C 530 240, 540 290, 490 280 Z', INK, 5, AMBER, 0.6),
    (ell(470, 222, 10, 46), INK, 5, INK, 0.4),                                       # body
    ('M466 178 Q 450 130 430 120 M474 178 Q 490 130 510 120', INK, 4, None, 0.3),   # antennae
    ('M462 262 l -16 40 M478 262 l 16 40', INK, 4, None, 0.2),                       # legs
], 0, 0)
tb0 = cue('butterfly', 0, 'butterflies')
pg.draw(fly, tb0 + 0.3, 1.0)
tft = cue('butterfly', 0, 'feet')
pg.draw(G([('M720 200 Q 600 230 510 296 M510 296 l 22 -4 M510 296 l 4 -22', RED, 6, None, 1)], 0, 0), tft, 0.35)
pg.text('TASTE BUDS', 790, 170, 40, RED, at=tft + 0.2, rot=-4)
tlk = cue('butterfly', 1, 'lick')
pg.text('*slurp*', 160, 280, 44, PURPLE, at=tlk, rot=-8)
ttoe = cue('butterfly', 1, 'toes')
popin(pg, ell(442, 304, 14, 7), INK, 3, RED, ttoe)                                   # tiny sneakers
popin(pg, ell(498, 304, 14, 7), INK, 3, RED, ttoe + 0.08)
pg.text('ew.', 800, 300, 44, GREEN, at=ttoe + 0.3, rot=6, pop=False)

# ---------------------------------------------------------------- page 3: Hawaiian pizza is Canadian
pg, S = fact_page(3, 'pizza', 'FACT #3', 'HAWAIIAN PIZZA WAS INVENTED', 'IN CANADA (1962)', cue('pizza', 0, 'hawaiian'), cue('pizza', 0, 'canada'))
slice_ = G([
    ('M90 130 L 350 170 L 170 390 Z', INK, 6, '#f2c14e', 1.4),
    ('M90 130 L 350 170', BROWN, 16, None, 0.4),                                     # crust
    ('M130 170 l 0 1 M220 230 l 0 1 M170 300 l 0 1', '#d9534f', 20, None, 0.2),     # sauce spots
], 0, 0)
tp0 = cue('pizza', 0, 'hawaiian')
pg.draw(slice_, S + 0.05, max(tp0 - S + 0.5, 1.0))
tpz = cue('pizza', 0, 'pizza')
for k, (x, y) in enumerate([(160, 190), (250, 200), (200, 260), (180, 330)]):
    popin(pg, f'M{x-14} {y-14} L {x+14} {y-14} L {x+14} {y+14} L {x-14} {y+14} Z', INK, 4, '#ffe066', tpz + 0.1 * k)   # pineapple
for k, (x, y) in enumerate([(130, 158), (270, 240), (220, 160)]):
    popin(pg, ell(x, y, 14), INK, 4, '#f59a8a', tpz + 0.05 + 0.1 * k)                                    # ham
tc = cue('pizza', 0, 'canada')
leaf = 'M710 150 l 12 24 l 16 -8 l -4 34 l 22 -20 l 6 14 l 20 -4 l -8 24 l 12 8 l -36 26 l 6 18 l -34 -6 l 0 34 l -12 0 l 0 -34 l -34 6 l 6 -18 l -36 -26 l 12 -8 l -8 -24 l 20 4 l 6 -14 l 22 20 l -4 -34 l 16 8 Z'
flag = G([
    ('M560 110 L 860 110 L 860 300 L 560 300 Z', INK, 6, WHITE, 1),
    ('M560 110 L 635 110 L 635 300 L 560 300 Z M785 110 L 860 110 L 860 300 L 785 300 Z', INK, 5, RED, 0.6),
    (leaf, INK, 4, RED, 0.8),
    ('M560 110 L 560 400', BROWN, 8, None, 0.3),
], 0, 0)
pg.draw(flag, tc - 0.1, 0.8)
pg.text('EH?', 860, 360, 44, RED, at=tc + 0.7, rot=6)
th1 = cue('pizza', 1, 'hawaii')
palm = G([
    ('M450 394 Q 440 320 462 250', BROWN, 12, None, 0.6),
    ('M462 250 Q 420 220 380 250 Q 420 236 462 250 Z M462 250 Q 500 214 548 240 Q 500 232 462 250 Z M462 250 Q 470 200 440 180 Q 470 200 462 250 Z', INK, 4, '#5cb85c', 0.8),
], 0, 0)
pg.draw(palm, th1, 0.5)
tn = cue('pizza', 1, 'nothing')
pg.draw(G([('M400 220 L 520 392 M520 220 L 400 392', RED, 10, None, 1)], 0, 0), tn, 0.3)
pg.text('NOPE', 460, 104, 44, RED, at=tn + 0.3, rot=-5)

# ---------------------------------------------------------------- page 4: humans glow
pg, S = fact_page(4, 'glow', 'FACT #4', 'HUMANS GLOW IN THE DARK,', '~1000x TOO FAINT TO SEE', cue('glow', 0, 'humans'), cue('glow', 0, 'thousand'))
NIGHT = '#1d2340'; GLOW = '#fff3a0'
pg.draw(G([('M40 84 L 900 84 L 900 404 L 40 404 Z', INK, 6, NIGHT, 1)], 0, 0), S + 0.05, 0.5)
popin(pg, 'M800 112 A 36 36 0 1 0 836 168 A 28 28 0 1 1 800 112 Z', GLOW, 4, GLOW, S + 0.5)   # moon
for k, (x, y) in enumerate([(120, 130), (220, 170), (640, 120), (700, 200)]):
    popin(pg, star(x, y, 9), GLOW, 2, GLOW, S + 0.6 + 0.07 * k)
tg = cue('glow', 0, 'glow')
person = G([
    (ell(420, 160, 26), INK, 5, SKIN, 0.5),
    ('M420 186 L 420 290 M420 214 L 380 260 M420 214 L 460 260 M420 290 L 390 370 M420 290 L 450 370', WHITE, 7, None, 0.8),
], 0, 0)
pg.draw(person, tg - 0.3, 0.6)
halo = pg.path(ell(420, 260, 92, 140), GLOW, 3)
op('set', '#'+halo, tg + 0.2, {'opacity': 0.35}); op('to', '#'+halo, tg + 0.2, {'strokeDashoffset': 0, 'duration': 0.5, 'ease': 'none'})
pg.text('glow', 560, 150, 36, GLOW, at=tg + 0.3, rot=-6, pop=False)
tt = cue('glow', 0, 'thousand')
pg.text('(barely.)', 610, 210, 32, GLOW, at=tt + 0.3, rot=-3, pop=False)
tnl = cue('glow', 1, 'nightlight')
pg.draw(G([('M440 330 Q 620 400 830 330', WHITE, 4, None, 0.7), ('M828 300 L 880 300 L 880 360 L 828 360 Z', INK, 4, WHITE, 0.3)], 0, 0), tnl - 0.2, 0.5)
pg.text('NIGHTLIGHT', 200, 300, 34, AMBER, at=tnl, rot=-6)
tbs = cue('glow', 1, 'bastard')
popin(pg, 'M130 196 L 230 196 L 230 240 L 130 240 Z M230 208 l 10 0 l 0 20 l -10 0', WHITE, 4, None, tbs)      # dead battery
popin(pg, 'M136 202 L 150 202 L 150 234 L 136 234 Z', RED, 2, RED, tbs + 0.1)

# ---------------------------------------------------------------- page 5: outro
pg = Page(5); S = SEC['outro']['start']
pg.text('HOMEWORK:', PW/2, 150, 96, BLUE, at=cue('outro', 0, 'class'), rot=-2)
s1, _ = fit('WHICH PRESIDENT', 840, 150)
pg.text('WHICH PRESIDENT', PW/2, 310, s1, RED, at=cue('outro', 1, 'which'), rot=-1.5)
s2, _ = fit('WRESTLED?', 820, 150)
pg.text('WRESTLED?', PW/2, 458, s2, RED, at=cue('outro', 1, 'wrestled'), rot=1)
u = pg.path(squiggle(170, 780, 492, 9, 8), RED, 9)
tc = cue('outro', 1, 'comment')
op('set', '#'+u, tc, {'opacity': 1}); op('to', '#'+u, tc, {'strokeDashoffset': 0, 'duration': 0.3, 'ease': 'none'})
pg.text('answer in the comments', PW/2, 596, 52, GREEN, at=tc + 0.1, rot=-1)
greg.append((cue('outro', 1, 'wrestled'), 'tap', (PX + 270, PY + 478)))
pages.append((pg, 'outro'))
