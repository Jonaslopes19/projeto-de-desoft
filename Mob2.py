import pygame
import random
from init import HEIGHT, WIDTH, BLACK, mobs
from os import path
from init import HEIGHT, WIDTH, BLACK, img_dir, snd_dir, fundos, FPS, INIT, GAME, QUIT 

# Classe Mob que representa o inimigo
class Mob2(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.           
        self.imgs = []
        n=6
        for i in range(n):
            self.imgs.append(pygame.image.load(path.join(img_dir, "Ns{0}.png".format(i+1))).convert())
        self.frame = 0
        self.image = self.imgs[self.frame]
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, (75, 100))
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.x = WIDTH + 50
        # Sorteia um lugar inicial em y
        self.rect.y = HEIGHT/2 - 45
        # Sorteia uma velocidade inicial
        self.speedx = random.randrange(-9, -3)
        self.speedy = 0
        self.step = 5
        self.ticks = 0
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
    # Metodo que atualiza a posição do personagem
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
            self.image = pygame.transform.scale(self.image, (75, 100))
    
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
      
            self.rect = self.image.get_rect()
            self.rect.x = center[0]
            self.rect.y = center[1]
            
        if self.rect.left < -25:
            self.rect.x = WIDTH + 50
            self.rect.y = HEIGHT/2 - 45
            self.speedx = random.randrange(-8, -2)
            self.speedy = 0
            