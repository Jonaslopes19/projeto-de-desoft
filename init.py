# -*- coding: utf-8 -*-
"""
Created on Fri May 10 14:19:33 2019

@author: User
"""
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
fundos = path.join(path.dirname(__file__), 'Fundos')
personagem = path.join(path.dirname(__file__), 'Personagem1')
mobs =  path.join(path.dirname(__file__), 'Mob1')


# Dados gerais do jogo.
WIDTH = 1000 # Largura da tela
HEIGHT = 445 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
