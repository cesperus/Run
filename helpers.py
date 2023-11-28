import pygame

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


WIDTH = 720 * (3 / 2)
HEIGHT = 720


def make_background(screen):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    plaintile = pygame.image.load('assets/images/groundtextures/plain_ground.png')
    plain_dirtupper = pygame.image.load('assets/images/groundtextures/plainupper.png')
    plain_dirtupperright = pygame.image.load('assets/images/groundtextures/plaincornerUR.png')
    bigrocks = pygame.image.load('assets/images/groundtextures/bigrocks.png')
    pebbles = pygame.image.load('assets/images/groundtextures/rocky.png')
    rocky_dirtupper = pygame.image.load('assets/images/groundtextures/rockyupper.png')

    # get tile size info
    tile_width = plaintile.get_width()
    tile_height = plaintile.get_height()
    # make a background
    background = pygame.Surface((WIDTH, HEIGHT))
    # draw ground tiles
    for x in range(0, WIDTH, tile_width):
        for y in range(0, HEIGHT, tile_height):
            background.blit(plaintile, (x, y))
    # draw sand tile
    for x in range(0, WIDTH, tile_width):
        background.blit(bigrocks, (x, HEIGHT - tile_height))
    # draw sand top tile
    for x in range(0, WIDTH, tile_width):
        background.blit(plain_dirtupper, (x, HEIGHT - 2 * tile_height))
    return background
