# Import Modules
import pygame
import sys
import random


# General Setup
pygame.init()
clock = pygame.time.Clock()

# Making the Window
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Making Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
opponent = pygame.Rect(screen_width - 20, screen_height / 3 - 70, 10, screen_height / 6)
player = pygame.Rect(10, screen_height / 3 - 70, 10, screen_height / 6)

# Colors
bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

# Game Variables
ball_speed_x = 7
ball_speed_y = 7
rest_ball_speed_x = ball_speed_x
rest_ball_speed_y = ball_speed_y
player_speed = 0
opponent_speed = 4

# Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 25)

# Score Timer
score_time = None


# Defining
def move_ball():
    global ball_speed_y, ball_speed_x, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y -= ball_speed_y
    #    collisions

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
        pygame.mixer.music.load('pong.ogg')
        pygame.mixer.music.play(0)
    if ball.left <= 0:
        opponent_score += 1
        score_time = pygame.time.get_ticks()
        pygame.mixer.music.load('score.ogg')
        pygame.mixer.music.play(0)
    if ball.right >= screen_width:
        player_score += 1
        score_time = pygame.time.get_ticks()
        pygame.mixer.music.load('score.ogg')
        pygame.mixer.music.play(0)
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        pygame.mixer.music.load('pong.ogg')
        pygame.mixer.music.play(0)


def move_opponent():
    global opponent_speed, ball, opponent, screen_height, screen_width, ball_speed_x
    if ball.x >= screen_width / 2 and ball_speed_x >= 0:
        if opponent.y < ball.y:
            opponent.y += opponent_speed
        if opponent.y > ball.y:
            opponent.y -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def player_collision():
    global player, screen_height
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def events():
    global player_speed
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # player down
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_s:
                player_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player_speed -= 7
        # player up
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed += 7

def ball_restart():
    global ball_speed_y, ball_speed_x, score_time

    ball.center = (screen_width / 2, screen_height / 2)
    current_time = pygame.time.get_ticks()

    if current_time - score_time < 700:
        number_three = game_font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width / 2 - 20, screen_height / 2 - 40))

    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", False, light_grey)
        screen.blit(number_two, (screen_width / 2 - 20, screen_height / 2 - 40))

    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", False, light_grey)
        screen.blit(number_one, (screen_width / 2 - 20, screen_height / 2 - 40))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_x = rest_ball_speed_x * random.choice((-1, 1))
        ball_speed_y = rest_ball_speed_y * random.choice((-1, 1))
        score_time = None


# Main Loop
while True:
    # Getting Inputs
    events()
    # Game Logic
    #   Moves
    player.y += player_speed
    move_ball()
    player_collision()
    move_opponent()
    # Refreshing Visuals
    #   Graphics
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
    #   Texts
    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (screen_width / 2 - 22, screen_height / 2))
    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (screen_width / 2 + 10, screen_height / 2))

    #   Score Timer
    if score_time:
        ball_restart()
    # Updating the Window
    pygame.display.flip()
    clock.tick(120)
