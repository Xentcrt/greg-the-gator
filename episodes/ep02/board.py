# Episode 2 boards. Runs inside engine/build.py (exec), so it uses the engine's helpers:
# Page, fact_page, G, GX, ell, squiggle, cue, op, sfx, greg, pages, SEC and the colour constants.
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
pg.text('(100% true. 0% useful.)', PW/2, 602, 50, GREEN, at=cue('intro', 1, 'nobody'), rot=-1)
greg.append((cue('intro', 1, 'facts'), 'tap', (PX + 300, PY + 500)))
pages.append((pg, 'intro'))


# ---------------------------------------------------------------- page 1: emu war
pg, S = fact_page(1, 'emu', 'FACT #1', '1932: AUSTRALIA vs. EMUS', 'WINNER: EMUS', cue('emu', 0, 'australia'), cue('emu', 1, 'won'))
emu = G([
    # body
    ('M60 150 C 50 95, 120 60, 200 70 C 270 78, 300 120, 290 165 C 282 205, 230 228, 160 226 C 95 224, 66 196, 60 150 Z', INK, 7, '#c9ab88', 3),
    ('M62 138 C 36 124, 26 138, 16 126 M60 160 C 32 160, 22 176, 10 166 M70 184 C 44 194, 38 210, 24 206', INK, 6, None, 1),
    ('M105 112 q 12 12 24 0 M158 98 q 12 12 24 0 M212 108 q 12 12 24 0 M126 150 q 12 12 24 0 M182 142 q 12 12 24 0 M150 188 q 12 12 24 0 M206 184 q 12 12 24 0', '#8a5a2b', 5, None, 1),
    # legs
    ('M140 222 L 132 290 L 126 330 M126 330 L 98 342 M126 330 L 132 350 M126 330 L 158 340', INK, 8, None, 1.2),
    ('M210 224 L 226 286 L 236 328 M236 328 L 210 344 M236 328 L 246 350 M236 328 L 270 336', INK, 8, None, 1.2),
    # neck + head
    ('M238 94 C 262 60, 266 20, 260 -22 L 292 -22 C 300 24, 292 76, 274 112 Z', INK, 6, '#a9c3df', 1.4),
    (ell(284, -42, 36, 29), INK, 6, '#a9c3df', 1),
    ('M314 -48 C 336 -50, 354 -44, 364 -36 C 348 -28, 330 -28, 314 -32 Z', INK, 5, '#f2c14e', 0.6),
    (ell(294, -46, 10), INK, 4, WHITE, 0.4), (ell(297, -45, 4), INK, 3, INK, 0.2),
    ('M280 -62 L 306 -55', INK, 6, None, 0.3), ('M300 -26 Q 310 -20 318 -26', INK, 4, None, 0.3),
    # victory: helmet + medal
    ('M254 -64 C 254 -100, 314 -100, 314 -64 Z', INK, 6, '#5f8d45', 0.8), ('M244 -64 L 324 -64', INK, 8, None, 0.3),
    ('M238 104 L 250 126 L 262 104', RED, 6, None, 0.3), (ell(250, 136, 13), INK, 5, '#f2c14e', 0.4),
], 150, 152, 0.72)
pg.draw(emu, S + 0.05, min(SEC['emu']['sentences'][0]['e'] - S - 1.0, 2.4))
soldier = G([
    ('M-34 112 L 6 112 M-46 146 L 0 146 M-34 180 L 6 180', BLUE, 6, None, 0.5),
    ('M92 92 L 130 92 L 142 182 L 82 182 Z', INK, 6, '#7f9f5c', 1),
    ('M96 106 L 56 74 M126 106 L 172 132', INK, 9, None, 0.6),
    ('M98 182 L 70 232 L 42 226 M126 182 L 152 236 L 180 250', INK, 9, None, 0.8),
    (ell(110, 58, 33), INK, 6, '#f4d3b5', 1),
    (ell(98, 52, 8), INK, 3, WHITE, 0.2), (ell(124, 52, 8), INK, 3, WHITE, 0.2),
    (ell(99, 53, 3), INK, 3, INK, 0.1), (ell(125, 53, 3), INK, 3, INK, 0.1),
    (ell(111, 76, 7, 9), INK, 4, '#5a1f1f', 0.2),
    ('M150 34 q 6 12 0 16 q -6 -4 0 -16 Z', BLUE, 4, '#9cc7f2', 0.2), ('M74 40 q 6 12 0 16 q -6 -4 0 -16 Z', BLUE, 4, '#9cc7f2', 0.2),
    ('M150 -2 C 150 -32, 206 -32, 206 -2 Z', INK, 5, '#5f8d45', 0.5), ('M142 -2 L 214 -2', INK, 6, None, 0.2), ('M218 -30 l 14 -10 M222 -12 l 16 -2', INK, 4, None, 0.2),
    ('M56 74 L 46 -6', INK, 5, None, 0.3), ('M46 -6 L 4 0 L 8 28 L 50 22 Z', INK, 5, WHITE, 0.4),
], 610, 112, 0.95)
pg.draw(soldier, cue('emu', 0, 'with'), 0.9)
pg.text('!!', 860, 128, 84, RED, at=cue('emu', 0, 'guns'), rot=10, pop=False)

# ---------------------------------------------------------------- page 2: lobster
pg, S = fact_page(2, 'lobster', 'FACT #2', 'LOBSTERS PEE OUT OF', 'THEIR FACES', cue('lobster', 0, 'pee'), cue('lobster', 0, 'faces'))
LP = '#f6a59b'
def lobster(extra=()):
    return [
        ('M340 112 C 360 90, 380 72, 410 66', RED, 9, None, 0.5), ('M340 168 C 360 190, 380 208, 410 214', RED, 9, None, 0.5),
        ('M300 104 L 296 74 L 306 60 M270 102 L 262 72 L 270 56 M240 102 L 228 74 L 234 58 M300 176 L 296 206 L 306 220 M270 178 L 262 208 L 270 224 M240 178 L 228 206 L 234 222', RED, 5, None, 1),
        ('M372 134 C 430 120, 470 90, 520 -6 M372 146 C 430 158, 470 186, 520 282', RED, 4, None, 0.8),
        ('M152 116 L 62 124 C 50 126, 48 154, 62 156 L 152 164 Z', RED, 6, LP, 1),
        ('M62 124 C 40 108, 22 112, 8 120 L 34 140 L 8 160 C 22 168, 40 172, 62 156 Z', RED, 6, LP, 0.8),
        ('M130 118 Q 120 140 130 162 M106 120 Q 96 140 106 160 M84 122 Q 74 140 84 158', RED, 5, None, 0.6),
        ('M150 140 C 150 110, 200 98, 260 100 C 320 102, 360 118, 374 140 C 360 162, 320 178, 260 180 C 200 182, 150 170, 150 140 Z', RED, 7, LP, 2.2),
        ('M200 116 Q 230 112 260 116 M200 164 Q 230 168 260 164', '#e98375', 5, None, 0.3),
        ('M410 66 C 420 30, 490 20, 512 50 C 485 46, 465 54, 455 64 C 482 64, 506 74, 508 92 C 470 102, 425 96, 410 66 Z', RED, 6, LP, 1.4),
        ('M410 214 C 420 250, 490 260, 512 230 C 485 234, 465 226, 455 216 C 482 216, 506 206, 508 188 C 470 178, 425 184, 410 214 Z', RED, 6, LP, 1.4),
        ('M366 128 L 386 116 M366 152 L 386 164', RED, 5, None, 0.2),
        (ell(390, 112, 10), INK, 4, WHITE, 0.2), (ell(393, 112, 4), INK, 3, INK, 0.1),
        (ell(390, 168, 10), INK, 4, WHITE, 0.2), (ell(393, 168, 4), INK, 3, INK, 0.1),
    ] + list(extra)
lashes = [('M383 101 l -4 -9 M391 100 l 0 -10 M399 102 l 4 -9 M383 179 l -4 9 M391 180 l 0 10 M399 178 l 4 9', INK, 3, None, 0.3)]
pg.draw(G(lobster(), 22, 112, 0.7), S + 0.05, cue('lobster', 0, 'pee') - S + 0.15)
pee = G([
    ('M296 196 Q 450 70 604 200', AMBER, 10, None, 2),
    ('M622 214 l 6 12 M608 226 l -2 13 M636 196 l 12 4', AMBER, 7, None, 0.6),
], 0, 0)
pg.draw(pee, cue('lobster', 0, 'out'), 0.55)
her = GX(lobster(lashes + [(ell(330, 154, 13, 8), '#ff8fb1', 2, '#ff8fb1', 0.2)]), 822, 160, -0.5, 0.5)
pg.draw(her, cue('lobster', 0, 'faces') - 0.1, 0.6)
bow = G([('M688 196 l -24 -14 l 0 28 Z M688 196 l 24 -14 l 0 28 Z', INK, 4, '#ff8fb1', 0.6), (ell(688, 196, 7), INK, 3, '#ff8fb1', 0.2)], 0, 0)
pg.draw(bow, cue('lobster', 0, 'faces') + 0.3, 0.3)
hx, hy = 724, 108
hid = pg.path(f'M{hx} {hy+34} C {hx-70} {hy-10}, {hx-28} {hy-58}, {hx} {hy-22} C {hx+28} {hy-58}, {hx+70} {hy-10}, {hx} {hy+34} Z', RED, 7, RED)
t = cue('lobster', 1, 'flirt')
op('set', '#'+hid, t, {'opacity': 1, 'strokeDashoffset': 0, 'fillOpacity': 1})
op('fromTo', '#'+hid, t, {'scale': 1, 'duration': 0.3, 'ease': 'back.out(3)'}, {'scale': 0.2, 'transformOrigin': '50% 50%'})
pg.text('(romance.)', 760, 352, 50, GREEN, at=t + 0.1, rot=-4)

# ---------------------------------------------------------------- page 3: the can
pg, S = fact_page(3, 'can', 'FACT #3', 'PRINGLES CAN INVENTOR:', 'BURIED IN ONE', cue('can', 0, 'pringles'), cue('can', 1, 'buried'))
can = G([
    ('M-270 276 C -200 222, 200 222, 270 276 Z', INK, 6, '#c08b55', 1.2),
    ('M-230 262 l -6 -20 M-222 262 l 2 -22 M-214 262 l 8 -18 M200 258 l -6 -20 M208 258 l 2 -22 M216 258 l 8 -18', GREEN, 5, None, 0.6),
    ('M-150 250 l 10 4 M-110 240 l 8 6 M120 244 l -8 6 M160 252 l -10 4', '#8a5a2b', 5, None, 0.3),
    ('M-70 92 C -120 62, -160 72, -172 42 C -142 50, -132 30, -152 10 C -112 20, -92 40, -70 62 Z', INK, 5, WHITE, 0.8),
    ('M70 92 C 120 62, 160 72, 172 42 C 142 50, 132 30, 152 10 C 112 20, 92 40, 70 62 Z', INK, 5, WHITE, 0.8),
    ('M-70 0 L -70 230 C -70 254, 70 254, 70 230 L 70 0 C 70 18, -70 18, -70 0 Z', INK, 7, '#fbe9c6', 2),
    ('M-70 62 C -70 80, 70 80, 70 62 L 70 172 C 70 190, -70 190, -70 172 Z', INK, 5, '#e0473f', 1),
    (ell(0, 0, 70, 18), INK, 7, '#c9302a', 0.8), (ell(0, 0, 54, 11), '#f08a84', 4, None, 0.3),
    ('M-40 214 q 20 -12 40 0 q 20 -12 40 0', '#d9a12b', 6, None, 0.4),
    (ell(0, -54, 60, 14), AMBER, 8, None, 0.6),
], 474, 82, 0.95)
pg.draw(can, S + 0.05, SEC['can']['sentences'][0]['e'] - S - 0.4)
pg.text('R.I.P.', 474, 222, 54, WHITE, at=cue('can', 1, 'ashes'), pop=False)
for fx, pc in ((770, '#ff8fb1'), (850, '#b88cf0')):
    flower = G([
        ('M0 300 C -6 260, 6 230, 0 196', GREEN, 6, None, 1), ('M0 254 C 14 236, 34 238, 36 250 C 24 262, 10 260, 0 254 Z', GREEN, 4, '#7cc47a', 0.5),
        (ell(0, 168, 14) + ' ' + ell(-22, 184, 14) + ' ' + ell(22, 184, 14) + ' ' + ell(-13, 206, 14) + ' ' + ell(13, 206, 14), INK, 4, pc, 1.4),
        (ell(0, 190, 10), INK, 4, '#f6c543', 0.3),
    ], fx, 54)
    pg.draw(flower, S + 1.0 + (fx - 770) / 300, 0.7)
ghost = G([
    ('M0 120 C 0 30, 130 30, 130 120 L 130 235 l -22 -20 l -21 20 l -22 -20 l -22 20 l -21 -20 l -22 20 Z', BLUE, 7, '#eef4ff', 3),
    (ell(42, 104, 8, 11), INK, 3, INK, 0.2), (ell(88, 104, 8, 11), INK, 3, INK, 0.2),
    ('M48 138 Q 66 156 84 138', INK, 6, None, 0.4), (ell(30, 128, 9, 5), '#ffb3c7', 2, '#ffb3c7', 0.1), (ell(100, 128, 9, 5), '#ffb3c7', 2, '#ffb3c7', 0.1),
    ('M128 150 C 150 140, 160 126, 164 112', BLUE, 7, None, 0.4), (ell(170, 100, 18, 11), INK, 4, '#f2c14e', 0.4),
], 120, 112, 0.9)
pg.draw(ghost, cue('can', 1, 'buried') - 0.1, 0.6)
pg.text('"WORTH IT"', 200, 128, 40, BLUE, at=cue('can', 1, 'one') + 0.1, rot=-6, pop=False)

# ---------------------------------------------------------------- page 4: unicorn
pg, S = fact_page(4, 'unicorn', 'FACT #4', "SCOTLAND'S NATIONAL ANIMAL:", 'THE UNICORN', cue('unicorn', 0, 'national'), cue('unicorn', 0, 'unicorn'))
flag = G([
    ('M0 0 L 0 270', '#8a5a2b', 9, None, 0.8), (ell(0, -6, 9), INK, 4, '#f6c543', 0.2),
    ('M0 10 C 50 -5, 100 25, 200 10 L 200 136 C 100 151, 50 121, 0 136 Z', INK, 6, '#2b62c9', 1.5),
    ('M10 20 L 190 126 M190 20 L 10 126', WHITE, 16, None, 1),
], 660, 70)
pg.draw(flag, S + 0.05, 0.85)
pg.text('SCOTLAND', 770, 262, 40, BLUE, at=S + 0.55, pop=False)
uni = G([
    ('M196 118 C 244 104, 270 146, 250 172 C 286 180, 292 226, 266 242 C 298 258, 296 304, 262 326 L 236 330 C 246 300, 232 260, 218 230 C 208 200, 204 160, 196 118 Z', INK, 6, '#cfaaf5', 1.6),
    ('M212 142 C 242 150, 246 180, 234 200 M228 212 C 262 222, 266 250, 250 270 M242 284 C 266 294, 264 314, 252 328', '#ff8fb1', 6, None, 0.8),
    ('M250 330 C 250 260, 236 200, 200 160 C 180 138, 150 128, 126 136 C 96 146, 70 180, 52 214 C 42 234, 54 254, 76 252 L 130 240 C 150 252, 164 272, 170 300 L 174 330 Z', INK, 7, WHITE, 3),
    ('M176 144 L 194 96 L 210 152 Z', INK, 6, WHITE, 0.5), ('M186 136 L 194 112 L 200 138', '#ffb3c7', 4, None, 0.2),
    (ell(150, 176, 9, 11), INK, 3, INK, 0.3), (ell(147, 172, 3), WHITE, 2, WHITE, 0.1),
    ('M140 166 l -10 -8 M146 163 l -4 -11 M154 163 l 2 -11', INK, 4, None, 0.2),
    ('M66 230 q 6 -6 12 0', INK, 5, None, 0.2), ('M66 246 Q 90 252 112 240', INK, 5, None, 0.3),
    (ell(118, 214, 12, 7), '#ffb3c7', 2, '#ffb3c7', 0.1),
    ('M158 298 C 200 312, 240 312, 272 300 L 276 330 C 240 342, 200 342, 156 330 Z', INK, 6, '#d9534f', 0.8),
    ('M250 328 L 262 382 L 286 378 L 272 326 Z', INK, 5, '#d9534f', 0.4),
    ('M180 306 L 178 336 M210 310 L 210 340 M240 308 L 242 338 M264 340 L 276 370', '#178a4a', 4, None, 0.3),
    ('M158 316 C 200 326, 240 326, 274 316', '#f2c14e', 3, None, 0.2),
], 182, 0, 0.95)
tu = cue('unicorn', 0, 'unicorn')
pg.draw(uni, S + 0.85, tu - S - 0.95)
horn = G([
    ('M150 132 L 126 36 L 174 126 Z', INK, 6, '#f6c543', 1.6), ('M140 112 L 162 106 M135 90 L 154 85 M130 68 L 145 64', '#c08a12', 4, None, 0.5),
    ('M60 70 L 66 84 L 80 90 L 66 96 L 60 110 L 54 96 L 40 90 L 54 84 Z', AMBER, 5, '#fff1b8', 1),
    ('M372 40 L 376 50 L 386 54 L 376 58 L 372 68 L 368 58 L 358 54 L 368 50 Z', AMBER, 5, '#fff1b8', 0.8),
], 182, 0, 0.95)
pg.draw(horn, tu - 0.05, 0.45)
pg.text('(NOT REAL)', 140, 352, 48, GREEN, at=cue('unicorn', 1, "isn't"), rot=-8)

# ---------------------------------------------------------------- page 5: koala
pg, S = fact_page(5, 'koala', 'FACT #5', 'KOALA FINGERPRINTS', 'LOOK JUST LIKE YOURS', cue('koala', 0, 'fingerprints'), cue('koala', 0, 'yours'))
koala = G([
    (ell(105, 74, 58, 52), INK, 6, '#b9bcc2', 1.2), (ell(351, 74, 58, 52), INK, 6, '#b9bcc2', 1.2),
    (ell(110, 80, 32, 27), '#f2c6cf', 2, '#f2c6cf', 0.3), (ell(346, 80, 32, 27), '#f2c6cf', 2, '#f2c6cf', 0.3),
    ('M50 56 l -14 -6 M46 80 l -16 2 M54 104 l -14 8 M406 56 l 14 -6 M410 80 l 16 2 M402 104 l 14 8', INK, 5, None, 0.5),
    ('M228 60 C 150 60, 105 120, 110 185 C 115 255, 170 300, 228 300 C 286 300, 340 255, 345 185 C 350 120, 305 60, 228 60 Z', INK, 7, '#c9ccd2', 3),
    (ell(228, 266, 48, 24), '#e2e3e6', 2, '#f4f4f6', 0.3),
    ('M228 150 C 205 150, 200 185, 205 215 C 210 240, 246 240, 251 215 C 256 185, 251 150, 228 150 Z', INK, 7, '#3a3a40', 1),
    ('M216 168 q 4 -8 10 -10', '#8a8a92', 4, None, 0.1),
    (ell(175, 168, 10), INK, 3, INK, 0.2), (ell(281, 168, 10), INK, 3, INK, 0.2),
    (ell(172, 164, 3.5), WHITE, 2, WHITE, 0.1), (ell(278, 164, 3.5), WHITE, 2, WHITE, 0.1),
    ('M208 264 Q 228 278 248 264', INK, 6, None, 0.3),
    ('M120 222 l -14 8 M124 244 l -12 12 M336 222 l 14 8 M332 244 l 12 12', INK, 5, None, 0.3),
], 130, 50)
tf = cue('koala', 0, 'fingerprints')
pg.draw(koala, S + 0.05, max(tf - S + 0.35, 1.0))
loops = []
cx, cy = 120, 156
for k, r in enumerate((10, 22, 34, 46, 58, 70)):
    a = r * 1.25
    loops.append((f'M{cx-r} {cy+16} L {cx-r} {cy} A {r} {a:.0f} 0 0 1 {cx+r} {cy} L {cx+r} {cy+24+k*6}', BLUE, 5, None, 1))
loops.append((f'M{cx-82} {cy+96} C {cx-60} {cy+60}, {cx+60} {cy+60}, {cx+82} {cy+96}', BLUE, 5, None, 0.8))
loops.append((f'M{cx-82} {cy+118} C {cx-50} {cy+90}, {cx+50} {cy+90}, {cx+82} {cy+118}', BLUE, 5, None, 0.8))
card = G([('M8 20 L 232 20 L 232 300 L 8 300 Z', INK, 6, WHITE, 1.5), ('M110 20 l 20 0', RED, 12, None, 0.2)] + loops +
         [(ell(184, 244, 44), INK, 9, None, 0.8), ('M216 276 L 258 318', '#8a5a2b', 15, None, 0.4), ('M162 226 q 8 -12 22 -14', BLUE, 5, None, 0.2)], 630, 50)
pg.draw(card, tf + 0.25, 0.95)
pg.text('=', 548, 240, 110, INK, at=cue('koala', 0, 'look'), pop=False)
tm = cue('koala', 1, 'frame')
mask = pg.path('M140 148 C 180 138, 276 138, 316 148 L 320 188 C 276 197, 180 197, 136 188 Z', INK, 6, INK, tr='translate(130 50)')
op('set', '#'+mask, tm, {'opacity': 1, 'strokeDashoffset': 0, 'fillOpacity': 1})
eyes = pg.path('M175 168 l 1 1 M281 168 l 1 1', WHITE, 13, tr='translate(130 50)')
op('set', '#'+eyes, tm, {'opacity': 1, 'strokeDashoffset': 0})
nose2 = pg.path('M228 150 C 205 150, 200 185, 205 215 C 210 240, 246 240, 251 215 C 256 185, 251 150, 228 150 Z', INK, 7, '#3a3a40', tr='translate(130 50)')
op('set', '#'+nose2, tm, {'opacity': 1, 'strokeDashoffset': 0, 'fillOpacity': 1})
sfx.append((tm, 'pop'))
pg.text('EVIDENCE', 750, 52, 50, RED, at=cue('koala', 1, 'murder'), rot=-4)

# ---------------------------------------------------------------- page 6: sharks vs trees
pg, S = fact_page(6, 'shark', 'FACT #6', 'SHARKS ARE OLDER', 'THAN TREES', cue('shark', 0, 'sharks'), cue('shark', 0, 'trees'))
SK = '#a9bfd4'
shark = G([
    ('M170 116 L 204 34 L 252 122 Z', BLUE, 6, SK, 0.8),
    ('M186 214 L 214 286 L 256 222 Z', BLUE, 6, SK, 0.8),
    ('M20 170 C 90 95, 250 85, 345 150 L 410 100 L 392 170 L 415 235 L 345 190 C 250 245, 100 240, 20 170 Z', BLUE, 7, SK, 4),
    ('M34 180 C 100 214, 240 220, 330 188 C 250 200, 120 198, 34 180 Z', BLUE, 3, WHITE, 0.6),
    ('M128 146 q -8 20 0 40 M146 144 q -8 22 0 44 M164 144 q -8 20 0 40', BLUE, 5, None, 0.6),
    (ell(80, 150, 9), INK, 3, INK, 0.2), (ell(77, 147, 3), WHITE, 2, WHITE, 0.1),
    (ell(80, 150, 19), INK, 5, None, 0.3), ('M99 150 L 116 148', INK, 5, None, 0.1),
    ('M62 128 q 18 -12 38 -2', WHITE, 8, None, 0.2),
    ('M36 186 Q 78 206 118 192', INK, 6, None, 0.4), ('M46 189 l 8 10 l 8 -8 l 8 10 l 8 -8 l 8 9 l 8 -8', INK, 4, WHITE, 0.4),
], 40, 46)
to = cue('shark', 0, 'older')
pg.draw(shark, S + 0.02, max(to - S, 0.8))
pg.text('>', 528, 244, 150, RED, at=to, pop=False)
tree = G([
    ('M50 332 L 185 332', '#8a5a2b', 7, None, 0.4),
    ('M95 330 C 100 270, 98 230, 90 196 L 142 196 C 132 230, 130 270, 136 330 Z', INK, 6, '#b07a42', 1),
    ('M92 200 C 40 205, 20 150, 60 125 C 40 80, 95 50, 125 75 C 150 40, 215 60, 200 110 C 245 125, 235 195, 180 198 C 165 210, 150 205, 140 200 Z', INK, 7, '#7cc47a', 3),
    (ell(80, 150, 9) + ' ' + ell(150, 110, 9) + ' ' + ell(190, 160, 9), INK, 3, RED, 0.4),
    ('M100 120 q 12 -10 24 -4 M150 150 q 12 -10 24 -4', '#3f8f3d', 4, None, 0.2),
], 620, 4)
pg.draw(tree, to + 0.15, cue('shark', 0, 'trees') - to - 0.1)
tl2 = cue('shark', 1, 'fucking')
pg.text('450 MILLION YRS', 250, 378, 38, BLUE, at=tl2, pop=False)
pg.text('350 MILLION YRS', 736, 378, 38, GREEN, at=tl2 + 0.25, pop=False)


# ---------------------------------------------------------------- page 7: outro
pg = Page(7); S = SEC['outro']['start']
pg.text('HOMEWORK:', PW/2, 150, 96, BLUE, at=cue('outro', 0, 'class'), rot=-2)
tg = cue('outro', 1, 'go')
pg.text('GO ANNOY', PW/2, 310, 150, RED, at=tg, rot=-1.5)
pg.text('SOMEBODY', PW/2, 458, 150, RED, at=cue('outro', 1, 'somebody'), rot=1)
u = pg.path(squiggle(120, 830, 492, 9, 8), RED, 9)
te = SEC['outro']['end']
op('set', '#'+u, te - 0.15, {'opacity': 1}); op('to', '#'+u, te - 0.15, {'strokeDashoffset': 0, 'duration': 0.3, 'ease': 'none'})
pg.text('follow for more useless facts', PW/2, 596, 52, GREEN, at=te + 0.2, rot=-1)
greg.append((cue('outro', 1, 'annoy'), 'tap', (PX + 270, PY + 478)))
pages.append((pg, 'outro'))
