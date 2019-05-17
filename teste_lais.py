import time
import random
import pygame
from os import path
from init import HEIGHT, WIDTH, BLACK, img_dir, snd_dir, fundos, FPS
from player import Player
from Bullet import Bullet
from mob import Mob
from Mob2 import Mob2
from Mob3 import Mob3
from Rasengan import Rasengan
from plataforma import Plataforma

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Corrida Naruto")

clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(fundos, 'Fundo2.png')).convert()
background_rect = background.get_rect()

x = 0 
vx=0


# Carrega os sons do jogo
pygame.mixer.music.load(path.join(snd_dir, 'naruto.mp3'))
pygame.mixer.music.set_volume(0.4)
boom_sound = pygame.mixer.Sound(path.join(snd_dir, 'expl3.wav'))
destroy_sound = pygame.mixer.Sound(path.join(snd_dir, 'expl6.wav'))
pew_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))

player = Player()


# Cria um grupo só do inimigo
monsters = pygame.sprite.Group()

plat1 = Plataforma(700, HEIGHT-300, 50, 50)

#Cria um grupo para plataformas
plataformas = pygame.sprite.Group()

#Cria plataforma 1
plat1 = Plataforma(700, HEIGHT-300, 50, 50)

#Cria plataforma 2
plat2 = Plataforma(900, HEIGHT-300, 50, 50)

#Cria plataforma 3
plat3 = Plataforma (600, HEIGHT-300, 50,50 )

#Cria plataforma 4 
plat4 =  Plataforma (650, HEIGHT-300, 50, 50)

#Cria plataforma 5
plat5 =  Plataforma (1100, HEIGHT-300, 50, 50)

#Cria plataforma 6
plat6 =  Plataforma (1150, HEIGHT-300, 50, 50)

#Cria plataforma 7 
plat7 =  Plataforma (1500, HEIGHT-300, 50, 50)

# Cria um grupo de todos os sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

all_sprites.add(plat1)
plataformas.add(plat1)

all_sprites.add(plat2)
plataformas.add(plat2)

all_sprites.add(plat3)
plataformas.add(plat3)

all_sprites.add(plat4)
plataformas.add(plat4)

all_sprites.add(plat5)
plataformas.add(plat5)

all_sprites.add(plat6)
plataformas.add(plat6)

all_sprites.add(plat7)
plataformas.add(plat7)

bullets = pygame.sprite.Group()

try:
    
    pygame.mixer.music.play(loops=-1)
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        if random.randrange(1,100) == 1:
            mob2 = Mob2()
            all_sprites.add(mob2)
            monsters.add(mob2)
        if random.randrange(1,200) == 1:
            mob3 = Mob3()
            all_sprites.add(mob3)
            monsters.add(mob3)
            if random.randrange(1,10) == 1:
                bullet = Bullet(mob3.rect.centerx, mob3.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                pew_sound.play()
        if random.randrange(1,200) == 1:
            mob = Mob()
            # Cria um grupo só do inimigo
            all_sprites.add(mob)
            monsters.add(mob)
        
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    vx = 8
                    player.imgs = []
                    n=6
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join("Left{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.step = 5
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                if event.key == pygame.K_RIGHT:
                    vx = -8
                    player.imgs = []
                    n=6
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join("Run{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                if event.key == pygame.K_UP:
                    player.speedy = -10
                if event.key == pygame.K_DOWN:
                    player.speedy = 10
                if event.key == pygame.K_SPACE:
                    player.imgs = []
                    n=5
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join("Punch{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.step=5
                    player.image = pygame.transform.scale(player.image, (1,1))
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    pew_sound.play()
                if event.key == pygame.K_m:
                    player.imgs = []
                    n=6
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join("R{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.step=5
                    player.image = pygame.transform.scale(player.image, (11,1))
                    ras = Rasengan(player.rect.centerx, player.rect.top)
                    all_sprites.add(ras)
                    bullets.add(ras)
                    pew_sound.play()

                                
                    
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    vx = 0
                    player.imgs = []
                    n=6
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join("Naruto{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    vx = 0
                    player.imgs = []
                    n=6
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join("Naruto{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    player.speedx = 0
                if event.key == pygame.K_UP:
                    player.speedy = 0
                if event.key == pygame.K_DOWN:
                    player.speedy = 0
                if event.key == pygame.K_SPACE:
                    player.imgs = []
                    n=6
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join("Naruto{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    player.speedx = 0
                    player.step=10
                if event.key == pygame.K_m:
                    player.imgs = []
                    n=6
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join("Naruto{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    player.speedx = 0
        
        # Verifica se houve colisão entre tiro e inimigo
        hits = pygame.sprite.groupcollide(monsters, bullets, True, True)
        for hit in hits: # Pode haver mais de um
            # O meteoro e destruido e precisa ser recriado
            destroy_sound.play()
            #m = Mob()
            #all_sprites.add(m)
            #monsters.add(m)
        
        # Verifica se houve colisão entre personagem e inimigo
        hits = pygame.sprite.spritecollide(player, monsters, False, pygame.sprite.collide_circle)
        if hits:
            # Toca o som da colisão
            boom_sound.play()
            time.sleep(1) # Precisa esperar senão fecha
            
            running = False
                    
        
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
        
        #Colisão entre personagem e plataforma
        hits = pygame.sprite.spritecollide(player, plataformas, False)
        if hits:
            
            player.speedy = 0
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        rel_x = x % background.get_rect().width
        x+= vx
        screen.blit(background, (rel_x -background.get_rect().width , 0))
        plat1.rect.x +=vx
        plat2.rect.x +=vx
        plat3.rect.x +=vx
        plat4.rect.x +=vx
        plat5.rect.x +=vx
        plat6.rect.x +=vx
        plat7.rect.x +=vx
        
        if  rel_x  < WIDTH:
            screen.blit(background, (rel_x, 0))
        all_sprites.draw(screen)
        
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
        
        
finally:
    
    pygame.quit()