from Entity import Entity

class Snake(Entity):
    def __init__(self, imagePath, size, screen):
        super().__init__(imagePath, size, screen)
        
        self.snakeLength = 5
        self.count = 0

    def drawTrail(self):

        if(len(self.trail) > 6):
            for x in range(self.snakeLength):

                index = len(self.trail) - (x + 1)
                
                point = self.trail[index]
                self.screen.blit(self.img, (point[0], point[1]))



    def eatFruit(self):
        self.snakeLength = self.snakeLength + 1