import pygame
import os

ASSETS_DIR = './assets'

SCREEN_SIZE = (1000,600)
FLOOR_POSITION = 550

class Entity () :
    def __init__(self, imagePath, size, screen) -> None:

        img = pygame.image.load(os.path.join(ASSETS_DIR, imagePath))
        self.img = pygame.transform.scale(img, size)

        self.leaveTrail = False
        self.trail = []


        self.screen = screen
        self.pos = [SCREEN_SIZE[0]/2, 0]
        self.velocity = [0,0]
        
        self.inputsActive = False
        self.inputs = {}

        # self.keyPressed 
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
    
    def enableTrail(self):
        self.leaveTrail = True
        
    def disableTrain(self):
        self.leaveTrail = False
        self.trail = []
        
    def drawTrail(self):
        if(len(self.trail) > 2):
            pygame.draw.lines(self.screen, 'black', False,self.trail)
            
    
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

        if(self.leaveTrail):
            self.trail.append((self.pos[0], self.pos[1]))
            self.drawTrail()

        self.draw()
        pass
