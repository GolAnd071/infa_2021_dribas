import pygame
from pygame.draw import *

pygame.init()

window_w = 600
window_h = 800
white = (255, 255, 255)
black = (0, 0, 0)
bird_color = white
bird_color_1 = (255, 221, 85)
fish_body_color = (71, 136, 147)
fish_fin_color = (102, 99, 112)
fish_eye_color_1 = (1, 54, 177)
fish_eye_color_2 = (5, 64, 85)
fish_eye_color_3 = (104, 157, 184)
FPS = 30
screen = pygame.display.set_mode((window_w, window_h))

second = False


# background
def bg_bird(x, y, w, h, angle):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))

    arc(surf, white, ((0, 0), (w / 2, 2 * h)), 0, 3.14 * 3 / 4)
    arc(surf, white, ((w / 2, 0), (w / 2, 2 * h)), 3.14 / 4, 3.14)

    screen.blit(pygame.transform.rotate(surf, angle), (x, y))


def bg():
    # lines
    h1 = window_h * 0.1
    h2 = window_h * 0.05
    h3 = window_h * 0.1
    h4 = window_h * 0.15
    h5 = window_h * 0.1
    h6 = window_h * 0.5
    c1 = (33, 33, 120)
    c2 = (141, 95, 211)
    c3 = (205, 135, 222)
    c4 = (222, 135, 170)
    c5 = (255, 153, 85)
    c6 = (0, 102, 128)
    rect(screen, c1, ((0, 0), (window_w, h1)))
    rect(screen, c2, ((0, h1), (window_w, h2)))
    rect(screen, c3, ((0, h1 + h2), (window_w, h3)))
    rect(screen, c4, ((0, h1 + h2 + h3), (window_w, h4)))
    rect(screen, c5, ((0, h1 + h2 + h3 + h4), (window_w, h5)))
    rect(screen, c6, ((0, h1 + h2 + h3 + h4 + h5), (window_w, h6)))
    # birds
    if second:
        bird_w1 = window_w / 3
        bird_h1 = window_h / 24
        bg_bird(window_w / 10, window_h / 18, bird_w1, bird_h1, 30)
        bg_bird(window_w * 3 / 5, window_h / 6, bird_w1, bird_h1, 0)
        bg_bird(window_w / 5, window_h / 3, bird_w1, bird_h1, -10)

        # bird_w2 = window_w / 9
        # bird_h2 = window_h / 72
    else:
        bird_w1 = window_w / 3
        bird_h1 = window_h / 24
        bg_bird(window_w / 10, window_h / 18, bird_w1, bird_h1, 30)
        bg_bird(window_w * 3 / 5, window_h / 6, bird_w1, bird_h1, 0)
        bg_bird(window_w / 5, window_h / 3, bird_w1, bird_h1, -10)


# bird
def bird_tail(supersurf, x, y, w, h, angle):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))

    points = ((w * 89 / 98, h * 121 / 121),
              (w * 44 / 98, h * 116 / 121),
              (w * 30 / 98, h * 110 / 121),
              (w * 14 / 98, h * 105 / 121),
              (w * 8 / 98, h * 103 / 121),
              (w * 5 / 98, h * 100 / 121),
              (w * 0 / 98, h * 96 / 121),
              (w * 1 / 98, h * 83 / 121),
              (w * 6 / 98, h * 69 / 121),
              (w * 15 / 98, h * 46 / 121),
              (w * 19 / 98, h * 33 / 121),
              (w * 28 / 98, h * 19 / 121),
              (w * 38 / 98, h * 12 / 121),
              (w * 52 / 98, h * 3 / 121),
              (w * 62 / 98, h * 5 / 121),
              (w * 67 / 98, h * 14 / 121),
              (w * 71 / 98, h * 35 / 121),
              (w * 74 / 98, h * 47 / 121),
              (w * 78 / 98, h * 59 / 121),
              (w * 83 / 98, h * 71 / 121),
              (w * 91 / 98, h * 80 / 121),
              (w * 98 / 98, h * 87 / 121))
    polygon(surf, bird_color, points)
    aalines(surf, black, False, points)

    supersurf.blit(pygame.transform.rotate(surf, angle), (x, y))


def bird_wing(supersurf, x, y, w, h, angle):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))

    points = ((w * 213 / 288, h * 152 / 152),
              (w * 197 / 288, h * 143 / 152),
              (w * 170 / 288, h * 124 / 152),
              (w * 158 / 288, h * 107 / 152),
              (w * 145 / 288, h * 94 / 152),
              (w * 133 / 288, h * 87 / 152),
              (w * 112 / 288, h * 81 / 152),
              (w * 84 / 288, h * 78 / 152),
              (w * 66 / 288, h * 73 / 152),
              (w * 50 / 288, h * 65 / 152),
              (w * 34 / 288, h * 48 / 152),
              (w * 13 / 288, h * 23 / 152),
              (w * 1 / 288, h * 6 / 152),
              (w * 0 / 288, h * 0 / 152),
              (w * 7 / 288, h * 2 / 152),
              (w * 22 / 288, h * 13 / 152),
              (w * 43 / 288, h * 24 / 152),
              (w * 78 / 288, h * 35 / 152),
              (w * 112 / 288, h * 41 / 152),
              (w * 138 / 288, h * 43 / 152),
              (w * 162 / 288, h * 43 / 152),
              (w * 177 / 288, h * 42 / 152),
              (w * 198 / 288, h * 41 / 152),
              (w * 219 / 288, h * 42 / 152),
              (w * 241 / 288, h * 47 / 152),
              (w * 262 / 288, h * 74 / 152),
              (w * 276 / 288, h * 100 / 152),
              (w * 288 / 288, h * 130 / 152))
    polygon(surf, bird_color, points)
    aalines(surf, black, False, points)

    supersurf.blit(pygame.transform.rotate(surf, angle), (x, y))


def bird_leg_ellipse(supersurf, x, y, w, h, angle):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))
    ellipse(surf, bird_color, (0, 0, w, h))
    supersurf.blit(pygame.transform.rotate(surf, angle), (x, y))


def bird_paw(supersurf, x, y, w, h, angle):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))

    points = ((w * 1 / 74, h * 26 / 61),
              (w * 0 / 74, h * 31 / 61),
              (w * 0 / 74, h * 46 / 61),
              (w * 2 / 74, h * 51 / 61),
              (w * 5 / 74, h * 61 / 61),
              (w * 8 / 74, h * 47 / 61),
              (w * 10 / 74, h * 38 / 61),
              (w * 12 / 74, h * 27 / 61),
              (w * 15 / 74, h * 22 / 61),
              (w * 19 / 74, h * 19 / 61),
              (w * 26 / 74, h * 19 / 61),
              (w * 41 / 74, h * 26 / 61),
              (w * 57 / 74, h * 31 / 61),
              (w * 69 / 74, h * 37 / 61),
              (w * 60 / 74, h * 27 / 61),
              (w * 48 / 74, h * 20 / 61),
              (w * 33 / 74, h * 18 / 61),
              (w * 48 / 74, h * 18 / 61),
              (w * 61 / 74, h * 21 / 61),
              (w * 74 / 74, h * 28 / 61),
              (w * 65 / 74, h * 19 / 61),
              (w * 52 / 74, h * 13 / 61),
              (w * 35 / 74, h * 13 / 61),
              (w * 39 / 74, h * 10 / 61),
              (w * 48 / 74, h * 9 / 61),
              (w * 60 / 74, h * 9 / 61),
              (w * 67 / 74, h * 12 / 61),
              (w * 70 / 74, h * 14 / 61),
              (w * 66 / 74, h * 6 / 61),
              (w * 57 / 74, h * 1 / 61),
              (w * 49 / 74, h * 0 / 61),
              (w * 38 / 74, h * 2 / 61),
              (w * 29 / 74, h * 5 / 61),
              (w * 20 / 74, h * 9 / 61),
              (w * 16 / 74, h * 11 / 61))
    polygon(surf, bird_color_1, points)
    aalines(surf, black, False, points)

    supersurf.blit(pygame.transform.rotate(surf, angle), (x, y))


def bird_leg(supersurf, x, y, w, h, angle):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))

    # leg_body
    bird_leg_ellipse(surf, 0, 0, w * 0.4, h * 0.2, -60)
    bird_leg_ellipse(surf, w * 0.2, h * 0.4, w * 0.4, h * 0.15, -30)
    # paw
    bird_paw(surf, w * 85 / 175, h * 115 / 175, w * 55 / 175, h * 65 / 175, 0)

    supersurf.blit(pygame.transform.rotate(surf, angle), (x, y))


def bird_head_beak(supersurf, x, y, w, h, angle):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))

    points1 = ((w * 1 / 76, h * 6 / 28),
               (w * 10 / 76, h * 4 / 28),
               (w * 26 / 76, h * 3 / 28),
               (w * 42 / 76, h * 0 / 28),
               (w * 59 / 76, h * 0 / 28),
               (w * 75 / 76, h * 17 / 28),
               (w * 50 / 76, h * 20 / 28))
    points2 = ((w * 1 / 76, h * 7 / 28),
               (w * 10 / 76, h * 10 / 28),
               (w * 25 / 76, h * 12 / 28),
               (w * 35 / 76, h * 14 / 28),
               (w * 63 / 76, h * 14 / 28),
               (w * 68 / 76, h * 13 / 28),
               (w * 74 / 76, h * 10 / 28),
               (w * 72 / 76, h * 16 / 28),
               (w * 60 / 76, h * 28 / 28),
               (w * 39 / 76, h * 28 / 28),
               (w * 25 / 76, h * 24 / 28),
               (w * 9 / 76, h * 23 / 28),
               (w * 0 / 76, h * 21 / 28))
    polygon(surf, bird_color_1, points1)
    aalines(surf, black, False, points1)
    polygon(surf, bird_color_1, points2)
    aalines(surf, black, False, points2)

    supersurf.blit(pygame.transform.rotate(surf, angle), (x, y))


def bird_head(supersurf, x, y, w, h, angle):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))

    # bird_beak
    bird_head_beak(surf, w * 144 / 220, h * 14 / 71, w * 74 / 220, h * 26 / 71, 0)
    # bird_head_body
    ellipse(surf, bird_color, (0, h / 3, w / 2, h * 2 / 3))
    ellipse(surf, bird_color, (w * 2 / 5, 0, w / 3, h * 2 / 3))
    # bird_eye
    ellipse(surf, black, (w * 115 / 220, h * 16 / 71, w * 14 / 220, h * 9 / 71))

    supersurf.blit(pygame.transform.rotate(surf, angle), (x, y))


def bird(x, y, w, h, angle, orientation):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))

    # tail
    bird_tail(surf, w * 0.16, h * 0.4, w * 0.2, h * 0.2, 5)
    # wings
    wing_w = w * 2 / 5
    wing_h = h / 3
    bird_wing(surf, w / 8, 0, wing_w, wing_h, -20)
    bird_wing(surf, w / 24, h / 6, wing_w, wing_h, 0)
    # body
    ellipse(surf, bird_color, (w * 0.3, h * 0.4, w * 0.4, h * 0.25))
    # legs
    bird_leg(surf, w * 0.45, h * 0.45, w * 0.55, h * 0.5, 0)
    bird_leg(surf, w * 0.35, h * 0.5, w * 0.55, h * 0.5, 0)
    # head
    bird_head(surf, w * 2 / 3, h * 0.43, w / 3, h / 6, 0)

    if orientation == 1:
        surf = pygame.transform.flip(surf, True, False)

    screen.blit(pygame.transform.rotate(surf, angle), (x, y))


# fish
def fish_fin_up(supersurf, x, y, w, h, angle):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))

    points = ((w * 134 / 214, h * 27 / 103),
              (w * 118 / 214, h * 13 / 103),
              (w * 103 / 214, h * 4 / 103),
              (w * 95 / 214, h * 0 / 103),
              (w * 164 / 214, h * 9 / 103),
              (w * 168 / 214, h * 13 / 103),
              (w * 171 / 214, h * 17 / 103),
              (w * 172 / 214, h * 21 / 103),
              (w * 171 / 214, h * 26 / 103),
              (w * 169 / 214, h * 31 / 103),
              (w * 134 / 214, h * 27 / 103))
    polygon(surf, fish_fin_color, points)
    aalines(surf, black, False, points)

    supersurf.blit(pygame.transform.rotate(surf, angle), (x, y))


def fish_fin_down_left(supersurf, x, y, w, h, angle):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))

    points = ((w * 94 / 214, h * 62 / 103),
              (w * 91 / 214, h * 70 / 103),
              (w * 84 / 214, h * 78 / 103),
              (w * 77 / 214, h * 82 / 103),
              (w * 109 / 214, h * 88 / 103),
              (w * 112 / 214, h * 84 / 103),
              (w * 112 / 214, h * 75 / 103),
              (w * 111 / 214, h * 67 / 103),
              (w * 94 / 214, h * 62 / 103))
    polygon(surf, fish_fin_color, points)
    aalines(surf, black, False, points)

    supersurf.blit(pygame.transform.rotate(surf, angle), (x, y))


def fish_fin_down_right(supersurf, x, y, w, h, angle):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))

    points = ((w * 157 / 214, h * 72 / 103),
              (w * 157 / 214, h * 88 / 103),
              (w * 159 / 214, h * 95 / 103),
              (w * 165 / 214, h * 103 / 103),
              (w * 194 / 214, h * 86 / 103),
              (w * 182 / 214, h * 83 / 103),
              (w * 174 / 214, h * 78 / 103),
              (w * 168 / 214, h * 72 / 103),
              (w * 157 / 214, h * 72 / 103))
    polygon(surf, fish_fin_color, points)
    aalines(surf, black, False, points)

    supersurf.blit(pygame.transform.rotate(surf, angle), (x, y))


def fish_body(supersurf, x, y, w, h, angle):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))

    points1 = ((w * 61 / 214, h * 49 / 103),
               (w * 102 / 214, h * 33 / 103),
               (w * 128 / 214, h * 27 / 103),
               (w * 142 / 214, h * 26 / 103),
               (w * 165 / 214, h * 28 / 103),
               (w * 182 / 214, h * 33 / 103),
               (w * 196 / 214, h * 41 / 103),
               (w * 214 / 214, h * 55 / 103),
               (w * 199 / 214, h * 64 / 103),
               (w * 180 / 214, h * 70 / 103),
               (w * 165 / 214, h * 74 / 103),
               (w * 142 / 214, h * 74 / 103),
               (w * 115 / 214, h * 70 / 103),
               (w * 79 / 214, h * 58 / 103),
               (w * 61 / 214, h * 49 / 103))
    points2 = ((w * 61 / 214, h * 49 / 103),
               (w * 9 / 214, h * 84 / 103),
               (w * 0 / 214, h * 38 / 103),
               (w * 15 / 214, h * 43 / 103),
               (w * 33 / 214, h * 48 / 103),
               (w * 48 / 214, h * 50 / 103),
               (w * 57 / 214, h * 49 / 103),
               (w * 61 / 214, h * 49 / 103))
    polygon(surf, fish_body_color, points1)
    aalines(surf, black, False, points1)
    polygon(surf, fish_body_color, points2)
    aalines(surf, black, False, points2)


    supersurf.blit(pygame.transform.rotate(surf, angle), (x, y))


def fish_eye_ellipse(supersurf, x, y, w, h, angle):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))
    ellipse(surf, fish_eye_color_3, (0, 0, w, h))
    supersurf.blit(pygame.transform.rotate(surf, angle), (x, y))


def fish_eye(supersurf, x, y, w, h, angle):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))

    ellipse(surf, fish_eye_color_1, (w * 173 / 214, h * 43 / 103, w * 18 / 214, h * 20 / 103))
    ellipse(surf, fish_eye_color_2, (w * 180 / 214, h * 51 / 103, w * 7 / 214, h * 9 / 103))
    fish_eye_ellipse(surf, w * 176 / 214, h * 49 / 103, w * 5 * 2 ** 0.5 / 214, h * 5 * 2 ** 0.5 / 103, -45)

    supersurf.blit(pygame.transform.rotate(surf, angle), (x, y))


def fish(x, y, w, h, angle, orientation):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))

    # fish_fin
    fish_fin_up(surf, 0, 0, w, h, 0)
    fish_fin_down_left(surf, 0, 0, w, h, 0)
    fish_fin_down_right(surf, 0, 0, w, h, 0)
    # fish_body
    fish_body(surf, 0, 0, w, h, 0)
    # fish_eye
    fish_eye(surf, 0, 0, w, h, 0)

    if orientation == 1:
        surf = pygame.transform.flip(surf, True, False)

    screen.blit(pygame.transform.rotate(surf, angle), (x, y))


bg()
if second:
    pass
    # bird(window_w * 0.1, window_h * 0.5, window_w * 0.65, window_h * 0.35, 0, 0)
    # bird(window_w * 0.1, window_h * 0.5, window_w * 0.65, window_h * 0.35, 0, 1)
    # bird(window_w * 0.1, window_h * 0.5, window_w * 0.65, window_h * 0.35, 0, 0)
    # fish(window_w * 0.6, window_h * 0.8, window_w * 0.25, window_h * 0.1, 0, 0)
    # fish(window_w * 0.6, window_h * 0.8, window_w * 0.25, window_h * 0.1, 0, 1)
    # fish(window_w * 0.6, window_h * 0.8, window_w * 0.25, window_h * 0.1, 0, 0)
else:
    bird(window_w * 0.1, window_h * 0.5, window_w * 0.65, window_h * 0.35, 0, 0)
    fish(window_w * 0.6, window_h * 0.8, window_w * 0.25, window_h * 0.1, 0, 0)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
