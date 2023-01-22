from settings import *
import pygame 
from Tile import Tile
from player import Player
from bamboo import Bamboo

class Level:
    def __init__(self) -> None:
        # Sprite Groups
        self.sprite_group = groups

        self.sur = pygame.display.get_surface()
        self.create_level()
        
    def create_level(self):
        level = level_1
        
        for row_index, row in enumerate(level):
            for col_index,col in enumerate(row):
                x = row_index * 64
                y = col_index * 64

                global active_tiles
                active_tiles = []

                if col == 'x':
                    Tile(img='./assets/Tiles/tile1.png',pos=(x,y),groups=[self.sprite_group[2],self.sprite_group[3]])
                
                if col == 'p':
                    self.player = Player(vel=2,health=5,groups=self.sprite_group[0],pos=(x,y),g=9.8)

                if col == 'b':
                    Tile(img='./assets/Player/bamboo_1.png',groups=[self.sprite_group[2],self.sprite_group[1]],pos=(x,y))

                if col == 's':
                    pass

    # Player on bamboo                  
    def player_onbamboo(self,player):
        e = pygame.key.get_pressed()
        for sprite in self.sprite_group[1]:
            if sprite.rect.colliderect(player.rect) and e[pygame.K_SPACE] and not player.on_bamboo:
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

        # Jumping from bamboo to bamboo tree
        if player.on_bamboo and e[pygame.K_SPACE]:
                pass

        # Jump off bamboo
        if e[pygame.K_e] and player.on_bamboo:
            player.on_bamboo = False
            player.vel = 3
            player.moving_x = True
            print('Off Bamboo',player.on_bamboo)

    # Player collision
    def player_collision(self,player):
        for sprite in self.sprite_group[3]:
            if sprite.rect.colliderect(player.rect):
                print('hit floor')


    def run(self):
        self.player_onbamboo(self.player)
        self.player_collision(self.player)

         # Drawing Sprites
        for i in range(len(self.sprite_group)):
            self.sprite_group[i].draw(self.sur)
            self.sprite_group[i].update()

