import pygame
from init import HEIGHT, WIDTH, BLACK, plataforma
from os import path

class Plataforma(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y, w, h):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        plataforma_img = pygame.image.load(path.join(plataforma, "blocos4.png")).convert()
        self.image = plataforma_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(plataforma_img, (50, 38))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza na tela.
        self.rect.x = x
        self.rect.y = y
        
        