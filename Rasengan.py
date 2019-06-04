import pygame
from os import path
from init import HEIGHT, WIDTH, BLACK, img_dir, snd_dir, fundos, FPS

class Rasengan(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        kunai_img = pygame.image.load(path.join(img_dir, "Rasengan.png")).convert()
        self.image = kunai_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(kunai_img, (40, 40))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = y + 75
        self.rect.centerx = x + 40
        self.speedx = 15

    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()
        elif self.rect.x > WIDTH:
            self.kill()
            
class Power(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        kunai_img = pygame.image.load(path.join(img_dir, "Power.png")).convert()
        self.image = kunai_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(kunai_img, (250, 100))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = y + 100
        self.rect.centerx = x + 40
        self.speedx = 15

    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()
        elif self.rect.x > WIDTH:
            self.kill()
            
class Nrpower(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        

        self.imgs = []
        n=13
        for i in range(n):
            self.imgs.append(pygame.image.load(path.join(img_dir, "Nrpower{0}.png".format(i+1))).convert())
        self.frame = 0
        self.image = self.imgs[self.frame]
        self.step = 0.5
    
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(self.image, (250, 100))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = y + 100
        self.rect.centerx = x + 80
        self.speedx = 5
        self.step = 5
        self.ticks = 0
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        
          
        self.ticks +=1
        
        if self.ticks % self.step == 0:
            self.frame += 1
            
            if self.frame == len(self.imgs):
                self.frame = 0
                self.ticks = 0
            
            center = [self.rect.x, self.rect.y]
            self.image = self.imgs[self.frame]
            self.image = pygame.transform.scale(self.image, (75, 100))
    
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
      
            self.rect = self.image.get_rect()
            self.rect.x = center[0]
            self.rect.y = center[1]
        
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()
        elif self.rect.x > WIDTH:
            self.kill()
            
class Nrm(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        

        self.imgs = []
        n=5
        for i in range(n):
            self.imgs.append(pygame.image.load(path.join(img_dir, "Nrm{0}.png".format(i+1))).convert())
        self.frame = 0
        self.image = self.imgs[self.frame]
        self.step = 0.5
    
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(self.image, (250, 100))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = y + 100
        self.rect.centerx = x + 40
        self.speedx = 5
        self.step = 5
        self.ticks = 0
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        
          
        self.ticks +=1
        
        if self.ticks % self.step == 0:
            self.frame += 1
            
            if self.frame == len(self.imgs):
                self.frame = 0
                self.ticks = 0
            
            center = [self.rect.x, self.rect.y]
            self.image = self.imgs[self.frame]
            self.image = pygame.transform.scale(self.image, (75, 100))
    
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
      
            self.rect = self.image.get_rect()
            self.rect.x = center[0]
            self.rect.y = center[1]
        
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()
        elif self.rect.x > WIDTH:
            self.kill()

class Clone(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        

        self.imgs = []
        n=8
        for i in range(n):
            self.imgs.append(pygame.image.load(path.join(img_dir, "Nr{0}.png".format(i+1))).convert())
        self.frame = 0
        self.image = self.imgs[self.frame]
        self.step = 0.5
    
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(self.image, (75, 100))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = y + 100
        self.rect.centerx = x + 40
        self.speedx = 5
        self.step = 5
        self.ticks = 0
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        
          
        self.ticks +=1
        
        if self.ticks % self.step == 0:
            self.frame += 1
            
            if self.frame == len(self.imgs):
                self.frame = 0
                self.ticks = 0
            
            center = [self.rect.x, self.rect.y]
            self.image = self.imgs[self.frame]
            self.image = pygame.transform.scale(self.image, (75, 100))
    
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
      
            self.rect = self.image.get_rect()
            self.rect.x = center[0]
            self.rect.y = center[1]
        
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()
        elif self.rect.x > WIDTH:
            self.kill()
            
class PowerMob(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        kunai_img = pygame.image.load(path.join(img_dir, "Power.png")).convert()
        self.image = kunai_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(kunai_img, (250, 100))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = y + 100
        self.rect.centerx = x + 40
        self.speedx = -5

    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()
        elif self.rect.x > WIDTH:
            self.kill()