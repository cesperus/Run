import pygame





# bullet class
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 5)
    def move(self, speed):
        self.rect.x += speed
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
