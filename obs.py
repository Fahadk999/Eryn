#-------- Obstacle --------
import pygame

class Obstacle:
    def __init__(self, width, height, sWidth, sHeight, speed=4):
        self.width = width
        self.height = height
        self.sWidth = sWidth
        self.sHeight = sHeight
        self.x = sWidth - 30
        self.y = sHeight - self.height
        self.speed = speed
        self.color = "cyan"
        self.outOfScreen = False

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, other):
        self.rect.x -= self.speed
        if self.rect.x >= 100:
            self.outOfScreen = True
