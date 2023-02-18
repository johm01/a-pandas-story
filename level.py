from settings import *
import pygame 
from Tile import Tile
from player import Player
from collectible import Collectible
class Level:
    def __init__(self) -> None:
        # Sprite Groups
        self.sprite_group = orders

        self.sur = pygame.display.get_surface()
        self.create_level()

        self.leaf_cnt = 50 
        
    def create_level(self):
        level = level_1
        
        for row_index, row in enumerate(level):
            for col_index,col in enumerate(row):
                x = row_index * 64
                y = col_index * 64

                self.coins = []

                if col == 'x':
                    self.tile = Tile(img='./assets/Tiles/tile1.png',pos=(x,y),groups=[self.sprite_group[1],self.sprite_group[2]])
                
                if col == 'p':
                    self.player = Player(vel=4,health=5,groups=self.sprite_group[3],pos=(x,y),g=1.2,hp_mod=0)

                if col == 'b':
                    self.bamboo = Tile(img='./assets/Player/bamboo_1.png',groups=[self.sprite_group[0]],pos=(x,y))

                if col == 'l':
                    self.item = Collectible(groups=[self.sprite_group[5]],pos=(x+25,y-45),type='coin')

                if col == 's':
                    self.platform = Tile(img='./assets/Tiles/slab.png',pos=(x,y),groups=[self.sprite_group[1],self.sprite_group[2]])

                if col == 't':
                    self.trap = Tile(img='./assets/Tiles/spike.png',pos=(x,y),groups=[self.sprite_group[1],self.sprite_group[4]]) 

    def trap_collision(self,trap):
        for t in trap:
            if t.rect.colliderect(self.player.rect):
                # Checking health everytime we hit a trap instead of constantly checking it within the player update method
                self.player.health -= 1
                self.player.health_check()
                if self.player.direction.y > 0: 
                        self.player.rect.bottom = t.rect.top
                        self.player.direction.y = 0
                elif self.player.direction.y < 0:
                        self.player.rect.top = t.rect.bottom
                        self.player.direction.y = 0

                if self.player.direction.x < 0:
                        self.player.rect.left = t.rect.right
                elif self.player.direction.x > 0:
                        self.player.rect.right = t.rect.left
    
    def collectible_collision(self):
        for c in self.sprite_group[5]:
            if c.rect.colliderect(self.player.rect) and self.item.type == 'coin':
                print('yes')

    def run(self):
        # Drawing Sprites
        for i in range(len(self.sprite_group)):
            self.sprite_group[i].draw(self.sur)
            self.sprite_group[i].update()

        self.collectible_collision()
        self.trap_collision(self.sprite_group[4])
