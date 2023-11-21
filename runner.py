import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.image = pygame.image.load(os.path.join('assets', 'images', 'players and turret stuff', 'tile_0110.png'))
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 50, 290
        self.velocity = 2.5

    def update(self):
        self.rect.x = self.velocity
        self.rect.y = self.velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)