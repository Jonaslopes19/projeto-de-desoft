import time
import random
import pygame
from os import path
from init import HEIGHT, WIDTH, BLACK, WHITE, img_dir, snd_dir, FPS, OVER, QUIT,HS_FILE, PLAYER_STATE_MORRENDO, PLAYER_STATE_MORTO, PLAYER_STATE_VIVO
from player import Player
from Bullet import Bullet
from mob import Mob
from Mob2 import Mob2
from Mob3 import Mob3, Mob4, Amaterasu, Golpetras, Sasori, Kisame, Water, Deidara, Bird
from Rasengan import Rasengan, Nrpower, Nrm, Clone
from bullet_1 import Bullet1



#def load_assets(img_dir, snd_dir, fnt_dir):
    #assets = {}
    #assets["score_font"] = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
    #return assets
#load_assets  
#print

highscore = 0
score = 0

font_name = pygame.font.match_font('arial')
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
    
     
    if random.randrange(1,10)%2 == 0:
        m = 'naruto_normal.mp3'
    else:
        m = 'naruto.mp3'
        
    # Carrega os sons do jogo
    pygame.mixer.music.load(path.join(snd_dir, '{0}'.format(m)))
    pygame.mixer.music.set_volume(0.7)
    boom_sound = pygame.mixer.Sound(path.join(snd_dir, 'expl3.wav'))
    destroy_sound = pygame.mixer.Sound(path.join(snd_dir, 'expl6.wav'))
    kunai_sound = pygame.mixer.Sound(path.join(snd_dir, 'kunai_sound.wav'))
    rasengan_sound = pygame.mixer.Sound(path.join(snd_dir, 'rasengan.wav'))
    rasenshuriken_sound = pygame.mixer.Sound(path.join(snd_dir, 'Rasenshurikenlongo.wav'))
    kage_bushin = pygame.mixer.Sound(path.join(snd_dir, 'Som_Kagebushin.wav'))
    amaterasu_sound = pygame.mixer.Sound(path.join(snd_dir, 'Amaterasu.wav'))
    madara_voice = pygame.mixer.Sound(path.join(snd_dir, 'madara_voice.wav'))
    
    
    player = Player()
    # Cria um grupo só do inimigo
    monsters = pygame.sprite.Group()
    
    
    # Cria um grupo de todos os sprites e adiciona a nave.
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    power = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    pygame.mixer.music.play(loops=-1)
    PLAYING = 0
    state = PLAYING
    DONE = 2
    running=True
    
## Primeiro while
    while state != DONE and score < 500 and running:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        if random.randrange(1,21) == 1:
            mob1 = Mob2()
            all_sprites.add(mob1)
            monsters.add(mob1)    
        
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    player.speedx = -4
                    player.imgs = []
                    n=6
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Left{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.step = 5
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    
                if event.key == pygame.K_RIGHT:
                    player.speedx = 4
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
                    
                if event.key == pygame.K_SPACE and chakra >= 10:
                    chakra -= 10
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
                    kunai_sound.play()
                    
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
                    rasengan_sound.play()

                                
            #################################        
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                    player.imgs = []
                    n=6
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Run{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    player.speedx = 0
                    
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                    player.imgs = []
                    n=6
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Run{0}.png".format(i+1))).convert())
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

        running = player.vidas >= 0
            
        chakra += 0.5
        if chakra > 149.5:
            chakra =150
        elif chakra < 0.5:
            chakra = 0
        vx = -8 - (score/1000)
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
        #Vida
        draw_text(screen, str(player.vidas), 35, WIDTH/2-350, 0)
        draw_text(screen, "Vida", 40, WIDTH/2-450, 0)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
    chakra = 400
##Segundo while
    while state != DONE and score >= 500  and running:
        
        # Ajusta a velocidade do jogo.
        
        clock.tick(FPS)
        if score >= 500:
            if random.randrange(1,300) == 1:
                deid = Deidara()
                all_sprites.add(deid)
                monsters.add(deid)
                bird = Bird()
                all_sprites.add(bird)
                monsters.add(bird)
               
        if score >= 1000:
            if random.randrange(1,300) == 1:
                mob4 = Mob4()
                am = Amaterasu()
                amaterasu_sound.play()
                all_sprites.add(am)
                all_sprites.add(mob4)
                monsters.add(am)
                monsters.add(mob4)
                
        if score >= 500:
            if random.randrange(1,200) == 1:
                tobi = Mob3()
                all_sprites.add(tobi)
                monsters.add(tobi)
                
            if random.randrange(1,500) == 1:
                madara_voice.play()
                madara = Golpetras()
                all_sprites.add(madara)
                monsters.add(madara)
                
        if score >= 1300:
            if random.randrange(1,400) == 1:
                sas = Sasori()
                all_sprites.add(sas)
                monsters.add(sas)
                
        if score >= 2000:   
            if random.randrange(1,500) == 1:
                ki = Kisame()
                all_sprites.add(ki)
                monsters.add(ki)
                wa = Water()
                all_sprites.add(wa)
                monsters.add(wa)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    player.speedx = -4
                    player.imgs = []
                    n=2
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Dash{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.step = 5
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    
                if event.key == pygame.K_RIGHT:
                    player.speedx = 4
                    player.imgs = []
                    n=2
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Dash{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.step = 3
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
                    
                if event.key == pygame.K_UP and player.rect.y == HEIGHT/2 - 45.5:#pulo
                    player.speedy = -20
                    g = 1
                    
                if event.key == pygame.K_SPACE and chakra>=20:
                    chakra-=20
                    bullet = Nrpower(player.rect.centerx, player.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    rasengan_sound.play()
                    
                if event.key == pygame.K_m and chakra >= 300:
                    chakra -= 300
                    powe = Nrm(player.rect.centerx, player.rect.top)
                    all_sprites.add(powe)
                    power.add(powe)
                    rasenshuriken_sound.play()
                
                if event.key == pygame.K_n and chakra >= 25:
                    chakra -= 25
                    clone = Clone(player.rect.centerx, player.rect.top)
                    all_sprites.add(clone)
                    bullets.add(clone)
                    kage_bushin.play()

                                
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
                    
                if event.key == pygame.K_SPACE:
                    player.imgs = []
                    chakra -= 25
                    n=8
                    for i in range(n):
                        player.imgs.append(pygame.image.load(path.join(img_dir, "Nr{0}.png".format(i+1))).convert())
                    player.frame = 0
                    player.image = player.imgs[player.frame]
                    player.image = pygame.transform.scale(player.image, (1,1))
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
                
                if event.key == pygame.K_n:
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
                    
        
                    
        if player.rect.y < HEIGHT/2 - 45.5:#gravidade
            player.speedy +=g 
                    
        # Verifica se houve colisão entre tiro e inimigo
        hits = pygame.sprite.groupcollide(monsters, bullets, True, True)
        for hit in hits: # Pode haver mais de um
            # O meteoro e destruido e precisa ser recriado
            destroy_sound.play()
            contador += 1
            score += 100
            
        hits = pygame.sprite.groupcollide(monsters, power, True, False)
        for hit in hits: # Pode haver mais de um
            # O meteoro e destruido e precisa ser recriado
            destroy_sound.play()
            contador += 1
            score += 100
            
        # Verifica se houve colisão entre personagem e inimigo
        hits = pygame.sprite.spritecollide(player, monsters, False, pygame.sprite.collide_circle)
        for hit in hits:
            # Toca o som da colisão
            boom_sound.play()
            hit.kill()
            player.morrer()
            
        running = player.vidas >= 0
        
        chakra += 1.5
        if chakra > 399.5:
            chakra =400
        elif chakra < 0.5:
            chakra = 0
        vx = -8 - (score/1000)
        x += vx
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
        
        screen.fill(BLACK)
        rel_x = x % background.get_rect().width
        screen.blit(background, (rel_x -background.get_rect().width , 0))
        
        if  rel_x  < WIDTH:
            screen.blit(background, (rel_x, 0))
        all_sprites.draw(screen)
        
        # Desenha o score
        vidas = player.vidas
        
        #pontuação
        draw_text(screen, str(score), 35, WIDTH/2, 0)
        draw_text(screen, "Score", 40, WIDTH/2-150, 0)
        #chakra
        draw_text(screen, str(chakra), 35, WIDTH/2+400, 0)
        draw_text(screen, "Chakra", 40, WIDTH/2+200, 0)
        #Vida
        draw_text(screen, str(vidas), 35, WIDTH/2-350, 0)
        draw_text(screen, "Vida", 40, WIDTH/2-450, 0)
                            
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    
    if score > highscore:
        highscore=score
    return (OVER, score, highscore)
