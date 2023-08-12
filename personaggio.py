import pygame
from random import randint

BLACK = (0, 0, 0)


class Personaggio(pygame.sprite.Sprite):

    def __init__(self, width, height, path, x, y):
        super().__init__()
        
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
            
    def draw(self, surf):
        surf.blit(self.image, self.rect)
    



    
    
