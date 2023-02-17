import pygame 
from settings import *

class Player(pygame.sprite.Sprite):
    images = player_img
    def __init__(self, groups, pos, vel: int , health: int,g: float,hp_mod: int) -> None:
        super().__init__(groups)

         # Player image 
        self.image = pygame.image.load(self.images[0]).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.gravity = g
        self.vel = vel
        self.health = health 
        self.hp_mod = hp_mod

        # Player states
        self.on_bamboo = False
        self.moving_x = True 
        self.is_ground = False
        self.on_floor = True 
        self.falling = True
        self.is_dead = False
        self.state = 'idle'

        self.sprite_groups = orders

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

        # Player jump
        if key[pygame.K_SPACE] and self.is_ground:
            self.state = 'jump'
            self.is_ground = False
            self.jump()
                
    def jump(self):
        self.direction.y = -20
    
    # Player and Bamboo interaction               
    def player_onbamboo(self):
        e = pygame.key.get_pressed()
        for sprite in self.sprite_groups[0]:
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

    # Vertical Collision
    def collision_v(self,sprite):
        self.p_gravity()
        for s in sprite:
            if s.rect.colliderect(self.rect):
                self.is_ground = True
                if sprite == self.sprite_groups[4]:
                    if self.direction.y > 0: 
                            self.rect.bottom = s.rect.top
                            self.direction.y = 0
                            self.health -= 1
                    elif self.direction.y < 0:
                            self.rect.top = s.rect.bottom
                            self.direction.y = 0
                            self.health -= 1

                if self.direction.y > 0: 
                    self.rect.bottom = s.rect.top
                    self.direction.y = 0
                elif self.direction.y < 0:
                    self.rect.top = s.rect.bottom
                    self.direction.y = 0

    # Horizontal Collision
    def collision_h(self,sprite):
        self.rect.x += self.direction.x * self.vel
        for s in sprite:
            if s.rect.colliderect(self.rect):
                # if the player collides with a trap
                if sprite == self.sprite_groups[4]:
                    if self.direction.x < 0:
                        self.rect.left = s.rect.right
                        self.health = self.health - 1
                    elif self.direction.x > 0:
                        self.rect.right = s.rect.left
                        self.health = self.health - 1

                # Player colliding with anything else 
                if self.direction.x < 0:
                    self.rect.left = s.rect.right
                elif self.direction.x > 0:
                    self.rect.right = s.rect.left
    
    def health_check(self):
        if self.health == 0 and self.is_dead == False:
            print('player is dead')
            self.is_dead = True
        
        # Player dead 
        if self.is_dead:
            self.image = pygame.image.load('./assets/Tiles/dead.png').convert_alpha()

    def p_gravity(self):
        if self.falling:
            self.direction.y += self.gravity
            self.rect.y += self.direction.y

    def update(self):
        self.movement(pygame.key.get_pressed())
        self.player_onbamboo()
        self.collision_v(self.sprite_groups[4])
        self.collision_h(self.sprite_groups[4])
