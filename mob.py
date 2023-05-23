import pygame 
from settings import * 

class Mob(pygame.sprite.Sprite):
    def __init__(self,img,pos,type,target):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(topleft=(pos[0],pos[1]-64))
        self.type = type 
        self.target = target
        self.sprite_group = s_groups

        self.direction = pygame.math.Vector2(0,0)
        self.vel = 0.3
        self.gravity = 4.8
        self.is_dead = False
        self.is_falling = True
        self.is_ground = False

        self.can_hit = []
    
    def mob_collision(self,direction: str):
        # Mob collision 
        if direction == 'horizontal':
            gravity(self,self.is_falling)
            for i in self.sprite_group['collide']:
                if i.rect.colliderect(self.rect):
                    self.is_ground = True
                    if self.direction.y > 0: 
                        self.rect.bottom = i.rect.top
                        self.direction.y = 0
                    elif self.direction.y < 0:
                        self.rect.top = i.rect.bottom
                        self.direction.y = 0

        if direction == 'vertical':
            self.rect.x += self.direction.x * self.vel
            for sprites in self.sprite_group['collide']:
                if sprites.rect.colliderect(self.rect):
                    if self.direction.x < 0:
                        self.rect.left = sprites.rect.right
                    elif self.direction.x > 0:
                        self.rect.right = sprites.rect.left


    def update(self):
        self.mob_collision('vertical')
        self.mob_collision('horizontal')