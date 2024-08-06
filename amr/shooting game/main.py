#import modules
import pygame
import random
import time
pygame.init()

#creating screen
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("shooting")
time_event = pygame.event.custom_type()
pygame.time.set_timer(time_event, 930)
#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLACK1 = (100,100,100)
RED = (255,0,0)
RED1 = (150,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (190,190,0)
YELLOW1 = (200,230,0)
PURPLE = (128,0,128)
PURPLE1 = (100,0,100)
BROWN = (128,128,128)
ORANGE = (255,165,0)
GREY = (128,128,128)
#varuables
start = False
dead = False
dead1 = False
player_dead = False
warning = False
timer = 0
game_speed = 3
new_game_speed = game_speed
fps = game_speed*30
clock = pygame.time.Clock()
y_speed = 0
x_speed = 0
bullet_y_speed = 0
bullet_x_speed = 0
bullet_speed = 0
bullet1_y_speed = 0
bullet1_x_speed = 0
bullet1_speed = 0
bullet2_speed = 0
bullet2_x_speed = 0
bullet2_y_speed = 0
health_width = 55
health_width1 = 55
main_health_width = 500
enemy_y = random.randint(50,660)
enemy1_y = random.randint(50,700)
enemy_x_speed = 3/2
if enemy_y-150 >= enemy1_y >= enemy_y+150:
    enemy1_y += 300
score_killed = 0
score_released = 0
score_landed = 0 
#msgs and fonts
font = pygame.font.Font(None,30)
font1 = pygame.font.Font(None,40)
font2 = pygame.font.Font(None,25)
msg = font1.render("welcome to the shooting game!!",True,BLUE)
msg2 = font.render("how to play",True,WHITE)
msg3 = font.render("game settings",True,WHITE)
msg1 = font.render("play",True,WHITE)
msg4 = font.render("main menu",True,WHITE)
msg5 = font.render("press: P",True,RED)
msg6 = font.render("press: SPACE",True,BLACK)
msg7 = font.render("press: S",True,YELLOW)
msg8 = font.render("press: D",True,PURPLE)
msg9 = font.render("press: p",True,BLUE)
msg10 = font.render("quit",True,WHITE)
msg11 = font1.render("1- the game is simple:",True,WHITE)
msg12 = font2.render("2- there are enemies that want to attack your house and they get stronger as the game progresses",True,WHITE)
msg13 = font2.render("3- you need to protect your house and avoid colliding with them ",True,WHITE)
msg15 = font2.render("5- to move left press: A     to move right press: D  ",True,WHITE)
msg16 = font2.render("6- you can also shoot them by pressing the space bar , remember....u only have 3 bullets",True,WHITE)
msg14 = font2.render("4- to move down press: S      to move up press: W",True,WHITE)
msg16_1 = font2.render("7- your bullets reload every time you hit an enemy  but you have to stay still and not move while they reload",True,WHITE)
msg17 = font.render("to decrease press left           to increase press right",True,WHITE)
msg18 = font2.render("1 is lowest                3 is mid               5 is hieghst",True,BLACK)
msg19 = font1.render(f"speed: {game_speed}",True,BLACK1)
msg20 = font.render("DEFFEND YOUR HOUSE!!!!",True,RED)
dead_msg = font1.render("YOU DIED!!",True,BLUE)
health_msg = font1.render(f"your house health: {main_health_width}",True,YELLOW)
score_msg = font1.render(f"enemies killed :{score_killed}",True,WHITE)
score_msg1 = font1.render(f"shots fired :{score_released}",True,WHITE)
score_msg2 = font1.render(f"shots landed :{score_landed}",True,WHITE)
#objects
starter_character = pygame.Rect(300,440,50,50)
starter_character_feet = pygame.Rect(335,470,10,50)
starter_character_feet1 = pygame.Rect(305,470,10,50)
starter_character_weapon = pygame.Rect(340,465,60,15)
starter_bullets = pygame.Rect(starter_character_weapon.x+25,starter_character_weapon.y,20,15)
starter_enemy = pygame.Rect(600,440,50,50)
obj_how_to_play = pygame.Rect(290,690,150,40)
obj_play = pygame.Rect(90,690,70,40)
obj_settings = pygame.Rect(490,690,160,40)
obj_main_menu = pygame.Rect(600,750,140,40)
obj_quit = pygame.Rect(690,85,90,30)
obj_quit1 = pygame.Rect(850,85,130,30)
character = pygame.Rect(300,300,50,50)
character_feet = pygame.Rect(335,330,10,50)
character_feet1 = pygame.Rect(305,330,10,50)
character_weapon = pygame.Rect(340,325,60,15)
bullets = pygame.Rect(character_weapon.x+25,character_weapon.y,20,15)
bullets1 = pygame.Rect(character_weapon.x,character_weapon.y,20,15)
bullets2 = pygame.Rect(character_weapon.x+50,character_weapon.y,20,15)
enemy = pygame.Rect(1000,enemy_y,50,50)
enemy_health = pygame.Rect(enemy.x, enemy.y-20,health_width,10)
character_health = pygame.Rect(character.x, character.y-20,60,10)
enemy1 = pygame.Rect(1055,enemy1_y,50,50)
enemy1_health = pygame.Rect(enemy1.x,enemy1.y-20,health_width1,10)
main_health = pygame.Rect(250,750,main_health_width,20)
house = pygame.Rect(0,0,30,900)
health_boarder = pygame.Rect(245,745,505,30)
#functions
def play_screen(score_msg,score_msg1,score_msg2,health_msg):
    screen.fill(PURPLE1) 
    pygame.draw.rect(screen, RED, obj_quit1)
    screen.blit(msg5,(850,120))
    screen.blit(msg4, (850, 90))
    screen.blit(health_msg,(300,720))
    screen.blit(score_msg,(10,20))
    screen.blit(score_msg1,(320,20))
    screen.blit(score_msg2,(580,20))
    pygame.draw.rect(screen,WHITE,house)
def display_starter_screen():
    pygame.draw.rect(screen, YELLOW, obj_how_to_play)
    pygame.draw.rect(screen,BLACK,obj_play)
    pygame.draw.rect(screen,PURPLE,obj_settings)
    pygame.draw.rect(screen,BLUE,obj_quit)
    screen.blit(msg,(150,200))
    screen.blit(msg2,(300,700))
    screen.blit(msg1,(100,700))
    screen.blit(msg3,(500,700))
    screen.blit(msg6,(80,730))
    screen.blit(msg7, (300, 730))
    screen.blit(msg8, (500, 730))
    screen.blit(msg9, (695, 120))
    screen.blit(msg10, (710, 90))
    pygame.draw.rect(screen,WHITE,starter_character,border_radius=50)
    pygame.draw.rect(screen,WHITE,starter_character_feet)
    pygame.draw.rect(screen,WHITE,starter_character_feet1)
    pygame.draw.rect(screen,BLACK,starter_character_weapon)
    pygame.draw.rect(screen,ORANGE,starter_bullets,border_top_right_radius=30,border_bottom_right_radius=30)
    pygame.draw.rect(screen,RED,starter_enemy)
def display_how_to_play_msgs():
    pygame.draw.rect(screen,RED,obj_main_menu)
    screen.blit(msg4,(610,760))
    screen.blit(msg5, (610, 730))
    screen.blit(msg11, (100, 200))
    screen.blit(msg12, (100, 250))
    screen.blit(msg13, (100, 300))
    screen.blit(msg14, (100, 350)) 
    screen.blit(msg15, (100, 400))
    screen.blit(msg16, (100, 450))
    screen.blit(msg16_1, (100, 500))
def display_settings():
    pygame.draw.rect(screen, RED, obj_main_menu)
    screen.blit(msg17,(180,300))
    screen.blit(msg18, (50, 500))
    screen.blit(msg5, (610, 730))
    screen.blit(msg4, (610, 760))
def display_character():
    pygame.draw.rect(screen,WHITE,character,border_radius=50)
    pygame.draw.rect(screen,GREEN,main_health)
    pygame.draw.rect(screen,BLACK,health_boarder,5,5)
    pygame.draw.rect(screen,WHITE,character_feet)
    pygame.draw.rect(screen,WHITE, character_feet1)
    pygame.draw.rect(screen,BLACK,character_weapon)
    pygame.draw.rect(screen,GREEN,character_health)
def move_character(x_speed,y_speed,character,character_health,character_feet,character_feet1,character_weapon,bullets,bullets1,bullets2,bullet2_x_speed,bullet2_y_speed,bullet_y_speed,bullet_x_speed,bullet1_x_speed,bullet1_y_speed,):
    character.x += x_speed
    character.y += y_speed
    character_feet.x += x_speed
    character_feet.y += y_speed
    character_feet1.x += x_speed
    character_feet1.y += y_speed
    character_weapon.x += x_speed
    character_weapon.y += y_speed
    bullets.x += bullet_x_speed
    bullets.y += bullet_y_speed
    bullets1.x += bullet1_x_speed
    bullets1.y += bullet1_y_speed
    bullets2.x += bullet2_x_speed
    bullets2.y += bullet2_y_speed
    character_health.x += x_speed
    character_health.y += y_speed
def shoot(bullets,bullets1,bullets2,character_weapon,bullet_speed,bullet1_speed,bullet2_speed):
    pygame.draw.rect(screen,ORANGE,bullets,border_top_right_radius=30,border_bottom_right_radius=30)
    pygame.draw.rect(screen,ORANGE,bullets1,border_top_right_radius=30,border_bottom_right_radius=30)
    pygame.draw.rect(screen, ORANGE, bullets2, border_top_right_radius=30, border_bottom_right_radius=30)
    bullets.x += bullet_speed
    bullets1.x += bullet1_speed
    bullets2.x += bullet2_speed
def spawn_enemies():
    pygame.draw.rect(screen,RED,enemy)
    pygame.draw.rect(screen,GREEN,enemy_health)
    pygame.draw.rect(screen,PURPLE,enemy1)
    pygame.draw.rect(screen,GREEN,enemy1_health)
    enemy.x -= enemy_x_speed
    enemy1.x -= enemy_x_speed
    enemy_health.x -= enemy_x_speed
    enemy1_health.x -= enemy_x_speed
#game starter
def starter(fps,new_game_speed,game_speed):
    starter_bullets_speed = 3
    fps = new_game_speed * 30
    start = True
    while start:
        clock.tick(fps)
        mouse = pygame.mouse.get_pos()
        screen.fill(BROWN)
#event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play(start,screen,score_killed,score_released,score_landed,score_msg,score_msg1,score_msg2,health_msg,main_health_width,timer,dead,dead1,health_width,health_width1,dead_msg,msg20,player_dead,warning,new_game_speed,fps,game_speed,clock,x_speed,y_speed,character,character_health,character_feet,character_feet1,character_weapon,bullet_speed,bullets,bullets2,bullets1,bullet2_speed,bullet2_x_speed,bullet2_y_speed,enemy,enemy1,enemy_x_speed,bullet1_speed,bullet1_x_speed,bullet1_y_speed,bullet_y_speed,bullet_x_speed)
                if event.key == pygame.K_s:
                    how_to_play()
                if event.key == pygame.K_d:
                    settings(fps,new_game_speed,game_speed)
                if event.key == pygame.K_p:
                    satrt = False
                    pygame.quit()

#checking if pressed on play menu
        if 160>=mouse[0]>=80 and 730>=mouse[1]>=690:
            pygame.draw.rect(screen, BLACK1, obj_play)
            screen.blit(msg1, (100, 700))
            pygame.display.update(obj_play)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    start = False

#checking if pressed on how to play menu
        if 430>=mouse[0]>=280 and 730>=mouse[1]>=690:
            pygame.draw.rect(screen, YELLOW1, obj_how_to_play)
            screen.blit(msg2, (300, 700))
            pygame.display.update(obj_how_to_play)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    start = False
                    how_to_play()

#checking if pressed on settings menu
        if 650>=mouse[0]>=480 and 730>=mouse[1]>=690:
            pygame.draw.rect(screen, PURPLE1, obj_settings)
            screen.blit(msg3, (500, 700))
            pygame.display.update(obj_settings)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    start = False
#move starter bullets
        starter_bullets.x += starter_bullets_speed
        if starter_bullets_speed >=5:
            starter_bullets_speed =5
        if starter_bullets.x >= 600:
            starter_bullets.x = starter_character_weapon.x +25
#call functions
        display_starter_screen()
        pygame.display.update()
#how to play loop
def how_to_play():
    how_to_play_bol = True
    while how_to_play_bol:
        screen.fill(YELLOW)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    how_to_play_bol = False
                    starter(fps,new_game_speed,game_speed)

        display_how_to_play_msgs()
        pygame.display.update()

#settings loop
def settings(fps,new_game_speed,game_speed):
#function varuables
    settings_bol = True
    new_game_speed = game_speed
    fps = new_game_speed*30
    while settings_bol:
        screen.fill(ORANGE)
#event handling
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    settings_bol = False
                    starter(fps,new_game_speed,game_speed)
#adjusting game speed
                if event.key == pygame.K_RIGHT:
                    game_speed +=1
                    new_game_speed = game_speed

                if event.key == pygame.K_LEFT:
                    game_speed -=1
                    new_game_speed = game_speed
            if game_speed >=5:
                game_speed = 5
                new_game_speed = game_speed
            if game_speed <=1:
                game_speed = 1
                new_game_speed = game_speed
#call functions
        msg19 = font1.render(f"speed: {new_game_speed}", True, BLACK1)
        screen.blit(msg19, (300, 700))
        display_settings()
        fps = new_game_speed*26
        pygame.display.update()
#playing loop
def play(start,screen,score_killed,score_released,score_landed,score_msg,score_msg1,score_msg2,health_msg,main_health_width,timer,dead,dead1,health_width,health_width1,dead_msg,msg20,player_dead,warning,new_game_speed,fps,game_speed,clock,x_speed,y_speed,character,character_health,character_feet,character_feet1,character_weapon,bullet_speed,bullets,bullets2,bullets1,bullet2_speed,bullet2_x_speed,bullet2_y_speed,enemy,enemy1,enemy_x_speed,bullet1_speed,bullet1_x_speed,bullet1_y_speed,bullet_y_speed,bullet_x_speed):
    play = True
    fps = new_game_speed * 30
    warning = False
    while play:
        clock.tick(fps)
#event handling
#quitting the program
        for event in pygame.event.get():
            if event.type == time_event:
                timer += 1
            if event.type == pygame.QUIT:
                play = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    play = False
                    starter(fps, new_game_speed, game_speed)
#shooting button
                if event.key == pygame.K_SPACE:
                    if bullets2.x == character_weapon.x +50 :
                        bullet2_speed +=5
                    if bullets.x == character_weapon.x +25 and bullets2.x >= character_weapon.x +65:
                        bullet_speed += 5
                    if bullets1.x == character_weapon.x and bullets2.x >= character_weapon.x +65 and bullets.x >= character_weapon.x +35:
                        bullet1_speed += 5
#moving buttons
#moving up and down
                if event.key == pygame.K_w:
                    y_speed -=4
                    bullet_y_speed -=4
                    bullet1_y_speed -=4
                    bullet2_y_speed -=4
                    if bullets.x >= character_weapon.x+35:
                        bullet_y_speed = 0
                    if bullets1.x >= character_weapon.x+5:
                        bullet1_y_speed = 0
                    if bullets2.x >= character_weapon.x +60:
                        bullet2_y_speed = 0
                if event.key == pygame.K_s:
                    y_speed +=4
                    bullet_y_speed +=4
                    bullet1_y_speed +=4
                    bullet2_y_speed +=4
                    if bullets.x >= character_weapon.x+35:
                        bullet_y_speed = 0
                    if bullets1.x >= character_weapon.x+5:
                        bullet1_y_speed = 0
                    if bullets2.x >= character_weapon.x +60:
                        bullet2_y_speed = 0
#moving left and right
                if event.key == pygame.K_a:
                    x_speed -=4
                    bullet_x_speed -=4
                    bullet1_x_speed -=4
                    bullet2_x_speed -=4
                    if bullets.x >= character_weapon.x+35:
                        bullet_x_speed = 0
                    if bullets1.x >= character_weapon.x+5:
                        bullet1_x_speed = 0
                    if bullets2.x >= character_weapon.x +60:
                        bullet2_x_speed = 0
                if event.key == pygame.K_d:
                    x_speed +=4
                    bullet_x_speed +=4
                    bullet1_x_speed +=4
                    bullet2_x_speed +=4
                    if bullets.x >= character_weapon.x+35:
                        bullet_x_speed = 0
                    if bullets1.x >= character_weapon.x+5:
                        bullet1_x_speed = 0
                    if bullets2.x >= character_weapon.x +60:
                        bullet2_x_speed = 0
#if button is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    y_speed = 0
                    bullet_y_speed = 0
                    bullet1_y_speed = 0
                    bullet2_y_speed = 0
                if event.key == pygame.K_s:
                    y_speed = 0
                    bullet_y_speed = 0
                    bullet1_y_speed = 0
                    bullet2_y_speed = 0
                if event.key == pygame.K_d:
                    x_speed = 0
                    bullet_x_speed = 0
                    bullet1_x_speed = 0
                    bullet2_x_speed = 0
                if event.key == pygame.K_a:
                    x_speed = 0
                    bullet_x_speed = 0
                    bullet1_x_speed = 0
                    bullet2_x_speed = 0

#when character collides with boarder width
        if character.x >= 700:
            character.x = 700
            character_feet.x = 735
            character_feet1.x = 705
            character_weapon.x = 740
            character_health.x = 700

        if character.x <= 0:
            character.x = 0
            character_feet.x = 35
            character_feet1.x = 5
            character_weapon.x = 40
            character_health.x = 0
#when character collides with boarder height
        if character.y <= 0 :
            character.y = 0
            character_feet.y = 30
            character_feet1.y = 30
            character_weapon.y = 25
            character_health.y = -20

        if character.y >= 720 :
            character.y = 720
            character_feet.y = 750
            character_feet1.y = 750
            character_weapon.y = 745
            character_health.y = character.y -20
#change enemy health bar
        if enemy.x + 50 >= bullets.x >= enemy.x - 10 and enemy.y - 10 <= bullets.y <= enemy.y + 50:
            if enemy_health.width == 15:
                enemy_health.width = 0
                dead = True
            if enemy_health.width == 35:
                enemy_health.width = 15
            if enemy_health.width == 55:
                enemy_health.width = 35
            if enemy_health.width == 75:
                enemy_health.width = 55
            if enemy_health.width == 100:
                enemy_health.width = 75
            if enemy_health.width == 120:
                enemy_health.width = 100
            if enemy_health.width == 140:
                enemy_health.width = 120
            score_landed+=1
            score_msg2= font1.render(f"shots landed: {score_landed}",True,WHITE)
            screen.blit(score_msg2,(580,20))
            pygame.display.update()


        if enemy.x + 50 >= bullets1.x >= enemy.x - 10 and enemy.y - 15 <= bullets1.y <= enemy.y + 50:
            if enemy_health.width == 15:
                enemy_health.width = 0
                dead = True
            if enemy_health.width == 35:
                enemy_health.width = 15
            if enemy_health.width == 55:
                enemy_health.width = 35
            if enemy_health.width == 75:
                enemy_health.width = 55
            if enemy_health.width == 100:
                enemy_health.width = 75
            if enemy_health.width == 120:
                enemy_health.width = 100
            if enemy_health.width == 140:
                enemy_health.width = 120
            score_landed+=1
            score_msg2= font1.render(f"shots landed: {score_landed}",True,WHITE)
            screen.blit(score_msg2,(580,20))
            pygame.display.update()

        if enemy.x + 50 >= bullets2.x >= enemy.x - 10 and enemy.y - 15 <= bullets2.y <= enemy.y + 50:
            if enemy_health.width == 15:
                enemy_health.width = 0
                dead = True
            if enemy_health.width == 35:
                enemy_health.width = 15
            if enemy_health.width == 55:
                enemy_health.width = 35
            if enemy_health.width == 75:
                enemy_health.width = 55
            if enemy_health.width == 100:
                enemy_health.width = 75
            if enemy_health.width == 120:
                enemy_health.width = 100
            if enemy_health.width == 140:
                enemy_health.width = 120
            score_landed+=1
            score_msg2= font1.render(f"shots landed: {score_landed}",True,WHITE)
            screen.blit(score_msg2,(580,20))
            pygame.display.update()

# change enemy1 health bar
        if enemy1.x  >= bullets.x >= enemy1.x - 5 and enemy1.y - 15 <= bullets.y <= enemy1.y + 50:
            if enemy1_health.width == 15:
                enemy1_health.width = 0
                dead1 = True
            if enemy1_health.width == 35:
                enemy1_health.width = 15
            if enemy1_health.width == 55:
                enemy1_health.width = 35
            if enemy1_health.width == 75:
                enemy1_health.width = 55
            if enemy1_health.width == 100:
                enemy1_health.width = 75
            if enemy1_health.width == 120:
                enemy1_health.width = 100
            if enemy1_health.width == 140:
                enemy1_health.width = 120
            score_landed+=1
            score_msg2= font1.render(f"shots landed: {score_landed}",True,WHITE)
            screen.blit(score_msg2,(580,20))
            pygame.display.update()

        if enemy1.x  >= bullets1.x >= enemy1.x - 5 and enemy1.y - 10 <= bullets1.y <= enemy1.y + 50:
            if enemy1_health.width == 15:
                enemy1_health.width = 0
                dead1 = True
            if enemy1_health.width == 35:
                enemy1_health.width = 15
            if enemy1_health.width == 55:
                enemy1_health.width = 35
            if enemy1_health.width == 75:
                enemy1_health.width = 55
            if enemy1_health.width == 100:
                enemy1_health.width = 75
            if enemy1_health.width == 120:
                enemy1_health.width = 100
            if enemy1_health.width == 140:
                enemy1_health.width = 120
            score_landed+=1
            score_msg2= font1.render(f"shots landed: {score_landed}",True,WHITE)
            screen.blit(score_msg2,(580,20))
            pygame.display.update()

        if enemy1.x  >= bullets2.x >= enemy1.x - 5 and enemy1.y - 10 <= bullets2.y <= enemy1.y + 50:
            if enemy1_health.width == 15:
                enemy1_health.width = 0
                dead1 = True
            if enemy1_health.width == 35:
                enemy1_health.width = 15
            if enemy1_health.width == 55:
                enemy1_health.width = 35
            if enemy1_health.width == 75:
                enemy1_health.width = 55
            if enemy1_health.width == 100:
                enemy1_health.width = 75
            if enemy1_health.width == 120:
                enemy1_health.width = 100
            if enemy1_health.width == 140:
                enemy1_health.width = 120
            score_landed+=1
            score_msg2= font1.render(f"shots landed: {score_landed}",True,WHITE)
            screen.blit(score_msg2,(580,20))
            pygame.display.update()
#if enemy is dead
        if dead == True:
            score_killed+=1
            score_msg = font1.render(f"enemies killed: {score_killed}",True,WHITE)
            screen.blit(score_msg,(10,20))
            pygame.display.update()
            enemy.x = 1000
            enemy_health.x = 1000
            enemy.y = random.randint(20, 640)
            enemy_health.y = enemy.y - 20
            enemy_health.width = health_width
            dead = False
#if enemy1 is dead
        if dead1 == True:
            score_killed+=1
            score_msg = font1.render(f"enemies killed: {score_killed}",True,WHITE)
            screen.blit(score_msg,(10,20))
            pygame.display.update()
            enemy1.x = 1050
            enemy1_health.x = 1050
            enemy1.y = random.randint(20, 640)
            enemy1_health.y = enemy1.y - 20
            enemy1_health.width = health_width1
            dead1 = False
#change character health bar
        if enemy.x == character.x+ 105 and character.y+105>=enemy.y>= character.y-10 or enemy1.x == character.x+ 105 and character.y+105>=enemy1.y>= character.y-10:
            if character_health.width == 15:
                character_health.width = 0
                player_dead = True
            if character_health.width == 30:
                character_health.width = 15
            if character_health.width == 45:
                character_health.width = 30
            if character_health.width == 60:
                character_health.width = 45

#if player died
        if player_dead == True:
            score_msg = font1.render(f"total enemies killed: {score_killed}",True,BLUE)
            score_msg1 = font1.render(f"total shots fired: {score_released + 2}",True,BLUE)
            score_msg2 = font1.render(f"total shots landed: {score_landed}",True,BLUE)
            screen.blit(score_msg,(20,270))
            screen.blit(score_msg1,(350,270))
            screen.blit(score_msg2,(650,270))
            screen.blit(dead_msg,(370,400))
            pygame.display.update()
            time.sleep(5)
            start = False
            play = False
            pygame.quit()
#reset bullet
        if bullets.x >= 860 or enemy.x +50 >= bullets.x >= enemy.x-10 and enemy.y-10 <= bullets.y <= enemy.y+50 or enemy1.x  >= bullets.x >= enemy1.x - 5 and enemy1.y - 10 <= bullets.y <= enemy1.y + 50:
            y_speed = 0
            x_speed = 0
            bullets.x = character_weapon.x+25
            bullets.y = character_weapon.y
            bullet_speed = 0
            bullet1_y_speed = 0
            bullet1_x_speed = 0
            bullet2_y_speed = 0
            bullet2_x_speed = 0
            bullet_x_speed = 0
            bullet_y_speed = 0
            score_released+=1
            score_msg1 = font1.render(f"shots fired: {score_released}",True,WHITE)
            screen.blit(score_msg1,(320,20))
            pygame.display.update()

#reset bullet1
        if bullets1.x >= 860 or enemy.x +50 >= bullets1.x >= enemy.x-10 and enemy.y-10 <= bullets1.y <= enemy.y+50 or enemy1.x  >= bullets1.x >= enemy1.x - 5 and enemy1.y - 10 <= bullets1.y <= enemy1.y + 50:
            y_speed = 0
            x_speed = 0
            bullets1.x = character_weapon.x
            bullets1.y = character_weapon.y
            bullet1_speed = 0
            bullet_y_speed = 0
            bullet_x_speed = 0
            bullet2_y_speed = 0
            bullet2_x_speed = 0
            bullet1_y_speed = 0
            bullet1_x_speed = 0
            score_released+=1
            score_msg1 = font1.render(f"shots fired: {score_released}",True,WHITE)
            screen.blit(score_msg1,(320,20))
            pygame.display.update()
#reset bullet2
        if bullets2.x >= 860 or enemy.x + 50 >= bullets2.x >= enemy.x - 10 and enemy.y - 10 <= bullets2.y <= enemy.y + 50 or enemy1.x >= bullets2.x >= enemy1.x - 5 and enemy1.y - 10 <= bullets2.y <= enemy1.y + 50:
            y_speed = 0
            x_speed = 0
            bullets2.x = character_weapon.x+50
            bullets2.y = character_weapon.y
            bullet2_speed = 0
            bullet_y_speed = 0
            bullet_x_speed = 0
            bullet1_y_speed = 0
            bullet1_x_speed = 0
            bullet2_x_speed = 0
            bullet2_y_speed = 0
            score_released+=1
            score_msg1 = font1.render(f"shots fired: {score_released}",True,WHITE)
            screen.blit(score_msg1,(320,20))
            pygame.display.update()

#if bullet collides with boarder width or height
        if bullets.x <= character_weapon.x+25:
            bullets.x = character_weapon.x+25
        if bullets.x >= 700 and character_weapon.x >= 740:
            character_weapon.x = 740
            bullets.x = character_weapon.x +25
        if bullets.y <= 23 :
            bullets.y = 23
        if bullets.y >= 745:
            bullets.y = 745
#if bullet1 collides with boarder width or height
        if bullets1.x <= character_weapon.x:
            bullets1.x = character_weapon.x
        if bullets1.x >= 700 and character_weapon.x >= 740:
            character_weapon.x = 740
            bullets1.x = character_weapon.x
        if bullets1.y <= 23:
            bullets1.y = 23
        if bullets1.y >= 745:
            bullets1.y = 745
#if bullet2 collides with boarder width or height
        if bullets2.x <= character_weapon.x+50:
            bullets2.x = character_weapon.x+50
        if bullets2.x >= 700 and character_weapon.x >= 740:
            character_weapon.x = 740
            bullets2.x = character_weapon.x+50
        if bullets2.y <= 23:
            bullets2.y = 23
        if bullets2.y >= 745:
            bullets2.y = 745
#adjust bullet speed
        if bullet_speed >=4:
            bullet_speed = 4.2
        if bullet1_speed >=4:
            bullet1_speed = 3.5
        if bullet2_speed >= 4:
            bullet2_speed = 4.5
#increase game difficulty
        if timer == 10:
            health_width = 100
            health_width1 = 100
            enemy_health.width = health_width
            enemy1_health.width = health_width1
            if new_game_speed == 2:
                new_game_speed = 4.5
            if new_game_speed == 3:
                new_game_speed = 5.5
            if new_game_speed == 4:
                new_game_speed = 6
            if new_game_speed == 5:
                new_game_speed = 8
        fps = new_game_speed * 30
        if timer == 30:
            health_width = 140
            health_width1 = 140
            
#reset enemy
        if enemy.x <=0:
            enemy.x = 1000
            enemy_health.x = 1000
            enemy.y = random.randint(10,650)
            enemy_health.y = enemy.y-20
            enemy_health.width = health_width
#reset enemy1
        if enemy1.x <= 0:
            enemy1.x = 1030
            enemy1_health.x = 1030
            enemy1.y = random.randint(5, 680)
            enemy1_health.y = enemy1.y - 20
            enemy1_health.width = health_width1
#adjust the placement of the enemies
        if 1050 >= enemy.x>=800 and 1050 >=enemy1.x >=800:
            if enemy1.y+150 >= enemy.y >= enemy1.y-150:
                enemy.y +=250
                enemy_health.y = enemy.y-20
            if enemy.y >= 750:
                enemy.y = 700
                enemy_health.y = enemy.y -20
#change house health bar
        if 9.5<= enemy.x <=10 or 10>= enemy1.x >=9.5 :
                if main_health.width == 50:
                   main_health.width = 0
                   player_dead = True
                if main_health.width == 100:
                   main_health.width = 50
                if main_health.width == 150:
                    main_health.width = 100
                    warning = True
                if main_health.width == 200:
                   main_health.width = 150
                if main_health.width == 250:
                    main_health.width = 200
                if main_health.width == 300:
                    main_health.width = 250
                if main_health.width == 350:
                    main_health.width = 300
                if main_health.width == 400:
                    main_health.width = 350
                if main_health.width == 450:
                    main_health.width = 400
                if main_health.width == 500:
                    main_health.width = 450
                health_msg = font1.render(f"your house health: {main_health.width}",True,YELLOW)
                screen.blit(health_msg,(300,720))
                pygame.display.update()
#warning msg
        if warning == True:
            msg20 = font.render("DEFFEND YOUR HOUSE!!!!",True,RED)
            screen.blit(msg20,(300,700))
            pygame.display.update()
        

        play_screen(score_msg,score_msg1,score_msg2,health_msg)
        display_character()
        spawn_enemies()
        shoot(bullets,bullets1,bullets2, character_weapon, bullet_speed,bullet1_speed,bullet2_speed)
        move_character(x_speed,y_speed,character,character_health,character_feet,character_feet1,character_weapon,bullets,bullets1,bullets2,bullet2_x_speed,bullet2_y_speed,bullet_y_speed,bullet_x_speed,bullet1_x_speed,bullet1_y_speed)
        pygame.display.update()
starter(fps,new_game_speed = game_speed,game_speed = 3)
pygame.quit()

