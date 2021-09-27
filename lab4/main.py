import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))


# background
def bg_bird():
    pass


def background():
    pass


# bird
def bird_head():
    pass


def bird_wing():
    pass


def bird_paw():
    pass


def bird():
    pass


# fish



def fish():
    pass

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()