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

#Carrega tela inicial
inicio = pygame.image.load(path.join('tela3.png')).convert()
inicio_rect = inicio.get_rect()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(fundos, 'Fundo2.jpg')).convert()
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

#Cria um grupo para plataformas
plataformas = pygame.sprite.Group()

# Cria um grupo de todos os sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


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
            
        if random.randrange(1, 50) == 1:
            #Cria plataforma
            tamanhos = [1, 3, 5]
            plat = Plataforma(WIDTH, HEIGHT-300, tamanhos[random.randrange(0, 3)])
            all_sprites.add(plat)
            plataformas.add(plat)
        
        
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
        
        if  rel_x  < WIDTH:
            screen.blit(background, (rel_x, 0))
            
        for p in plataformas:
            p.move(vx)
            
            
        all_sprites.draw(screen)
        
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
        
        
finally:
    
    pygame.quit()