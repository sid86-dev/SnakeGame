import pygame
import random
import os
pygame.mixer.init()
loc1 = "Music\\SpringThaw.mp3"
loc2 = "Music\\CalvinHarris.mp3"
loc3 = "Music\\Beep.mp3"
loc4 = "Music\\gameover.wav"

pygame.init()
Screen_width = 800
Screen_height = 500
# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
light_blue = (201, 246, 255)
blue = (54, 79, 107)
orange = (255, 87, 51)
cream = (246, 247, 215)
purple = (221, 160, 221)
# Display
game_window = pygame.display.set_mode((Screen_width, Screen_height))
pygame.display.set_caption("Sid's Snake")
pygame.display.update()
font1 = pygame.font.SysFont('Ariel black', 65)
font2 = pygame.font.SysFont('Corbel', 40)
font3 = pygame.font.SysFont('Ariel', 40)
# function to present score in window
def screen_text1(text, color, x, y):
    text_in_screen = font1.render(text, True, color)
    game_window.blit(text_in_screen, [x, y])
def screen_text2(text, color, x, y):
    text_in_screen = font2.render(text, True, color)
    game_window.blit(text_in_screen, [x, y])
def screen_text3(text, color, x, y):
    text_in_screen = font3.render(text, True, color)
    game_window.blit(text_in_screen, [x, y])
# function to plot snake
def plot_snake(gamewindow, color, list, size):
    for x,y in list:
        pygame.draw.rect(gamewindow, color, [x, y, size, size])
# Welcome screen
def welcome():
    sound1 = pygame.mixer.Sound(loc2)
    sound1.set_volume(0.18)
    pygame.mixer.Channel(0).play(sound1)
    exit_game = False
    while not exit_game:
        game_window.fill(cream)
        screen_text1("WELCOME TO SNAKES", orange, 145 , 100)
        screen_text2("press space to play", blue, 245 , 220)
        screen_text2("--Sid", blue, 360 , 450)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(60)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
#function for game loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 85
    snake_y = 85
    snake_size = 27
    food_size = 35
    velocity_x = 0
    velocity_y = 0
    int_it_velocity = 3
    sensitivity = 20
    food_x = random.randint(100, 700)
    food_y = random.randint(120, 400)
    score = 0
    # fixing fps
    clock = pygame.time.Clock()
    fps = 60
    snake_lst = []
    snake_length = 1
    # check if hiscore file exist
    if (not os.path.exists('highscore.txt')):
        f = open('highscore.txt', 'w')
        f.write('0')
    # opening highscore file
    f = open("highscore.txt", 'r')
    high_score = f.read()
    while not exit_game:
        f = open("highscore.txt", 'w')
        f.write(str(high_score))
        if game_over:
            game_window.fill(orange)
            screen_text1("Game Over!!", white, 260, 100)
            screen_text1(f"Score: {score}", white, 300, 200)
            screen_text3("Please Press Enter to Continue....", cream, 170, 320)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        velocity_x = int_it_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -int_it_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -int_it_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = int_it_velocity
                        velocity_x = 0
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x) < sensitivity and abs(snake_y - food_y) < sensitivity:
                score += 1
                food_x = random.randint(20, 700)
                food_y = random.randint(20, 400)
                snake_length += 5

                sound2 = pygame.mixer.Sound(loc3)
                sound2.set_volume(0.5)
                pygame.mixer.Channel(1).play(sound2)
                if score>int(high_score):
                    high_score=score
            # change speed with levels
            if score>10:
                int_it_velocity = 4
            if score>25:
                int_it_velocity = 5

            # window background
            game_window.fill(cream)
            # change background with levels
            if score> 10:
                game_window.fill(light_blue)
            if score> 25:
                game_window.fill(purple)

            # making food
            pygame.draw.rect(game_window, red, [food_x, food_y, food_size, food_size])
            # making head of snake
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_lst.append(head)
            if len(snake_lst) > snake_length:
                del snake_lst[0]
            if snake_x < 0 or snake_x > Screen_width or snake_y < 0 or snake_y > Screen_height:
                game_over = True
                sound3 = pygame.mixer.Sound(loc4)
                sound3.set_volume(0.5)
                pygame.mixer.Channel(0).play(sound3)
            if head in snake_lst[:-1]:
                game_over = True
                sound3 = pygame.mixer.Sound(loc4)
                sound3.set_volume(0.5)
                pygame.mixer.Channel(0).play(sound3)
            plot_snake(game_window, blue, snake_lst, snake_size)
            # display score
            s = str(f"Score: {score}")
            h = str(f"HighScore: {high_score}")
            screen_text3(s, orange, 3, 3)
            screen_text3(h, orange, 610, 3)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
