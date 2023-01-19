import pygame 
from settings import *

class Player(pygame.sprite.Sprite):
    images = player_img
    def __init__(self, groups, pos, vel: int , health: int) -> None:
        super().__init__(groups)

         # Player image 
        self.image = pygame.image.load(self.images[0]).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
        
        self.vel = vel
        self.health = health 

        self.on_bamboo = False
        self.moving_x = True 

        # Player Movement
    def movement(self,key) -> None:
        if key[pygame.K_RIGHT] and self.moving_x:
            self.rect.x += self.vel
            #self.img = pygame.image.load(self.image[0 + 1])
            print('right')
        elif key[pygame.K_LEFT] and self.moving_x:
            self.rect.x -= self.vel
            print('left')

    def update(self):
        self.movement(pygame.key.get_pressed())

