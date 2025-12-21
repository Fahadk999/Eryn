import pygame

class Player:
    width = 30
    height = 30
    jumpPower = {
            "high" : 12,
            "mid" : 10,
            "low" : 8 
            }
    gravity = 0.6

    def __init__(self, sWidth, sHeight):
        self.alive = True
        self.sWidth = sWidth
        self.sHeight = sHeight
        self.x = sWidth // 4
        self.y = sHeight - self.height
        self.groundY = sHeight - self.height
        self.color = "red"

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.velY = 0
        self.onGround = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def jump(self, power):
        if self.onGround:
            self.velY = -self.jumpPower[power]
            self.onGround = False

    def update(self):
        self.velY += self.gravity
        self.rect.y += self.velY

        if self.rect.y >= self.groundY:
            self.rect.y = self.groundY
            self.velY = 0
            self.onGround = True
            



    
