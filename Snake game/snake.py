import pygame
import random
import time
pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode([dis_width, dis_height])
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont('Roboto', 30)
def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0, 0])
def snake(snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, black, [x[0],x[1],10,10])
def lose (msg):
    popup = font_style.render(msg, True, red)
    dis.blit(popup, [dis_width/6,dis_height/3])

def gameLoop():
    game_over =False
    game_close =False
    iX = dis_width/2
    iY = dis_height/2
    xmove = 0
    ymove = 0
    snake_list =[]
    snake_length = 1
    foodx=round(random.randrange(0,dis_width- 10)/10)*10
    foody=round(random.randrange(0,dis_height- 10)/10)*10
    while game_close != True:
        while game_over == True:
            dis.fill(white)
            lose('You hit the wall! Press Q-Quit or c to continue')
            Your_score(snake_length-1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close= True
                        game_over = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close == True
            if event.type == pygame .KEYDOWN:
                if event.key ==pygame.K_RIGHT:
                    xmove = 10
                    ymove = 0
                elif event.key ==pygame.K_LEFT:
                    xmove = -10
                    ymove = 0
                elif event.key ==pygame.K_UP:
                    xmove = 0
                    ymove = -10
                elif event.key ==pygame.K_DOWN:
                    xmove = 0
                    ymove = 10
        if (iX >= dis_width or iX ==0 or iY >= dis_height or iY ==0):
            game_over = True
        iX += xmove
        iY += ymove
        dis.fill(white)
        pygame.draw.rect(dis, green, [foodx, foody, 10, 10])
        snake_head =[]
        snake_head.append(iX)
        snake_head.append(iY)
        snake_list.append(snake_head)
        if len(snake_list)> snake_length:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True
        snake(snake_list)
        Your_score(snake_length - 1)
        pygame.display.update()
        if iX ==foodx and iY == foody:
                foodx=round(random.randrange(0,dis_width- 10)/10)*10
                foody=round(random.randrange(0,dis_height- 10)/10)*10
                snake_length += 1
        clock.tick(30)
    pygame.quit()
    quit()
gameLoop()