import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.image.load('assets/images/players and turret stuff/tile_0110.png'), 90)
        self.image = pygame.transform.scale_by(self.image, 1.6)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 50, 290
        self.velocity = 1

    def update(self, keys):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)