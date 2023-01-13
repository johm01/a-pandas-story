from csv import reader 
from os import walk 
import pygame 
import cv2

# Game settings 
WIDTH, HEIGHT = 1080,720
FPS = 60

player_img = ['./assets/Player/player.png','./assets/Player/player.png']
bamboo_img = ['./assets/Player/bamboo_1.png']

# CSV Layouts
def import_csv_layout(path):
    terrian_map = []
    with open(path) as level_map:
        layout = reader(level_map,delimiter = ',')
        for row in layout:
            terrian_map.append(list(row))
        return terrian_map

layouts = {
    #'level_1':import_csv_layout() 
}

