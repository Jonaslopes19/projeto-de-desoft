#player
import pygame
from init import HEIGHT, WIDTH, BLACK, personagem, PLAYER_STATE_MORRENDO, PLAYER_STATE_MORTO, PLAYER_STATE_VIVO
from os import path
from init import img_dir, snd_dir, fundos, FPS, INIT, GAME, QUIT


#vidas

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.speedx = 0
        self.speedy = 0
        
        if self.speedx == 0:
            self.imgs = []
            n=6
            for i in range(n):
                self.imgs.append(pygame.image.load(path.join(img_dir, "Naruto{0}.png".format(i+1))).convert())
            self.frame = 0
            self.image = self.imgs[self.frame]
            self.step = 5
        else:
            self.imgs = []
            n=6
            for i in range(n):
                self.imgs.append(pygame.image.load(path.join(img_dir, "Run{0}.png".format(i+1))).convert())
            self.frame = 0
            self.image = self.imgs[self.frame]
            self.step = 5
        
        self.image = pygame.transform.scale(self.image, (75, 100))
    
        self.image.set_colorkey(BLACK)
    
        morte_anim = []
        for i in range(7):
            
            img = (pygame.image.load(path.join(img_dir, "MorteNr{0}.png".format(i+1))).convert())
            img = pygame.transform.scale(img, (100, 100))        
            img.set_colorkey(BLACK)
            morte_anim.append(img)
        self.morte_anim = morte_anim
        self.morte_frame = 0

    
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
    
        # Centraliza embaixo da tela.
        self.rect.x = WIDTH / 2 -150
        self.rect.y= HEIGHT/2 - 45.5
        
        self.radius = 25
        
        self.step = 5
        self.ticks = 0
        
        self.state = PLAYER_STATE_VIVO
        self.vidas = 3
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        
        
        self.ticks +=1
        
        if self.ticks % self.step == 0:
            self.frame += 1
            
            if self.frame == len(self.imgs):
                self.frame = 0
                self.ticks = 0
            
            center = [self.rect.x, self.rect.y]
            self.image = self.imgs[self.frame]
            self.image = pygame.transform.scale(self.image, (100, 100))
    
            self.image.set_colorkey(BLACK)
      
            self.rect = self.image.get_rect()
            self.rect.x = center[0]
            self.rect.y = center[1]
        
        if self.state == PLAYER_STATE_MORRENDO:
            if self.ticks % self.step == 0:
                self.morte_frame += 1
            self.image = self.morte_anim[self.morte_frame]
            if self.morte_frame == 6:
                if self.vidas <= 0:
                    self.state = PLAYER_STATE_MORTO
                else:
                    self.state = PLAYER_STATE_VIVO
                self.morte_frame = 0
                
        if self.vidas == 2:
            self.state = PLAYER_STATE_MORTO
            
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.y < -30:
            self.rect.y = -30
        if self.rect.y > HEIGHT/2 - 45.5:
            self.rect.y = HEIGHT/2 - 45.5  
            
    def morrer(self):
        self.state = PLAYER_STATE_MORRENDO
        self.vidas -= 1
