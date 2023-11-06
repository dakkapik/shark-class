import pygame
import os

ASSETS_DIR = './assets'
SCREEN_SIZE = (1000,600)
FLOOR_POSITION = 550

class Entity () :

    def __init__(self, position, screen, ident) -> None:
        self.ident = ident
        self.pos = position
        self.screen = screen
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
    
    def setKeyPressed(self, obj):

        self.keyPressed = obj
    

    def checkInputs(self):

        self.velocity[0] = 0

        if(self.keyPressed[self.inputs['right']]):

            self.velocity[0] = 5
            

        if(self.keyPressed[self.inputs['left']]):

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

