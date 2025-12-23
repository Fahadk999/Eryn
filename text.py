import pygame
import os

pygame.font.init()

class Text:
    # File path to font
    # Fix this font for numbers
    fontFilePath = os.path.join("Resources", "Fonts", "Arena-rvwaK.ttf")

    def __init__(self, txt, x, y, width, height, color, size):
        try:
            self.font = pygame.font.SysFont(None, size)
        except FileNotFoundError:
            print(f"File not found {self.fontFilePath}")

        self.txt = txt
        self.color = color
        self.textSurface = self.font.render(self.txt, True, self.color)
        self.rect = self.textSurface.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.textSurface, self.rect)

    def updateText(self, txt):
        self.txt = txt
        self.textSurface = self.font.render(self.txt, True, self.color)

    def setFontSize(self, size):
        self.font = pygame.font.SysFont(None, size)
        self.textSurface = self.font.render(self.txt, True, self.color)
    
    def setPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y
