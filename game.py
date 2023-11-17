# Example file showing a basic pygame "game loop"
import pygame
import os
from helpers import *
from runner import *
from turret import *

# initialize pygame
pygame.init()

# set screen size
WIDTH = 1080
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# just adding in a rectangle to hold the place of where I want my turret eventually, on the far right side, in the middle.
# Maybe I will make it so that this can move later
# Also adding locations as variables
turret_loc = (1040, (640/2)-(40/2), 40, 40)
turret_placehold = pygame.Rect(turret_loc)
player_loc = (50, (640/2)-(60/2), 50, 60)
player_placeholder = pygame.Rect(player_loc)

# import assets for interactable objects
player = pygame.image.load(os.path.join('assets', 'images', 'players and turret stuff', 'tile_0110.png'))
turret = pygame.image.load(os.path.join('assets', 'images', 'players and turret stuff', 'weapon_bow_arrow.png'))

# make a clock
clock = pygame.time.Clock()
FPS = 60

# set player speed
player_speed = 2.5
player_x, player_y = player_placeholder.x, player_placeholder.y

run = True
while run:
    # fill in color for background
    screen.fill((0, 255, 0))

    # gives the placeholder turret a color value, and draws it on the screen
    pygame.draw.rect(screen, (200, 0, 0), turret_placehold)

    # draw player placeholder
    pygame.draw.rect(screen, (0, 200, 0), player_placeholder)

    # add some key actions to move a player + make the stop when they hit an x or y bound
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] and player_x - player_speed > 0:
        player_x -= player_speed
    elif keys_pressed[pygame.K_d] and player_x + player_speed < WIDTH - player_placeholder.width:
        player_x += player_speed
    elif keys_pressed[pygame.K_w] and player_y - player_speed > 0:
        player_y -= player_speed
    elif keys_pressed[pygame.K_s] and player_y + player_speed < HEIGHT - player_placeholder.height:
        player_y += player_speed

    # Update player position as integers
    player_placeholder.x, player_placeholder.y = int(player_x), int(player_y)

    # general ender
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    # show the most recent things drawn
    pygame.display.update()

    #control the frame rate
    clock.tick(FPS)





# set the resolution of our game window


# Make my background once!
background = make_background(screen)




# make map

# would be cool to add foxholes, will definitely add walls and stuff to hide behind

pygame.quit()
