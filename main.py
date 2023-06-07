import pygame
from settings import * 
from level import Level


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.bg = pygame.image.load('./assets/Tiles/background.png')
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.sur = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

        self.start = False
        self.level = True
        self.lev = Level()
     
if __name__ == '__main__':
    game = Game()
