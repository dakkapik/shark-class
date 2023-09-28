import pygame
import sys
import os
from Game import Game
from Entity import Entity

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

ball_1 = Entity("ball.png", (50,50), screen)
ball_2 = Entity("ball.png", (50,50), screen)
ball_3 = Entity("ball.png", (50,50), screen)

ball_1.setKeyPressed(keyPressed)

ball_1.setRightKey('d')
ball_1.setLeftKey('a')

ball_1.enableTrail()

ball_2.changePosition([100,0])
ball_3.changePosition([300,0])

pygame.mouse.set_visible(0)

pygame.display.set_caption('Shark Pals Game')

# fix indentation

while (True):

    clock.tick(60)

    game.update()
    ball_1.update()

    ball_2.update()
    ball_3.update()
 
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if(event.key == pygame.K_w):
                ball_1.jump()
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