import pygame
import os

pygame.font.init()

class Text:
    # File path to font
    fontFilePath = os.path.join("Resources", "Fonts", "Arena-rvwaK.ttf")

    def __init__(self, txt, x, y, width, height):
        try:
            self.font = pygame.font.Font(self.fontFilePath, 30)
        except FileNotFoundError:
            print(f"File not found {self.fontFilePath}")
            self.font = pygame.font.SysFont(None, 30)

        self.textSurface = self.font.render(txt, True, "red")
        self.rect = self.textSurface.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.textSurface, self.rect)
