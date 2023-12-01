import pygame
import math

WIDTH = 1088
HEIGHT = 640

# this function will take 2 surfaces and center the 2nd surface on the first one
def center_surfaces(bg, fg):
    # get the bg width and height
    bg_width = bg.get_width()
    bg_height = bg.get_height()
    # get the front surface width and height
    fg_width = fg.get_width()
    fg_height = fg.get_height()
    # blit the text on the surface
    bg.blit(fg, (bg_width / 2 - fg_width / 2, bg_height / 2 - fg_height / 2))


def tile_repo(tile_num):
    if tile_num == 0:
        return pygame.image.load('assets/images/groundtextures/plain_ground.png')
    if tile_num == 1:
        return pygame.image.load('assets/images/groundtextures/plainupper.png')
    if tile_num == 2:
        return pygame.image.load('assets/images/groundtextures/plaincornerUR.png')
    if tile_num == 3:
        return pygame.image.load('assets/images/groundtextures/bigrocks.png')
    if tile_num == 4:
        return pygame.image.load('assets/images/groundtextures/rocky.png')
    if tile_num == 5:
        return pygame.image.load('assets/images/groundtextures/rockyupper.png')
    if tile_num == 6:
        return pygame.image.load('assets/images/groundtextures/plaincornerSUL.png')
    if tile_num == 7:
        return pygame.image.load('assets/images/groundtextures/rail.png')

def make_background(screen):  # adam led me through a lot of this
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    bg = pygame.Surface((WIDTH, HEIGHT))

    # make a background
    background = [
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7],
            [3, 4, 4, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3, 4, 4, 3, 7],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 3],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 3],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 3],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
    ]

    for y in range(0,10):
        for x in range(0,17):
            tile = background[y][x]
            tile_type = tile_repo(tile)
            tile_type = pygame.transform.scale(tile_type, (64,64))
            bg.blit(tile_type, (x*64, y*64))


    return bg

def Menu(screen):
    None
def UDied(screen):
    None
