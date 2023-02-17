import pygame 
from settings import * 

class Tile(pygame.sprite.Sprite):
    def __init__(self,img,pos,groups,type):
        super().__init__(groups)
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(topleft=(pos[0],pos[1]-64))
        self.type = type

    def collectible_collision(self):
        print('yes')

    def update(self):
        if self.type == 'coin':
            self.collectible_collision()
