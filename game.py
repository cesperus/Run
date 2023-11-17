# Example file showing a basic pygame "game loop"
import pygame
from helpers import *
from runner import *
from turret import *

# set screen size

WIDTH = 1080
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# just adding in a rectangle to hold the place of where I want my turret eventually,
# on the far right side, in the middle. Maybe I will make it so that this can move later
turret_placehold = pygame.Rect((1040, (640/2)-(40/2), 40, 40))
player_placeholder = pygame.Rect((50, (640/2)-(60/2), 50, 60))


# initialize pygame
pygame.init()

run = True
while run:

    # give player placeholder
    pygame.draw.rect(screen, (0, 200, 0), player_placeholder)

    # gives the placeholder turret a color value, and draws it on the screen
    pygame.draw.rect(screen, (200 , 0 , 0), turret_placehold)

    # add some key actions to move a player


    # general ender
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # show the most recent things drawn
    pygame.display.update()




# make a clock
clock = pygame.time.Clock()
# set the resolution of our game window


# Make my background once!
background = make_background(screen)




# make map

# would be cool to add foxholes, will definitely add walls and stuff to hide behind

pygame.quit()
