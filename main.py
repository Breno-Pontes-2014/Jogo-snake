import pygame
import random

pygame.init()
pygame.display.set_caption('Jogo Snake Python')
largura = 1200
altura = 400
tela = pygame.display.set_mode((largura, altura))
relógio = pygame.time.Clock()

preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0,)

tamanho_do_quadrado = 20
velocidade_da_cobrinha = 15

def rodar_o_jogo():
    fim_jogo = False

    x = largura / 2
    


    while not fim_jogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
        
        pass
rodar_o_jogo()