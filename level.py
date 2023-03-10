from settings import *
import pygame 
from Tile import Tile
from player import Player

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

class Level:
    def __init__(self) -> None:
        self.sprite_group = orders
        self.bg = pygame.image.load('./assets/Tiles/background.png').convert_alpha()
        self.sur = pygame.display.get_surface()
        self.state = None
        self.start = False
        self.replace = False
        self.clock = pygame.time.Clock()
        self.start_game()

    def create_level(self):
        tile = tiles_img
        for row_index, row in enumerate(self.level):
            for col_index,col in enumerate(row):
                x = row_index * 64
                y = col_index * 64

                global player
                self.coins = []

                if col == 'x':
                    self.sprite_group[1].add(Tile(img='./assets/Tiles/tile1.png',pos=(x,y),groups=[self.sprite_group[1],self.sprite_group[2]]))

                if col == 'n':
                    self.tile_1 = Tile(img='./assets/Tiles/tile_2.png',pos=(x,y),groups=[self.sprite_group[1],self.sprite_group[2]])
                
                if col == 'p':
                    player = Player(vel=4,health=5,groups=self.sprite_group[4],pos=(x,y),g=1.2,hp_mod=0)

                if col == 'b':
                    self.sprite_group[0].add(Tile(img=tile[2],groups=[self.sprite_group[0]],pos=(x,y)))

                if col == 'l':
                    self.sprite_group[3].add(Collectible(groups=[self.sprite_group[3]],pos=(x+25,y-45),type='coin'))

                if col == 's':
                    self.sprite_group[2].add(Tile(img=tile[1],pos=(x,y),groups=[self.sprite_group[1],self.sprite_group[2]]))

                if col == 't':
                    self.sprite_group[5].add(Tile(img='./assets/Tiles/spike.png',pos=(x,y),groups=[self.sprite_group[1],self.sprite_group[5]]))
    
    def replace_level(self):
        for row_index, row in enumerate(self.level):
            for col_index,col in enumerate(row):
                x = row_index * 64
                y = col_index * 64

                global player
                self.cols = ['x','n','p','b','l','s','t','']

                if col == 't':
                    Tile(img='./assets/Tiles/dead.png',pos=(x,y),groups=[self.sprite_group[1]])
                   
    def trap_collision(self,trap):
        for t in trap:
            if t.rect.colliderect(player.rect):
                # Checking health everytime we hit a trap instead of constantly checking it within the player update method
                player.health -= 1
                player.health_check()
                if player.direction.y > 0: 
                        player.rect.bottom = t.rect.top
                        player.direction.y = 0
                elif player.direction.y < 0:
                        player.rect.top = t.rect.bottom
                        player.direction.y = 0

                if player.direction.x < 0:
                        player.rect.left = t.rect.right
                elif player.direction.x > 0:
                        player.rect.right = t.rect.left

    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.b1.collidepoint(pygame.mouse.get_pos()):
                        print('starting level')
                        self.level = level_1
                        self.create_level()
                    
                    if self.b2.collidepoint(pygame.mouse.get_pos()):
                        print('clearing level')
                        # Replacing the current level
                        self.level = empty
                        for i in range(len(self.sprite_group)):
                            self.sprite_group[i].empty()
            
            self.sur.blit(self.bg,(0,0))

            # Buttons
            self.b1 = button(self.sur,(150,0),'Level 1',level_1)
            #self.b3 = button(self.screen,(350,0),'Level 2')
            self.b2 = button(self.sur,(250,0),'Clear Level',empty)

            self.run()
            pygame.display.update()
            self.clock.tick(FPS)

    def run(self):
        # Drawing Sprites
        for i in range(len(self.sprite_group)):
            self.sprite_group[i].draw(self.sur)
            self.sprite_group[i].update()

        self.trap_collision(self.sprite_group[5])
    
class Collectible(pygame.sprite.Sprite):
    def __init__(self, groups, pos, type) -> None:
        super().__init__(groups)
        self.sur = pygame.display.get_surface()
        self.image = pygame.image.load('./assets/Tiles/dead.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.sprite_groups = orders
        self.type = type
        self.collected = False

        if self.type == 'coin':
            self.image = pygame.image.load('./assets/Tiles/coin.png').convert_alpha()
        elif self.type == 'fruit':
            self.image = pygame.image.load('./assets/Tiles/fruit.png').convert_alpha()
        elif self.type == 'soda':
            self.image = pygame.image.load('./assets/Tiles/can.png').convert_alpha()

    def collision(self):
        for s in self.sprite_groups[4]:
            if s.rect.colliderect(self.rect) and self.type == 'coin':
                self.image = pygame.image.load('./assets/Tiles/dead.png').convert_alpha()
                self.collected = True 
            # If the player walks over the already collected coin 
            elif s.rect.colliderect(self.rect) and self.type == 'coin' and self.collected:
                pass

            if s.rect.colliderect(self.rect) and self.type == 'fruit':
                self.collected = True 
                if not player.is_dead and player.health >= 1:
                    player.health += 2
                else:
                    player.health += player.hp_mod

    def update(self):
        self.collision()
