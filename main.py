import pygame
from settings import * 
from Enemy import Enemy
from Tile import Tile

# Main Player class 
class Player():
    
    # Loading Player sprites 
    images = player_img

    def __init__(self,vel,health) -> None:

        # Player image 
        self.img = pygame.image.load(self.images[0]).convert_alpha()
        self.rect = self.img.get_rect()
        pygame.transform.scale(self.img,(4,4))
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

# Bamboo object class
class Bamboo(pygame.sprite.Sprite):
    def __init__(self,groups,pos) -> None:
        super().__init__(groups)
        self.image = pygame.image.load(bamboo_img[0])
        self.rect = self.image.get_rect(topleft=pos)
            
class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.sur = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

        # Sprite groups 
        self.visable_sprite = pygame.sprite.Group()
        self.obstacle_sprite = pygame.sprite.Group()

        # Game objects 
        self.player = Player(vel=3,health=5)
        self.enemy = Enemy()

    # Drawing players and other sprites 
    def draw(self):
        self.sur.blit(self.player.img,self.player.rect)
        self.visable_sprite.draw(self.sur)
    
    # Level Loading 
    def loadlevel(self,level):
        for row_index, row in enumerate(level):
            for col_index,col in enumerate(row):
                x = row_index * 64
                y = col_index * 64

                global active_tiles 
                active_tiles = []

                if col == 'x':
                    Tile(img='./assets/Tiles/tile1.png',pos=(x,y),groups=self.visable_sprite)
                elif col == 'b':
                    Bamboo(pos=(x,y),groups=self.visable_sprite)
    def run(self): 
        # Main game loop 
        while True:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()

               # Getting user input  
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

                    # Jumping from bamboo to bamboo tree
                    if self.player.on_bamboo and event.key == pygame.K_SPACE:
                        pass

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
            self.loadlevel(level_1)
            self.draw()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
