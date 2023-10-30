import pygame

ASSETS_DIR = './assets'

class Game () :
    def __init__(self, screen, imagePath = False, size = (1000,600)) -> None:
        self.screen = screen
        self.players = []
        self.entities = []

        if(imagePath):
            img = pygame.image.load(os.path.join(ASSETS_DIR, imagePath))
            self.img = pygame.transform.scale(img, size)
        else:
            self.img = False
        
    # def collision (self) :
    #     for i in range(len(self.entities)):
    #         for o in range(len(self.entities)):
    #             self.entities[i]

    # def ABcollision (self, A, B) :
    #     deltaX = A

    def draw(self):
        if(self.img):
            self.screen.blit(self.img, (0,0))
        else:
            self.screen.fill("white")
        pass
    
    def update(self):
        self.draw()
        pass
        