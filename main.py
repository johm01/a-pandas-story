import pygame
from settings import * 
from Level import *

# Main Player class 
class Player():
    
    # Loading Player sprites 
    images = player_img

    def __init__(self,vel) -> None:

        # Player image 
        self.img = pygame.image.load(self.images[0]).convert_alpha()
        self.rect = self.img.get_rect()
        pygame.transform.scale(self.img,(4,4))
        self.vel = vel

        self.on_bamboo = False
        self.moving_x = True 

    # Player Movement
    def movement(self,key) -> None:
        if key[pygame.K_RIGHT] and self.moving_x:
            self.rect.x += self.vel
            self.img = pygame.image.load(self.images[0+ 1])
            print('right')
        elif key[pygame.K_LEFT] and self.moving_x:
            self.rect.x -= self.vel
            print('left')

# Bamboo object class
class Bamboo:
    def __init__(self) -> None:
        self.img = pygame.image.load(bamboo_img[0])
        self.rect = self.img.get_rect()
            
class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.sur = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

        self.player = Player(3)
        self.bamboo = Bamboo()

    # Drawing player and other things 
    def draw(self):
        self.sur.blit(self.player.img,self.player.rect)
        self.sur.blit(self.bamboo.img,self.bamboo.rect)

    def run(self): 
        # Main game loop 
        while True:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()

               if event.type == pygame.KEYDOWN: 
                    # Stick to bamboo
                    if event.key == pygame.K_q and pygame.Rect.colliderect(self.player.rect,self.bamboo.rect) and not self.player.on_bamboo:
                        self.player.on_bamboo = True
                        # Player is on bamboo
                        if self.player.on_bamboo:
                            self.player.vel = 3
                            self.player.moving_x = False
                            print('On Bamboo',self.player.on_bamboo)

                    # Player moving up and down bamboo
                    if event.key == pygame.K_UP and self.player.on_bamboo:
                        self.player.rect.y -= self.player.vel 
                    elif event.key == pygame.K_DOWN and self.player.on_bamboo:
                        self.player.rect.y += self.player.vel

                    # Jump off bamboo
                    if event.key == pygame.K_e and self.player.on_bamboo:
                        self.player.on_bamboo = False
                        self.player.vel = 3
                        self.player.moving_x = True
                        print('Off Bamboo', self.player.on_bamboo)

            # Getting Inputs 
            keys = pygame.key.get_pressed()
            self.player.movement(keys)

            # Updating display
            self.screen.fill('black')
            self.draw()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()