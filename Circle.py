import pygame, os
from Entity import Entity
ASSETS_DIR = './assets'

class Circle (Entity):
    def __init__(self, position, radius, imagePath, screen):
        super().__init__(position, screen)

        img = pygame.image.load(os.path.join(ASSETS_DIR, imagePath))
        self.img = pygame.transform.scale(img, (radius, radius))

        self.radius = radius
        pass
    
    def draw(self):
        self.screen.blit(self.img, (self.pos[0] + self.radius, self.pos[1] - self.radius))
        pass

