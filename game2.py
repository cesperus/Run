import pygame
import os
from helpers import *


# initialize pygame
pygame.init()

# set screen size
WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# make background

background = make_background(screen)

