import pygame
import sys
import os

import math


from Game import Game


from Entity import Entity


from Snake import Snake 



# from pygame.locals import *



ASSETS_DIR = './assets'



SCREEN_SIZE = (1000,600)


FLOOR_POSITION = 550



keyPressed = ({


    'd':False,

    'a':False


})



pygame.init()  # initialize pygame



clock = pygame.time.Clock()



screen = pygame.display.set_mode(SCREEN_SIZE) 



# Load the background image here. Make sure the file exists!



# bg = pygame.image.load(os.path.join("./", "background.png"))


game = Game(screen)

diameter = 50
rad = diameter/2

snake = Snake("ball.png", (diameter, diameter), screen)


ball_2 = Entity("ball.png", (diameter, diameter), screen)


snake.setKeyPressed(keyPressed)


snake.setRightKey('d')

snake.setLeftKey('a')

# snake.enableTrail()


ball_2.setKeyPressed(keyPressed)

# ball_2.setRightKey('rightArrow')

# ball_2.setLeftKey('leftArrow')



ball_2.changePosition([100,0])


# ball_3.changePosition([300,0])

pygame.mouse.set_visible(0)



pygame.display.set_caption('Shark Pals Game')



# fix indentation

def collision ():

    deltaX = snake.pos[0] - ball_2.pos[0]

    deltaY = snake.pos[1] - ball_2.pos[1]

    h = math.sqrt((deltaX*deltaX)+(deltaY*deltaY))
    
    if(h < rad*2):
        snake.velocity[1] = -5
        ball_2.velocity[1] = -5
        print('they are touching')



while (True):



    clock.tick(60)



    game.update()

    snake.update()


    ball_2.update()


    collision()


    for event in pygame.event.get():



        if event.type == pygame.KEYDOWN:


            if(event.key == pygame.K_w):

                snake.jump()


            if(event.key == pygame.K_d):
                

                keyPressed['d'] = True


            if(event.key == pygame.K_a):


                keyPressed['a'] = True
            


            # print(event.key)



        if(event.type == pygame.KEYUP):


            if(event.key == pygame.K_d):


                keyPressed['d'] = False


            if(event.key == pygame.K_a):


                keyPressed['a'] = False



        if event.type == pygame.QUIT:



            sys.exit()




    pygame.display.update()