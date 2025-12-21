import pygame

from player import Player
from obs import Obsticle
from random import choice
from text import Text

class Game:
    def __init__(self, sWidth, sHeight):
        self.sWidth = sWidth
        self.sHeight = sHeight
        self.SPAWNENEMY = pygame.event.custom_type()
        pygame.time.set_timer(self.SPAWNENEMY, 2500)

        self.player = Player(sWidth, sHeight)
        self.others = []
        self.text = Text("Text", 10, 10, 100, 100) 

    def draw(self, screen):
        self.text.draw(screen)
        self.player.draw(screen)
        for other in self.others:
            other.draw(screen)

    def update(self, screen):
        screen.fill("grey")
        self.player.update()
        self.player.collideCheck(self.others)
        for other in self.others:
            other.move(self.player)

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
            if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
                self.player.jump()
        if event.type == self.SPAWNENEMY:
            self.addEnemy()

    def makeMenu(self, screen):
        pass
    def makeGameover(self, screen):
        pass
