# Episode 8 boards. Runs inside engine/build.py (exec), so it uses the engine's helpers:
# Page, fact_page, G, GX, ell, squiggle, cue, op, sfx, greg, pages, SEC, fit and the colour constants.
def popin(pg, d, color, w, fill, t, tr=''):
    i = pg.path(d, color, w, fill, tr)
    op('set', '#'+i, t, {'opacity': 1, 'strokeDashoffset': 0, 'fillOpacity': 1})
    op('fromTo', '#'+i, t, {'scale': 1, 'duration': 0.28, 'ease': 'back.out(3)'}, {'scale': 0.2, 'transformOrigin': '50% 50%'})
    return i

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
pg.text('(100% true. 0% useful.)', PW/2, 602, 50, GREEN, at=cue('intro', 0, 'horse'), rot=-1)
greg.append((cue('intro', 0, 'dead'), 'tap', (PX + 300, PY + 500)))
pages.append((pg, 'intro'))

# ---------------------------------------------------------------- page 1: dead jockey wins
pg, S = fact_page(1, 'jockey', 'FACT #1', 'IN 1923 A JOCKEY DIED MID-RACE', 'AND HIS HORSE STILL WON', cue('jockey', 0, 'jockey'), cue('jockey', 0, 'won'))
HORSE = '#a0632f'; SILK = '#2e8fd6'
pg.draw(G([('M30 392 L 930 392', GREEN, 8, None, 1)], 0, 0), S + 0.05, 0.3)            # turf
horse = G([
    (ell(330, 270, 120, 52), INK, 6, HORSE, 1),                                      # body
    ('M430 250 L 490 170 L 520 180 L 470 270 Z', INK, 6, HORSE, 0.6),               # neck
    (ell(520, 176, 44, 24), INK, 6, HORSE, 0.5),                                     # head
    ('M500 150 l 6 -22 l 10 20', INK, 5, HORSE, 0.2),                                # ear
    ('M520 168 l 0 1', INK, 10, None, 0.1),                                          # eye
    ('M240 300 L 200 380 M290 318 L 280 388 M380 318 L 400 388 M420 300 L 470 370', INK, 12, None, 0.6),  # galloping legs
    ('M212 250 q -60 0 -80 50', INK, 10, None, 0.3),                                  # tail
], 0, 0)
tj = cue('jockey', 0, 'jockey')
pg.draw(horse, tj - 0.3, 0.9)
jockey = G([
    ('M320 216 L 380 216 L 370 160 L 330 160 Z', INK, 5, SILK, 0.6),                 # jockey body, slumped
    (ell(372, 140, 26), INK, 5, SKIN, 0.5),                                           # head
    ('M360 132 l 8 8 m 0 -8 l -8 8 M378 132 l 8 8 m 0 -8 l -8 8', INK, 4, None, 0.2),  # X X eyes
    ('M362 156 q 10 -6 20 0', INK, 4, None, 0.1),                                     # frown
], 0, 0)
pg.draw(jockey, tj + 0.3, 0.6)
td = cue('jockey', 0, 'died')
popin(pg, ell(372, 98, 34, 10), AMBER, 6, None, td)                                  # halo
pg.text('R.I.P.', 230, 140, 40, PURPLE, at=td + 0.2, rot=-8, pop=False)
tw = cue('jockey', 0, 'won')
flag = G([('M760 392 L 760 120', INK, 8, None, 0.5),
          ('M760 120 L 880 120 L 880 200 L 760 200 Z', INK, 5, WHITE, 0.3),
          ('M760 120 h 30 v 20 h -30 Z M820 120 h 30 v 20 h -30 Z M790 140 h 30 v 20 h -30 Z M850 140 h 30 v 20 h -30 Z M760 160 h 30 v 20 h -30 Z M820 160 h 30 v 20 h -30 Z M790 180 h 30 v 20 h -30 Z M850 180 h 30 v 20 h -30 Z', INK, 2, INK, 0.4)], 0, 0)
pg.draw(flag, tw - 0.5, 0.6)
popin(pg, 'M640 250 l 14 30 l 32 4 l -24 22 l 6 32 l -28 -16 l -28 16 l 6 -32 l -24 -22 l 32 -4 Z', INK, 4, AMBER, tw + 0.1)
pg.text('WINNER', 660, 380, 40, RED, at=tw + 0.3, rot=-4, pop=False)
pg.text('still dead', 660, 220, 30, PURPLE, at=cue('jockey', 1, 'dead'), rot=5, pop=False)

# ---------------------------------------------------------------- page 2: rats laugh when tickled
pg, S = fact_page(2, 'rats', 'FACT #2', 'RATS LAUGH WHEN', 'YOU TICKLE THEM', cue('rats', 0, 'rats'), cue('rats', 0, 'tickle'))
RAT = '#9aa0a8'; PINK = '#f4a6b8'
tr_ = cue('rats', 0, 'rats')
rat = G([
    (ell(330, 300, 130, 70), INK, 6, RAT, 1),                                        # body (on its back)
    (ell(330, 300, 80, 40), INK, 4, '#d5d9de', 0.4),                                 # belly
    (ell(470, 270, 52, 44), INK, 6, RAT, 0.6),                                       # head
    (ell(470, 220, 26), INK, 5, PINK, 0.3), (ell(510, 236, 22), INK, 5, PINK, 0.3),  # ears
    (ell(520, 282, 8), INK, 3, PINK, 0.1),                                           # nose
    ('M460 262 q 6 -8 12 0 M484 262 q 6 -8 12 0', INK, 4, None, 0.2),                # happy squint eyes
    ('M470 290 q 16 18 32 0', INK, 4, None, 0.2),                                    # grin
    ('M280 236 l -10 -40 M360 236 l 10 -40', INK, 8, None, 0.3),                     # paws in the air
    ('M200 310 q -80 10 -120 -40 q -20 -30 10 -50', PINK, 9, None, 0.4),             # tail
], 0, 0)
pg.draw(rat, tr_ - 0.2, 1.0)
tt = cue('rats', 0, 'tickle')
feather = G([('M600 170 Q 700 120 760 200 Q 700 220 600 170 Z', INK, 5, '#f7d35c', 0.6),
             ('M600 170 L 420 320', INK, 5, None, 0.4)], 0, 0)
pg.draw(feather, tt - 0.1, 0.5)
th = cue('rats', 0, 'high')
for k in range(3):
    popin(pg, f'M{560 + 30*k} {250 - 10*k} q {16+6*k} {30+10*k} 0 {60+20*k}', BLUE, 6, None, th + 0.1 * k)
pg.text('hee hee', 760, 300, 46, BLUE, at=th + 0.3, rot=-6, pop=False)
pg.text('(50 kHz)', 760, 350, 32, PURPLE, at=cue('rats', 0, 'hear'), rot=-6, pop=False)
pg.text('DREAM JOB', 160, 130, 44, GREEN, at=cue('rats', 1, 'dream'), rot=-8)

# ---------------------------------------------------------------- page 3: Hell, Norway freezes over
pg, S = fact_page(3, 'hell', 'FACT #3', "THERE'S A TOWN IN NORWAY CALLED", 'HELL. IT FREEZES OVER', cue('hell', 0, 'norway'), cue('hell', 0, 'freezes'))
SNOW = '#eef6ff'; ICE = '#9fd6f5'
pg.draw(G([('M30 360 Q 250 330 480 360 T 930 356 L 930 404 L 30 404 Z', INK, 5, SNOW, 1)], 0, 0), S + 0.05, 0.5)
tt = cue('hell', 0, 'town')
sign = G([('M120 380 L 120 250 M300 380 L 300 250', BROWN, 12, None, 0.5),
          ('M90 150 L 330 150 L 330 250 L 90 250 Z', INK, 6, '#1f5fbf', 1)], 0, 0)
pg.draw(sign, tt, 0.6)
pg.text('HELL', 210, 222, 72, WHITE, at=cue('hell', 0, 'hell'), rot=0)
tf = cue('hell', 0, 'freezes')
for k, x in enumerate([110, 160, 210, 260, 310]):
    popin(pg, f'M{x-10} 250 L {x} {290 + 12*(k%2)} L {x+10} 250 Z', INK, 3, ICE, tf + 0.06 * k)   # icicles
snowman = G([
    (ell(650, 320, 64, 50), INK, 6, WHITE, 0.8),
    (ell(650, 230, 46, 40), INK, 6, WHITE, 0.6),
    ('M626 220 l 0 1 M672 220 l 0 1', INK, 10, None, 0.1),
    ('M630 250 q 20 -12 40 0', INK, 4, None, 0.1),                                    # unhappy
    ('M612 262 L 690 262 L 700 300 L 684 300 L 676 270 L 612 270 Z', INK, 4, RED, 0.3),  # scarf
], 0, 0)
tw = cue('hell', 0, 'winter')
pg.draw(snowman, tw - 0.2, 0.7)
popin(pg, 'M616 196 q -14 -30 4 -46 q 0 24 14 36 Z M684 196 q 14 -30 -4 -46 q 0 24 -14 36 Z', INK, 4, RED, tw + 0.5)  # devil horns
pg.draw(G([('M760 380 L 760 160', INK, 6, None, 0.6), ('M736 160 L 736 130 M760 160 L 760 122 M784 160 L 784 130 M736 160 L 784 160', INK, 6, None, 0.4)], 0, 0), tw + 0.7, 0.4)  # pitchfork
for k, (x, y) in enumerate([(450, 120), (520, 180), (860, 130), (420, 260), (880, 260)]):
    popin(pg, f'M{x-14} {y} L {x+14} {y} M{x} {y-14} L {x} {y+14} M{x-10} {y-10} L {x+10} {y+10} M{x+10} {y-10} L {x-10} {y+10}', ICE, 4, None, cue('hell', 1, 'freezes') + 0.08 * k)
pg.text('BRRR', 520, 330, 44, BLUE, at=cue('hell', 1, 'january'), rot=-6)

# ---------------------------------------------------------------- page 4: stomach lining renews every few days
pg, S = fact_page(4, 'stomach', 'FACT #4', 'YOUR STOMACH LINING REPLACES', 'ITSELF EVERY FEW DAYS', cue('stomach', 0, 'stomach'), cue('stomach', 0, 'itself'))
TUM = '#f29bab'; ACID = '#8fdc5a'
ts = cue('stomach', 0, 'stomach')
tum = 'M300 110 C 300 170, 330 190, 380 180 C 470 160, 560 200, 560 290 C 560 380, 420 400, 330 370 C 260 350, 230 300, 250 250 C 270 210, 270 160, 260 110 Z'
pg.draw(G([(tum, INK, 7, TUM, 1),
           ('M560 300 q 40 10 50 60', INK, 14, None, 0.3)], 0, 0), ts - 0.2, 0.9)
pg.draw(G([('M262 300 C 300 330, 420 360, 540 300 C 530 370, 400 390, 320 360 C 290 345, 270 325, 262 300 Z', INK, 4, ACID, 0.8)], 0, 0), ts + 0.6, 0.5)
tl = cue('stomach', 0, 'acid')
for k, (x, y) in enumerate([(340, 340), (400, 352), (460, 336), (500, 318)]):
    popin(pg, ell(x, y, 9), INK, 3, '#c6f59a', tl + 0.06 * k)
pg.text('ACID', 420, 300, 36, GREEN, at=tl + 0.2, rot=-4, pop=False)
cal = G([('M660 130 L 900 130 L 900 300 L 660 300 Z', INK, 5, WHITE, 1),
         ('M660 130 L 900 130 L 900 170 L 660 170 Z', INK, 5, RED, 0.4),
         ('M700 110 l 0 36 M860 110 l 0 36', INK, 6, None, 0.2)], 0, 0)
pg.draw(cal, cue('stomach', 0, 'days') - 0.4, 0.6)
pg.text('3-5 DAYS', 780, 248, 38, INK, at=cue('stomach', 0, 'days'), rot=0)
tg = cue('stomach', 1, 'gut')
popin(pg, 'M330 220 l 0 1 M400 216 l 0 1', INK, 12, None, tg)                          # eyes
popin(pg, 'M318 204 l 24 8 M412 200 l -24 10', INK, 5, None, tg + 0.05)               # angry brows
popin(pg, 'M340 260 q 30 20 60 0', INK, 5, None, tg + 0.1)                            # evil grin
pg.text('NOM', 160, 160, 52, RED, at=cue('stomach', 1, 'digest'), rot=-10)
pg.text('sleep tight', 780, 370, 36, PURPLE, at=cue('stomach', 1, 'sleep'), rot=-4, pop=False)

# ---------------------------------------------------------------- page 5: outro
pg = Page(5); S = SEC['outro']['start']
pg.text('HOMEWORK:', PW/2, 150, 96, BLUE, at=cue('outro', 0, 'class'), rot=-2)
s1, _ = fit('HOW DID A DEAD MAN', 840, 150)
pg.text('HOW DID A DEAD MAN', PW/2, 310, s1, RED, at=cue('outro', 1, 'how'), rot=-1.5)
s2, _ = fit('WIN A RACE?', 820, 150)
pg.text('WIN A RACE?', PW/2, 458, s2, RED, at=cue('outro', 1, 'win'), rot=1)
u = pg.path(squiggle(170, 780, 492, 9, 8), RED, 9)
tc = cue('outro', 1, 'comment')
op('set', '#'+u, tc, {'opacity': 1}); op('to', '#'+u, tc, {'strokeDashoffset': 0, 'duration': 0.3, 'ease': 'none'})
pg.text('answer in the comments', PW/2, 596, 52, GREEN, at=tc + 0.1, rot=-1)
greg.append((cue('outro', 1, 'race'), 'tap', (PX + 270, PY + 478)))
pages.append((pg, 'outro'))
