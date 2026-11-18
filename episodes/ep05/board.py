# Episode 5 boards. Runs inside engine/build.py (exec), so it uses the engine's helpers:
# Page, fact_page, G, GX, ell, squiggle, cue, op, sfx, greg, pages, SEC, fit and the colour constants.
def popin(pg, d, color, w, fill, t, tr=''):
    i = pg.path(d, color, w, fill, tr)
    op('set', '#'+i, t, {'opacity': 1, 'strokeDashoffset': 0, 'fillOpacity': 1})
    op('fromTo', '#'+i, t, {'scale': 1, 'duration': 0.28, 'ease': 'back.out(3)'}, {'scale': 0.2, 'transformOrigin': '50% 50%'})
    return i

def drop(x, y):
    return f'M{x} {y} q 8 18 0 26 q -8 -8 0 -26 Z'

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
pg.text('(100% true. 0% useful.)', PW/2, 602, 50, GREEN, at=cue('intro', 0, 'sit'), rot=-1)
greg.append((cue('intro', 0, 'bunnies'), 'tap', (PX + 300, PY + 500)))
pages.append((pg, 'intro'))

# ---------------------------------------------------------------- page 1: Napoleon vs rabbits
pg, S = fact_page(1, 'rabbits', 'FACT #1', 'NAPOLEON GOT SWARMED BY', 'RABBITS AT A HUNT (1807)', cue('rabbits', 0, 'napoleon'), cue('rabbits', 0, 'rabbit'))
FUR = '#d9d4cc'
def rabbit(x, y, s):
    return GX([
        (ell(0, 0, 46, 34), INK, 6, FUR, 1),                                      # body
        (ell(42, -30, 26, 22), INK, 6, FUR, 0.6),                                 # head
        ('M34 -48 C 26 -90, 40 -96, 44 -50 M50 -48 C 54 -92, 70 -90, 58 -46', INK, 6, FUR, 0.6),   # ears
        ('M40 -40 l 12 6 M62 -40 l -8 6', RED, 5, None, 0.2),                    # angry brows
        ('M48 -26 l 0 1', INK, 8, None, 0.1),
        ('M-46 -6 l -8 0', INK, 10, None, 0.1),                                   # tail
        ('M-20 30 l -12 10 M20 30 l 14 10', INK, 6, None, 0.2),
    ], x, y, s, s)
tn = cue('rabbits', 0, 'napoleon')
nap = G([
    ('M712 250 L 700 380 L 820 380 L 808 250 Z', INK, 6, '#2d4fa8', 1.2),             # blue coat
    ('M736 250 L 760 300 L 784 250', AMBER, 5, None, 0.3),
    (ell(760, 212, 38), INK, 6, '#ffd9b3', 1),                                       # face
    ('M690 186 Q 760 106 830 186 Q 760 168 690 186 Z', INK, 6, '#1f1f24', 1),       # bicorne
    (ell(746, 210, 7) + ' ' + ell(776, 210, 7), INK, 4, WHITE, 0.3),               # wide eyes
    (ell(761, 236, 9, 11), INK, 5, '#3a1e1e', 0.2),                                  # screaming mouth
], 0, 0)
pg.draw(nap, S + 0.05, max(tn - S + 0.3, 1.0))
tr0 = cue('rabbits', 0, 'rabbit')
for k, (x, y, s) in enumerate([(120, 330, 1.0), (250, 300, 0.85), (90, 210, 0.75), (370, 330, 1.05), (220, 190, 0.7)]):
    pg.draw(rabbit(x, y, s), tr0 + 0.12 * k, 0.4)
tc = cue('rabbits', 0, 'charged')
pg.draw(G([('M470 270 L 640 270 M450 310 L 630 310 M480 230 L 600 230', INK, 5, None, 1)], 0, 0), tc, 0.3)
pg.text('CHARGE!', 330, 104, 50, RED, at=tc + 0.1, rot=-6)
popin(pg, drop(820, 200), BLUE, 3, '#9cc7f2', tc + 0.3)
popin(pg, drop(700, 196), BLUE, 3, '#9cc7f2', tc + 0.4)
tran = cue('rabbits', 1, 'ran')
pg.text('RETREAT!!', 760, 94, 44, PURPLE, at=tran, rot=4)
temp = cue('rabbits', 1, 'emperor')
pg.draw(G([('M840 330 L 840 200', BROWN, 7, None, 0.5)], 0, 0), temp - 0.1, 0.2)
popin(pg, 'M840 200 L 900 212 L 846 236 Z', INK, 4, WHITE, temp + 0.1)          # white flag

# ---------------------------------------------------------------- page 2: shrimp heart in head
pg, S = fact_page(2, 'shrimp', 'FACT #2', "A SHRIMP'S HEART IS", 'IN ITS HEAD', cue('shrimp', 0, 'heart'), cue('shrimp', 0, 'head'))
PINK = '#f59a8a'
shrimp = G([
    ('M360 352 l -40 30 l 12 -46 Z M360 352 l 30 32 l -2 -48 Z', INK, 5, PINK, 0.4),  # tail fan
    (ell(368, 312, 34), INK, 6, PINK, 0.4),
    (ell(400, 258, 40), INK, 6, PINK, 0.4),
    (ell(392, 196, 44), INK, 6, PINK, 0.4),
    (ell(256, 190, 96, 64), INK, 7, PINK, 1.2),                                      # big head
    ('M172 160 C 120 110, 80 100, 40 120 M178 150 C 140 90, 100 80, 60 84', INK, 4, None, 0.5),  # antennae
    ('M196 168 l 0 1', INK, 12, None, 0.1),                                          # eye
    ('M220 246 l -10 30 M250 252 l -4 30 M280 250 l 4 30', INK, 5, None, 0.3),     # legs
], 0, 0)
th = cue('shrimp', 0, 'heart')
pg.draw(shrimp, S + 0.05, max(th - S, 1.0))
HEART = lambda x, y, s: f'M{x} {y+8*s} C {x-22*s} {y-8*s}, {x-14*s} {y-26*s}, {x} {y-14*s} C {x+14*s} {y-26*s}, {x+22*s} {y-8*s}, {x} {y+8*s} Z'
popin(pg, HEART(266, 200, 1.4), INK, 4, RED, th + 0.2)
thd = cue('shrimp', 0, 'head')
pg.draw(G([('M300 104 Q 280 130 270 162 M270 162 l -2 -22 M270 162 l 18 -12', RED, 5, None, 1)], 0, 0), thd, 0.3)
pg.text('HEART HERE?!', 400, 96, 40, RED, at=thd + 0.2, rot=-4)
tt = cue('shrimp', 1, 'thinks')
bub = G([
    (ell(480, 200, 10) + ' ' + ell(510, 168, 15), INK, 4, WHITE, 0.3),
    ('M560 150 C 540 80, 650 60, 680 100 C 720 60, 840 80, 820 150 C 880 190, 820 270, 760 250 C 720 300, 600 290, 600 250 C 530 260, 520 180, 560 150 Z', INK, 6, WHITE, 1),
], 0, 0)
pg.draw(bub, tt - 0.1, 0.6)
popin(pg, HEART(690, 180, 2.4), INK, 4, RED, cue('shrimp', 1, 'feelings'))
pg.text('feelings', 690, 360, 40, PURPLE, at=cue('shrimp', 1, 'feelings') + 0.3, rot=-3)
pg.text('ugh.', 860, 330, 40, INK, at=cue('shrimp', 1, 'bitch'), rot=6, pop=False)

# ---------------------------------------------------------------- page 3: Eiffel Tower grows in summer
pg, S = fact_page(3, 'eiffel', 'FACT #3', 'THE EIFFEL TOWER GROWS ~15 CM', 'IN THE SUMMER HEAT', cue('eiffel', 0, 'eiffel'), cue('eiffel', 0, 'summer'))
IRON = '#9a6a3a'
tower = G([
    ('M260 92 L 272 160 L 300 250 L 352 384 L 306 384 Q 260 316 214 384 L 168 384 L 220 250 L 248 160 Z', INK, 6, IRON, 2),
    ('M238 196 L 282 196 M216 252 L 304 252', INK, 6, None, 0.4),
    ('M248 160 L 280 250 M272 160 L 240 250 M228 256 L 300 330 M292 256 L 220 330', '#c79a5e', 3, None, 0.6),
    ('M260 92 L 260 70', INK, 5, None, 0.1),
], 0, 0)
te = cue('eiffel', 0, 'eiffel')
pg.draw(tower, S + 0.05, max(te - S + 0.6, 1.0))
tf = cue('eiffel', 0, 'fifteen')
pg.draw(G([('M400 380 L 400 74 M388 92 l 12 -18 l 12 18', RED, 6, None, 1), ('M260 70 L 420 70', RED, 3, None, 0.4)], 0, 0), tf, 0.4)
pg.text('+15 CM', 500, 120, 46, RED, at=tf + 0.3, rot=-4)
ts = cue('eiffel', 0, 'summer')
sun = G([
    (ell(720, 210, 66), INK, 6, AMBER, 1.2),
    ('M720 120 l 0 -26 M720 300 l 0 26 M630 210 l -26 0 M810 210 l 26 0 M656 146 l -16 -16 M784 146 l 16 -16 M656 274 l -16 16 M784 274 l 16 16', AMBER, 7, None, 0.8),
    (ell(696, 200, 22, 14) + ' ' + ell(744, 200, 22, 14), INK, 4, INK, 0.4), ('M718 198 L 722 198', INK, 5, None, 0.1),  # sunglasses
    ('M700 236 Q 720 252 740 236', INK, 5, None, 0.2),
], 0, 0)
pg.draw(sun, ts - 0.2, 0.7)
thot = cue('eiffel', 1, 'hot')
therm = G([
    ('M870 120 L 870 320', INK, 26, None, 0.6), ('M870 120 L 870 320', WHITE, 14, None, 0.1),
    (ell(870, 344, 24), INK, 5, RED, 0.4),
], 0, 0)
pg.draw(therm, thot - 0.1, 0.5)
mer = pg.path('M870 336 L 870 140', RED, 12)
op('set', '#'+mer, thot + 0.4, {'opacity': 1}); op('to', '#'+mer, thot + 0.4, {'strokeDashoffset': 0, 'duration': 0.6, 'ease': 'none'})
pg.text('IRON EXPANDS', 620, 392, 38, BLUE, at=cue('eiffel', 1, 'expands'), rot=-2, pop=False)
tp = cue('eiffel', 1, 'puberty')
for k, (x, y) in enumerate([(250, 230), (282, 290), (232, 330)]):
    popin(pg, ell(x, y, 8), INK, 3, '#ff6f6f', tp + 0.08 * k)                     # zits on the tower
pg.text('NOT PUBERTY', 520, 300, 30, PURPLE, at=tp + 0.2, rot=-6)

# ---------------------------------------------------------------- page 4: Oxford older than the Aztec Empire
pg, S = fact_page(4, 'oxford', 'FACT #4', 'OXFORD UNIVERSITY IS OLDER', 'THAN THE AZTEC EMPIRE', cue('oxford', 0, 'oxford'), cue('oxford', 0, 'aztec'))
STONE = '#e3d3a8'
uni = G([
    ('M70 300 L 70 190 L 290 190 L 290 300 Z', INK, 6, STONE, 1.4),
    ('M150 190 L 150 110 L 180 70 L 210 110 L 210 190 Z', INK, 6, STONE, 0.8),     # tower
    ('M100 220 l 0 40 a 12 12 0 0 1 24 0 l 0 -40 M236 220 l 0 40 a 12 12 0 0 1 24 0 l 0 -40', INK, 4, None, 0.4),
    ('M166 140 l 0 30 a 14 14 0 0 1 28 0 l 0 -30', INK, 4, None, 0.3),
    ('M160 300 l 0 -44 a 20 20 0 0 1 40 0 l 0 44', INK, 5, '#6b4a2b', 0.4),        # door
], 0, 0)
to = cue('oxford', 0, 'oxford')
pg.draw(uni, S + 0.05, max(to - S + 0.5, 1.0))
line = G([('M30 336 L 910 336', INK, 6, None, 1)], 0, 0)
pg.draw(line, to + 0.5, 0.4)
pg.text('1096', 180, 388, 34, INK, at=to + 0.7, pop=False)
pg.text('(teaching)', 180, 426, 26, BLUE, at=to + 0.8, pop=False)
ta = cue('oxford', 0, 'aztec')
pg.text('1325', 720, 388, 34, INK, at=ta, pop=False)
pg.text('(Tenochtitlan)', 720, 426, 26, GREEN, at=ta + 0.1, pop=False)
pg.draw(G([('M300 176 Q 500 90 690 160 M690 160 l -4 -26 M690 160 l -26 -2', RED, 6, None, 1)], 0, 0), ta + 0.3, 0.4)
pg.text('229 YRS', 500, 104, 40, RED, at=ta + 0.6, rot=-3)
tst = cue('oxford', 1, 'students')
stu = G([
    (ell(380, 244, 30), INK, 6, '#ffd9b3', 0.8),
    ('M346 222 L 380 206 L 414 222 L 380 236 Z', INK, 5, INK, 0.4),                 # mortarboard
    ('M414 222 l 6 22', AMBER, 4, None, 0.1),
    ('M364 244 l 12 0 M386 244 l 12 0', INK, 5, None, 0.1),                          # half-closed eyes
    ('M370 262 Q 380 256 390 262', INK, 4, None, 0.1),
    ('M380 274 L 380 330', INK, 8, None, 0.4),
], 0, 0)
pg.draw(stu, tst, 0.6)
pg.text('Zzz', 440, 200, 40, PURPLE, at=cue('oxford', 1, 'hungover'), rot=-10, pop=False)
popin(pg, 'M410 290 L 446 290 L 442 326 L 414 326 Z M446 298 q 14 4 0 18', INK, 4, '#b07a4a', cue('oxford', 1, 'hungover') + 0.2)  # coffee
tsh = cue('oxford', 1, 'showed')
temple = G([
    ('M600 320 L 840 320 L 820 280 L 620 280 Z', INK, 6, '#c9b07a', 1),
    ('M630 280 L 810 280 L 792 240 L 648 240 Z', INK, 6, '#c9b07a', 0.8),
    ('M658 240 L 782 240 L 766 200 L 674 200 Z', INK, 6, '#c9b07a', 0.6),
    ('M686 200 L 754 200 L 754 160 L 686 160 Z', INK, 6, RED, 0.4),
    ('M700 320 L 700 200 M740 320 L 740 200', '#8a6a3a', 4, None, 0.3),
], 0, 0)
pg.draw(temple, tsh - 0.3, 0.7)
pg.text('late.', 860, 160, 40, GREEN, at=cue('oxford', 1, 'shit'), rot=8)

# ---------------------------------------------------------------- page 5: outro
pg = Page(5); S = SEC['outro']['start']
pg.text('HOMEWORK:', PW/2, 150, 96, BLUE, at=cue('outro', 0, 'class'), rot=-2)
th1 = cue('outro', 1, 'who')
pg.text('WHO BEAT', PW/2, 310, 150, RED, at=th1, rot=-1.5)
s2, _ = fit('NAPOLEON?', 820, 150)
pg.text('NAPOLEON?', PW/2, 458, s2, RED, at=cue('outro', 1, 'napoleon'), rot=1)
u = pg.path(squiggle(170, 780, 492, 9, 8), RED, 9)
tc = cue('outro', 1, 'comment')
op('set', '#'+u, tc, {'opacity': 1}); op('to', '#'+u, tc, {'strokeDashoffset': 0, 'duration': 0.3, 'ease': 'none'})
pg.text('answer in the comments', PW/2, 596, 52, GREEN, at=tc + 0.1, rot=-1)
greg.append((cue('outro', 1, 'napoleon'), 'tap', (PX + 270, PY + 478)))
pages.append((pg, 'outro'))
