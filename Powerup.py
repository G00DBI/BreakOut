import pygame
from random import randint
from ball import Ball
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (126, 126, 126)
 
class powerup(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [(0,-3)]
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[1]
        self.velocity[1] = randint(-8,8)
