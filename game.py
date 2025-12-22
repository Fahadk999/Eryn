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
        self.base_spawn_interval = 2500  # starting spawn interval in ms
        pygame.time.set_timer(self.SPAWNENEMY, self.base_spawn_interval)

        self.score = 0
        self.player = Player(sWidth, sHeight)
        self.base_speed = 6
        self.speed = self.base_speed
        self.others = []
        self.scoreText = Text(f"Score: {self.score}", 10, 10, 300, 100, "black")

        # Level-based scaling
        self.level = 1
        self.next_level_score = 20  # score required to reach next level
        self.level_increment = 0.5   # speed increase per level
        self.min_spawn_interval = 500

    def draw(self, screen):
        self.scoreText.draw(screen)
        self.player.draw(screen)
        for other in self.others:
            other.draw(screen)

    def update(self, screen, dt):
        # Update score
        self.score += dt * self.speed
        self.scoreText.updateText(f"Score: {int(self.score)}")

        # Check if we should increase level
        if self.score >= self.next_level_score:
            self.level += 1
            self.speed += self.level_increment
            self.next_level_score += 20  # next level at higher score

            # Decrease spawn interval slightly
            new_interval = max(self.min_spawn_interval, 
                               int(self.base_spawn_interval - (self.level - 1) * 100))
            pygame.time.set_timer(self.SPAWNENEMY, new_interval)

        # Update obstacle speed
        for other in self.others:
            other.speed = self.speed
            other.move(self.player)

        # Update player
        screen.fill("grey")
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
        if event.type == self.SPAWNENEMY:
            self.addEnemy()

    def makeMenu(self, screen):
        pass

    def makeGameover(self, screen):
        pass
