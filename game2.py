import pygame
import os
from helpers import *
from turret import *
from runner import *


# initialize pygame
pygame.init()
# sound mixer
pygame.mixer.init()

shooting_sound = pygame.mixer.Sound('assets/audios/shooting.wav')
scurry_sound = pygame.mixer.Sound('assets/audios/scurry.wav')
scurry_sound.set_volume(.4)
tank_sound = pygame.mixer.Sound('assets/audios/tank.wav')
tank_sound.set_volume(.4)


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

# make bullet group
bullet_group = pygame.sprite.Group()

# shooting cooldown to prevent spam & lag
SHOOT_COOLDOWN = 400
lastshot = 0


run = True
while run:
    # draw the background on the screen
    screen.blit(background, (0, 0))

    # general ender and event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # events for moving tank
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                my_turret.move(-10)  # Adjust the movement values as needed
                tank_sound.play()
            elif event.button == 5:  # Scroll down
                my_turret.move(10)  # Adjust the movement values as needed
                tank_sound.play()
            elif event.button == 1:
                # how long since last shot
                timenow = pygame.time.get_ticks()
                if timenow - lastshot > SHOOT_COOLDOWN:
                    # bullet instance and add it to the bullet group
                    bullet = Bullet(my_turret.rect.center)
                    bullet_group.add(bullet)
                    lastshot = timenow
                    # Play the shooting sound
                    shooting_sound.play()


        # events for moving player
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                my_player.rect.y -= my_player.velocity  # Move up
                scurry_sound.play()
            elif event.key == pygame.K_a:
                my_player.rect.x -= my_player.velocity  # Move left
                scurry_sound.play()
            elif event.key == pygame.K_s:
                my_player.rect.y += my_player.velocity  # Move down
                scurry_sound.play()
            elif event.key == pygame.K_d:
                my_player.rect.x += my_player.velocity  # Move right
                scurry_sound.play()


    keys = pygame.key.get_pressed()
    player_group.update(keys)
    player_group.draw(screen)

    turret_group.draw(screen)

    bullet_group.update(player_group)
    bullet_group.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

    print("Player Rect:", my_player.rect)


# would be cool to add foxholes, will definitely add walls and stuff to hide behind

pygame.quit()