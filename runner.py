import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.image.load('assets/images/players and turret stuff/tile_0110.png'), 90)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (40, 320)
        self.velocity = 1.5

    def move(self, up, down, right, left):
        self.rect.y -= up
        self.rect.y += down
        self.rect.x += right
        self.rect.x -= left
        # Keep the player within the screen bounds
        self.rect.y = max(0, min(self.rect.y, 640 - self.rect.height))
        self.rect.x = max(0, min(self.rect.x, 1088 - self.rect.width))


def draw(self, screen):
        screen.blit(self.image, self.rect)