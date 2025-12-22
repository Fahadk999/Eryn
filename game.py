import pygame
from player import Player
from obs import Obstacle
from random import choice
from text import Text

class Game:
    def __init__(self, sWidth, sHeight):
        self.sWidth = sWidth
        self.sHeight = sHeight

        self.SPAWNENEMY = pygame.event.custom_type()
        self.baseSpawnInterval = 2500  # starting spawn interval in ms
        pygame.time.set_timer(self.SPAWNENEMY, self.baseSpawnInterval)

        self.score = 0
        self.gameOverText = Text("Game Over!", self.sWidth//2 - 100, self.sHeight//2 - 50, 200, 100, "black", 40)
        self.player = Player(sWidth, sHeight)
        self.baseSpeed = 6
        self.speed = self.baseSpeed
        self.others = []
        self.scoreText = Text(f"Score: {self.score}", 10, 10, 150, 100, "black", 30)

        # Level-based scaling
        self.level = 1
        self.nextLevelScore = 100  # score required to reach next level
        self.levelIncrement = 0.5   # speed increase per level
        self.minSpawnInterval = 500

    def draw(self, screen):
        if self.player.alive:
            self.scoreText.draw(screen)
            self.player.draw(screen)
            for other in self.others:
                other.draw(screen)
        else:
            self.makeGameover(screen)

    def update(self, screen, dt):
        screen.fill("grey")
        if self.player.alive:
            # Update score
            self.score += dt * 10
            self.scoreText.updateText(f"Score: {int(self.score)}")

            # Check if we should increase level
            if self.score >= self.nextLevelScore:
                self.level += 1
                self.speed += self.levelIncrement
                self.nextLevelScore += 100  # next level at higher score

                # Decrease spawn interval slightly
                newInterval = max(self.minSpawnInterval, 
                                   int(self.baseSpawnInterval - (self.level - 1) * 100))
                pygame.time.set_timer(self.SPAWNENEMY, newInterval)

            # Update obstacle speed
            for other in self.others:
                other.speed = self.speed
                other.move(self.player)

            # Update player
            self.player.update()
            self.player.collideCheck(self.others)

    def addEnemy(self):
        blocks = (
            Obstacle(45, 45, self.sWidth, self.sHeight, self.speed),
            Obstacle(30, 30, self.sWidth, self.sHeight, self.speed),
            Obstacle(30, 60, self.sWidth, self.sHeight, self.speed),
            Obstacle(60, 30, self.sWidth, self.sHeight, self.speed),
            Obstacle(70, 40, self.sWidth, self.sHeight, self.speed),
        )
        self.others.append(choice(blocks))

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
                self.player.jump()
            if not self.player.alive and event.key == pygame.K_RETURN:
                self.player.alive = True
                self.score = 0
                self.level = 1
                self.nextLevelScore = 100
                self.others.clear()
                self.scoreText.setPosition(10, 10)
                self.speed = self.baseSpeed
                pygame.time.set_timer(self.SPAWNENEMY, self.baseSpawnInterval)
                
        if event.type == self.SPAWNENEMY:
            self.addEnemy()

    def makeGameover(self, screen):
        self.gameOverText.draw(screen)
        self.scoreText.setPosition(self.sWidth//2 - 75, self.sHeight//2)
        self.scoreText.draw(screen) # set position of score text and retry button
