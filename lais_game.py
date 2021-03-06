import time
import random
import pygame
from os import path
from init import HEIGHT, WIDTH, BLACK, WHITE, img_dir, snd_dir, FPS, QUIT, OVER, HS_FILE, PLAYER_STATE_MORRENDO, PLAYER_STATE_MORTO, PLAYER_STATE_VIVO
from player import Player
from Bullet import Bullet
from mob import Mob
from Mob2 import Mob2
from Mob3 import Mob3
from Rasengan import Rasengan, Nrpower, Nrm
from bullet_1 import Bullet1



#def load_assets(img_dir, snd_dir, fnt_dir):
    #assets = {}
    #assets["score_font"] = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
    #return assets
#load_assets  
#print


font_name = pygame.font.match_font('arial')
highscore = 0
score = 0

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)



def game_screen(screen):
    
    g = 1
    
    contador = 0
    
    clock = pygame.time.Clock()
    # Carrega o fundo do jogo
    background = pygame.image.load(path.join('Fundo4.jpg')).convert()
    x = 0 
    vx = 0
    
    #Cria pontuação
    score = 0
    
    chakra = 150
    #assets = load_assets(img_dir, snd_dir, fnt_dir)
    #score_font = assets["score_font"]
    
    dir = path.dirname(__file__)
    with open(path.join(dir, HS_FILE), 'w') as f:
        try:
            highscore = int(f.read())
        except:
            highscore = 0
    
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
    pygame.mixer.music.play(loops=-1)
    PLAYING = 0
    state = PLAYING
    DONE = 2
    running=True
    
    
    
                
            
            
    
## Primeiro while
    while state != DONE and contador < 25 and running:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        if random.randrange(1,100) == 1:
            mob1 = Mob3()
            all_sprites.add(mob1)
            monsters.add(mob1)
            
        if random.randrange(1,200) == 1:
            mob2 = Mob2()
            all_sprites.add(mob2)
            monsters.add(mob2)
            disparo = Bullet1(mob2.rect.centerx, mob2.rect.top)
            all_sprites.add(disparo)
            bullets.add(disparo)
        
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    vx = 8
                    player.imgs = []
                    n=6
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Left{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.step = 5
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    
                if event.key == pygame.K_RIGHT:
                    vx = -8
                    player.imgs = []
                    n=6
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Run{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.step = 5
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    
                if event.key == pygame.K_UP and player.rect.y == HEIGHT/2 - 45.5:#pulo
                    player.speedy = -20
                    
                if event.key == pygame.K_SPACE and chakra >= 5:
                    chakra -= 5
                    player.imgs = []
                    n=5
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Punch{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.step=5
                    player.image = pygame.transform.scale(player.image, (1,1))
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    pew_sound.play()
                    
                if event.key == pygame.K_m and chakra >= 50:
                    chakra -= 50
                    player.imgs = []
                    n=6
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "R{0}.png".format(i+1))).convert())
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
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Naruto{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    player.speedx = 0
                    
                if event.key == pygame.K_RIGHT:
                    vx = 0
                    player.imgs = []
                    n=6
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Naruto{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    player.speedx = 0
                    
                if event.key == pygame.K_SPACE:
                    player.imgs = []
                    n=6
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Run{0}.png".format(i+1))).convert())
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
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Run{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.steps = 5
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    player.speedx = 0
                    
        if player.rect.y < HEIGHT/2 - 45.5:#gravidade
            player.speedy += g
                    
        # Verifica se houve colisão entre tiro e inimigo
        hits = pygame.sprite.groupcollide(monsters, bullets, True, True)
        for hit in hits: # Pode haver mais de um
            # O meteoro e destruido e precisa ser recriado
            destroy_sound.play()
            contador += 1
            score += 50
            #m = Mob() 
            #all_sprites.add(m)
            #monsters.add(m)
        
        # Verifica se houve colisão entre personagem e inimigo
        hits = pygame.sprite.spritecollide(player, monsters, False, pygame.sprite.collide_circle)
        for hit in hits:
            # Toca o som da colisão
            boom_sound.play()
            hit.kill()
            player.morrer()

        print(player.vidas)
        running = player.vidas >= 0
            
        chakra += 0.5
        if chakra > 150:
            chakra =150
            vx = -8            
        x += vx
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        rel_x = x % background.get_rect().width
        
        screen.blit(background, (rel_x -background.get_rect().width , 0))
        
        if  rel_x  < WIDTH:
            screen.blit(background, (rel_x, 0))
        all_sprites.draw(screen)
        
        #pontuação
        draw_text(screen, str(score), 35, WIDTH/2, 0)
        draw_text(screen, "Score", 40, WIDTH/2-150, 0)
        #chakra
        draw_text(screen, str(chakra), 35, WIDTH/2+400, 0)
        draw_text(screen, "Chakra", 40, WIDTH/2+200, 0)
        
        
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
        

##Segundo while
    while state != DONE and contador >= 25 and running:
        
        # Ajusta a velocidade do jogo.
        
        clock.tick(FPS)
        if random.randrange(1,200) == 1:
            mob2 = Mob2()
            all_sprites.add(mob2)
            monsters.add(mob2)
            if mob2.rect.x-player.rect.x <= 450:
                disparo = Bullet1(player.rect.centerx, player.rect.top)
                all_sprites.add(disparo)
                bullets.add(disparo)

        
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    vx = 8
                    player.imgs = []
                    n=5
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Flip{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.step = 5
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    
                if event.key == pygame.K_RIGHT:
                    vx = -8
                    player.imgs = []
                    n=8
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Nr{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.step = 3
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    
                if event.key == pygame.K_UP and player.rect.y == HEIGHT/2 - 45.5:#pulo
                    player.speedy = -15
                    g = 1
                    
                if event.key == pygame.K_SPACE and chakra>=10:
                    chakra-=10
                    player.imgs = []
                    n=10
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "P{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.step = 5
                    player.image = pygame.transform.scale(player.image, (1,1))
                    bullet = Nrpower(player.rect.centerx, player.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    pew_sound.play()
                    
                if event.key == pygame.K_m and chakra >= 25:
                    chakra -= 25
                    player.imgs = []
                    n=5
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "NrP{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.step = 5
                    player.image = pygame.transform.scale(player.image, (1,1))
                    powe = Nrm(player.rect.centerx, player.rect.top)
                    all_sprites.add(powe)
                    bullets.add(powe)
                    pew_sound.play()

                                
            #################################        
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    vx = 0
                    player.imgs = []
                    n=8
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Nr{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    player.speedx = 0
                    
                if event.key == pygame.K_RIGHT:
                    vx = 0
                    player.imgs = []
                    n=8
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Nr{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    player.speedx = 0
                    
                if event.key == pygame.K_UP:
                    if event.key == pygame.K_RIGHT:
                        vx = 0
                        player.imgs = []
                        n=8
                        for i in range(n):
                            player.imgs.append(pygame.image.load(path.join(img_dir, "Nr{0}.png".format(i+1))).convert())
                        player.frame = 0
                        player.image = player.imgs[player.frame]
                        player.image = pygame.transform.scale(player.image, (1,1))
                    player.speedx = 0
                    
                if event.key == pygame.K_SPACE:
                    player.imgs = []
                    chakra -= 25
                    n=8
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Nr{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    player.speedx = 0
                    player.step=5
                    
                if event.key == pygame.K_m:
                    player.imgs = []
                    player.steps = 5
                    chakra -= 25
                    n=8
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Nr{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.steps = 5
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    player.speedx = 0
                    
        
                    
        if player.rect.y < HEIGHT/2 - 45.5:#gravidade
            player.speedy +=g 
                    
        # Verifica se houve colisão entre tiro e inimigo
        hits = pygame.sprite.groupcollide(monsters, bullets, True, True)
        for hit in hits: # Pode haver mais de um
            # O meteoro e destruido e precisa ser recriado
            destroy_sound.play()
            contador += 1
            score += 100
            #m = Mob() 
            #all_sprites.add(m)
            #monsters.add(m)
        
        # Verifica se houve colisão entre personagem e inimigo
        hits = pygame.sprite.spritecollide(player, monsters, False, pygame.sprite.collide_circle)
        if hits:
            # Toca o som da colisão
            boom_sound.play()
            hits.kill() # Precisa esperar senão fecha
            
        
        chakra += 1
        if chakra > 149.5:
            chakra =150
        vx = -8            
        x += vx
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
        
        
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        rel_x = x % background.get_rect().width
        screen.blit(background, (rel_x -background.get_rect().width , 0))
        
        if  rel_x  < WIDTH:
            screen.blit(background, (rel_x, 0))
        all_sprites.draw(screen)


        
        
        # Desenha o score
        #text_surface = score_font.render("{:08d}".format(score), True, YELLOW)
        #text_rect = text_surface.get_rect()
        #text_rect.midtop = (500, -100 )
        #screen.blit(text_surface, text_rect)
        
        #pontuação
        draw_text(screen, str(score), 35, WIDTH/2, 0)
        draw_text(screen, "Score", 40, WIDTH/2-150, 0)
        #chakra
        draw_text(screen, str(chakra), 35, WIDTH/2+400, 0)
        draw_text(screen, "Chakra", 40, WIDTH/2+200, 0)
        
        
        
        
        
        
        if  rel_x  < WIDTH:
            screen.blit(background, (rel_x, 0))
            
    #if player.vidas<0:
       # state==OVER
       # if score > highscore:
        #    highscore = score
         #   draw_text(background, " NEW HIGH SCORE!", 40, WIDTH/2-150, 200)
          #  with open(path.join(dir, HS_FILE), 'w') as f:
           #     f.white(str(score))
        #else: 
         #   draw_text(background, str(score), 35, WIDTH/2, 100)
          #  draw_text(background, "Score", 40, WIDTH/2-150, 100)
            
           # draw_text(background, str(highscore), 35, WIDTH/2, 200)
            #draw_text(background, "High Score", 40, WIDTH/2-150, 200)
                
            
        
                
            
            
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    
    return (OVER, score, highscore)










       
