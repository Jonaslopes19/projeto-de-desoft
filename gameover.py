import pygame
from os import path
from init import HEIGHT, WIDTH, BLACK, WHITE, img_dir, snd_dir, fundos, FPS, INIT, GAME, QUIT, fnt_dir


def over_screen(screen):
    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join('gameover.png')).convert()
    background_rect = background.get_rect()
    
    
    running = True
    while running:
        
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
        
            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_p:
                    state = GAME
                    running = False
            
                if event.key == pygame.K_q:
                    state = QUIT
                    running = False
    
    
        screen.fill(BLACK);
        screen.blit(background, background_rect)
    
        pygame.display.flip()

    return state

    