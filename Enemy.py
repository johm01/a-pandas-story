import pygame 
from settings import *

class Enemy:
    sprite = enemy_img
    def __init__(self) -> None:
        self.img = pygame.image.load(enemy_img[0])
        self.rect = self.img.get_rect()