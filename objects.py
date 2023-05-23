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

class Trap(pygame.sprite.Sprite):
    def __init__(self, groups,type,pos) -> None:
        super().__init__(groups)
        self.type = type 
        self.image = pygame.Surface()
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.sur = pygame.display.get_surface()
        self.img = pygame.image.load('').convert_alpha()

        if self.type == 'spike':
            pass
    
    def update(self):
        pygame.draw.circle(self.image,(255,0,0),(50,50), 5)
        self.image.blit()
