import pygame
from settings import *

class Level():
    def __init__(self) -> None:
        self.visable_sprite = pygame.sprite.Group()

    # Loading levels with tiles 
    def loadlevel(self,level):
        for row_index, row in enumerate(level):
            for col_index,col in enumerate(row):
                x = row_index * 64
                y = col_index * 64
                if col == ' ':
                    return 'yes'
