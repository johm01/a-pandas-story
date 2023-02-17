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

        self.level = Level()

    def run(self): 
        # Main game loop 
        while True:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit() 

            # Updating display
            self.screen.fill('black')
            self.screen.blit(self.bg,(0,0))
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
