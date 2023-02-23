from settings import *
import pygame 
from Tile import Tile
from player import Player
class Level:
    def __init__(self,level) -> None:
        self.sprite_group = orders
        self.sur = pygame.display.get_surface()
        self.level = level
        self.create_level()
  
    def create_level(self):
        tile = tiles_img
        for row_index, row in enumerate(self.level):
            for col_index,col in enumerate(row):
                x = row_index * 64
                y = col_index * 64

                global player
                self.coins = []

                if col == 'x':
                    self.tile = Tile(img='./assets/Tiles/tile1.png',pos=(x,y),groups=[self.sprite_group[1],self.sprite_group[2]])

                if col == 'n':
                    self.tile = Tile(img='./assets/Tiles/tile_2.png',pos=(x,y),groups=[self.sprite_group[1],self.sprite_group[2]])
                
                if col == 'p':
                    player = Player(vel=4,health=5,groups=self.sprite_group[4],pos=(x,y),g=1.2,hp_mod=0)

                if col == 'b':
                    self.bamboo = Tile(img=tile[2],groups=[self.sprite_group[0]],pos=(x,y))

                if col == 'l':
                    self.sprite_group[3].add(Collectible(groups=[self.sprite_group[3]],pos=(x+25,y-45),type='coin'))

                if col == 's':
                    self.platform = Tile(img=tile[1],pos=(x,y),groups=[self.sprite_group[1],self.sprite_group[2]]) 

                if col == 't':
                    self.trap = Tile(img='./assets/Tiles/spike.png',pos=(x,y),groups=[self.sprite_group[1],self.sprite_group[5]]) 

    def trap_collision(self,trap):
        for t in trap:
            if t.rect.colliderect(player.rect):
                # Checking health everytime we hit a trap instead of constantly checking it within the player update method
                player.health -= 1
                player.health_check()
                if player.direction.y > 0: 
                        player.rect.bottom = t.rect.top
                        player.direction.y = 0
                elif player.direction.y < 0:
                        player.rect.top = t.rect.bottom
                        player.direction.y = 0

                if player.direction.x < 0:
                        player.rect.left = t.rect.right
                elif player.direction.x > 0:
                        player.rect.right = t.rect.left
                        
    def clear_level(self):
        for i in range(len(self.sprite_group)):
            self.sprite_group[i].empty()
    
    def run(self):
        # Drawing Sprites
        for i in range(len(self.sprite_group)):
            self.sprite_group[i].draw(self.sur)
            self.sprite_group[i].update()
        self.trap_collision(self.sprite_group[5])
    
class Collectible(pygame.sprite.Sprite):
    def __init__(self, groups, pos, type) -> None:
        super().__init__(groups)
        self.sur = pygame.display.get_surface()
        self.image = pygame.image.load('./assets/Tiles/dead.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.sprite_groups = orders
        self.type = type
        self.collected = False

        if self.type == 'coin':
            self.image = pygame.image.load('./assets/Tiles/coin.png').convert_alpha()
        elif self.type == 'fruit':
            self.image = pygame.image.load('./assets/Tiles/fruit.png').convert_alpha()
        elif self.type == 'soda':
            self.image = pygame.image.load('./assets/Tiles/can.png').convert_alpha()

    def collision(self):
        for s in self.sprite_groups[4]:
            if s.rect.colliderect(self.rect) and self.type == 'coin':
                self.image = pygame.image.load('./assets/Tiles/dead.png').convert_alpha()
                self.collected = True 
            # If the player walks over the already collected coin 
            elif s.rect.colliderect(self.rect) and self.type is 'coin' and self.collected:
                pass

            if s.rect.colliderect(self.rect) and self.type == 'fruit':
                self.collected = True 
                if not player.is_dead and player.health >= 1:
                    player.health += 2
                else:
                    player.health += player.hp_mod

    def update(self):
        self.collision()
