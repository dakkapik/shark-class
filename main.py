import pygame
import sys
import os
import math

from Game import Game
from Circle import Circle

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

A = Circle([100,100], 50, "ball.png", screen)
B = Circle([200,100], 50, "ball.png", screen)

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
    A.update()
    B.update()

    for event in pygame.event.get():



        if event.type == pygame.KEYDOWN:


            if(event.key == pygame.K_w):

                pass

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