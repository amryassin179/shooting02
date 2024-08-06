#import libraries
import random
import pygame
import time
import sys
pygame. init()


#define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLACK = (0,0,0)
CYAN = (0,255,255)

#display screen
screen = pygame.display.set_mode((900,700))

#define varuables
game_name = pygame.display.set_caption = ("flappy bird game")
collision = False
score = 0
run = False
wait = True

#define fonts
font = pygame.font.Font(None,45)
font1 = pygame.font.Font(None,30)
font2 = pygame.font.Font(None,32)

#define messgaes
message = "YOU LOST!!"
message2 = "WELCOME TO MY FLAPPY BORD GAME....PLEASE PRESS SPACE TO PLAY"
text = font.render(message, True, RED)
text2 = font2.render(message2,True,WHITE)

#define speed
speed1 = 5
bird_y_change = 0
clock = pygame.time.Clock()


#define objects
floor = pygame.Rect(0,600,900,100)
bird = pygame.Rect(300,300,50,50)
upper_pipe_x = 800
upper_pipe1_x = 800
lower_pipe_x = 800
upper_pipe_height = 100
lower_pipe_height = 600-upper_pipe_height-150
upper_pipe = pygame.Rect(upper_pipe_x,0,50,upper_pipe_height)
lower_pipe = pygame.Rect(lower_pipe_x,upper_pipe.height+180,50,700)
upper_pipe1 = pygame.Rect(upper_pipe_x,0,50,upper_pipe_height)
lower_pipe1 = pygame.Rect(lower_pipe_x,upper_pipe1.height+180,50,700)
gab = pygame.Rect(upper_pipe_x,upper_pipe.height,50,180)
gab1 = pygame.Rect(upper_pipe1.x,upper_pipe1.height,50,180)


#functions
def display_screen():
    screen.fill(CYAN)
def display_floor():
    pygame.draw.rect(screen,RED,floor)
    pygame.draw.rect(screen, CYAN , gab)
    pygame.draw.rect(screen, CYAN, gab1)
def display_bird():
    pygame.draw.rect(screen,GREEN, bird,border_radius=60)
def display_pipes(upper_pipe_height):
    upper_pipe_height = random.randint(150,500)
    pygame.draw.rect(screen,BLACK,upper_pipe)
    pygame.draw.rect(screen,BLACK,lower_pipe)
    upper_pipe_height = random.randint(150,500)
    pygame.draw.rect(screen,BLACK,upper_pipe1)
    pygame.draw.rect(screen,BLACK,lower_pipe1)
def move_pipes():
    upper_pipe.x -=speed1
    lower_pipe.x -=speed1
    upper_pipe1.x -=speed1
    lower_pipe1.x -=speed1
    gab.x -=speed1
    gab1.x -=speed1
def move_bird():
    bird.y += bird_y_change
def respawn_pipes():
    upper_pipe.height = random.randint(60, 500)
    lower_pipe.y = upper_pipe.height + 180
    upper_pipe_height =upper_pipe.height
    lower_pipe_height = lower_pipe.height
    upper_pipe.x = 900
    lower_pipe.x = 900
    gab.x = upper_pipe.x
    gab.y = upper_pipe.height
def respawn_pipes1():
    upper_pipe1.height = random.randint(50, 450)
    lower_pipe1.y = upper_pipe1.height + 180
    upper_pipe1.x = 800
    lower_pipe1.x = 800
    upper_pipe1.x = upper_pipe1_x
    gab1.x = upper_pipe1.x
    gab1.y = upper_pipe1.height
def show_lose_text():
    screen.blit(text, (300, 500))
def display_score():
    text1 = font1.render(f"SCORE: {score}", True, WHITE)
    screen.blit(text1, (50,50) )
def show_start_text():
    screen.blit(text2, (10,200))
#starter screen

while wait:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                wait = False
                run = True

    display_screen()
    show_start_text()
    display_pipes(upper_pipe_height)
    display_bird()
    pygame.display.update()


#game loop
while run:
    clock.tick(60)
    #check if you want to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        #check if you press the space bar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = -5
       #check if you release the space bar
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
               bird_y_change = 3
    #check if you hit the ground or the top
    if bird.y >= floor.y-50:
        bird.y = floor.y-50
        show_lose_text()
        run = False
        wait = True
    if bird.y<=0:
        bird.y = 0
        run = False
        wait = True
    #respawn pipes
    if upper_pipe.x <= 20:
        respawn_pipes()
    if upper_pipe1.x <= 5:
        respawn_pipes1()
    #make sure pipes arent too close to each other and gabs
    if 0<= upper_pipe1.x -upper_pipe.x <=200:
         upper_pipe1.x = upper_pipe1.x + 350
         lower_pipe1.x = upper_pipe1.x
         lower_pipe1_x = lower_pipe1.x
         gab1.x = upper_pipe1.x

    if 0<=upper_pipe.x -upper_pipe1.x <=200:
        upper_pipe.x = upper_pipe.x + 350
        lower_pipe.x = upper_pipe.x
        lower_pipe_x = lower_pipe.x
        gab.x = upper_pipe.x

#check if collision happend
    if upper_pipe.x -40 == bird.x:
        if bird.y <gab.y:
            collision = True
            time.sleep(1)
        if bird.y >gab.y+180:
           collision = True
           time.sleep(1)

    if upper_pipe1.x -40 == bird.x:
        if bird.y <gab1.y:
            collision = True
            time.sleep(1)
        if bird.y >gab1.y+180:
            collision = True
            time.sleep(1)


#add score
    if bird.x == upper_pipe.x or bird.x == upper_pipe1.x:
        score +=1












#call functions
    display_screen()
    display_floor()
    display_bird()
    move_bird()
    display_pipes(upper_pipe_height)
    move_pipes()
    display_score()


    pygame.display.update()

#addint delay
show_lose_text()
pygame.display.update()
time.sleep(1)
wait = True
#quitting the program

    