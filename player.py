import pygame

class Player:
    width = 30
    height = 30
    jumpPower = 12
    gravity = 0.68

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

    def jump(self):
        if self.onGround:
            self.velY = -self.jumpPower
            self.onGround = False

    def update(self):
        self.velY += self.gravity
        self.rect.y += self.velY

        if self.rect.y >= self.groundY:
            self.rect.y = self.groundY
            self.velY = 0
            self.onGround = True
    
    def collideCheck(self, other):
        for wall in other:
            if self.rect.colliderect(wall.rect):
                self.alive = False
                print("dead")
                return
