# Episode 9 boards. Runs inside engine/build.py (exec), so it uses the engine's helpers:
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
pg.text('(100% true. 0% useful.)', PW/2, 602, 50, GREEN, at=cue('intro', 0, 'guinea'), rot=-1)
greg.append((cue('intro', 0, 'illegal'), 'tap', (PX + 300, PY + 500)))
pages.append((pg, 'intro'))

# ---------------------------------------------------------------- page 1: one guinea pig is illegal in Switzerland
pg, S = fact_page(1, 'guinea', 'FACT #1', "IN SWITZERLAND YOU CAN'T OWN", 'JUST ONE GUINEA PIG', cue('guinea', 0, 'own'), cue('guinea', 0, 'guinea'))
PIG = '#c98a4b'; PATCH = '#f3e3c8'; PINK = '#f4a6b8'
flag = G([('M760 90 L 900 90 L 900 200 L 760 200 Z', INK, 5, RED, 0.6),
          ('M818 112 h 24 v 32 h 32 v 24 h -32 v 32 h -24 v -32 h -32 v -24 h 32 Z', INK, 3, WHITE, 0.4),
          ('M760 90 L 760 300', INK, 7, None, 0.2)], 0, 0)
pg.draw(flag, S + 0.05, 0.5)
def pig(ox, oy, sad):
    face = ('M-38 -14 q 6 -8 12 0', INK, 4, None, 0.1) if not sad else ('M-40 -8 l 14 -6', INK, 4, None, 0.1)
    mouth = ('M-62 18 q 10 -8 20 0', INK, 4, None, 0.1) if sad else ('M-62 12 q 10 10 20 0', INK, 4, None, 0.1)
    return G([(ell(0, 0, 110, 68), INK, 6, PIG, 1),
              (ell(30, -10, 50, 40), INK, 4, PATCH, 0.4),
              (ell(-64, -50, 22, 16), INK, 5, PINK, 0.3),
              ('M-34 -20 l 0 1', INK, 12, None, 0.1), face,
              (ell(-100, 8, 10, 8), INK, 3, PINK, 0.1), mouth,
              ('M-60 64 l 0 14 M-10 66 l 0 14 M40 66 l 0 14 M80 60 l 0 14', INK, 8, None, 0.3)], ox, oy)
pg.draw(pig(300, 300, True), cue('guinea', 0, 'guinea') - 0.4, 0.9)
tl = cue('guinea', 0, 'lonely')
popin(pg, 'M250 306 q -8 16 0 22 q 8 -6 0 -22 Z', INK, 3, '#9fd6f5', tl)              # tear
pg.text('so alone', 300, 170, 40, PURPLE, at=tl + 0.1, rot=-6, pop=False)
pg.text('ILLEGAL', 560, 150, 56, RED, at=cue('guinea', 0, 'get'), rot=-12)
pg.draw(pig(600, 320, False), cue('guinea', 1, 'swiss'), 0.7)                         # the legally required buddy
for k, (x, y) in enumerate([(440, 220), (470, 250)]):
    popin(pg, f'M{x} {y} c -10 -16 -30 -4 0 18 c 30 -22 10 -34 0 -18 Z', INK, 3, RED, cue('guinea', 1, 'feelings') + 0.1 * k)
pg.text('feelings', 160, 120, 40, GREEN, at=cue('guinea', 1, 'feelings'), rot=-8, pop=False)

# ---------------------------------------------------------------- page 2: first speeding ticket was 8 mph
pg, S = fact_page(2, 'speeding', 'FACT #2', 'THE FIRST SPEEDING TICKET (1896)', 'WAS FOR GOING 8 MPH', cue('speeding', 0, 'speeding'), cue('speeding', 0, 'eight'))
CAR = '#2e8fd6'; WOOD = '#a0632f'
pg.draw(G([('M30 392 L 930 392', INK, 6, None, 1)], 0, 0), S + 0.05, 0.3)            # road
ts = cue('speeding', 0, 'speeding')
car = G([('M150 260 L 420 260 L 420 330 L 150 330 Z', INK, 6, CAR, 1),             # carriage body
         ('M200 260 L 200 200 L 380 200 L 380 260', INK, 6, None, 0.5),              # canopy posts
         ('M180 200 L 400 200 L 380 180 L 200 180 Z', INK, 5, WOOD, 0.4),             # roof
         (ell(200, 350, 40), INK, 6, WHITE, 0.4), (ell(380, 350, 40), INK, 6, WHITE, 0.4),
         ('M200 312 l 0 76 M162 350 l 76 0 M380 312 l 0 76 M342 350 l 76 0', INK, 3, None, 0.3),  # spokes
         ('M420 280 l 40 -40', INK, 6, None, 0.2)], 0, 0)                               # tiller
pg.draw(car, ts - 0.3, 1.0)
te = cue('speeding', 0, 'eight')
for k in range(3):
    popin(pg, f'M{120 - 10*k} {270 + 26*k} l -{60 + 20*k} 0', INK, 5, None, te - 0.2 + 0.06 * k)   # "speed" lines
popin(pg, ell(700, 170, 90), INK, 6, WHITE, te)                                        # speedometer
popin(pg, 'M700 170 L 636 196', RED, 8, None, te + 0.1)                                # needle barely moving
pg.text('8', 700, 150, 52, INK, at=te + 0.15, rot=0, pop=False)
pg.text('MPH', 700, 226, 30, INK, at=te + 0.15, rot=0, pop=False)
snail = G([(ell(780, 360, 34), INK, 5, AMBER, 1),
           ('M780 360 m -16 0 a 16 16 0 1 1 16 16', INK, 4, None, 0.3),
           ('M740 392 L 860 392 q 20 0 20 -20 l -10 -20', INK, 5, '#9ad36a', 0.5),
           ('M870 352 l -6 -24 M876 352 l 10 -22', INK, 4, None, 0.2)], 0, 0)
pg.draw(snail, cue('speeding', 1, 'grandma'), 0.6)
pg.text('LOSER', 560, 330, 40, PURPLE, at=cue('speeding', 1, 'faster'), rot=-6)

# ---------------------------------------------------------------- page 3: a cloud weighs ~1 million pounds
pg, S = fact_page(3, 'cloud', 'FACT #3', 'A FLUFFY CUMULUS CLOUD WEIGHS', 'ABOUT 1,000,000 POUNDS', cue('cloud', 0, 'cloud'), cue('cloud', 0, 'million'))
CL = '#eef6ff'
tc = cue('cloud', 0, 'fluffy')
cloud = 'M220 230 C 180 230, 170 170, 220 160 C 220 110, 300 90, 330 130 C 360 80, 460 80, 480 130 C 530 100, 600 140, 580 190 C 630 200, 620 260, 570 260 L 230 260 C 210 260, 200 240, 220 230 Z'
pg.draw(G([(cloud, INK, 7, CL, 1)], 0, 0), tc - 0.3, 0.9)
popin(pg, 'M360 190 l 0 1 M440 190 l 0 1', INK, 12, None, tc + 0.5)                  # cute eyes
popin(pg, 'M380 214 q 20 14 40 0', INK, 5, None, tc + 0.55)
tm = cue('cloud', 0, 'million')
pg.draw(G([('M400 262 L 400 300', INK, 5, None, 0.3),
           ('M300 300 L 500 300 L 525 380 L 275 380 Z', INK, 6, '#5a5f6a', 1)], 0, 0), tm - 0.2, 0.5)   # dangling weight
pg.text('1,000,000 LBS', 400, 352, 24, WHITE, at=tm + 0.2, rot=0, pop=False)
tw = cue('cloud', 1, 'water')
for k, (x, y) in enumerate([(240, 300), (570, 300), (600, 340)]):
    popin(pg, f'M{x} {y} q -10 16 0 22 q 10 -6 0 -22 Z', INK, 3, '#9fd6f5', tw + 0.06 * k)
person = G([(ell(780, 280, 22), INK, 5, SKIN, 0.4),
            ('M780 302 L 780 350 M780 350 L 760 392 M780 350 L 800 392 M760 320 L 800 320', INK, 6, None, 0.6)], 0, 0)
pg.draw(person, cue('cloud', 1, 'pounds') - 0.3, 0.5)
pg.text('YOU', 840, 220, 40, RED, at=cue('cloud', 1, 'dumb'), rot=8)
popin(pg, 'M830 236 L 796 262', RED, 6, None, cue('cloud', 1, 'dumb') + 0.05)
pg.text('!', 740, 250, 50, RED, at=cue('cloud', 1, 'ass'), rot=0)

# ---------------------------------------------------------------- page 4: babies ~300 bones, adults 206
pg, S = fact_page(4, 'bones', 'FACT #4', 'BABIES HAVE ABOUT 300 BONES.', 'ADULTS HAVE 206', cue('bones', 0, 'babies'), cue('bones', 0, 'adults'))
BONE = '#fbf6e6'
tb = cue('bones', 0, 'babies')
baby = G([(ell(220, 220, 62), INK, 6, SKIN, 1),
          ('M196 210 l 0 1 M244 210 l 0 1', INK, 10, None, 0.1),
          ('M204 246 q 16 10 32 0', INK, 4, None, 0.1),
          ('M218 158 q 10 -20 -6 -26', INK, 4, None, 0.1),                             # hair curl
          (ell(220, 330, 60, 50), INK, 6, SKIN, 0.8),
          ('M168 340 Q 220 400 272 340 Z', INK, 5, WHITE, 0.4)], 0, 0)                 # diaper
pg.draw(baby, tb - 0.2, 0.9)
pg.text('300', 360, 160, 56, BLUE, at=cue('bones', 0, 'three'), rot=-8)
ta = cue('bones', 0, 'adults')
bone = lambda x, y: f'M{x-40} {y-6} L {x+40} {y-6} a 10 10 0 1 1 0 12 L {x-40} {y+6} a 10 10 0 1 1 0 -12 Z'
skel = G([(ell(680, 150, 44, 48), INK, 6, BONE, 1),
          ('M664 140 l 0 1 M696 140 l 0 1', INK, 14, None, 0.1),
          ('M666 172 l 28 0 M672 166 l 0 12 M680 166 l 0 12 M688 166 l 0 12', INK, 3, None, 0.1),
          ('M680 198 L 680 320 M640 230 L 720 230 M646 254 L 714 254 M652 278 L 708 278', INK, 8, None, 0.8),
          ('M680 230 L 620 300 M680 230 L 740 300 M680 320 L 650 392 M680 320 L 710 392', INK, 8, None, 0.6)], 0, 0)
pg.draw(skel, ta - 0.3, 0.8)
pg.text('206', 820, 160, 56, RED, at=cue('bones', 0, 'two'), rot=8)
pg.text('???', 470, 300, 50, PURPLE, at=cue('bones', 0, 'adults') + 0.8, rot=-6)
tf = cue('bones', 1, 'fused')
popin(pg, bone(470, 370), INK, 4, BONE, tf)
popin(pg, 'M470 344 l 0 52 M456 344 l 0 52', '#7a7f88', 6, None, tf + 0.15)          # duct-tape fix
pg.text('FUSED', 470, 240, 40, GREEN, at=tf + 0.2, rot=-4, pop=False)

# ---------------------------------------------------------------- page 5: outro
pg = Page(5); S = SEC['outro']['start']
pg.text('HOMEWORK:', PW/2, 150, 96, BLUE, at=cue('outro', 0, 'class'), rot=-2)
s1, _ = fit('WHERE IS ONE GUINEA PIG', 840, 150)
pg.text('WHERE IS ONE GUINEA PIG', PW/2, 310, s1, RED, at=cue('outro', 1, 'where'), rot=-1.5)
s2, _ = fit('ILLEGAL?', 820, 150)
pg.text('ILLEGAL?', PW/2, 458, s2, RED, at=cue('outro', 1, 'illegal'), rot=1)
u = pg.path(squiggle(170, 780, 492, 9, 8), RED, 9)
tc = cue('outro', 1, 'comment')
op('set', '#'+u, tc, {'opacity': 1}); op('to', '#'+u, tc, {'strokeDashoffset': 0, 'duration': 0.3, 'ease': 'none'})
pg.text('answer in the comments', PW/2, 596, 52, GREEN, at=tc + 0.1, rot=-1)
greg.append((cue('outro', 1, 'illegal'), 'tap', (PX + 270, PY + 478)))
pages.append((pg, 'outro'))
