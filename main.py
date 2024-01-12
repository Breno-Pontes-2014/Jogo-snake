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

def gerar_comidas():
    comida_x = round(random.randrange(0, largura - tamanho_do_quadrado) / 20.0) * 20.0
    comida_y - round(random.randrange(0, altura - tamanho_do_quadrado / 20.0) * 20.0)
    return comida_x, comida_y

def desenhar_comidas(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde [comida_x , comida_y , tamanho, tamanho])

def rodar_o_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    pixels = []

    comida_x = gerar_comidas()
    comida_y = gerar_comidas()

    while not fim_jogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True

        desenhar_comidas(tamanho_do_quadrado, comida_x, comida_y)

        pixels.append(x, y)
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        for pixel in pixels():
            if pixel == [x, y]:
                fim_jogo = True

        pygame.display.update()

        relógio.tick(velocidade_da_cobrinha)


rodar_o_jogo()