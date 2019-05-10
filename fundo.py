# -*- coding: utf-8 -*-
"""
Created on Fri May 10 14:21:40 2019

@author: User
"""
import pygame

class fundo(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        
         # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        