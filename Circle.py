import pygame, os
from Entity import Entity
ASSETS_DIR = './assets'

class Circle (Entity):
    def __init__(self, position, radius, imagePath, screen, ident):
        super().__init__(position, screen, ident)

        img = pygame.image.load(os.path.join(ASSETS_DIR, imagePath))
        self.img = pygame.transform.scale(img, (radius, radius))

        self.radius = radius
        pass
    
    def draw(self):
        # self.screen.blit(self.img, (self.pos[0] + self.radius, self.pos[1] - self.radius))
        pygame.draw.circle(self.screen, "blue", self.pos, self.radius)
        pass

