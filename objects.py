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
        self.gravity = 9.8
        self.is_dead = False
        self.is_falling = True
        self.is_ground = False

    def mob_collision(self):
        for t in self.type:
            if t.rect.colliderect(self.target.rect) and self.type == self.sprite_group["mob_1"]:
                print('yes')
    
    def update(self):
        collision_h(self,self.sprite_group["collide"])
        collision_v(self,self.sprite_group["collide"])
        self.mob_collision()
        
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
