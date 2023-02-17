from csv import reader 
from os import walk 
import pygame 
import cv2

# Game settings 
WIDTH, HEIGHT = 1280,720
FPS = 60

player_img = ['./assets/Player/player.png','./assets/Player/player.png']
bamboo_img = ['./assets/Player/bamboo_1.png']
enemy_img = ['./assets/Mobs/mob1.png']
tiles_img = ['./assets/Tiles/tile1.png']

# Sprite Groups
visable_sprite = pygame.sprite.Group()
collide_sprite = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
bamboo_sprite = pygame.sprite.Group()

# Order of sprite groups
orders = [bamboo_sprite,visable_sprite,collide_sprite,player_sprite]

# Levels 
level_1 = [
    ['','','','','','p','x','','','','','','','','','','','','',''],
    ['','','','','','','x','','','','','','','','','','','','',''],
    ['','','','','','','x','','','','','','','','','','','','',''],
    ['','','','','','','x','','','','','','','','','','','','',''],
    ['','','','','','s','x','','','','','','','','','','','','',''],
    ['l','','','','','t','x','','','','','','','','','','','','',''],
    ['l','','','','b','b','x','','','','','','','','','','','','',''],
    ['','','','','s','t','x','','','','','','','','','','','','',''],
    ['','','','','','t','x','','','','','','','','','','','','',''],
    ['','','','','s','','x','','','','','','','','','','','','',''],
    ['','','','','','','x','','','','','','','','','','','','',''],
    ['','','','s','','','x','','','','','','','','','','','','',''],
    ['','','','','','','x','','','','','','','','','','','','',''],
    ['','','','','','','x','','','','','','','','','','','','',''],
    ['','','','','','','x','','','','','','','','','','','','',''],
    ['','','','','s','','x','','','','','','','','','','','','',''],
    ['','','','','','','x','','','','','','','','','','','','',''],
    ['','','','','','','x','','','','','','','','','','','','',''],
    ['','','','','','','x','','','','','','','','','','','','',''],
    ['','','','','','b','x','','','','','','','','','','','','',''],
]

level_2 = [
    [' ','','','','','','','','','','','','','','','','','','',''],
    ['','','','','','','','','','','','','','','','','','','',''],
    ['','','','','','','','','','','','','','','','','','','',''],
    ['','','','','','','','','','','','','','','','','','','',''],
    ['','','','','','','','','','','','','','','','','','','',''],
    ['','','','','','','','','','','','','','','','','','','',''],
    ['','','','','','','','','','','','','','','','','','','',''],
    ['','','','','','','','','','','','','','','','','','','',''],
    ['','','','','','','','','','','','','','','','','','','',''],
    ['','','','','','','','','','','','','','','','','','','',''],
    ['','','','','','','','','','','','','','','','','','','',''],
    ['','','','','','','','','','','','','','','','','','','',''],
    ['','','','','','','','','','','','','','','','','','','',''],
    ['','','','','','','','','','','','','','','','','','','',''],
    ['','','','','','','','','','','','','','','','','','','',''],
    ['','','','','','','','','','','','','','','','','','','',''],
]

# Level order
levels = [level_1,level_2]
