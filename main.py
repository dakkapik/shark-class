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


entities = []

for i in range(30):
    entities.append(Circle([500,100], 50, "ball.png", screen, str(i)))


pygame.mouse.set_visible(0)

pygame.display.set_caption('Shark Pals Game')



# fix indentation

def collision (bodyA, bodyB):
    if(bodyA.ident == bodyB.ident): return

    deltaX = bodyA.pos[0] - bodyB.pos[0]
    deltaY = bodyA.pos[1] - bodyB.pos[1]
    # print("X: "+ str(deltaX))
    # print("Y: "+ str(deltaY))

    h = math.sqrt((deltaX*deltaX)+(deltaY*deltaY))
    # print(h)
    if(h < bodyA.radius + bodyB.radius):
        print('body : ' + bodyA.ident+ ' touching body: '+bodyB.ident)


while (True):
    clock.tick(60)

    game.update()

    for e in entities:
        for t in entities:
            collision(e, t)
        
        e.update()

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