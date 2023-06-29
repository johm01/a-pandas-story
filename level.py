from settings import *
import pygame 
from objects import Tile,Trap
from mob import Mob,Projectile,ProjectileSpawner
from player import Player

class Level:
    def __init__(self) -> None:
        self.sprite_group = s_groups
        self.bg = pygame.image.load('./assets/Tiles/background.png').convert_alpha()
        self.sur = pygame.display.get_surface()
        self.state = None
        self.start = False
        self.replace = False
        self.clock = pygame.time.Clock()
        self.levels_list = levels
        self.start_game()

    def create_level(self):
        tile = tiles_img
        for row_index, row in enumerate(self.levels_list[self.level]):
            for col_index,col in enumerate(row):
                x = row_index * 64
                y = col_index * 64

                global player

                if col == 'x':
                    self.sprite_group['collide'].add(Tile(img='./assets/Tiles/tile1.png',pos=(x,y)))

                if col == 'n':
                    self.sprite_group['collide'].add(Tile(img='./assets/Tiles/tile_2.png',pos=(x,y)))
                
                if col == 'p':
                    player = Player(vel=4,health=5,pos=(x,y),g=1.25,hp_mod=0,groups=[self.sprite_group['player']])

                if col == 'b':
                    self.sprite_group['bamboo'].add(Tile(img=tile[2],pos=(x,y)))

                if col == 'l':
                    self.sprite_group['item'].add(Collectible(pos=(x+25,y-45),type='fruit'))

                if col == 'r':
                    self.sprite_group['relic'].add(Collectible(pos=(x+2.5,y-35),type='relic'))
                
                if col == 'f':
                    self.sprite_group['flag'].add(Flag(pos=(x,y-62.5)))

                if col == 's':
                    self.sprite_group['collide'].add(Tile(img=tile[1],pos=(x,y)))

                if col == 't':
                    self.sprite_group['trap'].add(Tile(img='./assets/Tiles/spike.png',pos=(x,y)))

                # Create different mobs for passive and moving mobs 
                if col == 'm1':
                    self.sprite_group["mob_1"].add(Mob(img='./assets/Mobs/mob1.png',pos=(x,y),type='mob_1'))
                if col == 'm2':
                    self.sprite_group["mob_2"].add(Mob(img='./assets/Mobs/mob1.png',pos=(x,y),type='mob_2'))
                if col == 'pj':
                    self.sprite_group["proj_spawner"].add(ProjectileSpawner(pos=(x,y-25)))
                if col == 'ps':
                    self.sprite_group["projectile"].add(Projectile(pos=(x,y+20)))
    
    
    def empty_level(self):
        for i in self.sprite_group:  
            self.sprite_group[i].empty()

    def respawn(self):
        self.empty_level()
        self.create_level()

    def player_loss_hp(self,hp):
        player.health -= hp
        print(player.health)
        if player.health <= 0:
            self.respawn()

    def finish_level(self):
        if player.reclic_collected == len(self.sprite_group['relic']):
            # Change level when player has the same amount of relics as the level has
            self.level = self.level + 1
            self.respawn()

    # Player obj collision
    def obj_collision(self,obj):
        mob = ['mob_1','mob_2']
        for t in self.sprite_group[obj]:
            if obj == 'trap':
                if t.rect.colliderect(player.rect):
                    self.player_loss_hp(player.health)

            if obj == 'mob_2':
                if t.rect.colliderect(player.rect):
                    self.player_loss_hp(1)

            if obj == 'mob_1':
                if t.rect.colliderect(player.rect):
                    self.player_loss_hp(1)
                        
            if obj == 'flag':
                if t.rect.colliderect(player.rect):
                    self.finish_level()

    # GUI
    def create_ui(self):
        self.b1 = button(self.sur,(150,0),'Level 1')
        self.b3 = button(self.sur,(450,0),'Level 2')
        self.b2 = button(self.sur,(250,0),'Emtpy Level')

    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                # Button actions 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.b1.collidepoint(pygame.mouse.get_pos()):
                        print('starting level')
                        self.level = 0
                        self.empty_level()
                        self.create_level()
        
                    
                    if self.b3.collidepoint(pygame.mouse.get_pos()):
                        print('starting level')
                        self.level = 1
                        self.create_level()
                    
                    if self.b2.collidepoint(pygame.mouse.get_pos()):
                        print('clearing level')
                        # Clearing the current level 
                        self.level = 2
                        self.empty_level()

            # DO NOT SWAP THESE LOL IT WILL GIVE BRAIN ACHE 
            self.sur.blit(self.bg,(0,0))
            self.create_ui()

            self.run()
            pygame.display.update()
            self.clock.tick(FPS)

    def run(self):
        # Drawing Sprites
        for i in self.sprite_group:  
            self.sprite_group[i].draw(self.sur)
            self.sprite_group[i].update()

        self.obj_collision('trap')
        self.obj_collision('mob_1')
        self.obj_collision('mob_2')
        self.obj_collision('flag')

class Collectible(pygame.sprite.Sprite):
    def __init__(self,pos,type) -> None:
        super().__init__()
        self.sur = pygame.display.get_surface()
        self.image = pygame.image.load('./assets/Tiles/dead.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.sprite_groups = s_groups
        self.type = type
        self.fruit_collected = False
        self.fruit_gain = 2
        self.relic_gain = 1
        self.relic_collected = False

        if self.type == 'coin':
            self.image = pygame.image.load('./assets/Tiles/coin.png').convert_alpha()
        elif self.type == 'fruit':
            self.image = pygame.image.load('./assets/Tiles/fruit.png').convert_alpha()
        elif self.type == 'relic':
            self.image = pygame.image.load('./assets/Tiles/relic.png').convert_alpha()

    def collision(self):
        # Player sprite colliding with item sprite 
        for s in self.sprite_groups['player']:
            if s.rect.colliderect(self.rect) and self.type == 'coin':
                self.image = pygame.image.load('./assets/Tiles/dead.png').convert_alpha()
         
            if s.rect.colliderect(self.rect) and self.type == 'fruit':
                if not player.is_dead and player.health >= 1:
                    player.health += self.fruit_gain
                    self.fruit_collected = True
                    if self.fruit_collected:
                        self.image = pygame.image.load('./assets/Tiles/dead.png').convert_alpha()
                        self.fruit_gain = 0
                else:
                    player.health += player.hp_mod

            if s.rect.colliderect(self.rect) and self.type == 'relic':
                player.reclic_collected += self.relic_gain
                self.relic_collected = True
                if self.relic_collected:
                    self.image = pygame.image.load('./assets/Tiles/dead.png').convert_alpha()
                    self.relic_gain = 0

    def update(self):
        self.collision()

# Flag to move onto the next level
class Flag(pygame.sprite.Sprite):
    def __init__(self,pos) -> None:
        super().__init__()
        self.image = pygame.image.load('./assets/Tiles/flag.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
    
