import pygame 
from settings import *

class Player(pygame.sprite.Sprite):
    images = player_img
    def __init__(self, groups, pos, vel: int , health: int,g: float) -> None:
        super().__init__(groups)

         # Player image 
        self.image = pygame.image.load(self.images[0]).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
        
        self.vel = vel
        self.health = health 

        self.on_bamboo = False
        self.moving_x = True 
        self.is_jump = False
        self.jumpCount = 5

        # Player gravity
        self.gravity = g

        # Player state 
        self.state = 'idle'

        # Player Movement
    def movement(self,key) -> None:
        if key[pygame.K_RIGHT] and self.moving_x:
            self.state = 'right'
            self.rect.x += self.vel
        elif key[pygame.K_LEFT] and self.moving_x:
            self.state = 'left'
            self.rect.x -= self.vel

        # Player jump
        if not self.is_jump:
            if key[pygame.K_SPACE]:
                self.state = 'jump'
                self.is_jump = True
        else:
            if self.jumpCount >= -10:
                self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 2
            else:
                self.state = 'idle'
                self.jumpCount = 10
                self.is_jump = False
                
        print('State: ',self.state)

    def update(self):
        #self.rect.y += self.gravity
        self.movement(pygame.key.get_pressed())

