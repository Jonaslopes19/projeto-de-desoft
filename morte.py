import pygame
from init import BLACK, img_dir
from os import path


class Morte(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, center):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Carrega a animação de explosão
        morte_anim = []
        for i in range(7):
            img = (pygame.image.load(path.join(img_dir, "MorteNr{0}.png".format(i+1))).convert())
            #img = pygame.image.load(path.join(img_dir, filename)).convert()
            img = pygame.transform.scale(img, (32, 32))        
            img.set_colorkey(BLACK)
            morte_anim.append(img)
        self.morte_anim = morte_anim

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0
        self.image = self.morte_anim[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center

        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.morte_anim):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.morte_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center