import pygame
import os
from helpers import *
from turret import *
from runner import *


# initialize pygame
pygame.init()
# initialize sound mixer
pygame.mixer.init()
# initialize fonts
pygame.font.init()

# load in game sounds, & set volumes for sounds too loud
shooting_sound = pygame.mixer.Sound('assets/audios/shooting.wav')
scurry_sound = pygame.mixer.Sound('assets/audios/scurry.wav')
scurry_sound.set_volume(.4)
tank_sound = pygame.mixer.Sound('assets/audios/tank.wav')
tank_sound.set_volume(.4)
dead = pygame.mixer.Sound('assets/audios/death.mp3')
background_music = pygame.mixer.Sound('assets/audios/background.mp3')
background_music.set_volume(.1)


# set screen size
WIDTH = 1088
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# create clock object & set FPS
clock = pygame.time.Clock()
FPS = 60

# define game status
class GameState:
    MENU = 0
    PLAYING = 1
    GAME_OVER = 2
    WINNER = 3

# where the player needs to get (w/o being shot) in order to win (placed between both rock tile columns)
FINISH_LINE = 926

# initialize game state (on menu screen)
current_game_state = GameState.MENU

# make background
background = make_background(screen)

# set font for game text
font = pygame.font.SysFont('calibri', 80)

# create my turret instance & group
my_turret = Turret(screen)
turret_group = pygame.sprite.Group()
turret_group.add(my_turret)

# create my player instance & group
my_player = Player(screen)
player_group = pygame.sprite.Group()
player_group.add(my_player)

# create bullet group
bullet_group = pygame.sprite.Group()

# shooting cooldown to prevent spam & lag
SHOOT_COOLDOWN = 600 # .6 seconds between shot
lastshot = 0

# main game loop
run = True
while run:
    # draw the background on the screen @ top left
    screen.blit(background, (0, 0))

    # event loop & general ender
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # load menu game state
    if current_game_state == GameState.MENU:
        # display menu text - used Chat GPT for next 5 lines
        header_text = font.render("No Man's Land", True, (128, 0, 0))
        start_button_text = font.render("Start Game (Return)", True, (10, 10, 10))

        # draw the text at certain spots
        screen.blit(header_text, (WIDTH // 2 - header_text.get_width() // 2, 100))
        screen.blit(start_button_text, (WIDTH // 2 - start_button_text.get_width() // 2, 400))

        # check if return is pressed to start the game
        if keys[pygame.K_RETURN]:
            current_game_state = GameState.PLAYING

    # load playing game state
    elif current_game_state == GameState.PLAYING:
        for event in events:
            # events for moving tank
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # up scroll
                    my_turret.move(-10)
                    tank_sound.play()
                elif event.button == 5:  # down scroll
                    my_turret.move(10)
                    tank_sound.play()
                elif event.button == 1:
                    # get current time
                    timenow = pygame.time.get_ticks()
                    if timenow - lastshot > SHOOT_COOLDOWN:
                        # bullet instance and add it to the bullet group, spawn at center of turret
                        bullet = Bullet(my_turret.rect.center)
                        bullet_group.add(bullet)
                        lastshot = timenow
                        # Play the shooting sound
                        shooting_sound.play()

        # moving player; used Chat GPT to simplify (from something that was similar to the above)
        my_player.move(keys[pygame.K_w], keys[pygame.K_s], keys[pygame.K_d], keys[pygame.K_a])

        # update and draw everything
        player_group.update(keys)
        player_group.draw(screen)

        turret_group.draw(screen)

        bullet_group.update(player_group)
        bullet_group.draw(screen)

        # check for bullet collisions with player
        for player in player_group:
            hit = pygame.sprite.spritecollide(player, bullet_group, True)
            if hit:
                current_game_state = GameState.GAME_OVER
                dead.play()

        # check if player reaches the winning finish line
        if my_player.rect.x >= FINISH_LINE:
            current_game_state = GameState.WINNER

    elif current_game_state == GameState.GAME_OVER:
        # display game over text
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        restart_txt = font.render("Restart (Space)", True, (0, 0, 100))

        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, 270))
        screen.blit(restart_txt, (WIDTH // 2 - restart_txt.get_width() // 2, 400))

        # checks if space is pressed to restart game
        if keys[pygame.K_SPACE]:
            # reset game state to menu
            current_game_state = GameState.MENU

            # reset player position
            my_player.rect.x = 0
            my_player.rect.y = 320

            # reset turret position
            my_turret.rect.center = (1056, 320)

            # clear bullets from screen
            bullet_group.empty()

    # winning game state
    elif current_game_state == GameState.WINNER:
        # display winner text
        winner_text = font.render("You Win!", True, (0, 255, 0))
        screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, 300))

    # need to do this to show background
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()