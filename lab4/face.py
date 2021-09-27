import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# background
rect(screen, pygame.Color(200, 200, 200), (0, 0, 400, 400))

# face
circle(screen, pygame.Color(255, 255, 0), (200, 200), 120)
circle(screen, pygame.Color(0, 0, 0), (200, 200), 120, 1)  # border

# mouth
rect(screen, pygame.Color(0, 0, 0), (140, 260, 120, 20))


# eyes
def eye(x, y, radius):
    circle(screen, pygame.Color(255, 0, 0), (x, y), radius)
    circle(screen, pygame.Color(0, 0, 0), (x, y), radius, 1)  # border
    circle(screen, pygame.Color(0, 0, 0), (x, y), radius / 2)


eye(150, 180, 20)
eye(250, 175, 10)


# brows
polygon(screen, pygame.Color(0, 0, 0), [(219, 166), (298, 137), (301, 144), (223, 174)])
polygon(screen, pygame.Color(0, 0, 0), [(103, 116), (182, 166), (177, 174), (98, 124)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
