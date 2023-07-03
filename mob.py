class Projectile(pygame.sprite.Sprite):
    def __init__(self,pos,type):
        super().__init__()
        self.image = pygame.image.load('./assets/Tiles/arrow.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0,0)
        self.is_moving = True
        self.proj_vel = 8
        self.pos = pos 
        self.spritegroup = s_groups
        self.shooting = False
        self.type = type

    def shoot(self,dir):
        if self.is_moving:
            if dir == 'y':
                self.rect.y -= self.proj_vel
            if dir == 'x':
                self.rect.x -= self.proj_vel

    def spawnprojc(self,pj_amt):   
        for i in self.spritegroup['collide'] :
            if i.rect.colliderect(self.rect) and not self.shooting:
                self.shooting = True
                if self.shooting: 
                    for i in range(pj_amt):
                        self.spritegroup['projectile'].add(Projectile((self.pos[0],self.pos[1]),type=self.type))
            
    def update(self):
        self.spawnprojc(1)
        if self.type == 'reg':
            self.shoot('y')
        if self.type == 'x':
            self.shoot('x')
        
class Mob(pygame.sprite.Sprite):
    def __init__(self,img,pos,type,groups):
        super().__init__(groups)
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

        if self.type == 'mob_2':
           for i in range(1):
            self.sprite_group['projectile'].add(Projectile((self.pos[0],self.pos[1]-35),type='x'))
        self.mob_floor_collision('vertical','horizontal')
     
    def update(self):
        self.check_mob()
