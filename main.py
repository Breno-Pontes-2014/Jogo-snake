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
    comida_x = round(random.randrange(0, largura - tamanho_do_quadrado) / float(tamanho_do_quadrado))  * float(tamanho_do_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_do_quadrado) / float(tamanho_do_quadrado)) * float(tamanho_do_quadrado)
    return comida_x, comida_y

def desenhar_comidas(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde [comida_x , comida_y , tamanho, tamanho])

def desenhar_cobra(tamanho,pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuação(pontuação):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos; {pontuação, True, vermelha}")
    tela.blit(texto, [1, 1])
def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_do_quadrado 
    if tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_do_quadrado 
    if tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_do_quadrado 
        velocidade_y = 0
    if tecla == pygame.K_RIGHT:
        velocidade_x = -tamanho_do_quadrado 
        velocidade_y = 0
    return velocidade_x, velocidade_y
def rodar_o_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1

    pixels = []

    comida_x = gerar_comidas()
    comida_y = gerar_comidas()

    while not fim_jogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x = selecionar_velocidade(evento.key)
                velocidade_y = selecionar_velocidade(evento.key)

        desenhar_comidas(tamanho_do_quadrado, comida_x, comida_y)

        if x < 0 or x >= largura or  y < 0 or y >= altura:
            fim_jogo = True
        x += velocidade_x
        x += velocidade_y

        pixels.append(x, y)
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        desenhar_cobra(tamanho_do_quadrado, pixels)

        desenhar_pontuação(tamanho_cobra - 1)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x = gerar_comidas()
            comida_y = gerar_comidas()

        relógio.tick(velocidade_da_cobrinha)


rodar_o_jogo()