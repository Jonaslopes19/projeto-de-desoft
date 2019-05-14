import pygame
from os import path
from init import HEIGHT, WIDTH, BLACK, img_dir, snd_dir, fundos, FPS
from player import Player


def Pulo(player):
    player.speedy = -15
    g = 5
    while player.rect.y < HEIGHT/2 + 40:
        player.speedy += g        
    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        x+= vx
        screen.blit(background, (x, 0))
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
