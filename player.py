import pygame 
from settings import *
import time 

class Player(pygame.sprite.Sprite):
    images = player_img
    def __init__(self, groups, pos, vel: int , health: int,g: float) -> None:
        super().__init__(groups)

         # Player image 
        self.sprite_groups = s_groups 
        self.pos = pos
        self.img = './assets/Player/player.png'
        self.image = pygame.image.load(self.img).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.sur = pygame.display.get_surface()
        self.direction = pygame.math.Vector2(0,0)
        self.gravity = g
        self.vel = vel
        self.health = health 
        self.hp_mod = self.health / 2
        self.knockback_mod = 1 
        self.reclic_collected = 0

        # Player states
        self.on_bamboo = False
        self.moving_x = True 
        self.is_ground = False
        self.on_floor = True 
        self.falling = True
        self.is_dead = False
        self.on_trap = False
        self.is_hit = True 
        self.state = 'idle'
        
        # Mobs the player will have collisions with 
        self.can_hit = ['mob_1','mob_2']

        self.animations = {
            'idle':'./assets/Player/player.png',
            'right':'./assets/Player/player.png',
            'left':'./assets/Player/player_L.png',
            'jump':'./assets/Player/player.png',
        }

    # Player Movement
    def movement(self,key):
        if key[pygame.K_RIGHT] and self.moving_x:
            self.state = 'right'
            self.direction.x = 1
        elif key[pygame.K_LEFT] and self.moving_x:
            self.state = 'left'
            self.direction.x = -1
        else:
            self.direction.x = 0
            self.state = 'idle'

        # Player jump
        if key[pygame.K_SPACE] and self.is_ground:
            self.state = 'jump'
            self.is_ground = False
            self.jump()
        self.image = pygame.image.load(self.animations[self.state]).convert_alpha()

    def jump(self):
        self.direction.y = -20

    def player_mob_collision(self):
        # Looping through target list 
        for i in range(len(self.can_hit)):
            # Creating a var for each mob we want to have hit props 
            target = self.can_hit[i]
            # Colliding with each target 
            for sprite in self.sprite_groups[target]:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x >= 0:
                        self.direction.x = -20 * self.knockback_mod 
                    elif self.direction.x < 0:
                        self.direction.x = 20 * self.knockback_mod

    def output_hp(self):
        if (self.health < self.health):
            print(self.health)
        if (self.health > self.health):
            print(self.health) 
    
    # Player and Bamboo interaction               
    def player_onbamboo(self):
        e = pygame.key.get_pressed()
        for sprite in self.sprite_groups['bamboo']:
            if sprite.rect.colliderect(self.rect) and e[pygame.K_q] and not self.on_bamboo:
                self.on_bamboo = True
                self.falling = False
                self.is_ground = False
                print('On Bamboo')
                # Player is on bamboo

        if self.on_bamboo:
            self.moving_x = False
            print('On Bamboo', self.on_bamboo)

        # Player moving up and down bamboo
        if e[pygame.K_UP] and self.on_bamboo:
            self.rect.y -= self.vel / 2
        elif e[pygame.K_DOWN] and self.on_bamboo:
            self.rect.y += self.vel / 2

        # Jump off bamboo
        if e[pygame.K_e] and self.on_bamboo:
            self.on_bamboo = False
            self.falling = True
            self.moving_x = True
            self.is_ground = True
            print('Off Bamboo',self.on_bamboo)  
        # If player has reached the top of the bamboo 

    # Player collision with basic collidiable sprites
    def collision_floor_wall(self,sprite: list,direction):
        if direction == 'vertical':
            self.p_gravity()
            for s in range(len(sprite)):
                for sprites in self.sprite_groups['collide']:
                    if sprites.rect.colliderect(self.rect):
                        self.is_ground = True
                        if self.direction.y > 0: 
                            self.rect.bottom = sprites.rect.top
                            self.direction.y = 0
                        elif self.direction.y < 0:
                            self.rect.top = sprites.rect.bottom
                            self.direction.y = 0
        if direction == 'horizontal':
            self.rect.x += self.direction.x * self.vel
            for s in range(len(sprite)):
                for sprites in self.sprite_groups['collide']:
                    if sprites.rect.colliderect(self.rect):
                        if self.direction.x < 0:
                            self.rect.left = sprites.rect.right
                        elif self.direction.x > 0:
                            self.rect.right = sprites.rect.left

    def p_gravity(self):
        if self.falling:
            self.direction.y += self.gravity
            self.rect.y += self.direction.y

    def update(self):
        self.movement(pygame.key.get_pressed())
        self.player_onbamboo()
        self.output_hp()
        self.player_mob_collision()
        self.collision_floor_wall(self.can_hit,'vertical')
        self.collision_floor_wall(self.can_hit,'horizontal')
