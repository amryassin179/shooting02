# import modules
import pygame
import time
import random
pygame.init()

# create screen
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
time_event = pygame.event.custom_type()
pygame.time.set_timer(time_event, 930)
# colors
WHITE = (255 , 255 , 255 )
BLACK = (0 , 0 , 0 )
BLUE = (0 ,0 ,255 )
GREEN = (0 ,255 ,0 )
DARK_GREEN = (0,180,0)
YELLOW = (255,255,0)
DARK_YELLOW = (180,180,0)
RED = (255,0,0)
DARK_RED =(180,0,0)
GRAY = (128,128,128)
PINK = (255, 153, 255)
BROWN = (139,69,19)
# varuables
run = False
how_to_play = False
difficulty = 3
score = 0
lane_width = 15
lane_height = 70
speed = 0
speed1 = 4
speed2 = 1
height = 800
lane_move_y = 0
car_x = 350
enemy_x = car_x
enemy_y = 0
enemy_x1 = random.randint(90,180)
enemy_x2 = random.randint(200,350)
enemy_x3 = random.randint(390,480)
enemy_x4 = random.randint(500,610)
enemy_width = 45
enemy_height = 100

# objects
grass = pygame.Rect(0,0,100,800)
grass1 = pygame.Rect(700,0,100,800)
road = pygame.Rect(100,0,610,800)
boarder = pygame.Rect(90,0,10,800)
boarder1 = pygame.Rect(700,0,10,800)
car = pygame.Rect(car_x,650,45,100)
enemy = pygame.Rect(enemy_x,0,enemy_width,enemy_height)
enemy1 = pygame.Rect(enemy_x1,50,enemy_width,enemy_height)
enemy2 = pygame.Rect(enemy_x2,20,enemy_width,enemy_height)
enemy3 = pygame.Rect(enemy_x3,15,enemy_width,enemy_height)
enemy4 = pygame.Rect(enemy_x4,40,enemy_width,enemy_height)
option = pygame.Rect(50,580,150,60)
option1 = pygame.Rect(230,580,230,60)
option2 = pygame.Rect(500,580,200,60)
option3 = pygame.Rect(500,680,250,60)
main_menu = pygame.Rect(620,7,230,40)

# font and msgs
font = pygame.font.Font(None, 40)
font1 = pygame.font.Font(None,60)
font2 = pygame.font.Font(None,25)
font3 = pygame.font.Font(None,32)
msg = "YOU CRASHED!!"
msg1 = "WELCOME TO MY CAR GAME"
msg2 = "PLAY"
msg3 = "HOW TO PLAY"
msg4 = "difficulty"
msg5 = "HOW TO PLAY:  "
msg6 ="your car is the black car at the bottom and there are several cars you need to avoid  "
msg7 ="each car moves in a different speed "
msg8 ="fastest car is the red one be careful "
msg9 ="as the game progresses...the speed of the game will increase "
msg10 ="good luck and try to hit the best score you can "
msg11 = "GET BACK TO MAIN MENU"
msg12 = "press: A"
msg13 = "press: SPACE"
msg14 = "press: D"
text = font.render(msg, True, RED)
text1 = font1.render(msg1,True,BLACK)
text2 = font2.render(msg2,True,WHITE)
text3 = font2.render(msg3,True,WHITE)
text4 = font2.render(msg4,True,WHITE)
text5 = font.render(msg5,True,BLACK)
text6 = font2.render(msg6,True,BLACK)
text7 = font2.render(msg7,True,BLACK)
text8 = font2.render(msg8,True,BLACK)
text9 = font2.render(msg9,True,BLACK)
text10 = font2.render(msg10,True,BLACK)
text11 = font2.render(msg11,True,WHITE)
text12 = font2.render(msg12,True,YELLOW)
text13 = font2.render(msg13,True,DARK_GREEN)
text14 = font2.render(msg14,True,DARK_RED)
text15 = font1.render("difficulty: ",True,BLACK)
text16 = font2.render("1 = very easy       2 = easy ",True,YELLOW)
text17 = font2.render("3 = normal        4 = hard",True,YELLOW)
text18 = font2.render("5 = very hard",True,YELLOW)
text19 = font.render("press right to increase    press left to decrease",True,BLACK)
text20 = font.render("press: P", True,WHITE)
text21 = font.render("press A to move left             press D to move right",True,BLACK)
text23 = font3.render(f"SCORE: {score}",True,WHITE)
text24 = font.render("main menu: P",True,WHITE)
text25 = font2.render("you can get back to the main menu by pressing P",True,BLACK)
text26 = font2.render("the score and the difficulty level will show on the screen at top left",True,BLACK)
# functions
def display_view(text22,boarder1,boarder,grass,grass1,road,screen,difficulty):
    text22 = font3.render(f"difficulty: {difficulty}", True, RED)
    pygame.draw.rect(screen,GREEN,grass)
    pygame.draw.rect(screen,GREEN,grass1)
    pygame.draw.rect(screen,GRAY,road)
    pygame.draw.rect(screen,WHITE,boarder)
    pygame.draw.rect(screen,WHITE,boarder1)
    pygame.draw.rect(screen,BROWN,main_menu)
    screen.blit(text22,(10,50))
    screen.blit(text24,(620,10))
def display_car(screen,car):
    pygame.draw.rect(screen,BLACK,car)
def move_car(car,speed):
    car.x += speed
def move_enemy(enemy):
    enemy.y += speed2*9
    enemy1.y += speed2*6
    enemy2.y += speed2*7
    enemy3.y += speed2*5
    enemy4.y += speed2*8
def display_lanes(lane_move_y,screen,height,lane_height,lane_width):
    for y in range(lane_height * -2, height, lane_height * 2):
        pygame.draw.rect(screen, YELLOW, (300 , y + lane_move_y, lane_width, lane_height))
        pygame.draw.rect(screen, YELLOW, (500 , y + lane_move_y, lane_width, lane_height))
def display_enemy(screen,enemy,car,enemy_x,enemy1,enemy2,enemy3,enemy4):
    enemy_x = car.x
    pygame.draw.rect(screen,RED,enemy)
    pygame.draw.rect(screen,BLUE,enemy1)
    pygame.draw.rect(screen,YELLOW,enemy2)
    pygame.draw.rect(screen, PINK, enemy3)
    pygame.draw.rect(screen, BROWN, enemy4)
def display_start_msg():
    screen.blit(text1,(180,300))
    screen.blit(text2,(100,600))
    screen.blit(text3, (250, 600))
    screen.blit(text4, (550, 600))
    screen.blit(text12,(250,650))
    screen.blit(text13, (50, 650))
    screen.blit(text14, (550, 650))
def respawn_enemy():
    enemy.y = 0-enemy_height
    enemy.x = car.x
def display_options():
    pygame.draw.rect(screen,DARK_GREEN,option)
    pygame.draw.rect(screen,DARK_YELLOW,option1)
    pygame.draw.rect(screen,DARK_RED,option2)
def display_option1_msg():
    screen.blit(text5, (280, 100))
    screen.blit(text6, (10, 350))
    screen.blit(text7, (10, 400))
    screen.blit(text8, (10, 500))
    screen.blit(text9, (10, 600))
    screen.blit(text10, (10, 700))
    pygame.draw.rect(screen, BROWN, option3)
    screen.blit(text11, (500, 700))
    screen.blit(text20,(520,750))
    screen.blit(text21, (0,250))
    screen.blit(text25,(10,200))
    screen.blit(text26,(10,320))
def display_option2_msg():
    pygame.draw.rect(screen, BROWN, option3)
    screen.blit(text11, (500, 700))
    screen.blit(text16,(100,100))
    screen.blit(text17, (100, 200))
    screen.blit(text18, (100, 300))
    screen.blit(text19, (50, 600))
    screen.blit(text20, (520, 750))
def display_score(score):
    text23 = font3.render(f"SCORE: {score}", True, WHITE)
    screen.blit(text23, (10, 100))
def display_msg(score):
    screen.blit(text,(300,300))
    text23 = font3.render(f"SCORE: {score}", True, WHITE)
    screen.blit(text23,(300,400))
def collision(screen,score):
    display_msg(score)
    pygame.display.update()
    time.sleep(2)
    starter(screen,difficulty,new_difficulty=3)
# how to play loop
def how_to_play(screen):
    how_to_play = True
    while how_to_play:
        screen.fill(DARK_YELLOW)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    how_to_play = False
                    starter(screen,difficulty=3,new_difficulty=3)

        display_option1_msg()
        pygame.display.update()
    pygame.quit()
# difficulty loop
def difficulty_option(difficulty,new_difficulty):
    difficulty = 3
    new_difficulty = difficulty
    difficulty_bol = True
    while difficulty_bol:
        screen.fill(DARK_RED)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    difficulty_bol = False
                    starter(screen,difficulty,new_difficulty)

                if event.key == pygame.K_RIGHT:
                    difficulty+=1
                    new_difficulty = difficulty

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    difficulty-=1
                    new_difficulty = difficulty
        if difficulty>=5:
            difficulty = 5
            new_difficulty = difficulty
        if difficulty<=1:
            difficulty = 1
            new_difficulty = difficulty
        text15 = font1.render(f"difficulty:{difficulty} ", True, BLACK)
        screen.blit(text15, (300, 500))

        display_option2_msg()
        pygame.display.update()
    pygame.quit()
# starter game loop
def starter(screen,difficulty,new_difficulty):
    wait = True
    while wait:
        fps = new_difficulty*26
        clock.tick(fps)
        screen.fill(BLUE)
    #check the inputs of the user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wait = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play(difficulty,new_difficulty)
                if event.key == pygame.K_a:
                    how_to_play(screen)
                if event.key == pygame.K_d:
                    difficulty_option(difficulty,new_difficulty)
        display_options()
        display_start_msg()
        pygame.display.update()
    pygame.quit()
# play loop
def play(difficulty,new_difficulty):
# varuables
    new_difficulty = difficulty
    fps = new_difficulty*26
    collide = False
    difficulty = new_difficulty
    score = 0
    lane_width = 15
    lane_height = 70
    speed = 0
    speed1 = 4
    speed2 = 1
    height = 800
    lane_move_y = 0
    car_x = 350
    enemy_x = car_x
    enemy_x1 = random.randint(90, 180)
    enemy_x2 = random.randint(200, 350)
    enemy_x3 = random.randint(390, 480)
    enemy_x4 = random.randint(500, 610)
    enemy_width = 45
    enemy_height = 100
    run = True
    while run:
        clock.tick(fps)
# event handling
        for event in pygame.event.get():
            if event.type == time_event:
                score+=1
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    speed += 5
                if event.key == pygame.K_a:
                    speed -= 5
                if event.key == pygame.K_p:
                    run = False
            if event.type == pygame.KEYUP:
                speed = 0

# check if car collides with boarded
        if car.x >= boarder1.x-45:
            car.x = boarder1.x-45
            collision(screen)
            run = False
            starter(difficulty,new_difficulty)
        if car.x <= boarder.x+10:
            car.x = boarder.x+10
            collision(screen,score)
            run = False
            starter(difficulty,new_difficulty)
# move markers
        lane_move_y += speed1 * 2
        if lane_move_y >= lane_height * 2:
            lane_move_y = 0
# respawn enemy
        if enemy.y >= 800:
            respawn_enemy()
        if enemy1.y >= height:
            enemy1.y = 10-enemy_height
            enemy1.x = random.randint(90,200)
        if enemy2.y >=height:
            enemy2.x = random.randint(200,300)
            enemy2.y = 20-enemy_height
        if enemy3.y >=height:
            enemy3.x = random.randint(350,480)
            enemy3.y = 20-enemy_height
        if enemy4.y >=height:
            enemy4.x = random.randint(500,610)
            enemy4.y = 20-enemy_height
# enemy  collision
        if enemy.y == 0-enemy_height:
            if enemy1.x-50<=enemy.x<=enemy1.x+50:
                enemy.x+=170
            if enemy2.x-40<=enemy.x<=enemy2.x+40:
                enemy.x+=170
            if enemy3.x-40<=enemy.x<=enemy3.x+40:
                enemy.x+=170
            if enemy4.x-50 <= enemy.x <= enemy4.x+50:
                enemy.x += 170
        if enemy.x >=boarder1.x-50:
            enemy.x = boarder1.x-50
# car collision
        if enemy.x - 40 <= car.x <= enemy.x + 40 and car.y+car.height>= enemy.y >=car.y-90:
            collide = True
        if enemy1.x - 40 <= car.x <= enemy1.x + 40 and car.y+car.height>= enemy1.y >=car.y-90:
            collide = True
        if enemy2.x - 40 <= car.x <= enemy2.x + 40 and car.y+car.height>= enemy2.y >=car.y-90:
            collide = True
        if enemy3.x - 40 <= car.x <= enemy3.x + 40 and car.y+car.height>= enemy3.y >=car.y-90:
            collide = True
        if enemy4.x - 40 <= car.x <= enemy4.x + 40 and car.y+car.height>= enemy4.y >=car.y-90:
            collide = True
#check if collide happened
        if collide == True:
            collision(screen,score)
#add score every second

        display_view(screen,boarder1,boarder,grass,grass1,road,screen,difficulty)
        display_lanes(lane_move_y,screen,height,lane_height,lane_width)
        display_car(screen,car)
        display_enemy(screen,enemy,car,enemy_x,enemy1,enemy2,enemy3,enemy4)
        move_car(car, speed)
        move_enemy(enemy)
        display_score(score)
        pygame.display.update()
    pygame.quit()

starter(screen,difficulty= 3,new_difficulty=3)
pygame.quit()
