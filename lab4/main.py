import pygame
from pygame.draw import *

pygame.init()

window_w = 600
window_h = 800
white = (255, 255, 255)
black = (0, 0, 0)
FPS = 30
screen = pygame.display.set_mode((window_w, window_h))


def rotate(self, angle):
    pygame.transform.rotate(self, angle)


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
def bird_head():
    # bird_head
    # bird_eye
    # bird_beak
    pass


def bird_wing(x, y, w, h, angle, orientation):
    pass


def bird_paw(x, y, w, h, angle, orientation):
    pass


def bird(x, y, w, h, angle, orientation):
    pass


# fish
def fish_eye(x, y, w, h, angle):
    pass


def fish_fin(x, y, w, h, angle, orientation, curve):
    pass


def fish_body(x, y, w, h, angle, orientation):
    pass


def fish(x, y, w, h, angle, orientation):
    pass


bg()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
