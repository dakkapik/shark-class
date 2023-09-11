import pygame
import sys
import os
from pygame.locals import *

SCREEN_SIZE = (1000,800)
FLOOR_POSITION = 700


class Entity () :
    def __init__(self, imagePath, size, screen) -> None:
        img = pygame.image.load(os.path.join("./", imagePath))
        self.img = pygame.transform.scale(img, size)
        self.screen = screen

        self.pos = [SCREEN_SIZE[0]/2, 0]
        self.velocity = [0,0]
        pass
    
    def draw(self):
        self.screen.blit(self.img, (self.pos[0],self.pos[1]))
        pass

    def update( self ):
        self.pos[0] = self.pos[0] + self.velocity[0]
        self.pos[1] = self.pos[1] + self.velocity[1]

        if(self.pos[1] < FLOOR_POSITION):
            ball.velocity[1] = ball.velocity[1] + 0.01
        else:
            ball.velocity[1] = 0

        self.draw()
        pass





pygame.init()  # initialize pygame

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000, 800)) 


# Load the background image here. Make sure the file exists!

bg = pygame.image.load(os.path.join("./", "background.png"))


# ball = pygame.image.load(os.path.join("./", "ball.png"))

ball = Entity("ball.png", (50,50), screen)

# ball.velocity[0] = 1
# ball.velocity[1] = 1


pygame.mouse.set_visible(0)

pygame.display.set_caption('Space Age Game')


# fix indentation


while True:

    clock.tick(60)

    screen.blit(bg, (0, 0))

    ball.update()
 
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()


    pygame.display.update()