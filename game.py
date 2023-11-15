# initialize game

# Example file showing a basic pygame "game loop"
import pygame
from helpers import *
from runner import *
from turret import *

# pygame setup
pygame.init()
# make a clock
clock = pygame.time.Clock()
# set the resolution of our game window
WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Make my background once!
background = make_background(screen)




# make map

# would be cool to add foxholes, will definitely add walls and stuff to hide behind

