from settings import *
import pygame 

class Collectible(pygame.sprite.Sprite):
    def __init__(self, groups, pos, type) -> None:
        super().__init__(groups)
        self.img = './assets/Tiles/coin.png'
        self.image = pygame.image.load(self.img).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.sprite_groups = orders
        self.type = type

    def update(self):
        pass
