# Episode 4 boards. Runs inside engine/build.py (exec), so it uses the engine's helpers:
# Page, fact_page, G, GX, ell, squiggle, cue, op, sfx, greg, pages, SEC, fit and the colour constants.
def popin(pg, d, color, w, fill, t, tr=''):
    i = pg.path(d, color, w, fill, tr)
    op('set', '#'+i, t, {'opacity': 1, 'strokeDashoffset': 0, 'fillOpacity': 1})
    op('fromTo', '#'+i, t, {'scale': 1, 'duration': 0.28, 'ease': 'back.out(3)'}, {'scale': 0.2, 'transformOrigin': '50% 50%'})
    return i

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
greg.append((cue('intro', 0, 'moon'), 'tap', (PX + 300, PY + 500)))
pages.append((pg, 'intro'))

# ---------------------------------------------------------------- page 1: Cleopatra / pyramid / moon
pg, S = fact_page(1, 'cleo', 'FACT #1', 'THE GREAT PYRAMID WAS ~2,500', 'YEARS OLD TO CLEOPATRA', cue('cleo', 0, 'pyramid'), cue('cleo', 0, 'cleopatra'))
SAND = '#f2cf7a'
pyr = G([
    ('M40 322 L 120 182 L 200 322 Z', INK, 7, SAND, 2),
    ('M120 182 L 136 322', '#c79a3c', 5, None, 0.4),
    ('M70 270 L 170 270 M90 236 L 150 236 M56 298 L 186 298', '#c79a3c', 4, None, 0.5),
    # cobwebs = it's OLD
    ('M40 322 L 70 300 M40 322 L 64 290 M40 322 L 52 288 M52 304 Q 58 300 62 294', '#9a9aa6', 3, None, 0.4),
    ('M200 322 L 172 300 M200 322 L 178 290 M200 322 L 190 288 M188 304 Q 182 300 178 294', '#9a9aa6', 3, None, 0.4),
], 0, 0)
pg.draw(pyr, S + 0.05, 1.0)
line = G([('M30 336 L 910 336', INK, 6, None, 1)], 0, 0)
pg.draw(line, S + 1.0, 0.4)
pg.text('2560 BC', 120, 388, 34, INK, at=S + 1.2, pop=False)
tc = cue('cleo', 0, 'cleopatra')
cleo = G([
    ('M478 236 C 470 170, 610 170, 602 236 L 604 322 L 476 322 Z', INK, 6, '#1f1f24', 1.2),       # bob hair
    (ell(540, 256, 46, 52), INK, 6, '#e8b98c', 1.2),                                                # face
    ('M490 214 C 520 196, 560 196, 590 214', AMBER, 9, None, 0.4),                                  # gold band
    ('M540 200 c -8 -14 8 -22 0 -32', GREEN, 6, None, 0.3),                                         # snake
    ('M512 250 l 18 0 l 8 -6 M550 250 l 18 0 l 8 -6', INK, 5, None, 0.3),                            # winged liner
    ('M524 286 Q 540 296 556 286', '#c0302a', 5, None, 0.2),
], 0, 0)
pg.draw(cleo, tc - 0.6, 0.8)
pg.text('69 BC', 540, 388, 34, INK, at=tc, pop=False)
th = cue('cleo', 0, 'hundred')
a1 = G([('M130 164 Q 320 70 500 168 M500 168 l -6 -26 M500 168 l -26 -4', RED, 6, None, 1)], 0, 0)
pg.draw(a1, th, 0.4)
pg.text('2,500 YRS', 320, 104, 40, RED, at=th + 0.3, rot=-3)
ta = cue('cleo', 1, 'ancient')
moon = G([
    (ell(860, 252, 48), INK, 6, '#d6d8de', 1),
    (ell(842, 236, 10) + ' ' + ell(876, 272, 13) + ' ' + ell(870, 228, 6), '#9a9ca6', 4, None, 0.4),
    ('M884 206 L 884 160 L 912 170 L 884 180', INK, 4, RED, 0.4),                                  # tiny flag
], 0, 0)
pg.draw(moon, ta - 0.1, 0.6)
pg.text('1969', 860, 388, 34, INK, at=ta + 0.2, pop=False)
a2 = G([('M580 168 Q 720 90 840 192 M840 192 l 2 -26 M840 192 l -26 -6', GREEN, 6, None, 1)], 0, 0)
pg.draw(a2, ta + 0.4, 0.4)
pg.text('2,000 YRS', 724, 116, 40, GREEN, at=ta + 0.7, rot=3)
popin(pg, 'M600 230 q 8 18 0 26 q -8 -8 0 -26 Z', BLUE, 3, '#9cc7f2', cue('cleo', 1, 'shit'))      # sweat drop

# ---------------------------------------------------------------- page 2: bananas are berries
pg, S = fact_page(2, 'banana', 'FACT #2', 'BANANAS ARE BERRIES.', 'STRAWBERRIES ARE NOT.', cue('banana', 0, 'bananas'), cue('banana', 0, 'strawberries'))
ban = G([
    ('M100 180 C 120 330, 300 380, 410 270 C 330 320, 170 300, 130 172 Z', INK, 7, '#f7d94c', 2.4),
    ('M100 180 L 92 150 L 116 144 L 130 172', INK, 6, '#8a6a2b', 0.4),
    ('M410 270 l 12 -8', INK, 8, None, 0.1),
    ('M140 220 C 170 290, 260 320, 340 300', '#d9b52a', 4, None, 0.4),
    # sunglasses
    (ell(222, 292, 18, 11) + ' ' + ell(268, 286, 18, 11), INK, 4, INK, 0.4), ('M240 290 L 250 288', INK, 4, None, 0.1),
    ('M234 318 Q 248 324 262 314', INK, 4, None, 0.2),
], 0, 0)
tb = cue('banana', 0, 'bananas')
pg.draw(ban, S + 0.05, max(tb - S + 0.4, 1.0))
crown = 'M190 170 L 190 122 L 215 146 L 240 110 L 265 146 L 290 122 L 290 170 Z'
popin(pg, crown, INK, 6, AMBER, tb + 0.5, tr='translate(-10 -10)')
pg.text('BERRY', 250, 396, 44, GREEN, at=cue('banana', 0, 'berries'), rot=-3)
ts = cue('banana', 0, 'strawberries')
straw = G([
    ('M720 368 C 636 306, 618 208, 662 176 C 692 156, 748 156, 778 176 C 822 208, 804 306, 720 368 Z', INK, 7, '#e8413a', 2),
    ('M660 176 L 688 140 L 704 166 L 720 128 L 736 166 L 752 140 L 780 176 Z', INK, 5, '#3fae5a', 0.8),
    ('M680 220 l 0 1 M760 220 l 0 1 M690 290 l 0 1 M750 290 l 0 1 M720 320 l 0 1 M670 255 l 0 1 M770 255 l 0 1', '#ffe28a', 9, None, 0.4),
    ('M698 236 l 14 0 M730 236 l 14 0', INK, 5, None, 0.2),                                         # sad eyes
    ('M704 278 Q 720 266 736 278', INK, 5, None, 0.2),
], 0, 0)
pg.draw(straw, ts - 0.3, 0.8)
tf = cue('banana', 0, 'fucking')
pg.text('NOT A BERRY', 720, 400, 42, RED, at=tf + 0.2, rot=-6)
tr_ = cue('banana', 1, 'rigged')
popin(pg, 'M700 246 q 8 18 0 26 q -8 -8 0 -26 Z', BLUE, 3, '#9cc7f2', tr_)
popin(pg, 'M746 246 q 8 18 0 26 q -8 -8 0 -26 Z', BLUE, 3, '#9cc7f2', tr_ + 0.1)
pg.text('#JUSTICE4STRAWBERRY', 470, 96, 34, PURPLE, at=cue('banana', 1, 'bastards'), rot=-3)

# ---------------------------------------------------------------- page 3: Venus day > year
pg, S = fact_page(3, 'venus', 'FACT #3', 'A DAY ON VENUS (243 EARTH DAYS)', 'IS LONGER THAN ITS YEAR', cue('venus', 0, 'day'), cue('venus', 0, 'year'))
venus = G([
    (ell(310, 250, 112), INK, 7, '#eab56a', 2.4),
    ('M214 196 C 260 210, 330 180, 400 200 M204 254 C 270 270, 340 236, 418 256 M220 306 C 280 318, 340 296, 398 312', '#c98a3e', 6, None, 0.8),
    ('M262 240 Q 278 252 294 240 M326 240 Q 342 252 358 240', INK, 5, None, 0.3),                  # sleepy eyes
    ('M296 290 Q 310 280 324 290', INK, 5, None, 0.2),
], 0, 0)
td = cue('venus', 0, 'day')
pg.draw(venus, S + 0.05, max(td - S, 0.9))
spin = G([('M190 140 A 150 150 0 0 1 430 140 M430 140 l -26 -4 M430 140 l 4 -26', BLUE, 6, None, 1)], 0, 0)
pg.draw(spin, td + 0.1, 0.5)
pg.text('sloooow', 310, 402, 34, BLUE, at=td + 0.5, pop=False)
ty = cue('venus', 0, 'year')
pg.text('Zzz', 440, 230, 50, PURPLE, at=ty + 0.3, rot=-10, pop=False)
cal = G([
    ('M600 120 L 870 120 L 870 370 L 600 370 Z', INK, 7, WHITE, 1.4),
    ('M600 120 L 870 120 L 870 176 L 600 176 Z', INK, 6, RED, 0.6),
    ('M650 100 l 0 40 M820 100 l 0 40', INK, 8, None, 0.3),
], 0, 0)
tm = cue('venus', 1, 'two')
pg.draw(cal, tm - 0.1, 0.6)
pg.text('243 DAYS', 735, 162, 38, WHITE, at=tm + 0.5, pop=False)
pg.text('MONDAY', 735, 276, 54, INK, at=cue('venus', 1, 'monday'), rot=-2)
pg.text('(still)', 735, 340, 34, BLUE, at=cue('venus', 1, 'monday') + 0.4, pop=False)
pg.text('HELL.', 590, 410, 46, RED, at=cue('venus', 1, 'hell'), rot=-6)

# ---------------------------------------------------------------- page 4: taller in the morning
pg, S = fact_page(4, 'taller', 'FACT #4', "YOU ARE ~1 CM TALLER", 'IN THE MORNING', cue('taller', 0, 'centimeter'), cue('taller', 0, 'morning'))
SKIN = '#ffd9b3'
sun = G([
    (ell(96, 130, 34), INK, 5, AMBER, 1),
    ('M96 80 l 0 -12 M96 180 l 0 12 M46 130 l -12 0 M146 130 l 12 0 M60 94 l -8 -8 M132 94 l 8 -8 M60 166 l -8 8 M132 166 l 8 8', AMBER, 6, None, 0.6),
], 0, 0)
am = G([
    (ell(260, 126, 36), INK, 6, SKIN, 1),
    ('M246 120 l 0 1 M274 120 l 0 1', INK, 9, None, 0.1), ('M244 138 Q 260 152 276 138', INK, 5, None, 0.2),
    ('M260 162 L 260 282 M260 192 L 210 240 M260 192 L 312 160 M260 282 L 222 380 M260 282 L 298 380', INK, 8, None, 1.4),
    ('M312 160 l 4 -20', INK, 8, None, 0.2),                                                         # thumbs up
], 0, 0)
pg.draw(sun, S + 0.05, 0.5)
pg.draw(am, S + 0.5, 1.0)
tmn = cue('taller', 0, 'morning')
moonc = G([('M872 262 A 36 36 0 1 0 872 330 A 28 28 0 1 1 872 262 Z', INK, 5, '#fff2a8', 1)], 0, 0)
pm = G([
    (ell(620, 174, 36), INK, 6, SKIN, 1),
    ('M604 172 l 12 0 M626 172 l 12 0', INK, 5, None, 0.1), ('M606 194 Q 620 184 634 194', INK, 5, None, 0.2),
    ('M620 210 C 616 250, 626 270, 620 300 M620 230 L 572 272 M620 230 L 668 272 M620 300 L 590 380 M620 300 L 650 380', INK, 8, None, 1.4),
], 0, 0)
pg.draw(moonc, tmn - 0.5, 0.3)
pg.draw(pm, tmn - 0.2, 0.7)
dash = G([('M300 90 L 760 90 M660 138 L 760 138', RED, 4, None, 1), ('M740 92 L 740 136 M732 102 l 8 -10 l 8 10 M732 126 l 8 10 l 8 -10', RED, 4, None, 0.6)], 0, 0)
pg.draw(dash, tmn + 0.2, 0.5)
pg.text('+1 CM', 830, 128, 40, RED, at=tmn + 0.6, rot=-4)
tg = cue('taller', 1, 'gravity')
for k, ax in enumerate((560, 620, 680)):
    pg.draw(G([(f'M{ax} 84 L {ax} 124 M{ax-10} 114 l 10 10 l 10 -10', PURPLE, 6, None, 1)], 0, 0), tg + 0.1 * k, 0.25)
pg.text('squish', 480, 230, 40, PURPLE, at=cue('taller', 1, 'squishes'), rot=-8)
pg.text('ugh.', 720, 240, 40, INK, at=cue('taller', 1, 'dumbass'), rot=6, pop=False)

# ---------------------------------------------------------------- page 5: outro
pg = Page(5); S = SEC['outro']['start']
pg.text('HOMEWORK:', PW/2, 150, 96, BLUE, at=cue('outro', 0, 'class'), rot=-2)
th1 = cue('outro', 1, 'who')
s1, _ = fit("WHO'S CLOSER TO", 820, 130)
pg.text("WHO'S CLOSER TO", PW/2, 310, s1, RED, at=th1, rot=-1.5)
pg.text('THE MOON?', PW/2, 458, 150, RED, at=cue('outro', 1, 'moon'), rot=1)
u = pg.path(squiggle(170, 780, 492, 9, 8), RED, 9)
tc = cue('outro', 1, 'comment')
op('set', '#'+u, tc, {'opacity': 1}); op('to', '#'+u, tc, {'strokeDashoffset': 0, 'duration': 0.3, 'ease': 'none'})
pg.text('answer in the comments', PW/2, 596, 52, GREEN, at=tc + 0.1, rot=-1)
greg.append((cue('outro', 1, 'moon'), 'tap', (PX + 270, PY + 478)))
pages.append((pg, 'outro'))
