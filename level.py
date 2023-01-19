from settings import *
import pygame 
from Tile import Tile
from player import Player
from bamboo import Bamboo

class Level:
    def __init__(self) -> None:
        self.visable_sprite = pygame.sprite.Group()
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

                if col == 'b':
                    Bamboo(groups=self.visable_sprite,pos=(x,y))

                if col == 's':
                    Tile(img='./assets/Tiles/sky.png',pos=(x,y),groups=self.visable_sprite)

                if col == 'p':
                    self.player = Player(vel=2,health=5,groups=self.visable_sprite,pos=(x,y))

    def run(self):
        self.visable_sprite.draw(self.sur)
        self.visable_sprite.update()
