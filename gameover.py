import pygame
from os import path
from init import HEIGHT, WIDTH, BLACK, WHITE, img_dir, snd_dir, fundos, FPS, INIT, GAME, QUIT, fnt_dir, HS_FILE



font_name = pygame.font.match_font('times new roman')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def over_screen(screen, score, highscore):
    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join('gameover.png')).convert()
    background_rect = background.get_rect()
    
    pygame.mixer.music.load(path.join(snd_dir, 'sadness.mp3'))
    pygame.mixer.music.set_volume(0.4)
    
    pygame.mixer.music.play(loops=-1)
    
    
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
                    
        if score > highscore:
            highscore = score
            draw_text(background, " NEW HIGH SCORE!", 60, WIDTH/2, 100)
            dir = path.dirname(__file__)
            with open(path.join(dir, HS_FILE), 'w') as f:
                f.write(str(score))
        else: 
            draw_text(background, str(score), 60, WIDTH/2+150, 150)
            draw_text(background, "Score", 60, WIDTH/2, 150)
            
            draw_text(background, str(highscore), 60, WIDTH/2+180, 200)
            draw_text(background, "High Score", 60, WIDTH/2, 200)
    
    
        
         
        screen.fill(BLACK);
        screen.blit(background, background_rect)
    
        pygame.display.flip()

    return state

    