import pygame
import random
import math

class Turret(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        #self.image = pygame.Surface((150,50))
        #self.image.fill((0,0,220))
        self.image = pygame.transform.rotate(pygame.image.load('assets/images/players and turret stuff/tankBeige_outline.png'),0)
        self.image = pygame.transform.scale_by(self.image, .6)
        self.rect = self.image.get_rect()
        self.rect.center = (1056, 200)
        self.scroll_direction = 0  # 1 for scrolling up, -1 for scrolling down

    def update(self):
        self.rect.y += self.scroll_direction * 5  # Adjust the speed as needed
        self.rect.y = max(0, min(self.rect.y, 350))  # Keep the object within the screen bounds

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# bullet class, capped at 8 bullets at one time, and maybe add rocket with right click
class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        # attributes  image, rect, velocity
        self.image = pygame.image.load('assets/images/players and turret stuff/green_smallbullet.png')
        self.image = pygame.transform.scale_by(self.image, 0.05)
        self.rect = self.image.get_rect()
        self.rect.midleft = pos
        self.velocity = 3
        self.angle = angle
    def update(self):
        # bullet fires left
        self.rect.x -= self.velocity
    def update(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)




# wordbank: this is the scroll-wheel stuff for the turret

#    elif event.type == pygame.MOUSEBUTTONDOWN:
#    if event.button == 4:  # Scroll wheel up
#        self.object.scroll_direction = -1
#    elif event.button == 5:  # Scroll wheel down
#        self.object.scroll_direction = 1
#    elif event.type == pygame.MOUSEBUTTONUP:
#        if event.button in [4, 5]:
#            self.object.scroll_direction = 0