import pygame
import sys
import os
from pygame.locals import *

ASSETS_DIR = './assets'

SCREEN_SIZE = (1000,600)
FLOOR_POSITION = 550

keyPressed = ({
    'd':False,
    'a':False
})


class Game () :
    def __init__(self, imagePath = False, size = (1000,600)) -> None:
        self.size = size
        if(imagePath):
            img = pygame.image.load(os.path.join(ASSETS_DIR, imagePath))
            self.img = pygame.transform.scale(img, size)
        else:
            self.img = False
        
        
    def draw(self):
        if(self.img):
            self.screen.blit(self.img, (0,0))
        else:
            screen.fill("white")
        pass
    
    def update(self):
        self.draw()
        pass
        
class Entity () :
    def __init__(self, imagePath, size, screen) -> None:

        img = pygame.image.load(os.path.join(ASSETS_DIR, imagePath))
        self.img = pygame.transform.scale(img, size)

        self.screen = screen
        self.pos = [SCREEN_SIZE[0]/2, 0]
        self.velocity = [0,0]
        
        self.inputsActive = False
        self.inputs = {}

        pass
    
    def changePosition(self, coordinates):
        #this function will change position of the entity

        self.pos[0] = coordinates[0]
        self.pos[1] = coordinates[1]

        pass

    def jump(self):
        self.velocity[1] = -5
    
    def draw(self):
            self.screen.blit(self.img, (self.pos[0],self.pos[1]))
            pass
    
    def checkInputs(self):
        self.velocity[0] = 0
        if(keyPressed[self.inputs['right']]):
            self.velocity[0] = 5
            
        if(keyPressed[self.inputs['left']]):
            self.velocity[0] = -5
            
    def setRightKey(self, key):
        self.inputsActive = True
        self.inputs['right'] = key
    
    def setLeftKey(self, key):
        self.inputsActive = True
        self.inputs['left'] = key
    
    def update( self ):
        self.pos[0] = self.pos[0] + self.velocity[0]
        self.pos[1] = self.pos[1] + self.velocity[1]

        #this is just a comment, compiler will ignore

        if(self.pos[1] < FLOOR_POSITION):
            self.velocity[1] = self.velocity[1] + 0.08
        else:
            self.velocity[1] = 0

        if(self.inputsActive):
            self.checkInputs()

        self.draw()
        pass


pygame.init()  # initialize pygame

clock = pygame.time.Clock()

screen = pygame.display.set_mode(SCREEN_SIZE) 


# Load the background image here. Make sure the file exists!

# bg = pygame.image.load(os.path.join("./", "background.png"))
game = Game()

ball_1 = Entity("ball.png", (50,50), screen)
ball_2 = Entity("ball.png", (50,50), screen)
ball_3 = Entity("ball.png", (50,50), screen)

ball_1.setRightKey('d')
ball_1.setLeftKey('a')


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
            
            print(event.key)

        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_d):
                keyPressed['d'] = False
            if(event.key == pygame.K_a):
                keyPressed['a'] = False

        if event.type == pygame.QUIT:

            sys.exit()


    pygame.display.update()