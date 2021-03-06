import time
import pygame
from os import path
from init import HEIGHT, WIDTH, BLACK, img_dir, snd_dir, fundos, FPS
from player import Player
from Bullet import Bullet
from Rasengan import Rasengan

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Corrida Naruto")

clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(fundos, 'Fundo.png')).convert()
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
                    player.step = 5
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    
                if event.key == pygame.K_UP and player.rect.y == HEIGHT/2 - 45.5:#pulo
                    player.speedy = -15
                    g = 1
                    while player.rect.y < HEIGHT/2 - 45.5:#gravidade
                        player.speedy +=g 
                        all_sprites.update()
                        time.sleep(1e-2)
                        screen.fill(BLACK)
                        screen.blit(background, (x, 0))
                        all_sprites.draw(screen)
                        pygame.display.flip()
                        
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
                    player.image = pygame.transform.scale(player.image, (1,1))
                    ras = Rasengan(player.rect.centerx, player.rect.top)
                    all_sprites.add(ras)
                    bullets.add(ras)
                    pew_sound.play()

                                
            #################################        
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
                if event.key == pygame.K_DOWN:
                    player.speedy = 0
                if event.key == pygame.K_SPACE:
                    player.imgs = []
                    n=6
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join("Run{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    player.speedx = 0
                    player.step=5
                if event.key == pygame.K_m:
                    player.imgs = []
                    player.steps = 5
                    n=6
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join("Run{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.steps = 5
                    player.image = player.imgs[player.frame]
                    
                    player.image = pygame.transform.scale(player.image, (1,1))
                    player.speedx = 0
                   ######################### 
                while player.rect.y < HEIGHT/2 - 45.5:#gravidade
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
                        all_sprites.update()
                        time.sleep(1e-2)
                        screen.fill(BLACK)
                        screen.blit(background, (x, 0))
                        all_sprites.draw(screen)
                        pygame.display.flip()
                    
                    if event.key == pygame.K_RIGHT:
                        vx = -8
                        player.imgs = []
                        n=6
                        for i in range(n):
                            player.imgs.append(pygame.image.load(path.join("Run{0}.png".format(i+1))).convert())
                        player.frame = 0
                        player.step = 5
                        player.image = player.imgs[player.frame]
                        player.image = pygame.transform.scale(player.image, (1,1))
                        all_sprites.update()
                        time.sleep(1e-2)
                        screen.fill(BLACK)
                        screen.blit(background, (x, 0))
                        all_sprites.draw(screen)
                        pygame.display.flip()
                        
                    player.speedy +=g 
                    all_sprites.update()
                    time.sleep(8e-3)
                    screen.fill(BLACK)
                    screen.blit(background, (x, 0))
                    all_sprites.draw(screen)
                    pygame.display.flip()
                
                    
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
            time.sleep(5) # Precisa esperar senão fecha
            
            running = False
                    
        
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        x+= vx
        screen.blit(background, (x, 0))
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
        
        
finally:
    
    pygame.quit()