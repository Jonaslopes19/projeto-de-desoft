# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from init import HEIGHT, WIDTH, INIT, GAME, QUIT
from screen import init_screen
from game import game_screen

# Inicialização do Pygame.
pygame.init() 
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Naruto Run")

# Comando para evitar travamentos.
try:
    state = INIT 
    while state != QUIT:
        if state == INIT:
            state = init_screen(screen)
        elif state == GAME:
            state = game_screen(screen)
        else:
            state = QUIT
finally:
    pygame.quit()
