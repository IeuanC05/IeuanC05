# Using random and pygame modules in this project
import pygame, random
from pygame.locals import *
from sys import exit

# Pygame start
pygame.init()

# Screensize variables
dis_width = 960
dis_height = 560

# Colours saved to variables
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Setting snake game screen size
dis = pygame.display.set_mode((dis_width, dis_height))

# Set game caption to 'Snake'
pygame.display.set_caption('Snake')

# set clock variable for snake speed limiting fps
clock = pygame.time.Clock()

# Set snake size
snake_block = 20

# Set game over font for game over screen
gameover_font = pygame.font.SysFont("timesnewroman", 75)
gameover_font2 = pygame.font.SysFont("timesnewroman", 30)

# Set score font
score_font = pygame.font.SysFont("calibri", 35)

# Score function when called displays score on screen
def Score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [15, 15])

# snake function when called calls all snake attributes which builds players snake
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# message function when called displays game over screen
def message(msg, color, msg2):
    mesg = gameover_font.render(msg, True, color)
    dis.blit(mesg, [275, 200])
    Mesg2 = gameover_font2.render(msg2, True, color)
    dis.blit(Mesg2, [285, 325])

def showMenu():
    pass

# main function happens when application runs
def main():

    # game_over variable set to False. When True game stops running
    game_over = False
    
    # game_close variable set to False. When True game over screen displayed
    game_close = False

    # Set snake speed
    snake_speed = 10    

    # Sets initial player location
    player_x = dis_width / 2
    player_y = dis_height / 2

    # Sets player movement distance
    x_change = 0
    y_change = 0

    # keeps track of snake length
    snake_List = []
    Length_of_snake = 1

    # Sets apple location
    apple_x = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    apple_y = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

    # main game loop
    while not game_over:
        
        # when player dies
        while game_close == True:

            # game over screen
            dis.fill(black)
            message("YOU DIED", red, "Press any button to continue!")
            Score(Length_of_snake - 1)
            pygame.display.update()

            # determines if player wants to quit or play again
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                    if event.type == pygame.QUIT:
                        game_over = True
                        game_close = False
                    elif event.type == pygame.KEYDOWN:
                        main()

        # If player quits during game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False

            # Determines player direction based on button press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if x_change != snake_block or Length_of_snake < 3:
                        x_change = -snake_block
                        y_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if x_change != -snake_block or Length_of_snake < 3:
                        x_change = snake_block
                        y_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if y_change != snake_block or Length_of_snake < 3:
                        y_change = -snake_block
                        x_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if y_change != -snake_block or Length_of_snake < 3:
                        y_change = snake_block
                        x_change = 0

        # If player hits edge of screen displays game over screen
        if player_x >= dis_width or player_x < 0 or player_y >= dis_height or player_y < 0:
            game_close = True

        # moves player based on previous input
        player_x += x_change
        player_y += y_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [apple_x, apple_y, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(player_x)
        snake_Head.append(player_y)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block, snake_List)
        Score(Length_of_snake - 1)

        pygame.display.update()

        # if player co-ords are same as apple co-ords player gains point
        if player_x == apple_x and player_y == apple_y:            
            apple_x = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            apple_y = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
            snake_speed += 0.1
            
        clock.tick(snake_speed)
            
    pygame.quit()

    exit()

main()