import pygame

from player import Player
from obs import Obsticle
from random import choice

class Game:
    def __init__(self, sWidth, sHeight):
        self.sWidth = sWidth
        self.sHeight = sHeight
        self.SPAWNENEMY = pygame.event.custom_type()
        pygame.time.set_timer(self.SPAWNENEMY, 2500)

        self.player = Player(sWidth, sHeight)
        self.others = []

    def draw(self, screen):
        self.player.draw(screen)
        for other in self.others:
            other.draw(screen)

    def update(self):
        self.player.update()
        for other in self.others:
            other.move()

    def addEnemy(self):
        blocks = (
            Obsticle(45, 45, self.sWidth, self.sHeight), # normal
            Obsticle(30, 30, self.sWidth, self.sHeight), # short
            Obsticle(30, 60, self.sWidth, self.sHeight), # tall
            Obsticle(40, 80, self.sWidth, self.sHeight), # taller
            Obsticle(60, 30, self.sWidth, self.sHeight), # long
            Obsticle(80, 40, self.sWidth, self.sHeight), # longer
        )

        self.others.append(choice(blocks))
    
    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                self.player.jump("high")
            elif event.key == pygame.K_d:
                self.player.jump("mid")
            elif event.key == pygame.K_s:
                self.player.jump("low")
        if event.type == self.SPAWNENEMY:
            self.addEnemy()
