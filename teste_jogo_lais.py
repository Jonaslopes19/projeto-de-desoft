import time
import random
import pygame
from os import path
from init import HEIGHT, WIDTH, BLACK, img_dir, snd_dir, fundos, FPS, INIT, GAME, OVER, QUIT,  HS_FILE 
from teste_player_lais import Player
from Bullet import Bullet
from mob import Mob
from Mob2 import Mob2
from Mob3 import Mob3
from Rasengan import Rasengan, Power 
from teste_screen_lais import init_screen
from lais_game import game_screen
from gameover import over_screen

# Inicialização do Pygame.
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
