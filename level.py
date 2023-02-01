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
                    self.player = Player(vel=2,health=5,groups=self.sprite_group[3],pos=(x,y),g=9.8)

                if col == 'b':
                    Tile(img='./assets/Player/bamboo_1.png',groups=[self.sprite_group[1],self.sprite_group[0]],pos=(x,y))

                if col == 'l':
                    Tile(img='./assets/Tiles/leaf.png',groups=[self.sprite_group[1]],pos=(x,y))

                if col == 'f':
                    Tile(img='./assets/Tiles/fruit.png',groups=[self.sprite_group[1]],pos=(x,y))  

    # Player on bamboo                  
    def player_onbamboo(self,player):
        e = pygame.key.get_pressed()
        for sprite in self.sprite_group[0]:
            if sprite.rect.colliderect(player.rect) and e[pygame.K_q] and not player.on_bamboo:
                player.on_bamboo = True
                print('On Bamboo')
                # Player is on bamboo

        if player.on_bamboo:
            player.vel = 3
            player.moving_x = False
            print('On Bamboo', player.on_bamboo)

        # Player moving up and down bamboo
        if e[pygame.K_UP] and player.on_bamboo:
            player.rect.y -= player.vel 
        elif e[pygame.K_DOWN] and player.on_bamboo:
            player.rect.y += player.vel

        # Jump off bamboo
        if e[pygame.K_e] and player.on_bamboo:
            player.on_bamboo = False
            player.vel = 3
            player.moving_x = True
            print('Off Bamboo',player.on_bamboo)   

    def run(self):
        self.player_onbamboo(self.player)

         # Drawing Sprites
        for i in range(len(self.sprite_group)):
            self.sprite_group[i].draw(self.sur)
            self.sprite_group[i].update()
