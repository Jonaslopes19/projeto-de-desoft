import time
import random
import pygame
from os import path
from init import HEIGHT, WIDTH, BLACK, img_dir, snd_dir, fundos, FPS, INIT, GAME, QUIT, fnt_dir
from player import Player
from Bullet import Bullet
from mob import Mob
from Mob2 import Mob2
from Mob3 import Mob3
from Rasengan import Rasengan

def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join('Inicio1.png')).convert()
    background_rect = background.get_rect()
    
    naruto_is_showed = 60
    logo_is_showed = 120
    press_key = 180
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        naruto_is_showed -= 1
        logo_is_showed -= 1
        press_key -= 1
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False
                    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK);
        screen.blit(background, background_rect)
        if naruto_is_showed == 0:
            background = pygame.image.load(path.join('Inicio2.png')).convert()
            background_rect = background.get_rect()
        elif logo_is_showed == 0:
            background = pygame.image.load(path.join('Inicio3.png')).convert()
            background_rect = background.get_rect()
        elif press_key == 0:
            background = pygame.image.load(path.join('Inicio4.png')).convert()
            background_rect = background.get_rect()
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state