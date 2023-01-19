import pygame 
from settings import *

class Bamboo(pygame.sprite.Sprite):
    def __init__(self,groups,pos) -> None:
        super().__init__(groups)

        self.image = pygame.image.load(bamboo_img[0]).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
    
        
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

        