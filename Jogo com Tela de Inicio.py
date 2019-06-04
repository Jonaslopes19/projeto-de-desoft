        # -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from init import HEIGHT, WIDTH, INIT, GAME, OVER, QUIT
from screen import init_screen
from game1 import game_screen
from gameover import over_screen


# Inicializaçãqo do Pygame.
pygame.init() 
pygame.mixer.init()
# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Naruto Run")
score = 0
highscore = 0

# Comando para evitar travamentos.
try:
    state = INIT 
    while state != QUIT:
        if state == INIT:
            state = init_screen(screen)
        elif state == GAME:
            state, score, highscore = game_screen(screen) 
        elif state == OVER:
            state = over_screen(screen, score, highscore)
        else:
            state = QUIT
finally:
    pygame.quit()
 