import pygame
import sys

from game import Game

pygame.init()

WIDTH, HEIGHT = 1020, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

GAME = Game(WIDTH, HEIGHT)

running = True

while running:
    dt = clock.tick(60) / 1000 # seconds since last frame
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or
            (event.type == pygame.KEYDOWN and
             event.key == pygame.K_ESCAPE)):
            running = False
        GAME.handleEvent(event)

    GAME.update(screen, dt)

    GAME.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
# look in to task.txt for more to do
