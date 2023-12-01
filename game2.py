import pygame
import os
from helpers import *
from turret import *


# initialize pygame
pygame.init()

# set screen size
WIDTH = 1088
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# make background
background = make_background(screen)

# make a turret instance
my_turret = Turret(screen)
turret_group = pygame.sprite.Group()
turret_group.add(my_turret)

run = True
while run:
    # draw the background on the screen
    screen.blit(background, (0, 0))

     # general ender
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    turret_group.draw(screen)

    pygame.display.flip()
# would be cool to add foxholes, will definitely add walls and stuff to hide behind

pygame.quit()