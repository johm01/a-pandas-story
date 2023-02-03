import pygame 
from settings import *

class Player(pygame.sprite.Sprite):
    images = player_img
    def __init__(self, groups, pos, vel: int , health: int,g: float) -> None:
        super().__init__(groups)

         # Player image 
        self.image = pygame.image.load(self.images[0]).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.gravity = g
        self.vel = vel
        self.health = health 

        # Player states
        self.on_bamboo = False
        self.moving_x = True 
        self.is_jump = False
        self.on_floor = True 
        self.falling = True

        self.jumpCount = 10 

        # Player state 
        self.state = 'idle'

        self.sprite_groups = orders

        self.direction = pygame.math.Vector2(0,0)


    # Player Movement
    def movement(self,key) -> None:
        if key[pygame.K_RIGHT] and self.moving_x:
            self.state = 'right'
            self.rect.x += self.vel
        elif key[pygame.K_LEFT] and self.moving_x:
            self.state = 'left'
            self.rect.x -= self.vel

        # Player jump
        if key[pygame.K_SPACE] and not self.is_jump:
            self.state = 'jump'
            self.is_jump = True
            self.jump()

        if self.is_jump:
            self.is_jump = False
                    
    def jump(self):
        self.direction.y = -8
    
    # Player on bamboo                  
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
            self.rect.y -= self.vel 
        elif e[pygame.K_DOWN] and self.on_bamboo:
            self.rect.y += self.vel

        # Jump off bamboo
        if e[pygame.K_e] and self.on_bamboo:
            self.on_bamboo = False
            self.falling = True
            self.moving_x = True
            print('Off Bamboo',self.on_bamboo)   


    def collision(self):
            for sprite in self.sprite_groups[1]:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: 
                        self.rect.bottom = sprite.rect.top
                        self.direction.y = 0
                    elif self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                        self.direction.y = 0

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
        self.p_gravity()
        self.collision()
        self.player_onbamboo()
        self.movement(pygame.key.get_pressed())
