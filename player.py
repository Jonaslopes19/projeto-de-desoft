#player
import pygame
from init import HEIGHT, WIDTH, BLACK, personagem
from os import path
<<<<<<< HEAD



=======
import time
>>>>>>> 96169862add96bc727341e32da835597e721ca09
# Classe Jogador que representa a nave
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        self.imgs = []
        n=6
        for i in range(n):
            self.imgs.append(pygame.image.load(path.join(personagem, "Naruto{0}.png".format(i+1))).convert())
        self.frame = 0
        self.image = self.imgs[self.frame]
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(self.image, (75, 100))
    
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
    
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
    
        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT/2 + 40
        
        # Velocidade da nave
        self.speedx = 0
        self.speedy = 0
        
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 25
        
        self.step = 10
        self.ticks = 0
    
    # Metodo que atualiza a posição da navinha
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
        
        
        
        
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
