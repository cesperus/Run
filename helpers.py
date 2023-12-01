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


WIDTH = 1088
HEIGHT = 704


def make_background(screen):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()

    # make a background
    background = [
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
    ]

    for y in range(0,11):
        for x in range(0,17):
            tile = background[y][x]
            tile_type = tile_repo(tile)
            tile_type = pygame.transform.scale(tile_type, (64,64))
            background.blit(tile_type, (x*64, y*64))


    return background

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
