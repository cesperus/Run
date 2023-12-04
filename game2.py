import pygame
import os
from helpers import *
from turret import *
from runner import *


# initialize pygame
pygame.init()
# sound mixer
pygame.mixer.init()
# fonts for title
pygame.font.init()

shooting_sound = pygame.mixer.Sound('assets/audios/shooting.wav')
scurry_sound = pygame.mixer.Sound('assets/audios/scurry.wav')
scurry_sound.set_volume(.4)
tank_sound = pygame.mixer.Sound('assets/audios/tank.wav')
tank_sound.set_volume(.4)
dead = pygame.mixer.Sound('assets/audios/death.mp3')


# set screen size
WIDTH = 1088
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()  # Create a clock object
FPS = 60  # Adjust the frame rate as needed

# trying to add a 'You Died' screen
class GameState:
    MENU = 0
    PLAYING = 1
    GAME_OVER = 2
    WINNER = 3

# where the player needs to get (w/o being shot) in order to win
FINISH_LINE = 910

# Initialize game state
current_game_state = GameState.MENU

# make background
background = make_background(screen)

# Game title
font = pygame.font.SysFont('calibri', 80)

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
SHOOT_COOLDOWN = 600
lastshot = 0


run = True
while run:
    # draw the background on the screen
    screen.blit(background, (0, 0))

    # general ender and event loop
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if current_game_state == GameState.MENU:
        # Display menu elements - used Chat GPT for next 5 lines
        header_text = font.render("No Man's Land", True, (128, 0, 0))
        start_button_text = font.render("Start Game (Return)", True, (10, 10, 10))

        # Draw header and start button on the screen
        screen.blit(header_text, (WIDTH // 2 - header_text.get_width() // 2, 100))
        screen.blit(start_button_text, (WIDTH // 2 - start_button_text.get_width() // 2, 200))

        # Check for key press to start the game
        if keys[pygame.K_RETURN]:
            current_game_state = GameState.PLAYING

    elif current_game_state == GameState.PLAYING:
        for event in events:
            # events for moving tank
            if event.type == pygame.MOUSEBUTTONDOWN:
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
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
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

        my_player.move(keys[pygame.K_w], keys[pygame.K_s], keys[pygame.K_d], keys[pygame.K_a])

        player_group.update(keys)
        player_group.draw(screen)

        turret_group.draw(screen)

        bullet_group.update(player_group)
        bullet_group.draw(screen)

        # Check for bullet collisions with player
        for player in player_group:
            hit = pygame.sprite.spritecollide(player, bullet_group, True)
            if hit:
                current_game_state = GameState.GAME_OVER
                dead.play()

        # Check if player reaches the winning x position
        if my_player.rect.x >= FINISH_LINE:
            current_game_state = GameState.WINNER

    elif current_game_state == GameState.GAME_OVER:
        # Display game over elements
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        restart_txt = font.render("Restart (Space)", True, (10, 10, 10))
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, 300))

        if keys[pygame.K_SPACE]:
            # Reset game state
            current_game_state = GameState.MENU

            # Reset player position
            my_player.rect.x = 0
            my_player.rect.y = 320

            # Reset turret position
            my_turret.rect.center = (1056, 320)

            # Clear bullets
            bullet_group.empty()

    elif current_game_state == GameState.WINNER:
        # Display winner elements
        winner_text = font.render("You Win!", True, (0, 255, 0))
        screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, 300))

    pygame.display.flip()

    clock.tick(FPS)

# would be cool to add foxholes, will definitely add walls and stuff to hide behind

pygame.quit()