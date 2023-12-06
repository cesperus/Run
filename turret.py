import pygame
import random
import math

class Turret(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.image.load('assets/images/players and turret stuff/tankBeige_outline.png'),0)
        self.image = pygame.transform.scale_by(self.image, .6)
        self.rect = self.image.get_rect()
        self.rect.center = (1056, 320)

    def move(self, direction):
        '''moves turret vertically'''
        self.rect.y += direction
        # Keep the object within the screen bounds
        self.rect.y = max(0, min(self.rect.y, 590))

    def draw(self, screen):
        '''draws turret on screen'''
        screen.blit(self.image, self.rect)

# bullet class, capped at 8 bullets at one time, and maybe add rocket with right click
class Bullet(pygame.sprite.Sprite):
    def __init__(self, turret_position):
        super().__init__()
        self.image = pygame.image.load('assets/images/players and turret stuff/green_smallbullet.png')
        self.rect = self.image.get_rect()
        self.rect.center = turret_position
        self.velocity = 2
    def update(self, player_group):
        '''updates bullet's pos and checks if bullet collides goes off-screen'''
        # bullet first left
        self.rect.x -= self.velocity

        # remove the bullet when it goes off the screen
        if self.rect.right < 0:
            self.kill()