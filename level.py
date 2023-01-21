from settings import *
import pygame 
from Tile import Tile
from player import Player
from bamboo import Bamboo

class Level:
    def __init__(self) -> None:
        self.visable_sprite = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.Group()
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
                    Tile(img='./assets/Tiles/tile1.png',pos=(x,y),groups=self.visable_sprite)
                
                if col == 'p':
                    self.player = Player(vel=2,health=5,groups=self.player_sprite,pos=(x,y),g=9.8)

                if col == 'b':
                    Bamboo(groups=self.visable_sprite,pos=(x,y))

                if col == 's':
                    pass
                    
    def player_onbamboo(self,player):
        e = pygame.key.get_pressed()
        for sprite in self.visable_sprite:
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

  def run(self):
        self.player_onbamboo(self.player)
        
        # Drawing visable sprites
        self.visable_sprite.draw(self.sur)
        self.visable_sprite.update()

        # Drawing Player 
        self.player_sprite.draw(self.sur)
        self.player_sprite.update()
