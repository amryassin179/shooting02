# import modules
import pygame
import time
import math
pygame.init()

# display screen
width = 900
height = 700
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("pong game")
clock = pygame.time.Clock()

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLACK1 = (100,100,100)
RED = (255,0,0)
GREEN = (0,190,0)
GREEN1 = (0,150,0)
BLUE = (0,0,255)
YELLOW = (200,200,0)
YELLOW1 = (150,150,0)
PURPLE = (158,0,150)
PURPLE1 = (110,0,110)
BROWN = (128,128,128)
ORANGE = (255,165,0)
GREY = (128,128,128)

#varuables
speed = 0
speed1 = 0
speed2 = 4
y_speed = 4
x_speed = 5
angle = 0
ball_color = "white"
game_speed = 3
balls_saved = 0
balls_not_saved = 0
balls_saved1 = 0
balls_not_saved1 = 0

#msgs
font = pygame.font.Font(None,45)
font1 = pygame.font.Font(None,50)
font2 = pygame.font.Font(None,40)
msg = font.render("welcome to pong game!!",True,GREEN)
msg1 = font.render("play",True,WHITE)
msg2 = font.render("game settings",True,WHITE)
msg3 = font1.render("GAME SETTINGS",True, WHITE )
msg4 = font2.render(f"ball color: {ball_color}",True,WHITE)
msg5 = font2.render(f"game speed: {game_speed}",True,WHITE)
msg6 = font2.render("press left to decrease           press right to increase  ",True,WHITE)
msg7 = font2.render("press A",True,GREEN1)
msg8 = font2.render("press D",True,YELLOW1)
msg9 = font2.render("go back to main menu",True,WHITE)
msg10 = font2.render("press P",True,RED)
msg11 = font2.render(f"balls saved: {balls_saved}",True,WHITE)
msg12 = font2.render(f"balls not saved: {balls_not_saved}",True,WHITE)
msg13 = font2.render(f"balls saved: {balls_saved1}",True,WHITE)
msg14 = font2.render(f"balls not saved: {balls_not_saved1}",True,WHITE)
msg15 = font2.render("choose game color ",True,WHITE)

#objects
stick = pygame.Rect(width-100,height/2,40,150)
stick1 = pygame.Rect(width-850,height/2,40,150)
ball = pygame.Rect(width/2-100,height/2,40,40)
option_play = pygame.Rect(150,550,170,50)
option_settings = pygame.Rect(500,550,220,50)
main_menu = pygame.Rect(565,645,300,45)

#functions
def display_screen(screen):
    screen.fill(GREY)
    msg16 = font.render("press P to quit",True,BLACK)
    screen.blit(msg16,(300,10))
def display_sticks(stick,stick1):
    pygame.draw.rect(screen,BLUE,stick)
    pygame.draw.rect(screen,RED,stick1)
def move_sticks(stick,stick1,speed,speed1):
    stick.y += speed
    stick1.y += speed1
def move_ball(ball,x_speed,y_speed):
    ball.y += y_speed
    ball.x += x_speed
def display_start(angle,new_ball_color,ball_color):
    msg17 = font2.render("press P to quit",WHITE,True)
    ball_color = new_ball_color
    screen.fill(PURPLE)
    pygame.draw.rect(screen, GREEN, option_play)
    pygame.draw.rect(screen, YELLOW, option_settings)
    screen.blit(msg,(260,200))
    screen.blit(msg1,(200,560))
    screen.blit(msg2,(500,560))
    screen.blit(msg7,(150,600))
    screen.blit(msg8,(500,600))
    screen.blit(msg17,(700,10))
    pygame.draw.rect(screen,new_ball_color,(200*math.cos(angle)+400,200*math.sin(angle)+300,50,50),border_radius=50)
    ball.y += speed2
    ball.x += speed2
def display_setting():
    screen.fill(BLUE)
    screen.blit(msg3,(300,100))
    pygame.draw.rect(screen,RED,main_menu)
    screen.blit(msg9,(570,650))
    screen.blit(msg10,(600,600))
    screen.blit(msg15,(340,370))
def display_score(msg11,msg12,msg13,msg14):
    screen.blit(msg11,(550,10))
    screen.blit(msg12, (550, 35))
    screen.blit(msg13, (50, 10))
    screen.blit(msg14, (50, 35))
def display_setting_colors():
    pygame.draw.rect(screen, BLACK, (380, 400, 30, 30))
    pygame.draw.rect(screen, PURPLE, (420, 400, 30, 30))
    pygame.draw.rect(screen, GREEN, (460, 400, 30, 30))
    pygame.draw.rect(screen, YELLOW, (500, 400, 30, 30))
#game setting
def game_setting(game_speed,msg4,msg5,new_speed,ball_color,new_ball_color):
# function varuables
    game_speed = 3
    new_speed = game_speed
    fps = new_speed*25
    ball_color = "white"
    new_ball_color = ball_color
    setting = True
#setting loop
    while setting:
# adjust game speed
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    game_speed +=1
                    new_speed = game_speed
                if event.key == pygame.K_LEFT:
                    game_speed -=1
                    new_speed = game_speed

                if event.key == pygame.K_p:
                    setting = False
                    start(angle,new_speed,game_speed,new_ball_color,ball_color)

            if game_speed>=5:
                game_speed = 5
                new_speed = game_speed
            if game_speed<=1:
                game_speed1 = 1
                new_speed = game_speed
# changing ball color
        if 410>= mouse[0] >=380 and 430>= mouse[1] >=400:
            pygame.draw.rect(screen, BLACK1, (380, 400, 30, 30))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ball_color = "black"
                    new_ball_color = ball_color

        if 450>= mouse[0] >=420 and 430>= mouse[1] >=400:
            pygame.draw.rect(screen, PURPLE1, (420, 400, 30, 30))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ball_color = "purple"
                    new_ball_color = ball_color

        if 490>= mouse[0] >=460 and 430>= mouse[1] >=400:
            pygame.draw.rect(screen, GREEN1, (460, 400, 30, 30))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ball_color = "green"
                    new_ball_color = ball_color

        if 530>= mouse[0] >=500 and 430>= mouse[1] >=400:
            pygame.draw.rect(screen, YELLOW1, (500, 400, 30, 30))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ball_color = "yellow"
                    new_ball_color = ball_color

#call functions
        display_setting()
        msg4 = font2.render(f"ball color: {new_ball_color}", True, WHITE)
        screen.blit(msg4, (200, 500))
        msg5 = font2.render(f"game speed: {new_speed}", True, WHITE)
        screen.blit(msg5, (200, 550))
        screen.blit(msg6, (100, 300))
        display_setting_colors()
        pygame.display.update()

#starter option
def start(angle,game_speed,new_speed,new_ball_color,ball_color):
# function varuables
    new_speed = game_speed
    fps = new_speed*25
    start = True
    new_ball_color = ball_color
    while start:
        clock.tick(fps)
# event handeling
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    start = False
                if event.key == pygame.K_a:
                    start = False
                    play(new_ball_color,balls_saved,balls_saved1,width, height, screen, fps, clock, speed, speed1, x_speed, y_speed, ball, stick,
                         stick1,game_speed,new_speed,balls_not_saved,balls_not_saved1,msg11,msg14,msg13,msg12)
                if event.key == pygame.K_d:
                    start = False
                    game_setting( msg4, msg5,game_speed,new_speed,ball_color,new_ball_color)


            if event.type == pygame.QUIT:
               start = False
# get mouse position and pressed
        if  320>=mouse[0]>= 150 and 600>=mouse[1]>=550:
            pygame.draw.rect(screen,GREEN1,option_play)
            screen.blit(msg1, (200, 560))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    start = False
                    play(new_ball_color,balls_saved,balls_saved1,width,height,screen,fps,clock,speed,speed1,x_speed,y_speed,ball,stick,stick1,new_speed,game_speed,balls_not_saved,balls_not_saved1,msg11,msg12,msg13,msg14)

        if 720>=mouse[0]>=500 and 600>=mouse[1]>=550:
            pygame.draw.rect(screen,YELLOW1, option_settings)
            screen.blit(msg2, (500, 560))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    start = False
                    game_setting(game_speed,msg4,msg5,new_speed,ball_color,new_ball_color)
#call functions
        display_start(angle,new_ball_color,ball_color)
        angle += 0.03
        pygame.display.update()
#game loop
def play(new_ball_color,balls_saved,balls_saved1,width,height,screen,fps,clock,speed,speed1,x_speed,y_speed,ball,stick,stick1,new_speed,game_speed,balls_not_saved,balls_not_saved1,msg11,msg12,msg13,msg14):
# function varuables
    run = True
    new_speed = game_speed
    fps = new_speed*25
    while run:
        clock.tick(fps)

#event handling
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_p:
                   run = False
                   start(angle, game_speed, new_speed, new_ball_color, ball_color)

               if event.key == pygame.K_UP:
                   speed -= 5
               if event.key == pygame.K_DOWN:
                   speed += 5

               if event.key == pygame.K_w:
                    speed1 -= 5
               if event.key == pygame.K_s:
                    speed1 += 5
           if event.type == pygame.KEYUP:
               speed = 0
               speed1 = 0
# make sure sticks arent outside of the screen
        if stick.y >= height - 150:
            stick.y = height - 150
        if stick.y <= 0:
            stick.y = 0

        if stick1.y >= height - 150:
            stick1.y = height - 150
        if stick1.y <= 0:
            stick1.y = 0

#if ball collides with boarder
        if ball.x >= width:
            ball.x = width/2-30
            ball.y = height/2-30
            x_speed *= -1
            balls_not_saved +=1
            msg12 = font2.render(f"balls not saved: {balls_not_saved}", True, WHITE)
            screen.blit(msg11, (550, 10))
            pygame.display.update()
        if ball.x + 60 <= 0:
            ball.x = width / 2 - 30
            ball.y = height / 2 - 30
            x_speed *= -1
            balls_not_saved1 +=1
            msg14 = font2.render(f"balls not saved: {balls_not_saved1}", True, WHITE)
            screen.blit(msg14, (50, 10))
            pygame.display.update()

        if ball.y+50 >= height or ball.y-50 <= 0:
            y_speed *= -1

#if ball collides with sticks
        if stick.x-40 >= ball.x >= stick.x-50:
            if stick.y+150 >= ball.y >= stick.y-50:
                x_speed *= -1
                balls_saved += 1
                msg11 = font2.render(f"balls saved: {balls_saved}",True,WHITE)
                screen.blit(msg11, (550,10))
                pygame.display.update()

        if stick1.x+45 >= ball.x >= stick1.x+40:
            if stick1.y+150 >= ball.y >= stick1.y-50:
                x_speed *= -1
                balls_saved1 += 1
                msg13 = font2.render(f"balls saved: {balls_saved1}", True, WHITE)
                screen.blit(msg13, (550, 10))
                pygame.display.update()

#call functions
        display_screen(screen)
        display_sticks(stick,stick1)
        pygame.draw.rect(screen, new_ball_color, ball, border_radius=50)
        move_sticks(stick,stick1,speed,speed1)
        move_ball(ball,x_speed,y_speed)
        display_score(msg11,msg12,msg13,msg14) 
        pygame.display.update()
start(angle,game_speed=3,new_speed=game_speed,new_ball_color = ball_color,ball_color = "white")
pygame.quit()
