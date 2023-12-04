import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.image.load('assets/images/players and turret stuff/tile_0110.png'), 90)
        self.image = pygame.transform.scale(self.image, (40, 40))  # Set width and height
        self.rect = self.image.get_rect()
        self.rect.center = (50, 290)
        self.velocity = 8

    def move(self, where, far):
        self.rect.y += where
        self.rect.x += far
        # Keep the object within the screen bounds
        self.rect.y = max(0, min(self.rect.y, 590))
        self.rect.x = max(0, min(self.rect.x, 1050))

    def draw(self, screen):
        screen.blit(self.image, self.rect)