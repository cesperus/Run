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
        self.scroll_direction = 0

    def move(self, where):
        self.rect.y += where
        # Keep the object within the screen bounds
        self.rect.y = max(0, min(self.rect.y, 590))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# bullet class, capped at 8 bullets at one time, and maybe add rocket with right click
class Bullet(pygame.sprite.Sprite):
    def __init__(self, turret_position):
        super().__init__()
        # attributes  image, rect, velocity
        self.image = pygame.image.load('assets/images/players and turret stuff/green_smallbullet.png')
        self.image = pygame.transform.scale_by(self.image, 1)
        self.rect = self.image.get_rect()
        self.rect.center = turret_position
        self.velocity = 3
    def update(self, player_group):
        # bullet first left
        self.rect.x -= self.velocity

        # Check for collisions with player
        collisions = pygame.sprite.spritecollide(self, player_group, False)
        if collisions:
            # Handle collision with player (you can add specific actions here)
            self.kill()

        # Remove the bullet when it goes off the screen
        if self.rect.right < 0:
            self.kill()




# wordbank: this is the scroll-wheel stuff for the turret

#    elif event.type == pygame.MOUSEBUTTONDOWN:
#    if event.button == 4:  # Scroll wheel up
#        self.object.scroll_direction = -1
#    elif event.button == 5:  # Scroll wheel down
#        self.object.scroll_direction = 1
#    elif event.type == pygame.MOUSEBUTTONUP:
#        if event.button in [4, 5]:
#            self.object.scroll_direction = 0