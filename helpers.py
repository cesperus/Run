import pygame
from random import randint

# this function will take 2 surfaces and center the 2nd surface on the first one
def center_surfaces(bg, fg):
    # get the bg width and height
    bg_width = bg.get_width()
    bg_height = bg.get_height()
    # get the front surface width and height
    fg_width = fg.get_width()
    fg_height = fg.get_height()
    # blit the text on the surface
    bg.blit(fg, (bg_width/2 - fg_width/2, bg_height/2-fg_height/2 ))

def make_background(screen):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    ground_tile = pygame.image.load('assets/images/puffer_fish.png')

    # get tile size info
    tile_width = water_tile.get_width()
    tile_height = water_tile.get_height()

    # make a background
    background = pygame.Surface((WIDTH,HEIGHT))

    # draw ground tiles
    for x in range(0,WIDTH,tile_width):
        for y in range(0,HEIGHT,tile_height):
            background.blit(ground_tile, (x,y))

    # draw some small trash on ground
    num_plants = 6
    for p in range(num_plants):
        background.blit(plant_tile,
                        (randint(0, WIDTH),randint(HEIGHT-3*tile_height, HEIGHT-1*tile_height)))
    return background