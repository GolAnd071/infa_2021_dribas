import pygame
from pygame.draw import *

pygame.init()

window_w = 600
window_h = 800
white = (255, 255, 255)
black = (0, 0, 0)
FPS = 30
screen = pygame.display.set_mode((window_w, window_h))


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
    bird_w1 = window_w / 3
    bird_h1 = window_h / 24
    bg_bird(window_w / 10, window_h / 18, bird_w1, bird_h1, 30)
    bg_bird(window_w * 3 / 5, window_h / 6, bird_w1, bird_h1, 0)
    bg_bird(window_w / 5, window_h / 3, bird_w1, bird_h1, -10)


# bird
def bird_head(x, y, w, h, angle):
    # bird_head
    # bird_eye
    # bird_beak
    pass


def bird_wing(x, y, w, h, angle, orientation):
    pass


def bird_leg_ellipse(supersurf, x, y, w, h, angle):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))
    ellipse(surf, white, (0, 0, w, h))
    supersurf.blit(pygame.transform.rotate(surf, angle), (x, y))


def bird_paw(supersurf, x, y, w, h, angle, orientation):
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
    polygon(surf, (255, 230, 128), points)
    aalines(surf, black, False, points)

    supersurf.blit(pygame.transform.rotate(surf, angle), (x, y))


def bird_leg(supersurf, x, y, w, h, angle, orientation):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 0))

    # leg_body
    bird_leg_ellipse(surf, 0, 0, w * 0.4, h * 0.2, -60)
    bird_leg_ellipse(surf, w * 0.2, h * 0.4, w * 0.4, h * 0.15, -30)

    # paw
    bird_paw(surf, w * 85 / 175, h * 115 / 175, w * 55 / 175, h * 65 / 175, 0, 0)

    supersurf.blit(pygame.transform.rotate(surf, angle), (x, y))


def bird(x, y, w, h, angle, orientation):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 128))

    # body
    ellipse(surf, white, (w * 0.3, h * 0.3, w * 0.45, h * 0.25))
    #legs
    bird_leg(surf, w * 0.45, h * 0.35, w * 0.55, h * 0.5, 0, 0)
    bird_leg(surf, w * 0.35, h * 0.4, w * 0.55, h * 0.5, 0, 0)

    screen.blit(pygame.transform.rotate(surf, angle), (x, y))


# fish
def fish_eye(x, y, w, h, angle):
    pass


def fish_fin(x, y, w, h, angle, orientation, curve):
    pass


def fish_body(x, y, w, h, angle, orientation):
    pass


def fish(x, y, w, h, angle, orientation):
    pass



#    surf = pygame.Surface((w, h), pygame.SRCALPHA)
#    surf.fill((255, 255, 255, 0))
#    screen.blit(pygame.transform.rotate(surf, angle), (x, y))


bg()
bird(window_w * 0.1, window_h * 0.5, window_w * 0.65, window_h * 0.35, 0, 0)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
