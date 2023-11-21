import pygame
import random
import math

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

# bullet class, capped at 8 bullets at one time, and maybe add rocket with right click
class Bullet:
    def __init__(self, x, y, angle):
        self.rect = pygame.Rect(x, y, 5, 5)
        self.speed = 3
        self.angle = angle

    def update(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)