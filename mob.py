import pygame 
from settings import * 

import pygame 
from settings import * 

class Mob(pygame.sprite.Sprite):
    def __init__(self,img,pos,groups,type):
        super().__init__(groups)
        self.is_dead = False
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(topleft=(pos[0],pos[1]-64))
        self.type = type 
        self.sprite_group = orders

        # If mob is dead 
        if self.is_dead:
            for i in range(len(groups)):
                groups[i].sprite_group.empty()