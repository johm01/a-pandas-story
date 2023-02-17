from settings import *
import pygame 
from Tile import Tile
from player import Player

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

                global active_tiles
                active_tiles = []

                if col == 'x':
                    Tile(img='./assets/Tiles/tile1.png',pos=(x,y),groups=[self.sprite_group[1],self.sprite_group[2]])
                
                if col == 'p':
                    self.player = Player(vel=4,health=5,groups=self.sprite_group[3],pos=(x,y),g=1.2,hp_mod=0)

                if col == 'b':
                    Tile(img='./assets/Player/bamboo_1.png',groups=[self.sprite_group[0]],pos=(x,y))

                if col == 'l':
                    Tile(img='./assets/Tiles/leaf.png',groups=[self.sprite_group[1]],pos=(x,y))

                if col == 'f':
                    Tile(img='./assets/Tiles/sky2.png',groups=[self.sprite_group[1]],pos=(x,y)) 

                if col == 's':
                    Tile(img='./assets/Tiles/slab.png',pos=(x,y),groups=[self.sprite_group[1],self.sprite_group[2]])

                if col == 't':
                    Tile(img='./assets/Tiles/spike.png',pos=(x,y),groups=[self.sprite_group[1],self.sprite_group[4]]) 

    def trap_collision(self,trap):
        for t in trap:
            if t.rect.colliderect(self.player.rect):
                # Checking health everytime we hit a trap instead of constantly checking it within the player update method
                self.player.health_check()
                if self.player.direction.y > 0: 
                        self.player.rect.bottom = t.rect.top
                        self.player.direction.y = 0
                        self.player.health -= 1
                elif self.player.direction.y < 0:
                        self.player.rect.top = t.rect.bottom
                        self.player.direction.y = 0
                        self.player.health -= 1

                if self.player.direction.x < 0:
                        self.player.rect.left = t.rect.right
                        self.player.health -= 1
                elif self.player.direction.x > 0:
                        self.player.rect.right = t.rect.left
                        self.player.health -= 1
    # Player camera
    def camera(self):
        x = self.player.rect.centerx
        direction_x = self.player.direction.x

        if x < 200:
            WIDTH / 2

    def run(self):
        # Drawing Sprites
        for i in range(len(self.sprite_group)):
            self.sprite_group[i].draw(self.sur)
            self.sprite_group[i].update()
        self.trap_collision(self.sprite_group[4])
        self.camera()
