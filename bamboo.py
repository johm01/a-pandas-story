import pygame 
from settings import *

class Bamboo(pygame.sprite.Sprite):
    def __init__(self,groups,pos)-> None:
        super().__init__(groups)
        self.image = pygame.image.load(bamboo_img[0]).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        
