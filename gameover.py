import pygame
from os import path
from init import HEIGHT, WIDTH, BLACK, WHITE, img_dir, snd_dir, fundos, FPS, INIT, GAME, QUIT, fnt_dir



font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, 40)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def over_screen(screen):
    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join('gameover0.png')).convert()
    background_rect = background.get_rect()
    
    draw_text(screen, "GAME OVER", 50, WIDTH/2, 0)
    draw_text(screen, "Press C to continue", 40, WIDTH/2-150, 100)
    draw_text(screen, "Press Q to quit", 40, WIDTH/2-150, 200)
    
    running = True
    while running:
        
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
        
            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_C:
                    state = GAME
                    running = False
            
                if event.key == pygame.K_Q:
                    state = QUIT
                    running = False
    
    
        screen.fill(BLACK);
        screen.blit(background, background_rect)
    
        pygame.display.flip()

    return state

    