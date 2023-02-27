import pygame
from settings import * 
from level import Level
        
def button(screen,pos,text,level):
    font = pygame.font.SysFont("Arial",25)
    text_r = font.render(text,1,(255,255,0))
    x, y, w , h = text_r.get_rect()
    x, y = pos
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_r, (x, y))


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.bg = pygame.image.load('./assets/Tiles/background.png')
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.sur = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.b1 = button(self.screen,(150,0),'Level 1',level_1)
        self.b2 = button(self.screen,(250,0),'Clear Level',empty)

        self.start = False
        self.level = True
        self.level_select = None
    def run(self): 
        # Main game loop 
        while True:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit() 

               if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.b1.collidepoint(pygame.mouse.get_pos()) and not self.start:
                        print('starting level')
                        self.start = True
                        self.level_select = level_1
                        self.lev = Level(self.level_select)
                    
                    if self.b2.collidepoint(pygame.mouse.get_pos()):
                        print('clearing level')
                        self.level_select = empty
                        self.lev = Level(self.level_select)

            # Starting the level
            if self.start:
                self.screen.blit(self.bg,(0,0))
                self.lev.run()
            
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
