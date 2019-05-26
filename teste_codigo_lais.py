import time
import random
import pygame
from os import path
from init import HEIGHT, WIDTH, BLACK, WHITE, img_dir, snd_dir, fundos, FPS, INIT, GAME, OVER, QUIT, YELLOW, fnt_dir
from teste_player_lais import Player
from Bullet import Bullet
from mob import Mob
from Mob2 import Mob2
from Mob3 import Mob3
from Rasengan import Rasengan, Power, Nrpower, Nrm
from plataforma import Plataforma
#from morte import Morte
#plataforma
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, 40)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def game_screen(screen):
    contador = 0
    clock = pygame.time.Clock()
    # Carrega o fundo do jogo
    background = pygame.image.load(path.join('Fundo4.jpg')).convert()
    background_rect = background.get_rect()
    x = 0 
    vx = 0
    
    #gravidade
    g = 1
    
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
    pygame.mixer.music.play(loops=-1)
    PLAYING = 0
    state = PLAYING
    MORRENDO= 1
    DONE = 2
    
    
    #Cria Pontuação
    score = 0
    
    #Cria Vidas
    vidas=3
    
    while state != DONE and contador < 3:
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
        if random.randrange(1,200) == 1:
            mob = Mob()

            # Cria um grupo só do inimigo
            all_sprites.add(mob)
            monsters.add(mob)
        
        if random.randrange(1, 50) == 1:
            #Cria plataforma
            tamanhos = [1, 3, 5]
            plat = Plataforma(WIDTH, HEIGHT-325, tamanhos[random.randrange(0, 3)])
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
                    
                if event.key == pygame.K_UP:#pulo
                    player.speedy = -15
                        
                if event.key == pygame.K_DOWN:
                    player.speedy = 10
                    
                if event.key == pygame.K_SPACE:
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
                    
                if event.key == pygame.K_m:
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
                if event.key == pygame.K_UP:
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
                if event.key == pygame.K_DOWN:
                    player.speedy = 0
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
                player.speedy +=g 
                    
        # Verifica se houve colisão entre tiro e inimigo
        hits = pygame.sprite.groupcollide(monsters, bullets, True, True)
        for hit in hits:
            # Pode haver mais de um
            score += 50 
            # O meteoro e destruido e precisa ser recriado
            destroy_sound.play()
            contador += 1
            #m = Mob() 
            #all_sprites.add(m)
            #monsters.add(m)
            
        
        # Verifica se houve colisão entre personagem e inimigo
        hits = pygame.sprite.spritecollide(player, monsters, False, pygame.sprite.collide_circle)
        if hits:
            # Toca o som da colisão
            boom_sound.play()
            #time.sleep(5) # Precisa esperar senão fecha
            #morte
            #morte = Morte(hit.rect.center)
            #all_sprites.add(morte)
            
            boom_sound.play()
            #all_sprites.add(morte)
            #state = MORRENDO
            #morte_tick = pygame.time.get_ticks()
            #morte_duration = morte.frame_ticks * len(morte.morte_anim) + 400
            #if vidas<=0:
            player.kill()
            running = False
            #else:
                #vidas-=1
                
                
            
                    
        
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        rel_x = x % background.get_rect().width
        x+= vx
        screen.blit(background, (rel_x -background.get_rect().width , 0))
        
        if  rel_x  < WIDTH:
            screen.blit(background, (rel_x, 0))
        all_sprites.draw(screen)
        
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
    #Desenha pontuação
    draw_text(screen, str(score), 18, WIDTH/2, 50)
    #Desenha vidas
    #draw_text(screen, str(vidas), 18, WIDTH/2, 80)
        
        
    g = 0
        
    while state != DONE and contador >= 3:
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
        if random.randrange(1,200) == 1:
            mob = Mob()

        if random.randrange(1, 50) == 1:
            #Cria plataforma
            tamanhos = [1, 3, 5]
            plat = Plataforma(WIDTH, HEIGHT-325, tamanhos[random.randrange(0, 3)])
            all_sprites.add(plat)
            plataformas.add(plat)
            
        
        
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
                    
                if event.key == pygame.K_UP:#pulo
                    player.speedy = -15
                    
                    if player.rect.y < HEIGHT/2 - 45.5:#gravidade
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
                if event.key == pygame.K_m:
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
                if event.key == pygame.K_DOWN:
                    player.speedy = 0
                if event.key == pygame.K_SPACE:
                    player.imgs = []
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
                time.sleep(1e-2)
                
                    
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
            
            
        # No lugar do meteoro antigo, adicionar uma explosão.
        
        
        
        # Verifica se houve colisão entre personagem e inimigo
        hits = pygame.sprite.spritecollide(player, monsters, False, pygame.sprite.collide_circle)
        if hits:
            # Toca o som da colisão
            #morte = Morte(hit.rect.center)
            #all_sprites.add(morte)
            
            boom_sound.play()
            #all_sprites.add(morte)
            #state = MORRENDO
            #morte_tick = pygame.time.get_ticks()
            #morte_duration = morte.frame_ticks * len(morte.morte_anim) + 400
            #if vidas<=0:
            player.kill()
            state = DONE
            #else:
                #vidas-=1
                #state = MORRENDO
                #now = pygame.time.get_ticks()
                #if now - morte_tick > morte_duration:
                    #state = PLAYING
                
                
            
        #elif state == MORRENDO:
           # now = pygame.time.get_ticks()
            #if now - morte_tick > morte_duration:
             #   state = DONE
                
            time.sleep(5) # Precisa esperar senão fecha
            
                    
        
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
        
        hits = pygame.sprite.spritecollide(player, plataformas, False)
        if hits:
            player.rect.y = hits[0].rect.top
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
        
        #Desenha pontuação
        draw_text(screen, str(score), 18, WIDTH/2, 50)
        #Desenha vidas
        #draw_text(screen, str(vidas), 18, WIDTH/2, 80)
        
        
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    
    return OVER
        