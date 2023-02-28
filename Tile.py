import pygame 
from settings import * 

class Tile(pygame.sprite.Sprite):
    def __init__(self,img,pos,groups):
        super().__init__(groups)
        self.replace = False
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(topleft=(pos[0],pos[1]-64))
        self.sprite_group = orders

        if self.replace:
            self.image = pygame.image.load('./assets/Tiles/dead.png').convert_alpha()
