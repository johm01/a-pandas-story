import pygame
from settings import *

class Level():
    def __init__(self) -> None:
        self.visable_sprite = pygame.sprite.Group()

    def loadlevel(self,level):
        for style, layout in layouts.items():
            for row_index,row in enumerate(layout):
                for col_index,col in enumerate(row):
                    if style == level:
                        pass