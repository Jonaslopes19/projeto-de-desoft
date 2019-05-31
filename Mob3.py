import pygame
import random
from init import HEIGHT, WIDTH, BLACK, mobs
from os import path
from init import HEIGHT, WIDTH, BLACK, img_dir, snd_dir, fundos, FPS, INIT, GAME, QUIT 
from Bullet import Bullet
# Classe Mob que representa o inimigo
class Mob3(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.           
        self.imgs = []
        n=10
        for i in range(n):
            
            self.imgs.append(pygame.image.load(path.join(img_dir, "Tobi_walk{0}.png".format(i+1))).convert())
        self.frame = 0
        self.image = self.imgs[self.frame]
        self.image = pygame.transform.scale(self.image, (100, 100))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)

        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.x = 700
        # Sorteia um lugar inicial em y
        self.rect.y = HEIGHT/2 -45
        # Sorteia uma velocidade inicial
        self.speedx = -1
        self.speedy = 0
        self.step = 10
        self.ticks = 0
            
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
    # Metodo que atualiza a posição do personagem
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.ticks +=1
        
        if self.ticks % self.step == 0:
            self.frame += 1
            
            if self.frame == len(self.imgs):
                self.frame = 0
                self.ticks = 0
            
            center = [self.rect.x, self.rect.y]
            self.image = self.imgs[self.frame]
            self.image = pygame.transform.scale(self.image, (75, 100))
    
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
      
            self.rect = self.image.get_rect()
            self.rect.x = center[0]
            self.rect.y = center[1]
            
        # Se o meteoro passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = 700
            self.rect.y = HEIGHT/2 -20
            self.speedx = random.randrange(-2, -1)
            self.speedy = 0
            
class Mob4(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.           
        self.imgs = []
        n=9
        for i in range(n):
            
            self.imgs.append(pygame.image.load(path.join(img_dir, "Itachi_walk{0}.png".format(i+1))).convert())
        self.frame = 0
        self.image = self.imgs[self.frame]
        self.image = pygame.transform.scale(self.image, (100, 100))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)

        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.x = 700
        # Sorteia um lugar inicial em y
        self.rect.y = HEIGHT/2 -45
        # Sorteia uma velocidade inicial
        self.speedx = -1
        self.speedy = 0
        self.step = 10
        self.ticks = 0
            
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
        # Metodo que atualiza a posição do personagem
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.ticks +=1
        
        if self.ticks % self.step == 0:
            self.frame += 1
            
            if self.frame == len(self.imgs):
                self.frame = 0
                self.ticks = 0
            
            center = [self.rect.x, self.rect.y]
            self.image = self.imgs[self.frame]
            self.image = pygame.transform.scale(self.image, (75, 100))
    
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
      
            self.rect = self.image.get_rect()
            self.rect.x = center[0]
            self.rect.y = center[1]
            
        # Se o meteoro passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = 700
            self.rect.y = HEIGHT/2 -20
            self.speedx = random.randrange(-2, -1)
            self.speedy = 0

class Sasori(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.           
        self.imgs = []
        n=18
        for i in range(n):
            img = pygame.image.load(path.join(img_dir, "Sasori_walk{0}.png".format(i+1))).convert()
            img = pygame.transform.scale(img, (150, 140))
            self.imgs.append(img)
        self.frame = 0
        self.image = self.imgs[self.frame]
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)

        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.x = 700
        # Sorteia um lugar inicial em y
        self.rect.y = HEIGHT/2 -60
        # Sorteia uma velocidade inicial
        self.speedx = -0.5
        self.speedy = 0
        self.step = 5
        self.ticks = 0
            
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
        # Metodo que atualiza a posição do personagem
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.ticks +=1
        
        if self.ticks % self.step == 0:
            self.frame += 1
            
            if self.frame == len(self.imgs):
                self.frame = 0
                self.ticks = 0
            
            center = [self.rect.x, self.rect.y]
            self.image = self.imgs[self.frame]
            self.image = pygame.transform.scale(self.image, (150, 140))
    
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
      
            self.rect = self.image.get_rect()
            self.rect.x = center[0]
            self.rect.y = center[1]
            
        # Se o meteoro passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = 700
            self.rect.y = HEIGHT/2 -20
            self.speedx = random.randrange(-2, -1)
            self.speedy = 0


class Amaterasu(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.           
        self.imgs = []
        n=7
        for i in range(n):
            img = pygame.image.load(path.join(img_dir, "Am{0}.png".format(i+1))).convert()
            img = pygame.transform.scale(img, (100, 100))
            self.imgs.append(img)
        self.frame = 0
        self.image = self.imgs[self.frame]
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)

        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.x = 700
        # Sorteia um lugar inicial em y
        self.rect.y = HEIGHT/2 -45
        # Sorteia uma velocidade inicial
        self.speedx = -10
        self.speedy = 0
        self.step = 5
        self.ticks = 0
            
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
        # Metodo que atualiza a posição do personagem
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.ticks +=1
        
        if self.ticks % self.step == 0:
            self.frame += 1
            
            if self.frame == len(self.imgs):
                self.frame = 0
                self.ticks = 0
            
            center = [self.rect.x, self.rect.y]
            self.image = self.imgs[self.frame]
            self.image = pygame.transform.scale(self.image, (75, 100))
    
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
      
            self.rect = self.image.get_rect()
            self.rect.x = center[0]
            self.rect.y = center[1]
            
        # Se o meteoro passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = 700
            self.rect.y = HEIGHT/2 -20
            self.speedx = random.randrange(-2, -1)
            self.speedy = 0
   
class Golpetras(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.           
        self.imgs = []
        n=6
        for i in range(n):
            
            self.imgs.append(pygame.image.load(path.join(img_dir, "M{0}.png".format(i+1))).convert())
        self.frame = 0
        self.image = self.imgs[self.frame]
        self.image = pygame.transform.scale(self.image, (100, 100))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)

        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.x = WIDTH / 2 -400
        # Sorteia um lugar inicial em y
        self.rect.y = HEIGHT/2 -45
        # Sorteia uma velocidade inicial
        self.speedx = 7
        self.speedy = 0
        self.step = 10
        self.ticks = 0
            
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
        # Metodo que atualiza a posição do personagem
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.ticks +=1
        
        if self.ticks % self.step == 0:
            self.frame += 1
            
            if self.frame == len(self.imgs):
                self.frame = 0
                self.ticks = 0
            
            center = [self.rect.x, self.rect.y]
            self.image = self.imgs[self.frame]
            self.image = pygame.transform.scale(self.image, (100, 100))
    
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
      
            self.rect = self.image.get_rect()
            self.rect.x = center[0]
            self.rect.y = center[1]
            
        # Se o meteoro passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = 700
            self.rect.y = HEIGHT/2 -20
            self.speedx = random.randrange(-2, -1)
            self.speedy = 0
             
class Kisame(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.           
        self.imgs = []
        n=7
        for i in range(n):
            img = pygame.image.load(path.join(img_dir, "Ki{0}.png".format(i+1))).convert()
            img = pygame.transform.scale(img, (150, 140))
            self.imgs.append(img)
        self.frame = 0
        self.image = self.imgs[self.frame]
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)

        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.x = 700
        # Sorteia um lugar inicial em y
        self.rect.y = HEIGHT/2 -60
        # Sorteia uma velocidade inicial
        self.speedx = 0
        self.speedy = 0
        self.step = 5
        self.ticks = 0
            
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
        # Metodo que atualiza a posição do personagem
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.ticks +=1
        
        if self.ticks % self.step == 0:
            self.frame += 1
            
            if self.frame == len(self.imgs):
                self.frame = 0
                self.ticks = 0
            
            center = [self.rect.x, self.rect.y]
            self.image = self.imgs[self.frame]
            self.image = pygame.transform.scale(self.image, (150, 140))
    
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
      
            self.rect = self.image.get_rect()
            self.rect.x = center[0]
            self.rect.y = center[1]
            
        # Se o meteoro passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = 700
            self.rect.y = HEIGHT/2 -20
            self.speedx = random.randrange(-2, -1)
            self.speedy = 0
     
class Water(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.           
        self.imgs = []
        n=2
        for i in range(n):
            img = pygame.image.load(path.join(img_dir, "Kipower{0}.png".format(i+1))).convert()
            img = pygame.transform.scale(img, (235, 60))
            self.imgs.append(img)
        self.frame = 0
        self.image = self.imgs[self.frame]
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)

        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.x = 700
        # Sorteia um lugar inicial em y
        self.rect.y = HEIGHT/2 -20
        # Sorteia uma velocidade inicial
        self.speedx = -10
        self.speedy = 0
        self.step = 5
        self.ticks = 0
            
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
        # Metodo que atualiza a posição do personagem
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.ticks +=1
        
        if self.ticks % self.step == 0:
            self.frame += 1
            
            if self.frame == len(self.imgs):
                self.frame = 0
                self.ticks = 0
            
            center = [self.rect.x, self.rect.y]
            self.image = self.imgs[self.frame]
            self.image = pygame.transform.scale(self.image, (235, 60))
    
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
      
            self.rect = self.image.get_rect()
            self.rect.x = center[0]
            self.rect.y = center[1]
            
        # Se o meteoro passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = 700
            self.rect.y = HEIGHT/2 -20
            self.speedx = random.randrange(-2, -1)
            self.speedy = 0

class Deidara(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.           
        self.imgs = []
        n=8
        for i in range(n):
            img = pygame.image.load(path.join(img_dir, "Deidara{0}.png".format(i+1))).convert()
            img = pygame.transform.scale(img, (110, 110))
            self.imgs.append(img)
        self.frame = 0
        self.image = self.imgs[self.frame]
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)

        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.x = 700
        # Sorteia um lugar inicial em y
        self.rect.y = HEIGHT/2 -60
        # Sorteia uma velocidade inicial
        self.speedx = 0
        self.speedy = 0
        self.step = 5
        self.ticks = 0
            
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
        # Metodo que atualiza a posição do personagem
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.ticks +=1
        
        if self.ticks % self.step == 0:
            self.frame += 1
            
            if self.frame == len(self.imgs):
                self.frame = 0
                self.ticks = 0
            
            center = [self.rect.x, self.rect.y]
            self.image = self.imgs[self.frame]
            self.image = pygame.transform.scale(self.image, (110, 110))
    
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
      
            self.rect = self.image.get_rect()
            self.rect.x = center[0]
            self.rect.y = center[1]
            
        # Se o meteoro passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = 700
            self.rect.y = HEIGHT/2 -20
            self.speedx = random.randrange(-2, -1)
            self.speedy = 0
    
class Bird(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.           
        self.imgs = []
        n=9
        for i in range(n):
            img = pygame.image.load(path.join(img_dir, "Bird{0}.png".format(i+1))).convert()
            img = pygame.transform.scale(img, (150, 140))
            self.imgs.append(img)
        self.frame = 0
        self.image = self.imgs[self.frame]
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)

        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.x = 700
        # Sorteia um lugar inicial em y
        self.rect.y = HEIGHT/2 -60
        # Sorteia uma velocidade inicial
        self.speedx = -1
        self.speedy = 0
        self.step = 5
        self.ticks = 0
            
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
        # Metodo que atualiza a posição do personagem
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.ticks +=1
        
        if self.ticks % self.step == 0:
            self.frame += 1
            
            if self.frame == len(self.imgs):
                self.frame = 0
                self.ticks = 0
            
            center = [self.rect.x, self.rect.y]
            self.image = self.imgs[self.frame]
            self.image = pygame.transform.scale(self.image, (150, 140))
    
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
      
            self.rect = self.image.get_rect()
            self.rect.x = center[0]
            self.rect.y = center[1]
            
        # Se o meteoro passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = 700
            

            self.rect.y = HEIGHT/2 -20
            self.speedx = random.randrange(-2, -1)
            self.speedy = 0

class CloneNr(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.           
        self.imgs = []
        n=1
        for i in range(n):
            img = pygame.image.load(path.join(img_dir, "Nr{0}.png".format(i+1))).convert()
            img = pygame.transform.scale(img, (110, 110))
            self.imgs.append(img)
        self.frame = 0
        self.image = self.imgs[self.frame]
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)

        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.x = 100
        # Sorteia um lugar inicial em y
        self.rect.y = HEIGHT/2 -60
        # Sorteia uma velocidade inicial
        self.speedx = 10
        self.speedy = 0
        self.step = 5
        self.ticks = 0
            
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
        # Metodo que atualiza a posição do personagem
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.ticks +=1
        
        if self.ticks % self.step == 0:
            self.frame += 1
            
            if self.frame == len(self.imgs):
                self.frame = 0
                self.ticks = 0
            
            center = [self.rect.x, self.rect.y]
            self.image = self.imgs[self.frame]
            self.image = pygame.transform.scale(self.image, (110, 110))
    
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
      
            self.rect = self.image.get_rect()
            self.rect.x = center[0]
            self.rect.y = center[1]
            
        # Se o meteoro passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = 700
            self.rect.y = HEIGHT/2 -20
            self.speedx = random.randrange(-2, -1)
            self.speedy = 0
            
class CloneN(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.           
        self.imgs = []
        n=6
        for i in range(n):
            img = pygame.image.load(path.join(img_dir, "Run{0}.png".format(i+1))).convert()
            img = pygame.transform.scale(img, (110, 110))
            self.imgs.append(img)
        self.frame = 0
        self.image = self.imgs[self.frame]
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)

        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.x = 700
        # Sorteia um lugar inicial em y
        self.rect.y = HEIGHT/2 -60
        # Sorteia uma velocidade inicial
        self.speedx = 10
        self.speedy = 0
        self.step = 5
        self.ticks = 0
            
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
        # Metodo que atualiza a posição do personagem
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.ticks +=1
        
        if self.ticks % self.step == 0:
            self.frame += 1
            
            if self.frame == len(self.imgs):
                self.frame = 0
                self.ticks = 0
            
            center = [self.rect.x, self.rect.y]
            self.image = self.imgs[self.frame]
            self.image = pygame.transform.scale(self.image, (110, 110))
    
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
      
            self.rect = self.image.get_rect()
            self.rect.x = center[0]
            self.rect.y = center[1]
            
        # Se o meteoro passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = 700
            self.rect.y = HEIGHT/2 -20
            self.speedx = random.randrange(-2, -1)
            self.speedy = 0
    