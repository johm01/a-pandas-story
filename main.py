import pygame
from settings import * 
from Enemy import Enemy
from Tile import Tile
from level import Level

# Main Player class 
class Player(pygame.sprite.Sprite):
    
    # Loading Player sprites 
    images = player_img

    def __init__(self,vel,health,groups,pos) -> None:
        super().__init__(groups)

        # Player image 
        self.image = pygame.image.load(self.images[0]).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
        
        self.vel = vel
        self.health = health 

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

    def update(self):
        self.movement(pygame.key.get_pressed())

# Bamboo object class
class Bamboo(pygame.sprite.Sprite):
    def __init__(self,groups,pos) -> None:
        super().__init__(groups)
        self.image = pygame.image.load(bamboo_img[0])
        self.rect = self.image.get_rect(topleft=pos)
    
    def player_on_bamboo(self,player):
        e = pygame.key.get_pressed()
        if e[pygame.K_SPACE] and pygame.Rect.colliderect(player.rect,self.rect) and not player.on_bamboo:
            player.on_bamboo = True
            print('On Bamboo')
            # Player is on bamboo
            if player.on_bamboo:
                    player.vel = 3
                    player.moving_x = False
                    print('On Bamboo', player.on_bamboo)

        # Player moving up and down bamboo
        if e[pygame.K_UP] and player.on_bamboo:
                player.rect.y -= player.vel 
        elif e[pygame.K_DOWN] and player.on_bamboo:
                player.rect.y += player.vel

        # Jumping from bamboo to bamboo tree
        if player.on_bamboo and e[pygame.K_SPACE]:
                pass

        # Jump off bamboo
        if e[pygame.K_e] and player.on_bamboo:
                player.on_bamboo = False
                player.vel = 3
                player.moving_x = True
                print('Off Bamboo',player.on_bamboo)

class Game:
    def __init__(self) -> None:
        pygame.init()
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

            # Getting Inputs 
            self.player.update()

            # Updating display
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
