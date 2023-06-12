import pygame 
from settings import * 

class Mob(pygame.sprite.Sprite):
    def __init__(self,img,pos,type):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(topleft=(pos[0],pos[1]-64))
        self.type = type 
        self.sprite_group = s_groups

        self.direction = pygame.math.Vector2(0,0) 

        self.is_moving = True
        self.gravity = 4.3
        self.vel = -2
        self.is_falling = True
        self.is_ground = False
    
    def mob_movement(self):
            if self.is_moving:
                self.direction.x = 1
                
    # Mobs collision with collidable sprites
    def mob_floor_collision(self,direction: str):
        if direction == 'vertical':
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

        if direction == 'horizontal':
            self.rect.x += self.direction.x * self.vel
            for sprites in self.sprite_group['collide']:
                if sprites.rect.colliderect(self.rect):
                    if self.direction.x < 0:
                        self.rect.left = sprites.rect.right
                    elif self.direction.x > 0:
                        self.rect.right = sprites.rect.left

    # Checking wether we want the mob to be passive or aggressive 
    def check_mob(self):
        # if mob_1 we want it to move 
        if self.type == 'mob_1':
            self.mob_movement()
            self.mob_floor_collision('vertical')
            self.mob_floor_collision('horizontal')
        elif self.type == 'mob_2':
            self.mob_floor_collision('vertical')
            self.mob_floor_collision('horizontal')

    def update(self):
        self.check_mob()
