import pygame
import os
from helpers import *
from turret import *
from runner import *


# initialize pygame
pygame.init()

# set screen size
WIDTH = 1088
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()  # Create a clock object
FPS = 60  # Adjust the frame rate as needed

# make background
background = make_background(screen)

# my turret instance
my_turret = Turret(screen)
turret_group = pygame.sprite.Group()
turret_group.add(my_turret)

# my player instance
my_player = Player(screen)
player_group = pygame.sprite.Group()
player_group.add(my_player)


run = True
while run:
    # draw the background on the screen
    screen.blit(background, (0, 0))

     # general ender
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                my_turret.move(-10)  # Adjust the movement values as needed
            elif event.button == 5:  # Scroll down
                my_turret.move(10)  # Adjust the movement values as needed

    keys = pygame.key.get_pressed()

    # Update the player's position based on keys and velocity
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        my_player.rect.x -= 1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        my_player.rect.x += 1
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        my_player.rect.y -= 1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        my_player.rect.y += 1


    player_group.update(keys)
    player_group.draw(screen)


    turret_group.draw(screen)

    pygame.display.flip()
# would be cool to add foxholes, will definitely add walls and stuff to hide behind

pygame.quit()