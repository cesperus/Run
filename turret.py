import pygame
import random

class Turret(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        #self.image = pygame.Surface((150,50))
        #self.image.fill((0,0,220))
        self.image = pygame.transform.rotate(pygame.image.load('assets/images/players and turret stuff/weapon_bow_arrow.png'),90)
        self.image = pygame.transform.scale_by(self.image, .6)
        self.rect = self.image.get_rect()
        self.rect.x = 1040
        self.rect.y = (640/2)-(40/2)

    def update(self):
        None
    def draw(self, screen):
        screen.blit(self.image, self.rect)