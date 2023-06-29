from typing import Any
import pygame
import time
from settings import * 

class Projectile(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('./assets/Tiles/can.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0,0)
        self.is_moving = True
        self.projectile_vel = 2 
        self.pos = pos 
        self.spritegroup = s_groups
        self.shooting = False
    
    def shoot(self):
        if self.is_moving:
            self.rect.y -= 5 

    def spawnprojc(self):   
        for i in self.spritegroup['proj_spawner']:
            if i.rect.colliderect(self.rect) and not self.shooting:
                self.shooting = True
                if self.shooting: 
                    self.spritegroup['projectile'].add(Projectile((self.pos[0],self.pos[1]-15)))
            
    def update(self):
        self.spawnprojc()
        self.shoot()

class ProjectileSpawner(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.spritegroup = s_groups
        self.pos = pos
        self.image = pygame.image.load('./assets/Tiles/dead.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.shooting = True
        
class Mob(pygame.sprite.Sprite):
    def __init__(self,img,pos,type):
        super().__init__()
        self.pos = pos 
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
    def mob_floor_collision(self,direction: str,direction_2: str):
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

        if direction_2 == 'horizontal':
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
        self.mob_floor_collision('vertical','horizontal')
     
    def update(self):
        self.check_mob()
