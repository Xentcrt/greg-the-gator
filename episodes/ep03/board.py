# Episode 3 boards. Runs inside engine/build.py (exec), so it uses the engine's helpers:
# Page, fact_page, G, GX, ell, squiggle, cue, op, sfx, greg, pages, SEC, fit and the colour constants.
def heart(cx, cy, s=1.0):
    return (f'M{cx} {cy+30*s:.0f} C {cx-70*s:.0f} {cy-14*s:.0f}, {cx-28*s:.0f} {cy-62*s:.0f}, {cx} {cy-26*s:.0f} '
            f'C {cx+28*s:.0f} {cy-62*s:.0f}, {cx+70*s:.0f} {cy-14*s:.0f}, {cx} {cy+30*s:.0f} Z')

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
greg.append((cue('intro', 0, 'minutes'), 'tap', (PX + 300, PY + 500)))
pages.append((pg, 'intro'))

# ---------------------------------------------------------------- page 1: octopus
pg, S = fact_page(1, 'octopus', 'FACT #1', 'OCTOPUSES HAVE 3 HEARTS', 'AND BLUE BLOOD', cue('octopus', 0, 'hearts'), cue('octopus', 0, 'blue'))
OP = '#c9a3f2'
octo = G([
    # tentacles
    ('M150 250 C 110 290, 70 300, 60 350 C 56 372, 80 380, 92 362', PURPLE, 14, None, 0.8),
    ('M185 262 C 170 310, 140 340, 150 382', PURPLE, 14, None, 0.6),
    ('M225 268 C 225 320, 200 350, 222 388', PURPLE, 14, None, 0.6),
    ('M265 268 C 275 320, 300 345, 286 386', PURPLE, 14, None, 0.6),
    ('M300 260 C 330 300, 350 340, 340 380', PURPLE, 14, None, 0.6),
    ('M330 248 C 370 280, 410 300, 420 346 C 424 368, 400 376, 392 358', PURPLE, 14, None, 0.8),
    # head
    ('M240 40 C 150 40, 120 110, 130 180 C 138 240, 190 272, 240 272 C 290 272, 342 240, 350 180 C 360 110, 330 40, 240 40 Z', INK, 7, OP, 3),
    ('M190 80 q 20 -16 44 -8', WHITE, 9, None, 0.2),
    (ell(200, 180, 20, 24), INK, 4, WHITE, 0.3), (ell(280, 180, 20, 24), INK, 4, WHITE, 0.3),
    (ell(204, 186, 8), INK, 3, INK, 0.1), (ell(276, 186, 8), INK, 3, INK, 0.1),
    ('M178 150 l 40 10 M302 150 l -40 10', INK, 6, None, 0.2),   # grumpy brows
    ('M218 236 Q 240 226 262 236', INK, 6, None, 0.2),
    (ell(170, 220, 12, 7), '#ff8fb1', 2, '#ff8fb1', 0.1), (ell(310, 220, 12, 7), '#ff8fb1', 2, '#ff8fb1', 0.1),
], 40, 44, 0.9)
th = cue('octopus', 0, 'hearts')
pg.draw(octo, S + 0.05, max(th - S - 0.1, 1.0))
for k, hx in enumerate((500, 610, 720)):
    hid = pg.path(heart(hx, 120, 0.9), BLUE, 6, '#7fb0ff')
    t = th + 0.12 * k
    op('set', '#'+hid, t, {'opacity': 1, 'strokeDashoffset': 0, 'fillOpacity': 1})
    op('fromTo', '#'+hid, t, {'scale': 1, 'duration': 0.3, 'ease': 'back.out(3)'}, {'scale': 0.2, 'transformOrigin': '50% 50%'})
sfx.append((th, 'pop'))
pg.text('x3', 830, 132, 70, RED, at=th + 0.4, rot=8, pop=False)
phone = G([
    ('M600 200 L 760 200 C 772 200, 780 208, 780 220 L 780 384 C 780 396, 772 404, 760 404 L 600 404 C 588 404, 580 396, 580 384 L 580 220 C 580 208, 588 200, 600 200 Z', INK, 7, '#3a3a40', 1.5),
    ('M596 224 L 764 224 L 764 372 L 596 372 Z', INK, 3, WHITE, 0.6),
    ('M612 250 L 700 250 C 708 250, 712 256, 712 262 L 712 280 C 712 288, 706 292, 700 292 L 622 292 L 610 302 L 612 290 C 606 288, 604 284, 604 280 L 604 262 C 604 254, 606 250, 612 250 Z', BLUE, 4, '#d8e6ff', 0.6),
], 0, 0)
tt = cue('octopus', 1, 'text')
pg.draw(phone, cue('octopus', 1, 'bastard'), max(tt - cue('octopus', 1, 'bastard'), 0.5))
pg.text('hey :)', 658, 280, 30, BLUE, at=tt - 0.1, pop=False)
pg.text('Seen', 728, 350, 30, RED, at=tt + 0.2, rot=-4)

# ---------------------------------------------------------------- page 2: ketchup medicine
pg, S = fact_page(2, 'ketchup', 'FACT #2', 'IN THE 1830s, KETCHUP', 'WAS SOLD AS MEDICINE', cue('ketchup', 0, 'ketchup'), cue('ketchup', 0, 'medicine'))
KR = '#d9302a'
bottle = G([
    ('M188 40 L 252 40 L 256 70 L 184 70 Z', INK, 6, WHITE, 0.6),          # cap
    ('M192 70 L 248 70 C 250 110, 300 130, 304 180 L 304 360 C 304 384, 284 396, 260 396 L 180 396 C 156 396, 136 384, 136 360 L 136 180 C 140 130, 190 110, 192 70 Z', INK, 7, KR, 3),
    ('M150 210 L 290 210 L 290 330 L 150 330 Z', INK, 5, WHITE, 1),         # label
    ('M210 236 L 230 236 L 230 256 L 250 256 L 250 276 L 230 276 L 230 296 L 210 296 L 210 276 L 190 276 L 190 256 L 210 256 Z', INK, 4, RED, 0.6),
    ('M158 150 q 6 -30 26 -48', '#ff8a84', 8, None, 0.3),
], 40, 14)
pg.draw(bottle, S + 0.05, max(cue('ketchup', 0, 'medicine') - S - 0.2, 1.0))
pg.text('Rx', 260, 384, 44, INK, at=cue('ketchup', 0, 'sold'), pop=False)
# stethoscope draped over the bottle neck
steth = G([
    ('M220 96 C 170 120, 150 170, 190 200 M260 96 C 300 120, 320 170, 290 200', '#555a66', 6, None, 0.6),
    ('M290 200 C 300 250, 360 260, 370 220', '#555a66', 6, None, 0.4), (ell(374, 210, 16), INK, 5, '#c0c6d0', 0.3),
], 40, 14)
pg.draw(steth, cue('ketchup', 0, 'medicine'), 0.5)
tp = cue('ketchup', 1, 'tomato')
pills = []
for k, (px, py, rot) in enumerate(((580, 120, -20), (700, 90, 15), (820, 140, -35), (630, 220, 30), (760, 210, -10), (860, 250, 20))):
    pid = pg.path('M-38 0 C -38 -18, -20 -20, 0 -20 L 0 20 C -20 20, -38 18, -38 0 Z', INK, 5, KR, tr=f'translate({px} {py}) rotate({rot})')
    pid2 = pg.path('M0 -20 C 20 -20, 38 -18, 38 0 C 38 18, 20 20, 0 20 Z', INK, 5, WHITE, tr=f'translate({px} {py}) rotate({rot})')
    for i_ in (pid, pid2):
        t = tp + 0.08 * k
        op('set', '#'+i_, t, {'opacity': 1, 'strokeDashoffset': 0, 'fillOpacity': 1})
        op('fromTo', '#'+i_, t, {'scale': 1, 'duration': 0.25, 'ease': 'back.out(3)'}, {'scale': 0.2, 'transformOrigin': '50% 50%'})
sfx.append((tp, 'pop'))
pg.text('TAKE 2 SQUIRTS', 720, 350, 50, RED, at=cue('ketchup', 1, 'quack'), rot=-5)

# ---------------------------------------------------------------- page 3: Russia vs Pluto
pg, S = fact_page(3, 'pluto', 'FACT #3', 'RUSSIA IS WIDER', 'THAN PLUTO', cue('pluto', 0, 'russia'), cue('pluto', 0, 'pluto'))
russia = G([
    ('M40 250 C 40 210, 60 190, 90 196 C 110 160, 150 170, 170 150 C 200 120, 240 140, 270 118 C 300 96, 340 120, 370 100 '
     'C 410 76, 450 110, 490 96 C 530 82, 570 110, 600 120 C 630 130, 640 170, 618 190 C 600 205, 610 230, 590 250 '
     'C 570 270, 540 250, 520 270 C 495 295, 470 280, 450 300 C 420 320, 380 300, 350 310 C 310 322, 270 300, 230 312 '
     'C 190 324, 160 296, 130 300 C 96 304, 70 290, 56 276 C 46 266, 40 260, 40 250 Z', INK, 7, '#f2a6a0', 4),
    ('M110 240 q 30 -20 60 0 q 30 20 60 0 M330 200 q 30 -20 60 0 M460 230 q 24 -16 48 0', '#c75a52', 5, None, 0.6),
    (ell(150, 236, 8), INK, 3, INK, 0.2),                 # Moscow dot
], 0, 0)
pg.draw(russia, S + 0.05, max(cue('pluto', 0, 'wider') - S + 0.2, 0.9))
rul = G([('M40 356 L 620 356 M40 340 L 40 372 M620 340 L 620 372', BLUE, 6, None, 1)], 0, 0)
pg.draw(rul, cue('pluto', 0, 'wider'), 0.4)
pg.text('~9,000 KM', 330, 400, 40, BLUE, at=cue('pluto', 0, 'wider') + 0.3, pop=False)
tpl = cue('pluto', 0, 'pluto')
pluto = G([
    (ell(780, 230, 76), INK, 7, '#d8c2a6', 2),
    (heart(800, 262, 0.75), '#c9a882', 3, '#f6ead8', 0.6),
    (ell(752, 200, 7), INK, 3, INK, 0.1), (ell(800, 200, 7), INK, 3, INK, 0.1),
    ('M760 246 Q 776 236 792 246', INK, 5, None, 0.2),
], 0, 0)
pg.draw(pluto, tpl, 0.6)
rul2 = G([('M704 356 L 856 356 M704 340 L 704 372 M856 340 L 856 372', GREEN, 6, None, 1)], 0, 0)
pg.draw(rul2, tpl + 0.6, 0.3)
pg.text('2,377 KM', 780, 400, 40, GREEN, at=tpl + 0.8, pop=False)
tb = cue('pluto', 1, 'bodied')
tear = pg.path('M748 214 q 8 18 0 26 q -8 -8 0 -26 Z', BLUE, 3, '#9cc7f2')
op('set', '#'+tear, tb, {'opacity': 1, 'strokeDashoffset': 0, 'fillOpacity': 1})
op('fromTo', '#'+tear, tb, {'y': 22, 'duration': 0.8, 'ease': 'power1.in'}, {'y': 0})
pg.text('(dwarf planet)', 790, 120, 36, PURPLE, at=cue('pluto', 1, 'sad'), rot=-6)
pg.text('L', 692, 96, 90, RED, at=cue('pluto', 1, 'bitch'), rot=-12, pop=False)

# ---------------------------------------------------------------- page 4: shortest war
pg, S = fact_page(4, 'war', 'FACT #4', '1896: BRITAIN vs. ZANZIBAR', 'WAR LASTED 38 MINUTES', cue('war', 0, 'britain'), cue('war', 1, 'thirty'))
watch = G([
    ('M170 70 L 210 70 L 210 96 L 170 96 Z', INK, 6, '#c0c6d0', 0.4), ('M160 58 L 220 58', INK, 9, None, 0.2),
    (ell(190, 220, 120), INK, 8, WHITE, 2.4), (ell(190, 220, 104), '#c0c6d0', 4, None, 0.6),
    ('M190 124 l 0 18 M286 220 l -18 0 M190 316 l 0 -18 M94 220 l 18 0', INK, 6, None, 0.4),
], 20, 0)
pg.draw(watch, S + 0.05, 1.0)
# 38 of 60 minutes as a red wedge
a = math.radians(38 / 60 * 360 - 90)
wx, wy = 210 + 96 * math.cos(a), 220 + 96 * math.sin(a)
wedge = pg.path(f'M210 220 L 210 124 A 96 96 0 1 1 {wx:.0f} {wy:.0f} Z', RED, 4, '#f6b2ac')
hand = pg.path(f'M210 220 L {wx:.0f} {wy:.0f}', INK, 8)
t38 = cue('war', 1, 'thirty')
op('set', '#'+wedge, t38, {'opacity': 1, 'strokeDashoffset': 0}); op('to', '#'+wedge, t38, {'fillOpacity': 1, 'duration': 0.3})
op('set', '#'+hand, t38, {'opacity': 1, 'strokeDashoffset': 0})
pg.text('38', 168, 206, 54, INK, at=t38 + 0.1, pop=False)
ship = G([
    ('M540 280 L 880 280 L 850 340 L 570 340 Z', INK, 7, '#7d8796', 2),
    ('M600 280 L 600 220 L 720 220 L 720 280', INK, 6, '#b8c0cc', 1),
    ('M640 220 L 640 170 L 670 170 L 670 220', INK, 6, '#5a6270', 0.6),
    ('M720 246 L 800 236', INK, 12, None, 0.4),
    ('M590 310 l 0 1 M650 310 l 0 1 M710 310 l 0 1 M770 310 l 0 1 M830 310 l 0 1', INK, 12, None, 0.3),
    ('M520 360 q 30 -16 60 0 q 30 16 60 0 q 30 -16 60 0 q 30 16 60 0 q 30 -16 60 0 q 30 16 60 0', BLUE, 6, None, 0.8),
], 0, 0)
pg.draw(ship, S + 0.6, max(cue('war', 0, 'zanzibar') - S - 0.5, 0.8))
tf = cue('war', 0, 'fought')
puff = G([(ell(840, 220, 40, 30) + ' ' + ell(880, 196, 30, 24), INK, 5, '#f2f2f2', 1)], 0, 0)
pg.draw(puff, tf, 0.3)
pg.text('BOOM', 780, 130, 64, AMBER, at=tf + 0.1, rot=-8)
tl = cue('war', 1, 'lunch')
sand = G([
    ('M410 330 L 500 260 L 520 340 Z', INK, 6, '#f4d58d', 0.8),
    ('M414 326 L 500 268 L 516 330', '#7cc47a', 6, None, 0.4),
    ('M418 336 L 500 276 L 516 338', '#e0473f', 5, None, 0.3),
], 0, 0)
pg.draw(sand, tl - 0.15, 0.35)
pg.text('(lunch: 60 min)', 470, 400, 36, GREEN, at=tl + 0.2, rot=-3, pop=False)


# ---------------------------------------------------------------- page 5: outro
pg = Page(5); S = SEC['outro']['start']
pg.text('HOMEWORK:', PW/2, 150, 96, BLUE, at=cue('outro', 0, 'class'), rot=-2)
th1 = cue('outro', 1, 'how')
s1, _ = fit('HOW LONG WAS', 820, 140)
pg.text('HOW LONG WAS', PW/2, 310, s1, RED, at=th1, rot=-1.5)
pg.text('THE WAR?', PW/2, 458, 150, RED, at=cue('outro', 1, 'war'), rot=1)
u = pg.path(squiggle(170, 780, 492, 9, 8), RED, 9)
tc = cue('outro', 1, 'comment')
op('set', '#'+u, tc, {'opacity': 1}); op('to', '#'+u, tc, {'strokeDashoffset': 0, 'duration': 0.3, 'ease': 'none'})
pg.text('answer in the comments', PW/2, 596, 52, GREEN, at=tc + 0.1, rot=-1)
greg.append((cue('outro', 1, 'war'), 'tap', (PX + 270, PY + 478)))
pages.append((pg, 'outro'))
