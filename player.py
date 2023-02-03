import pygame 
from settings import *

class Player(pygame.sprite.Sprite):
    images = player_img
    def __init__(self, groups, pos, vel: int , health: int,g: float) -> None:
        super().__init__(groups)

         # Player image 
        self.image = pygame.image.load(self.images[0]).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.gravity = g
        self.vel = vel
        self.health = health 

        # Player states
        self.on_bamboo = False
        self.moving_x = True 
        self.is_ground = False
        self.on_floor = True 
        self.falling = True
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
        self.direction.y = -16
    
    # Player and Bamboo interaction               
    def player_onbamboo(self):
        e = pygame.key.get_pressed()
        for sprite in self.sprite_groups[0]:
            if sprite.rect.colliderect(self.rect) and e[pygame.K_q] and not self.on_bamboo:
                self.on_bamboo = True
                self.falling = False
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
            print('Off Bamboo',self.on_bamboo)   

    # Vertical Collision
    def collision(self):
        self.p_gravity()
        for sprite in self.sprite_groups[1]:
            if sprite.rect.colliderect(self.rect):
                self.is_ground = True
                if self.direction.y > 0: 
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                elif self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
    # Horizontal Collision
    def collision2(self):
        self.rect.x += self.direction.x * self.vel
        for sprite in self.sprite_groups[1]:
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                elif self.direction.x > 0:
                    self.rect.right = sprite.rect.left

    # Player gravity 
    def p_gravity(self):
        if self.falling:
            self.direction.y += self.gravity
            self.rect.y += self.direction.y

    def update(self):
        print(self.gravity)
        self.movement(pygame.key.get_pressed())
        self.collision2()
        self.collision()
        self.player_onbamboo()
