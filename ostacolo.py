import pygame
from random import randint
 
BLACK = (0, 0, 0)


class Ostacolo(pygame.sprite.Sprite):
    
    def __init__(self, width, height, path):
        super().__init__()
        
        self.image = self.image.load(path)
        self.image = pygame.transform.scale(self.image, (width, height))
        
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 220
        
    def draw(self, surf):
        surf.blit(self.image, self.rect)
        