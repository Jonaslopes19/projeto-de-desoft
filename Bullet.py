import pygame
from os import path
from init import HEIGHT, WIDTH, BLACK, img_dir, snd_dir, fundos, FPS

class Bullet(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        kunai_img = pygame.image.load(path.join(img_dir, "kunai1.png")).convert()
        self.image = kunai_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(kunai_img, (39, 52))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = y + 100
        self.rect.centerx = x + 40
        self.speedx = 150

    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()
        elif self.rect.x > WIDTH:
            self.kill()