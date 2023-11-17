# Example file showing a basic pygame "game loop"
import pygame
import os
from helpers import *
from runner import *
from turret import *
import math

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

# initialize empty bullet list
bullets = []
dead_bullets = []
BULLET_SIZE = (5,5)
MAX_BULLETS = 8
BULLET_COUNTDOWN = .1

# make a clock
clock = pygame.time.Clock()
FPS = 60

# set player speed
player_speed = 2.5
player_color = (0, 200, 0)
player_x, player_y = player_placeholder.x, player_placeholder.y

# bullet class, eventually cap # of bullets at 4 at one time, and maybe add rocket with right click
class Bullet:
    def __init__(self, x, y, angle):
        self.rect = pygame.Rect(x, y, *BULLET_SIZE)
        self.speed = 3
        self.angle = angle

    def update(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)

# make a turret instance
my_turret = Turret(screen)
turret_group = pygame.sprite.Group()
turret_group.add(my_turret)

cooldown_timer = 0
run = True
while run:
    # fill in color for background
    screen.fill((58, 100, 189))

    # shooting from turret event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Get the angle between turret and mouse
            # note: used ChatGPT to get the following 2 lines of code
            mouse_x, mouse_y = pygame.mouse.get_pos()
            angle = math.atan2(mouse_y - turret_placehold.centery, mouse_x - turret_placehold.centerx)
            # Check if the number of bullets is less than the limit
            if len(bullets) < MAX_BULLETS:
                # If there are inactive bullets, reuse one
                if dead_bullets:
                    bullet = dead_bullets.pop()
                    bullet.rect.x = turret_placehold.centerx
                    bullet.rect.y = turret_placehold.centery
                    bullet.angle = angle
                else:
                    # Otherwise, create a new bullet
                    bullet = Bullet(turret_placehold.centerx, turret_placehold.centery, angle)

                # Add the bullet to the active list
                bullets.append(bullet)
                # cooldown
                cooldown_timer = BULLET_COUNTDOWN

    # Update cooldown timer
    if cooldown_timer > 0:
        cooldown_timer -= 1 / FPS  # Decrement the timer

    # Update and draw active bullets
    for bullet in bullets:
        pygame.draw.rect(screen, (0, 0, 0), bullet.rect)
        bullet.update()

        # Check if the bullet hits the player
        if bullet.rect.colliderect(player_placeholder):
            player_color = (255, 0, 0)  # Change player color to red
            # You might want to handle additional logic here, such as reducing player health

            # Move the bullet to the inactive list
            bullets.remove(bullet)
            dead_bullets.append(bullet)
        # Check if the bullet is off-screen
        if not (0 <= bullet.rect.x <= WIDTH and 0 <= bullet.rect.y <= HEIGHT):
            # Move the bullet to the inactive list
            bullets.remove(bullet)
            dead_bullets.append(bullet)

    # Draw the placeholder turret
    pygame.draw.rect(screen, (200, 0, 0), turret_placehold)

    # Draw the real turret on top
    turret_group.draw(screen)

    # Draw the player placeholder
    pygame.draw.rect(screen, player_color, player_placeholder)

    # add some key actions to move a player + make the stop when they hit the x or y boundaries
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

# Make my background once
background = make_background(screen)
# make a map eventually

# would be cool to add foxholes, will definitely add walls and stuff to hide behind

pygame.quit()
