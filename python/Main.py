import os
import sys
import pygame
import Audios
import Imagens
from random import randint

pygame.init()

# cores
branco = (255,255,255)
preto = (0,0,0)
rosa = (235,52,222)
amarelo = (237,213,0)
vermelho = (255,0,0)
azul = (100,0,255)
cinza = (60,60,60)
azul_2 = (175,225,250)
vermelho_2 = (230,24,89)
cor_fundo_janela3 = (239,228,176)


# configuracoes da janela
largura, altura = 1366, 768
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Mario Diet")

# fontes

caminho_fonte_pixel_art = "midia/fontes/pixel_art.ttf"

fonte_base = pygame.font.Font(caminho_fonte_pixel_art, 60)
fonte_n = pygame.font.Font(caminho_fonte_pixel_art, 130)
fonte_temporzidor = pygame.font.Font(caminho_fonte_pixel_art, 50)
fonte_dica = pygame.font.Font(caminho_fonte_pixel_art, 33)
fonte_legenda = pygame.font.Font(caminho_fonte_pixel_art, 25)
fonte_reforço = pygame.font.Font(caminho_fonte_pixel_art, 26)
fonte_creditos = pygame.font.Font(caminho_fonte_pixel_art, 40)
fonte_pontuacao = pygame.font.Font(caminho_fonte_pixel_art, 45)
fonte_agradecimento = pygame.font.Font(caminho_fonte_pixel_art, 70)
fonte_perguntas = pygame.font.Font(caminho_fonte_pixel_art, 26)
fonte_tutorial = pygame.font.Font(caminho_fonte_pixel_art, 18)
fonte_reforço_relembrando = pygame.font.Font(caminho_fonte_pixel_art, 35)
fonte_baseado = pygame.font.Font(caminho_fonte_pixel_art, 18)
fonte_fases_corretas = pygame.font.Font(caminho_fonte_pixel_art, 26)
fonte_qr_code = pygame.font.Font(caminho_fonte_pixel_art, 23)



# pontuacao
pontuacao = [0]
pontuacao_inicial = pontuacao[0]


# audios globais
som_comeco_jogo = pygame.mixer.Sound(Audios.EFEITO_COMECO_JOGO) # cliques para começar
som_acerto = pygame.mixer.Sound(Audios.EFEITO_ACERTO) # item correto
som_erro = pygame.mixer.Sound(Audios.EFEITO_ERRO) # item incorreto e pygame.QUIT


# temporizador
def contador_de_tempo(tempoinicial):

    tempo_inicial = tempoinicial
    tempo_total = 60
    tempo_atual = pygame.time.get_ticks()
    tempo_decorrido = tempo_total - (tempo_atual - tempo_inicial) // 800 # transforma em segundos

    if tempo_decorrido < 0:
        tempo_decorrido = 0

    texto = fonte_temporzidor.render(f"{tempo_decorrido} segundos", True, branco) 
    janela.blit(texto, conteudo_interface_tempo) # coloca na tela o tempo decorrido

    return tempo_decorrido


# processamento do jogo com 4 itens
def andamento_jogo_4(item1, item2, item3, item4, fase, fase_ant, aparece_1, aparece_2, aparece_3, aparece_4):

    largura_item = 175
    altura_item = 175

    posicoes = [[100,200],[250,400],[575,400],[725,200]]

    # posicao aleatoria item 1
    if not posicoes_definidas[0]:
        num_rand = randint(0,3)
        posicao_item_1 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[0] = posicao_item_1
    else:
        posicao_item_1 = posicoes_definidas[0]

    # posicao aleatoria item 2
    if not posicoes_definidas[1]:
        num_rand = randint(0,2)
        posicao_item_2 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[1] = posicao_item_2
    else:
        posicao_item_2 = posicoes_definidas[1]

    # posicao aleatoria item 3
    if not posicoes_definidas[2]:
        num_rand = randint(0,1)
        posicao_item_3 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[2] = posicao_item_3
    else:
        posicao_item_3 = posicoes_definidas[2]

    # posicao aleatoria item 4
    if not posicoes_definidas[3]:
        num_rand = randint(0,0)
        posicao_item_4 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[3] = posicao_item_4
    else:
        posicao_item_4 = posicoes_definidas[3]


    if fase_10:

        if aparece_1:
            item_1 = item1
            tamanho_item_1 = (largura_item, altura_item)
            item_1 = pygame.transform.scale(item_1, tamanho_item_1)
            item_1_tela = pygame.Rect(posicao_item_1[0],posicao_item_1[1],tamanho_item_1[0],tamanho_item_1[1])
            janela.blit(item_1, (posicao_item_1))
            pes_sensiveis = fonte_legenda.render("São sensíveis", True, branco)
            janela.blit(pes_sensiveis,[posicao_item_1[0]+10,posicao_item_1[1]+165])

        if aparece_2:
            item_2 = item2
            tamanho_item_2 = (largura_item, altura_item)
            item_2 = pygame.transform.scale(item_2, tamanho_item_2)
            item_2_tela = pygame.Rect(posicao_item_2[0],posicao_item_2[1],tamanho_item_2[0],tamanho_item_2[1])
            janela.blit(item_2, (posicao_item_2))
            pes_ulceras = fonte_legenda.render("São mais ulceráveis", True, branco)
            janela.blit(pes_ulceras,[posicao_item_2[0]-28,posicao_item_2[1]+165])

        if aparece_3:
            item_3 = item3
            tamanho_item_3 = (largura_item, altura_item)
            item_3 = pygame.transform.scale(item_3, tamanho_item_3)
            item_3_tela = pygame.Rect(posicao_item_3[0],posicao_item_3[1],tamanho_item_3[0],tamanho_item_3[1])
            janela.blit(item_3, (posicao_item_3))
            pes_pele_fina = fonte_legenda.render("Têm a pele fina", True, branco)
            janela.blit(pes_pele_fina,[posicao_item_3[0]-10,posicao_item_3[1]+165])

        if aparece_4:
            item_4 = item4
            tamanho_item_4 = (largura_item, altura_item)
            item_4 = pygame.transform.scale(item_4, tamanho_item_4)
            item_4_tela = pygame.Rect(posicao_item_4[0],posicao_item_4[1],tamanho_item_4[0],tamanho_item_4[1])
            janela.blit(item_4, (posicao_item_4))
            pes_pouca_sensibilidade = fonte_legenda.render("Têm pouca sensibilidade", True, branco)
            janela.blit(pes_pouca_sensibilidade,[posicao_item_4[0]-45,posicao_item_4[1]+165])


    janela.blit(proxima_fase, (posicao_proxima_fase))
    janela.blit(fase_anterior, (posicao_fase_anterior))
    

    if event.type == pygame.MOUSEBUTTONDOWN:

        if aparece_1:
            if item_1_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]+150
                som_acerto.play()
                aparece_1 = False

        if aparece_2:
            if item_2_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]+150
                som_acerto.play()
                aparece_2 = False

        if aparece_3:
            if item_3_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]+150
                som_acerto.play()
                aparece_3 = False

        if aparece_4:
            if item_4_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]+150
                som_acerto.play()
                aparece_4 = False

    return aparece_1, aparece_2, aparece_3, aparece_4


# processamento do jogo com 5 itens
def andamento_jogo_5(item1, item2, item3, item4, item5, fase, fase_ant, aparece_1, aparece_2, aparece_3, aparece_4, aparece_5):
    
    largura_item = 175
    altura_item = 175

    posicoes = [[50,500],[275,200],[450,400],[600,200],[800,500]]

    # posicao aleatoria item 1
    if not posicoes_definidas[0]:
        num_rand = randint(0,4)
        posicao_item_1 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[0] = posicao_item_1
    else:
        posicao_item_1 = posicoes_definidas[0]

    # posicao aleatoria item 2
    if not posicoes_definidas[1]:
        num_rand = randint(0,3)
        posicao_item_2 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[1] = posicao_item_2
    else:
        posicao_item_2 = posicoes_definidas[1]

    # posicao aleatoria item 3
    if not posicoes_definidas[2]:
        num_rand = randint(0,2)
        posicao_item_3 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[2] = posicao_item_3
    else:
        posicao_item_3 = posicoes_definidas[2]

    # posicao aleatoria item 4
    if not posicoes_definidas[3]:
        num_rand = randint(0,1)
        posicao_item_4 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[3] = posicao_item_4
    else:
        posicao_item_4 = posicoes_definidas[3]

    # posicao aleatoria item 5
    if not posicoes_definidas[4]:
        num_rand = randint(0,0)
        posicao_item_5 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[4] = posicao_item_5
    else:
        posicao_item_5 = posicoes_definidas[4]


    if fase_6:

        if aparece_1:
            item_1 = item1
            tamanho_item_1 = (largura_item, altura_item)
            item_1 = pygame.transform.scale(item_1, tamanho_item_1)
            item_1_tela = pygame.Rect(posicao_item_1[0],posicao_item_1[1],tamanho_item_1[0],tamanho_item_1[1])
            janela.blit(item_1, (posicao_item_1))
            diariamente = fonte_legenda.render("Diariamente", True, branco)
            janela.blit(diariamente, [posicao_item_1[0]+12,posicao_item_1[1]+165])

        if aparece_2:
            item_2 = item2
            tamanho_item_2 = (largura_item, altura_item)
            item_2 = pygame.transform.scale(item_2, tamanho_item_2)
            item_2_tela = pygame.Rect(posicao_item_2[0],posicao_item_2[1],tamanho_item_2[0],tamanho_item_2[1])
            janela.blit(item_2, (posicao_item_2))
            tresxsemana = fonte_legenda.render("3x por semana", True, branco)
            janela.blit(tresxsemana, [posicao_item_2[0]+12,posicao_item_2[1]+165])

        if aparece_3:
            item_3 = item3
            tamanho_item_3 = (largura_item, altura_item)
            item_3 = pygame.transform.scale(item_3, tamanho_item_3)
            item_3_tela = pygame.Rect(posicao_item_3[0],posicao_item_3[1],tamanho_item_3[0],tamanho_item_3[1])
            janela.blit(item_3, (posicao_item_3))
            duasxsemana = fonte_legenda.render("2x por semana", True, branco)
            janela.blit(duasxsemana, [posicao_item_3[0],posicao_item_3[1]+165])

        if aparece_4:
            item_4 = item4
            tamanho_item_4 = (largura_item, altura_item)
            item_4 = pygame.transform.scale(item_4, tamanho_item_4)
            item_4_tela = pygame.Rect(posicao_item_4[0],posicao_item_4[1],tamanho_item_4[0],tamanho_item_4[1])
            janela.blit(item_4, (posicao_item_4))
            umaxmes = fonte_legenda.render("1x por mês", True, branco)
            janela.blit(umaxmes, [posicao_item_4[0]+20,posicao_item_4[1]+165])

        if aparece_5:
            item_5 = item5
            tamanho_item_5 = (largura_item, altura_item)
            item_5 = pygame.transform.scale(item_5, tamanho_item_5)
            item_5_tela = pygame.Rect(posicao_item_5[0],posicao_item_5[1],tamanho_item_5[0],tamanho_item_5[1])
            janela.blit(item_5, (posicao_item_5))
            nunca = fonte_legenda.render("Nunca", True, branco)
            janela.blit(nunca,[posicao_item_5[0]+55,posicao_item_5[1]+165])
    
    else:

        if aparece_1:
            item_1 = item1
            tamanho_item_1 = (largura_item, altura_item)
            item_1 = pygame.transform.scale(item_1, tamanho_item_1)
            item_1_tela = pygame.Rect(posicao_item_1[0],posicao_item_1[1],tamanho_item_1[0],tamanho_item_1[1])
            janela.blit(item_1, (posicao_item_1))

        if aparece_2:
            item_2 = item2
            tamanho_item_2 = (largura_item, altura_item)
            item_2 = pygame.transform.scale(item_2, tamanho_item_2)
            item_2_tela = pygame.Rect(posicao_item_2[0],posicao_item_2[1],tamanho_item_2[0],tamanho_item_2[1])
            janela.blit(item_2, (posicao_item_2))

        if aparece_3:
            item_3 = item3
            tamanho_item_3 = (largura_item, altura_item)
            item_3 = pygame.transform.scale(item_3, tamanho_item_3)
            item_3_tela = pygame.Rect(posicao_item_3[0],posicao_item_3[1],tamanho_item_3[0],tamanho_item_3[1])
            janela.blit(item_3, (posicao_item_3))

        if aparece_4:
            item_4 = item4
            tamanho_item_4 = (largura_item, altura_item)
            item_4 = pygame.transform.scale(item_4, tamanho_item_4)
            item_4_tela = pygame.Rect(posicao_item_4[0],posicao_item_4[1],tamanho_item_4[0],tamanho_item_4[1])
            janela.blit(item_4, (posicao_item_4))

        if aparece_5:
            item_5 = item5
            tamanho_item_5 = (largura_item, altura_item)
            item_5 = pygame.transform.scale(item_5, tamanho_item_5)
            item_5_tela = pygame.Rect(posicao_item_5[0],posicao_item_5[1],tamanho_item_5[0],tamanho_item_5[1])
            janela.blit(item_5, (posicao_item_5))


    janela.blit(proxima_fase, (posicao_proxima_fase))
    janela.blit(fase_anterior,(posicao_fase_anterior))


    if event.type == pygame.MOUSEBUTTONDOWN:

        if aparece_1:
            if item_1_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]+300
                som_acerto.play()
                aparece_1 = False

        if aparece_2:
            if item_2_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]-100
                som_erro.play()
                aparece_2 = False

        if aparece_3:
            if item_3_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]-100
                som_erro.play()
                aparece_3 = False

        if aparece_4:
            if item_4_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]-100
                som_erro.play()
                aparece_4 = False

        if aparece_5:
            if item_5_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]-100
                som_erro.play()
                aparece_5 = False

    return aparece_1, aparece_2, aparece_3, aparece_4, aparece_5


# processamento do jogo com 6 itens
def andamento_jogo_6(item1, item2, item3, item4, item5, item6, fase, fase_ant, aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6):

    largura_item = 160
    altura_item = 160

    posicoes = [[75,560],[150,350],[435,400],[450,200],[790,560],[725,325]]

    # posicao aleatoria item 1
    if not posicoes_definidas[0]:
        num_rand = randint(0,5)
        posicao_item_1 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[0] = posicao_item_1
    else:
        posicao_item_1 = posicoes_definidas[0]

    # posicao aleatoria item 2
    if not posicoes_definidas[1]:
        num_rand = randint(0,4)
        posicao_item_2 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[1] = posicao_item_2
    else:
        posicao_item_2 = posicoes_definidas[1]

    # posicao aleatoria item 3
    if not posicoes_definidas[2]:
        num_rand = randint(0,3)
        posicao_item_3 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[2] = posicao_item_3
    else:
        posicao_item_3 = posicoes_definidas[2]

    # posicao aleatoria item 4
    if not posicoes_definidas[3]:
        num_rand = randint(0,2)
        posicao_item_4 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[3] = posicao_item_4
    else:
        posicao_item_4 = posicoes_definidas[3]

    # posicao aleatoria item 5
    if not posicoes_definidas[4]:
        num_rand = randint(0,1)
        posicao_item_5 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[4] = posicao_item_5
    else:
        posicao_item_5 = posicoes_definidas[4]

    # posicao aleatoria item 6
    if not posicoes_definidas[5]:
        num_rand = randint(0,0)
        posicao_item_6 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[5] = posicao_item_6
    else:
        posicao_item_6 = posicoes_definidas[5]


    if fase_7:

        if aparece_1:
            item_1 = item1
            tamanho_item_1 = (largura_item, altura_item)
            item_1 = pygame.transform.scale(item_1, tamanho_item_1)
            item_1_tela = pygame.Rect(posicao_item_1[0],posicao_item_1[1],tamanho_item_1[0],tamanho_item_1[1])
            janela.blit(item_1, (posicao_item_1))
            posto_de_saude_1 = fonte_legenda.render("Hospital", True, branco)
            janela.blit(posto_de_saude_1,[posicao_item_1[0]+25,posicao_item_1[1]+165])

        if aparece_2:
            item_2 = item2
            tamanho_item_2 = (largura_item, altura_item)
            item_2 = pygame.transform.scale(item_2, tamanho_item_2)
            item_2_tela = pygame.Rect(posicao_item_2[0],posicao_item_2[1],tamanho_item_2[0],tamanho_item_2[1])
            janela.blit(item_2, (posicao_item_2))
            profissional_saude = fonte_legenda.render("Profissional da Saúde",True, branco)
            janela.blit(profissional_saude,[posicao_item_2[0]-70,posicao_item_2[1]+165])

        if aparece_3:
            item_3 = item3
            tamanho_item_3 = (largura_item, altura_item)
            item_3 = pygame.transform.scale(item_3, tamanho_item_3)
            item_3_tela = pygame.Rect(posicao_item_3[0],posicao_item_3[1],tamanho_item_3[0],tamanho_item_3[1])
            janela.blit(item_3, (posicao_item_3))
            posto_de_saude_2 = fonte_legenda.render("Unidade de Saúde", True, branco)
            janela.blit(posto_de_saude_2,[posicao_item_3[0]-25,posicao_item_3[1]+165])

        if aparece_4:
            item_4 = item4
            tamanho_item_4 = (largura_item, altura_item)
            item_4 = pygame.transform.scale(item_4, tamanho_item_4)
            item_4_tela = pygame.Rect(posicao_item_4[0],posicao_item_4[1],tamanho_item_4[0],tamanho_item_4[1])
            janela.blit(item_4, (posicao_item_4))
            nada = fonte_legenda.render("Nada", True, branco)
            janela.blit(nada,[posicao_item_4[0]+50,posicao_item_4[1]+165])

        if aparece_5:
            item_5 = item5
            tamanho_item_5 = (largura_item, altura_item)
            item_5 = pygame.transform.scale(item_5, tamanho_item_5)
            item_5_tela = pygame.Rect(posicao_item_5[0],posicao_item_5[1],tamanho_item_5[0],tamanho_item_5[1])
            janela.blit(item_5, (posicao_item_5))
            limpeza = fonte_legenda.render("Limpeza apenas", True, branco)
            janela.blit(limpeza,[posicao_item_5[0]-15,posicao_item_5[1]+165])

        if aparece_6:
            item_6 = item6
            tamanho_item_6 = (largura_item, altura_item)
            item_6 = pygame.transform.scale(item_6, tamanho_item_6)
            item_6_tela = pygame.Rect(posicao_item_6[0],posicao_item_6[1],tamanho_item_6[0],tamanho_item_6[1])
            janela.blit(item_6, (posicao_item_6))
            curativo = fonte_legenda.render("Curativo apenas", True, branco)
            janela.blit(curativo,[posicao_item_6[0]-15,posicao_item_6[1]+165])

    elif fase_9:

        if aparece_1:
            item_1 = item1
            tamanho_item_1 = (largura_item, altura_item)
            item_1 = pygame.transform.scale(item_1, tamanho_item_1)
            item_1_tela = pygame.Rect(posicao_item_1[0],posicao_item_1[1],tamanho_item_1[0],tamanho_item_1[1])
            janela.blit(item_1, (posicao_item_1))
            hora17 = fonte_legenda.render("17h", True, branco)
            janela.blit(hora17,[posicao_item_1[0]+60,posicao_item_1[1]+165])

        if aparece_2:
            item_2 = item2
            tamanho_item_2 = (largura_item, altura_item)
            item_2 = pygame.transform.scale(item_2, tamanho_item_2)
            item_2_tela = pygame.Rect(posicao_item_2[0],posicao_item_2[1],tamanho_item_2[0],tamanho_item_2[1])
            janela.blit(item_2, (posicao_item_2))
            hora18 = fonte_legenda.render("18h", True, branco)
            janela.blit(hora18,[posicao_item_2[0]+65,posicao_item_2[1]+165])

        if aparece_3:
            item_3 = item3
            tamanho_item_3 = (largura_item, altura_item)
            item_3 = pygame.transform.scale(item_3, tamanho_item_3)
            item_3_tela = pygame.Rect(posicao_item_3[0],posicao_item_3[1],tamanho_item_3[0],tamanho_item_3[1])
            janela.blit(item_3, (posicao_item_3))
            hora19 = fonte_legenda.render("19h", True, branco)
            janela.blit(hora19,[posicao_item_3[0]+65,posicao_item_3[1]+165])

        if aparece_4:
            item_4 = item4
            tamanho_item_4 = (largura_item, altura_item)
            item_4 = pygame.transform.scale(item_4, tamanho_item_4)
            item_4_tela = pygame.Rect(posicao_item_4[0],posicao_item_4[1],tamanho_item_4[0],tamanho_item_4[1])
            janela.blit(item_4, (posicao_item_4))
            hora8 = fonte_legenda.render("8h", True, branco)
            janela.blit(hora8,[posicao_item_4[0]+65,posicao_item_4[1]+165])

        if aparece_5:
            item_5 = item5
            tamanho_item_5 = (largura_item, altura_item)
            item_5 = pygame.transform.scale(item_5, tamanho_item_5)
            item_5_tela = pygame.Rect(posicao_item_5[0],posicao_item_5[1],tamanho_item_5[0],tamanho_item_5[1])
            janela.blit(item_5, (posicao_item_5))
            hora11 = fonte_legenda.render("11h", True, branco)
            janela.blit(hora11,[posicao_item_5[0]+65,posicao_item_5[1]+165])

        if aparece_6:
            item_6 = item6
            tamanho_item_6 = (largura_item, altura_item)
            item_6 = pygame.transform.scale(item_6, tamanho_item_6)
            item_6_tela = pygame.Rect(posicao_item_6[0],posicao_item_6[1],tamanho_item_6[0],tamanho_item_6[1])
            janela.blit(item_6, (posicao_item_6))
            hora16 = fonte_legenda.render("16h", True, branco)
            janela.blit(hora16,[posicao_item_6[0]+65,posicao_item_6[1]+165])

    else:

        if aparece_1:
            item_1 = item1
            tamanho_item_1 = (largura_item, altura_item)
            item_1 = pygame.transform.scale(item_1, tamanho_item_1)
            item_1_tela = pygame.Rect(posicao_item_1[0],posicao_item_1[1],tamanho_item_1[0],tamanho_item_1[1])
            janela.blit(item_1, (posicao_item_1))

        if aparece_2:
            item_2 = item2
            tamanho_item_2 = (largura_item, altura_item)
            item_2 = pygame.transform.scale(item_2, tamanho_item_2)
            item_2_tela = pygame.Rect(posicao_item_2[0],posicao_item_2[1],tamanho_item_2[0],tamanho_item_2[1])
            janela.blit(item_2, (posicao_item_2))

        if aparece_3:
            item_3 = item3
            tamanho_item_3 = (largura_item, altura_item)
            item_3 = pygame.transform.scale(item_3, tamanho_item_3)
            item_3_tela = pygame.Rect(posicao_item_3[0],posicao_item_3[1],tamanho_item_3[0],tamanho_item_3[1])
            janela.blit(item_3, (posicao_item_3))

        if aparece_4:
            item_4 = item4
            tamanho_item_4 = (largura_item, altura_item)
            item_4 = pygame.transform.scale(item_4, tamanho_item_4)
            item_4_tela = pygame.Rect(posicao_item_4[0],posicao_item_4[1],tamanho_item_4[0],tamanho_item_4[1])
            janela.blit(item_4, (posicao_item_4))

        if aparece_5:
            item_5 = item5
            tamanho_item_5 = (largura_item, altura_item)
            item_5 = pygame.transform.scale(item_5, tamanho_item_5)
            item_5_tela = pygame.Rect(posicao_item_5[0],posicao_item_5[1],tamanho_item_5[0],tamanho_item_5[1])
            janela.blit(item_5, (posicao_item_5))

        if aparece_6:
            item_6 = item6
            tamanho_item_6 = (largura_item, altura_item)
            item_6 = pygame.transform.scale(item_6, tamanho_item_6)
            item_6_tela = pygame.Rect(posicao_item_6[0],posicao_item_6[1],tamanho_item_6[0],tamanho_item_6[1])
            janela.blit(item_6, (posicao_item_6))


    janela.blit(proxima_fase, (posicao_proxima_fase))
    janela.blit(fase_anterior, (posicao_fase_anterior))


    if event.type == pygame.MOUSEBUTTONDOWN:

        if aparece_1:
            if item_1_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]+200
                som_acerto.play()
                aparece_1 = False

        if aparece_2:
            if item_2_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]+200
                som_acerto.play()
                aparece_2 = False

        if aparece_3:
            if item_3_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]+200
                som_acerto.play()
                aparece_3 = False

        if aparece_4:
            if item_4_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]-50
                som_erro.play()
                aparece_4 = False

        if aparece_5:
            if item_5_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]-50
                som_erro.play()
                aparece_5 = False

        if aparece_6:
            if item_6_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]-50
                som_erro.play()
                aparece_6 = False

    return aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6


# processamento do jogo com 8 itens
def andamento_jogo_8(item1, item2, item3, item4, item5, item6, item7, item8, fase, fase_ant, aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6, aparece_7, aparece_8):

    largura_item = 165
    altura_item = 165

    posicoes = [[50,600],[50,400],[50,200],[450,400],[450,200],[825,600],[825,400],[825,200]]

    # posicao aleatoria item 1
    if not posicoes_definidas[0]:
        num_rand = randint(0,7)
        posicao_item_1 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[0] = posicao_item_1
    else:
        posicao_item_1 = posicoes_definidas[0]

    # posicao aleatoria item 2
    if not posicoes_definidas[1]:
        num_rand = randint(0,6)
        posicao_item_2 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[1] = posicao_item_2
    else:
        posicao_item_2 = posicoes_definidas[1]

    # posicao aleatoria item 3
    if not posicoes_definidas[2]:
        num_rand = randint(0,5)
        posicao_item_3 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[2] = posicao_item_3
    else:
        posicao_item_3 = posicoes_definidas[2]

    # posicao aleatoria item 4
    if not posicoes_definidas[3]:
        num_rand = randint(0,4)
        posicao_item_4 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[3] = posicao_item_4
    else:
        posicao_item_4 = posicoes_definidas[3]

    # posicao aleatoria item 5
    if not posicoes_definidas[4]:
        num_rand = randint(0,3)
        posicao_item_5 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[4] = posicao_item_5
    else:
        posicao_item_5 = posicoes_definidas[4]

    # posicao aleatoria item 6
    if not posicoes_definidas[5]:
        num_rand = randint(0,2)
        posicao_item_6 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[5] = posicao_item_6
    else:
        posicao_item_6 = posicoes_definidas[5]

    # posicao aleatoria item 7
    if not posicoes_definidas[6]:
        num_rand = randint(0,1)
        posicao_item_7 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[6] = posicao_item_7
    else:
        posicao_item_7 = posicoes_definidas[6]

    # posicao aleatoria item 8
    if not posicoes_definidas[7]:
        num_rand = randint(0,0)
        posicao_item_8 = posicoes[num_rand]
        posicoes.pop(num_rand)
        posicoes_definidas[7] = posicao_item_8
    else:
        posicao_item_8 = posicoes_definidas[7]


    if aparece_1:
        item_1 = item1
        tamanho_item_1 = (largura_item, altura_item)
        item_1 = pygame.transform.scale(item_1, tamanho_item_1)
        item_1_tela = pygame.Rect(posicao_item_1[0],posicao_item_1[1],tamanho_item_1[0],tamanho_item_1[1])
        janela.blit(item_1, (posicao_item_1))

    if aparece_2:
        item_2 = item2
        tamanho_item_2 = (largura_item, altura_item)
        item_2 = pygame.transform.scale(item_2, tamanho_item_2)
        item_2_tela = pygame.Rect(posicao_item_2[0],posicao_item_2[1],tamanho_item_2[0],tamanho_item_2[1])
        janela.blit(item_2, (posicao_item_2))

    if aparece_3:
        item_3 = item3
        tamanho_item_3 = (largura_item, altura_item)
        item_3 = pygame.transform.scale(item_3, tamanho_item_3)
        item_3_tela = pygame.Rect(posicao_item_3[0],posicao_item_3[1],tamanho_item_3[0],tamanho_item_3[1])
        janela.blit(item_3, (posicao_item_3))

    if aparece_4:
        item_4 = item4
        tamanho_item_4 = (largura_item, altura_item)
        item_4 = pygame.transform.scale(item_4, tamanho_item_4)
        item_4_tela = pygame.Rect(posicao_item_4[0],posicao_item_4[1],tamanho_item_4[0],tamanho_item_4[1])
        janela.blit(item_4, (posicao_item_4))

    if aparece_5:
        item_5 = item5
        tamanho_item_5 = (largura_item, altura_item)
        item_5 = pygame.transform.scale(item_5, tamanho_item_5)
        item_5_tela = pygame.Rect(posicao_item_5[0],posicao_item_5[1],tamanho_item_5[0],tamanho_item_5[1])
        janela.blit(item_5, (posicao_item_5))

    if aparece_6:
        item_6 = item6
        tamanho_item_6 = (largura_item, altura_item)
        item_6 = pygame.transform.scale(item_6, tamanho_item_6)
        item_6_tela = pygame.Rect(posicao_item_6[0],posicao_item_6[1],tamanho_item_6[0],tamanho_item_6[1])
        janela.blit(item_6, (posicao_item_6))

    if aparece_7:
        item_7 = item7
        tamanho_item_7 = (largura_item, altura_item)
        item_7 = pygame.transform.scale(item_7, tamanho_item_7)
        item_7_tela = pygame.Rect(posicao_item_7[0],posicao_item_7[1],tamanho_item_7[0],tamanho_item_7[1])
        janela.blit(item_7, (posicao_item_7))

    if aparece_8:
        item_8 = item8
        tamanho_item_8 = (largura_item, altura_item)
        item_8 = pygame.transform.scale(item_8, tamanho_item_8)
        item_8_tela = pygame.Rect(posicao_item_8[0],posicao_item_8[1],tamanho_item_8[0],tamanho_item_8[1])
        janela.blit(item_8, (posicao_item_8))


    janela.blit(proxima_fase, (posicao_proxima_fase))
    janela.blit(fase_anterior, (posicao_fase_anterior))


    if event.type == pygame.MOUSEBUTTONDOWN:

        if aparece_1:
            if item_1_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]+100
                som_acerto.play()
                aparece_1 = False

        if aparece_2:
            if item_2_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]+100
                som_acerto.play()
                aparece_2 = False

        if aparece_3:
            if item_3_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]+100
                som_acerto.play()
                aparece_3 = False

        if aparece_4:
            if item_4_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]+100
                som_acerto.play()
                aparece_4 = False

        if aparece_5:
            if item_5_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]-25
                som_erro.play()
                aparece_5 = False

        if aparece_6:
            if item_6_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]-25
                som_erro.play()
                aparece_6 = False

        if aparece_7:
            if item_7_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]-25
                som_erro.play()
                aparece_7 = False

        if aparece_8:
            if item_8_tela.collidepoint(event.pos):
                pontuacao[0] = pontuacao[0]-25
                som_erro.play()
                aparece_8 = False

    return aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6, aparece_7, aparece_8


# botao voltar ao inicio (tela creditos)
volta_inicio = pygame.image.load(Imagens.BOTAO_VOLTAR_INICIO)
posicao_inicio = 1100,545
tamanho_inicio = 200,200
volta_inicio = pygame.transform.scale(volta_inicio, tamanho_inicio)
botao_voltar_inicio = pygame.Rect(posicao_inicio[0],posicao_inicio[1],tamanho_inicio[0],tamanho_inicio[1])

# botao next (tela bloco de notas)
next = pygame.image.load(Imagens.BOTAO_PROXIMA_FASE)
posicao_next = 1100,450
tamanho_next = 200,200
next = pygame.transform.scale(next, tamanho_next)
botao_next = pygame.Rect(posicao_next[0],posicao_next[1],tamanho_next[0],tamanho_next[1])

# botao jogar
jogar = pygame.image.load(Imagens.BOTAO_JOGAR)
posicao_jogar = 190,618
tamanho_jogar = 200,100
jogar = pygame.transform.scale(jogar, tamanho_jogar)
botao_jogar = pygame.Rect(posicao_jogar[0],posicao_jogar[1],tamanho_jogar[0],tamanho_jogar[1])

# botao sair
sair = pygame.image.load(Imagens.BOTAO_SAIR)
posicao_sair = 1000,618
tamanho_sair = 210,100
sair = pygame.transform.scale(sair, tamanho_sair)
botao_sair = pygame.Rect(posicao_sair[0],posicao_sair[1],tamanho_sair[0],tamanho_sair[1])

# botao creditos na tela de menu
creditos_menu = pygame.image.load(Imagens.BOTAO_CREDITOS)
posicao_creditos_menu = 590,618
tamanho_creditos_menu = 210,100
creditos_menu = pygame.transform.scale(creditos_menu, tamanho_creditos_menu)
botao_creditos_menu = pygame.Rect(posicao_creditos_menu[0],posicao_creditos_menu[1],tamanho_creditos_menu[0],tamanho_creditos_menu[1])

#botoes na tela de confirmaçao
imagem_botao_sim = pygame.image.load(Imagens.BOTAO_SIM)
posicao_botao_sim = 210,400
tamanho_botao_sim = 280,200
imagem_botao_sim = pygame.transform.scale(imagem_botao_sim, tamanho_botao_sim)
botao_sim = pygame.Rect(posicao_botao_sim[0],posicao_botao_sim[1],tamanho_botao_sim[0],tamanho_botao_sim[1])

imagem_botao_nao = pygame.image.load(Imagens.BOTAO_NAO)
posicao_botao_nao = 860,400
tamanho_botao_nao = 280,200
imagem_botao_nao = pygame.transform.scale(imagem_botao_nao, tamanho_botao_nao)
botao_nao = pygame.Rect(posicao_botao_nao[0],posicao_botao_nao[1],tamanho_botao_nao[0],tamanho_botao_nao[1])


# carregando imagens

fundo = pygame.image.load(Imagens.FUNDO_MENU)
fundo = pygame.transform.scale(fundo, (largura,altura))

logo = pygame.image.load(Imagens.LOGO_MENU)
logo = pygame.transform.scale(logo, (700, 100))

logo_2 = pygame.image.load(Imagens.LOGO_2)
logo_2 = pygame.transform.scale(logo_2, (600, 30))

mario_pergunta = pygame.image.load(Imagens.IMAGEM_MARIO_PERGUNTA)
mario_pergunta = pygame.transform.scale(mario_pergunta, (175,175))

nintendo_logo = pygame.image.load(Imagens.NINTENDO_LOGO)
nintendo_logo = pygame.transform.scale(nintendo_logo, (200,200))

Bloco_de_notas = pygame.image.load(Imagens.IMAGEM_BLOCO_DE_NOTAS)
Bloco_de_notas = pygame.transform.scale(Bloco_de_notas, (1300,700))

qr_code = pygame.image.load(Imagens.QR_CODE)
qr_code = pygame.transform.scale(qr_code, (250,250))

logo_medicina = pygame.image.load(Imagens.LOGO_MEDICINA)
logo_medicina = pygame.transform.scale(logo_medicina, (200,200))

fundo_pergunta = pygame.image.load(Imagens.FUNDO_PERGUNTA)
fundo_pergunta =  pygame.transform.scale(fundo_pergunta, (1119,503))

fundo_dica = pygame.image.load(Imagens.FUNDO_DICA)
fundo_dica = pygame.transform.scale(fundo_dica, (844,953))

fundo_fase = pygame.image.load(Imagens.FUNDO_FASE)
fundo_fase = pygame.transform.scale(fundo_fase, (847,955))

fundo_ponto = pygame.image.load(Imagens.FUNDO_PONTO)
fundo_ponto = pygame.transform.scale(fundo_ponto, (847,955))

fundo_tempo = pygame.image.load(Imagens.FUNDO_TEMPO)
fundo_tempo = pygame.transform.scale(fundo_tempo, (847,955))

cruz_vermelha = pygame.image.load(Imagens.IMAGEM_CRUZ_VERMELHA)
cruz_vermelha = pygame.transform.scale(cruz_vermelha, (25,20))

borda_qr_code = pygame.image.load(Imagens.BORDA_QR_CODE)
borda_qr_code = pygame.transform.scale(borda_qr_code, (550,600))


# logicas

mouse_pressionado = False

janela1 = True # menu

janela_confirmacao = False # confirmar saida

janela_tutorial = False # tutorial

# mostrar ou nao os itens
aparece_1 = True
aparece_2 = True
aparece_3 = True
aparece_4 = True
aparece_5 = True
aparece_6 = True
aparece_7 = True
aparece_8 = True

janela2 = False # jogo principal
fase_1 = False
fase_2 = False
fase_3 = False
fase_4 = False
fase_5 = False
fase_6 = False
fase_7 = False
fase_8 = False
fase_9 = False
fase_10 = False

janela3 = False # reforço e qr code

janela4 = False # creditos

jogo = True

event = None


musica_menu = pygame.mixer.music.load(Audios.MUSICA_MENU) # musica do menu
pygame.mixer.music.play()
pygame.mixer.music.rewind()

while jogo:
    for item in pygame.event.get(): 
        event = item
        if item.type == pygame.QUIT:
            jogo = False

    # tela menu
    if janela1:

        janela.blit(fundo, (0,0))
        janela.blit(logo, (largura//2-350,altura//2-300))
        janela.blit(logo_2, (largura//2-300,altura//2-200))
        janela.blit(jogar, (190,618))
        janela.blit(sair, (1000,618))
        janela.blit(creditos_menu, (590,618))
        janela.blit(cruz_vermelha, (571,324))
        janela.blit(cruz_vermelha, (234,393))
        janela.blit(cruz_vermelha, (1009,347))
        janela.blit(cruz_vermelha, (1225,372))
        janela.blit(cruz_vermelha, (797,353))


        if event.type == pygame.MOUSEBUTTONDOWN:
            if not mouse_pressionado:

                if botao_sair.collidepoint(event.pos):
                    janela1 = False
                    janela_confirmacao = True
                    pygame.mixer.music.pause()
                    musica_final = pygame.mixer.music.load(Audios.MUSICA_FINAL) # tela creditos
                    pygame.mixer.music.play()
                    
                elif botao_creditos_menu.collidepoint(event.pos):
                    janela1 = False
                    janela4 = True
                    pygame.mixer.music.stop()
                    musica_final = pygame.mixer.music.load(Audios.MUSICA_FINAL) # tela creditos
                    pygame.mixer.music.play()

                elif botao_jogar.collidepoint(event.pos):
                    janela1 = False
                    janela_tutorial = True
                    posicoes_definidas = [False, False, False, False, False, False, False, False]
                    aparece_1 = True
                    aparece_2 = True
                    aparece_3 = True
                    aparece_4 = True
                    aparece_5 = True
                    aparece_6 = True
                    aparece_7 = True
                    aparece_8 = True
                    som_comeco_jogo.play()
                    pygame.mixer.music.set_volume(0.5)


                mouse_pressionado = True
            else:
                mouse_pressionado = False


    # janela confirmação sair do jogo
    elif janela_confirmacao:

        janela.fill(preto) 
        texto_confirmacao = fonte_agradecimento.render("DESEJA SAIR DO JOGO?" , True, amarelo)
        janela.blit(texto_confirmacao, [235,90])

        janela.blit(imagem_botao_sim, posicao_botao_sim)

        janela.blit(imagem_botao_nao, posicao_botao_nao)


        if event.type == pygame.MOUSEBUTTONDOWN:
            if not mouse_pressionado:

                if botao_nao.collidepoint(event.pos):
                    janela_confirmacao = False
                    janela1 = True
                    pygame.mixer.music.stop()
                    musica_menu = pygame.mixer.music.load(Audios.MUSICA_MENU) # musica do menu
                    pygame.mixer.music.play()
                    som_comeco_jogo.play()

                elif botao_sim.collidepoint(event.pos):
                    jogo = False


            mouse_pressionado = True
        else:
            mouse_pressionado = False


    # tela tutorial
    elif janela_tutorial:
        
            tempo_inicial = pygame.time.get_ticks()

            janela.fill(preto)

            texto_tutorial1 = fonte_tutorial.render("Olá pessoal!" , True, amarelo)
            janela.blit(texto_tutorial1, [350,100]) 

            texto_tutorial2 = fonte_tutorial.render("Eu sou o Mario e estou aqui para te levar em uma jornada divertida e educativa chamada Mario Diet." , True , amarelo)
            janela.blit(texto_tutorial2 , [350,150])

            texto_tutorial3 = fonte_tutorial.render("Neste jogo, vamos aprender sobre a prevenção de feridas nos pés de pessoas com diabetes melitus II." , True , amarelo)
            janela.blit(texto_tutorial3, [350,200])

            texto_tutorial4 = fonte_tutorial.render("1 - Leia cada pergunta com atenção!" , True , amarelo)
            janela.blit(texto_tutorial4, [350,250])

            texto_tutorial5 = fonte_tutorial.render("2 - Clique nas respostas que você acha que estão corretas e depois na placa [-->] para passar a fase!" , True , amarelo)
            janela.blit(texto_tutorial5, [350,300])

            texto_tutorial6 = fonte_tutorial.render("3 - Aumente sua pontuação ao responder corretamente ou a diminua ao responder incorretamente!" , True, amarelo)
            janela.blit(texto_tutorial6, [350,350])

            texto_tutorial7 = fonte_tutorial.render("4 - O jogo possui 10 fases no total, tendo cada fase um ensinamento diferente!" , True , amarelo)
            janela.blit(texto_tutorial7, [350,400])

            texto_tutorial8 = fonte_tutorial.render("5 - Esse é o numero de respostas corretas em cada fase:" , True , amarelo)
            janela.blit(texto_tutorial8, [350,450])

            texto_tutorial9 = fonte_tutorial.render("*  Fase 1 até Fase 4   -   4  respostas corretas.", True, amarelo)
            janela.blit(texto_tutorial9, [385,500])

            texto_tutorial10 = fonte_tutorial.render("*  Fase 5    e   Fase 6   -   1  resposta correta." , True, amarelo)
            janela.blit(texto_tutorial10, [385,550])

            texto_tutorial11 = fonte_tutorial.render("*  Fase 7 até Fase 9   -   3  respostas corretas." , True, amarelo)
            janela.blit(texto_tutorial11, [385,600])

            texto_tutorial12 = fonte_tutorial.render("*  Fase 10   -    ***   SURPRESA   ***" , True, amarelo)
            janela.blit(texto_tutorial12, [385,650])

            imagem_mario_tutorial = pygame.image.load(Imagens.IMAGEM_MARIO_MENU)
            imagem_mario_tutorial_tamanho = pygame.transform.scale(imagem_mario_tutorial, (330,330))

            janela.blit(imagem_mario_tutorial_tamanho, [10,100])

            janela.blit(next, [1050,530] )

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not mouse_pressionado:

                    if botao_next.collidepoint(event.pos):
                        janela_tutorial = False
                        janela2 = True
                        fase_1 = True
                        posicoes_definidas = [False, False, False, False, False, False, False, False]
                        pygame.mixer.music.stop()
                        musica_jogo = pygame.mixer.music.load(Audios.MUSICA_JOGO) # musica do jogo principal
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_volume(0.7)
                        som_comeco_jogo.play()


                mouse_pressionado = True
            else:
                mouse_pressionado = False


    # tela do jogo principal
    elif janela2:

        janela.fill(cinza)
        janela.blit(fundo_pergunta, (-60,-148))
        janela.blit(fundo_dica, (762,-430))
        janela.blit(fundo_fase, (762,-240))
        janela.blit(fundo_tempo, (762,-47))
        janela.blit(fundo_ponto, (762,145))

        posicao_texto_dica = (1125,-3)
        posicao_texto_fase = (1015,187)
        posicao_texto_tempo = (1015,380)
        posicao_texto_pontuacao = (1015,576)

        conteudo_interface_dica = (1013,135)
        conteudo_interface_fase = (1215,170)
        conteudo_interface_tempo = (1015,500)
        conteudo_interface_pontuacao = (1020,690)

        largura_tela_interativa = 1000
        altura_tela_interativa = 576

        texto_fase = fonte_base.render("Fase", True, branco)
        janela.blit(texto_fase, [posicao_texto_fase[0], posicao_texto_fase[1], 366, 192])

        texto_tempo = fonte_base.render("Tempo", True, branco)
        janela.blit(texto_tempo, [posicao_texto_tempo[0], posicao_texto_tempo[1], 366,192])

        texto_dica = fonte_base.render("Dica", True, branco)
        janela.blit(texto_dica, [posicao_texto_dica[0], posicao_texto_dica[1], 366,192])

        texto_pontuação = fonte_base.render("Pontuação", True, branco)
        janela.blit(texto_pontuação, [posicao_texto_pontuacao[0], posicao_texto_pontuacao[1], 366,192])
        
        janela.blit(mario_pergunta, (36,12))

        proxima_fase = pygame.image.load(Imagens.BOTAO_PROXIMA_FASE)
        posicao_proxima_fase = 560,650
        tamanho_proxima_fase = 100,100
        proxima_fase = pygame.transform.scale(proxima_fase, tamanho_proxima_fase)
        botao_proxima_fase = pygame.Rect(posicao_proxima_fase[0],posicao_proxima_fase[1],tamanho_proxima_fase[0],tamanho_proxima_fase[1])

        fase_anterior = pygame.image.load(Imagens.BOTAO_FASE_ANTERIOR)
        posicao_fase_anterior = 440,650
        tamanho_fase_anterior = 100,100
        fase_anterior = pygame.transform.scale(fase_anterior, tamanho_fase_anterior)
        botao_fase_anterior = pygame.Rect(posicao_fase_anterior[0],posicao_fase_anterior[1],tamanho_fase_anterior[0],tamanho_fase_anterior[1])

        #musica_jogo.set_volume(0.2)

        # conteudo da fase 1
        if fase_1:
            
            item_1 = pygame.image.load(Imagens.IMAGEM_SAPATO_ADEQUADO_1)
            item_2 = pygame.image.load(Imagens.IMAGEM_SAPATO_ADEQUADO_2)
            item_3 = pygame.image.load(Imagens.IMAGEM_SAPATO_ADEQUADO_3)
            item_4 = pygame.image.load(Imagens.IMAGEM_SAPATO_ADEQUADO_4)
            item_5 = pygame.image.load(Imagens.IMAGEM_PE_DESCALCO)
            item_6 = pygame.image.load(Imagens.IMAGEM_CHINELO)
            item_7 = pygame.image.load(Imagens.IMAGEM_SANDALIA_SALTO)
            item_8 = pygame.image.load(Imagens.IMAGEM_SAPATO_ESTOURADO)

            aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6, aparece_7, aparece_8 = andamento_jogo_8(item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, proxima_fase, fase_anterior, aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6, aparece_7, aparece_8)

            tempo_decorrido = contador_de_tempo(tempo_inicial)
            if tempo_decorrido <= 0:

                fase_1 = False
                fase_2 = True

                aparece_1 = True
                aparece_2 = True
                aparece_3 = True
                aparece_4 = True
                aparece_5 = True
                aparece_6 = True
                aparece_7 = True
                aparece_8 = True

                posicoes_definidas = [False, False, False, False, False, False, False, False]

                tempo_inicial = pygame.time.get_ticks()

            n_fase = fonte_n.render("1", True, branco)
            janela.blit(n_fase, [conteudo_interface_fase[0], conteudo_interface_fase[1], 366, 192])
                
            pontos = fonte_pontuacao.render(str(pontuacao[0]) + " pontos", True, branco)
            janela.blit(pontos, (conteudo_interface_pontuacao))

            dica = fonte_dica.render("Calçados adequados", True, branco)
            janela.blit(dica, [conteudo_interface_dica[0], conteudo_interface_dica[1], 366, 192])

            texto_respostas = fonte_fases_corretas.render("4  respostas corretas", True, branco)
            janela.blit(texto_respostas, [1013,337])

            pergunta_fase_1_1 = fonte_perguntas.render("Diabéticos devem utilizar calçados apropriados e" , True, preto)
            janela.blit(pergunta_fase_1_1, [250,30])
            pergunta_fase_1_2 = fonte_perguntas.render("confortáveis, evitando andar descalços." , True, preto)
            janela.blit(pergunta_fase_1_2, [250,60])
            pergunta_fase_1_3 = fonte_perguntas.render("Quais desses calçados são mais apropriados?" , True, preto)
            janela.blit(pergunta_fase_1_3, [250,110])


            if event.type == pygame.MOUSEBUTTONDOWN:
                if not mouse_pressionado:

                    if botao_proxima_fase.collidepoint(event.pos):

                        fase_1 = False
                        fase_2 = True

                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True
                        aparece_6 = True
                        aparece_7 = True
                        aparece_8 = True

                        tempo_inicial = pygame.time.get_ticks()

                        posicoes_definidas = [False, False, False, False, False, False, False, False]

                        som_comeco_jogo.play()

                    elif botao_fase_anterior.collidepoint(event.pos):

                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True
                        aparece_6 = True
                        aparece_7 = True
                        aparece_8 = True

                        posicoes_definidas = [False, False, False, False, False, False, False, False]

                        pontuacao[0] = pontuacao_inicial

                        fase_1 = False
                        janela_2 = False
                        janela_tutorial = True

                        som_comeco_jogo.play()
                        musica_menu = pygame.mixer.music.load(Audios.MUSICA_MENU) # musica do menu
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_volume(0.7)


                mouse_pressionado = True
            else:
                mouse_pressionado = False


        # conteudo da fase 2
        elif fase_2:
            
            item_1 = pygame.image.load(Imagens.IMAGEM_MEIA_BRANCA)
            item_2 = pygame.image.load(Imagens.IMAGEM_MEIA_BEJE)
            item_3 = pygame.image.load(Imagens.IMAGEM_MEIA_AMARELA)
            item_4 = pygame.image.load(Imagens.IMAGEM_MEIA_AZUL_CLARA)
            item_5 = pygame.image.load(Imagens.IMAGEM_MEIA_VERMELHA)
            item_6 = pygame.image.load(Imagens.IMAGEM_MEIA_AZUL)
            item_7 = pygame.image.load(Imagens.IMAGEM_MEIA_PRETA)
            item_8 = pygame.image.load(Imagens.IMAGEM_MEIA_AZUL_MARINHO)

            aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6, aparece_7, aparece_8 = andamento_jogo_8(item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, proxima_fase, fase_anterior, aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6, aparece_7, aparece_8)
            

            tempo_decorrido = contador_de_tempo(tempo_inicial)
            if tempo_decorrido <= 0:

                fase_2 = False
                fase_3 = True

                aparece_1 = True
                aparece_2 = True
                aparece_3 = True
                aparece_4 = True
                aparece_5 = True
                aparece_6 = True
                aparece_7 = True
                aparece_8 = True

                posicoes_definidas = [False, False, False, False, False, False, False, False]

                tempo_inicial = pygame.time.get_ticks()

            n_fase = fonte_n.render("2", True, branco)
            janela.blit(n_fase, [conteudo_interface_fase[0], conteudo_interface_fase[1], 366, 192])

            pontos = fonte_pontuacao.render(str(pontuacao[0]) + " pontos", True, branco)
            janela.blit(pontos, (conteudo_interface_pontuacao))

            dica = fonte_dica.render("Meias claras", True, branco)
            janela.blit(dica, [conteudo_interface_dica[0], conteudo_interface_dica[1], 366, 192])

            texto_respostas = fonte_fases_corretas.render("4  respostas corretas", True, branco)
            janela.blit(texto_respostas, [1013,337])

            pergunta_fase_2_1 = fonte_perguntas.render("Usar meias claras e de algodão permite que sejam" , True, preto)
            janela.blit(pergunta_fase_2_1, [250,30])
            pergunta_fase_2_2 = fonte_perguntas.render("vistas quaisquer manchas causadas por ferimentos." , True, preto)
            janela.blit(pergunta_fase_2_2, [250,60])
            pergunta_fase_2_3 = fonte_perguntas.render("Quais dessas meias são mais apropriadas?" , True, preto)
            janela.blit(pergunta_fase_2_3, [250,110])


            if event.type == pygame.MOUSEBUTTONDOWN:
                if not mouse_pressionado:

                    if botao_proxima_fase.collidepoint(event.pos):

                        fase_2 = False
                        fase_3 = True

                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True
                        aparece_6 = True
                        aparece_7 = True
                        aparece_8 = True

                        posicoes_definidas = [False, False, False, False, False, False, False, False]

                        tempo_inicial = pygame.time.get_ticks()

                        som_comeco_jogo.play()

                    elif botao_fase_anterior.collidepoint(event.pos):

                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True
                        aparece_6 = True
                        aparece_7 = True
                        aparece_8 = True

                        posicoes_definidas = [False, False, False, False, False, False, False, False]

                        tempo_inicial = pygame.time.get_ticks()
                        
                        fase_1 = True
                        fase_2 = False

                        som_comeco_jogo.play()


                mouse_pressionado = True
            else:
                mouse_pressionado = False


        # conteudo da fase 3
        elif fase_3:

            item_1 = pygame.image.load(Imagens.IMAGEM_CREME_HIDRATANTE_1)
            item_2 = pygame.image.load(Imagens.IMAGEM_CREME_HIDRATANTE_2)
            item_3 = pygame.image.load(Imagens.IMAGEM_CREME_HIDRATANTE_3)
            item_4 = pygame.image.load(Imagens.IMAGEM_CREME_HIDRATANTE_4)
            item_5 = pygame.image.load(Imagens.IMAGEM_COLA_BRANCA)
            item_6 = pygame.image.load(Imagens.IMAGEM_PROTETOR_SOLAR)
            item_7 = pygame.image.load(Imagens.IMAGEM_SHAMPOO)
            item_8 = pygame.image.load(Imagens.IMAGEM_CONDICIONADOR)

            aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6, aparece_7, aparece_8 = andamento_jogo_8(item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, proxima_fase, fase_anterior, aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6, aparece_7, aparece_8)

            tempo_decorrido = contador_de_tempo(tempo_inicial)
            if tempo_decorrido <= 0:

                fase_3 = False
                fase_4 = True

                aparece_1 = True
                aparece_2 = True
                aparece_3 = True
                aparece_4 = True
                aparece_5 = True
                aparece_6 = True
                aparece_7 = True
                aparece_8 = True

                posicoes_definidas = [False, False, False, False, False, False, False, False]

                tempo_inicial = pygame.time.get_ticks()

            n_fase = fonte_n.render("3", True, branco)
            janela.blit(n_fase, [conteudo_interface_fase[0], conteudo_interface_fase[1], 366, 192])

            pontos = fonte_pontuacao.render(str(pontuacao[0]) + " pontos", True, branco)
            janela.blit(pontos, (conteudo_interface_pontuacao))

            dica = fonte_dica.render("Cremes hidratantes", True, branco)
            janela.blit(dica, [conteudo_interface_dica[0], conteudo_interface_dica[1], 366, 192])

            texto_respostas = fonte_fases_corretas.render("4  respostas corretas", True, branco)
            janela.blit(texto_respostas, [1013,337])

            pergunta_fase_3_1 = fonte_perguntas.render("Hidratantes são muito importantes, visto que a" , True, preto)
            janela.blit(pergunta_fase_3_1, [250,30])
            pergunta_fase_3_2 = fonte_perguntas.render("pele ressecada dos pés causa rachaduras." , True, preto)
            janela.blit(pergunta_fase_3_2, [250,60])
            pergunta_fase_3_3 = fonte_perguntas.render("Quais dessas opções são mais recomendadas?" , True, preto)
            janela.blit(pergunta_fase_3_3, [250,110])


            if event.type == pygame.MOUSEBUTTONDOWN:
                if not mouse_pressionado:

                    if botao_proxima_fase.collidepoint(event.pos):

                        fase_3 = False
                        fase_4 = True

                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True
                        aparece_6 = True
                        aparece_7 = True
                        aparece_8 = True

                        posicoes_definidas = [False, False, False, False, False, False, False, False]

                        tempo_inicial = pygame.time.get_ticks()

                        som_comeco_jogo.play()

                    elif botao_fase_anterior.collidepoint(event.pos):

                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True
                        aparece_6 = True
                        aparece_7 = True
                        aparece_8 = True

                        posicoes_definidas = [False, False, False, False, False, False, False, False]

                        tempo_inicial = pygame.time.get_ticks()

                        fase_2 = True
                        fase_3 = False

                        som_comeco_jogo.play()    
                    

                mouse_pressionado = True
            else:
                mouse_pressionado = False


        # conteudo da fase 4
        elif fase_4:

            item_1 = pygame.image.load(Imagens.IMAGEM_UNHA_LINHA_RETA_1)
            item_2 = pygame.image.load(Imagens.IMAGEM_UNHA_LINHA_RETA_2)
            item_3 = pygame.image.load(Imagens.IMAGEM_UNHA_LINHA_RETA_3)
            item_4 = pygame.image.load(Imagens.IMAGEM_UNHA_LINHA_RETA_4)
            item_5 = pygame.image.load(Imagens.IMAGEM_UNHA_ENCRAVADA)
            item_6 = pygame.image.load(Imagens.IMAGEM_UNHA_CURVADA)
            item_7 = pygame.image.load(Imagens.IMAGEM_UNHA_GRANDE)
            item_8 = pygame.image.load(Imagens.IMAGEM_UNHA_RACHADA)

            aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6, aparece_7, aparece_8 = andamento_jogo_8(item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, proxima_fase, fase_anterior, aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6, aparece_7, aparece_8)

            tempo_decorrido = contador_de_tempo(tempo_inicial)
            if tempo_decorrido <= 0:

                fase_4 = False
                fase_5 = True

                aparece_1 = True
                aparece_2 = True
                aparece_3 = True
                aparece_4 = True
                aparece_5 = True
                aparece_6 = True
                aparece_7 = True
                aparece_8 = True

                posicoes_definidas = [False, False, False, False, False]

                tempo_inicial = pygame.time.get_ticks()

            n_fase = fonte_n.render("4", True, branco)
            janela.blit(n_fase, [conteudo_interface_fase[0], conteudo_interface_fase[1], 366, 192])

            pontos = fonte_pontuacao.render(str(pontuacao[0]) + " pontos", True, branco)
            janela.blit(pontos, (conteudo_interface_pontuacao))

            dica = fonte_dica.render("Unhas retas", True, branco)
            janela.blit(dica, [conteudo_interface_dica[0], conteudo_interface_dica[1], 366, 192])

            texto_respostas = fonte_fases_corretas.render("4  respostas corretas", True, branco)
            janela.blit(texto_respostas, [1013,337])

            pergunta_fase_4_1 = fonte_perguntas.render("Cortar unhas em linha reta é um hábito simples" , True, preto)
            janela.blit(pergunta_fase_4_1, [250,30])
            pergunta_fase_4_2 = fonte_perguntas.render("que pode evitar as unhas encravadas e feridas." , True, preto)
            janela.blit(pergunta_fase_4_2, [250,60])
            pergunta_fase_4_3 = fonte_perguntas.render("Quais desses cortes são mais apropriados?" , True, preto)
            janela.blit(pergunta_fase_4_3, [250,110])


            if event.type == pygame.MOUSEBUTTONDOWN:
                if not mouse_pressionado:

                    if botao_proxima_fase.collidepoint(event.pos):

                        fase_4 = False
                        fase_5 = True

                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True

                        posicoes_definidas = [False, False, False, False, False]

                        tempo_inicial = pygame.time.get_ticks()

                        som_comeco_jogo.play()

                    elif botao_fase_anterior.collidepoint(event.pos):

                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True
                        aparece_6 = True
                        aparece_7 = True
                        aparece_8 = True

                        posicoes_definidas = [False, False, False, False, False, False, False, False]

                        tempo_inicial = pygame.time.get_ticks()

                        fase_3 = True
                        fase_4 = False
                        
                        som_comeco_jogo.play()
                    

                mouse_pressionado = True
            else:
                mouse_pressionado = False


        # conteudo da fase 5
        elif fase_5:

            item_1 = pygame.image.load(Imagens.IMAGEM_AGUA_MORNA)
            item_2 = pygame.image.load(Imagens.IMAGEM_AGUA_QUENTE)
            item_3 = pygame.image.load(Imagens.IMAGEM_AGUA_FERVENTE)
            item_4 = pygame.image.load(Imagens.IMAGEM_TERMOMETRO_ZERADO)
            item_5 = pygame.image.load(Imagens.IMAGEM_TERMOMETRO_100C)

            aparece_1, aparece_2, aparece_3, aparece_4, aparece_5 = andamento_jogo_5(item_1, item_2, item_3, item_4, item_5, proxima_fase, fase_anterior, aparece_1, aparece_2, aparece_3, aparece_4, aparece_5)

            tempo_decorrido = contador_de_tempo(tempo_inicial)
            if tempo_decorrido <= 0:

                fase_5 = False
                fase_6 = True

                aparece_1 = True
                aparece_2 = True
                aparece_3 = True
                aparece_4 = True
                aparece_5 = True

                posicoes_definidas = [False, False, False, False, False]

                tempo_inicial = pygame.time.get_ticks()

            n_fase = fonte_n.render("5", True, branco)
            janela.blit(n_fase, [conteudo_interface_fase[0], conteudo_interface_fase[1], 366, 192])

            pontos = fonte_pontuacao.render(str(pontuacao[0]) + " pontos", True, branco)
            janela.blit(pontos, (conteudo_interface_pontuacao))

            dica = fonte_dica.render("Água morna", True, branco)
            janela.blit(dica, [conteudo_interface_dica[0], conteudo_interface_dica[1], 366, 192])

            texto_respostas = fonte_fases_corretas.render("1  resposta correta", True, branco)
            janela.blit(texto_respostas, [1013,337])

            pergunta_fase_5_1 = fonte_perguntas.render("Diabéticos têm a sensibilidade dos pés reduzida," , True, preto)
            janela.blit(pergunta_fase_5_1, [250,30])
            pergunta_fase_5_2 = fonte_perguntas.render("por isso devem lavar os pés com água morna, 30°C." , True, preto)
            janela.blit(pergunta_fase_5_2, [250,60])
            pergunta_fase_5_3 = fonte_perguntas.render("Qual dessas temperaturas é a mais adequada?" , True, preto)
            janela.blit(pergunta_fase_5_3, [250,110])


            if event.type == pygame.MOUSEBUTTONDOWN:
                if not mouse_pressionado:

                    if botao_proxima_fase.collidepoint(event.pos):

                        fase_5 = False
                        fase_6 = True
                        
                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True
                        
                        posicoes_definidas = [False, False, False, False, False]

                        tempo_inicial = pygame.time.get_ticks()

                        som_comeco_jogo.play()

                    elif botao_fase_anterior.collidepoint(event.pos):

                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True
                        aparece_6 = True
                        aparece_7 = True
                        aparece_8 = True

                        posicoes_definidas = [False, False, False, False, False, False, False, False]

                        tempo_inicial = pygame.time.get_ticks()

                        fase_4 = True
                        fase_5 = False

                        som_comeco_jogo.play()


                mouse_pressionado = True
            else:
                mouse_pressionado = False


        # conteudo da fase 6
        elif fase_6:

            item_1 = pygame.image.load(Imagens.IMAGEM_ESPELHO_DIARIAMENTE)
            item_2 = pygame.image.load(Imagens.IMAGEM_ESPELHO_3X_SEMANA)
            item_3 = pygame.image.load(Imagens.IMAGEM_ESPELHO_2X_SEMANA)
            item_4 = pygame.image.load(Imagens.IMAGEM_ESPELHO_1X_MES)
            item_5 = pygame.image.load(Imagens.IMAGEM_ESPELHO_NUNCA)

            aparece_1, aparece_2, aparece_3, aparece_4, aparece_5 = andamento_jogo_5(item_1, item_2, item_3, item_4, item_5, proxima_fase, fase_anterior, aparece_1, aparece_2, aparece_3, aparece_4, aparece_5)

            tempo_decorrido = contador_de_tempo(tempo_inicial)
            if tempo_decorrido <= 0:

                fase_6 = False
                fase_7 = True

                aparece_1 = True
                aparece_2 = True
                aparece_3 = True
                aparece_4 = True
                aparece_5 = True
                aparece_6 = True

                posicoes_definidas = [False, False, False, False, False, False]

                tempo_inicial = pygame.time.get_ticks()

            n_fase = fonte_n.render("6", True, branco)
            janela.blit(n_fase, [conteudo_interface_fase[0], conteudo_interface_fase[1], 366, 192])

            pontos = fonte_pontuacao.render(str(pontuacao[0]) + " pontos", True, branco)
            janela.blit(pontos, (conteudo_interface_pontuacao))

            dica = fonte_dica.render("Todos os dias", True, branco)
            janela.blit(dica, [conteudo_interface_dica[0], conteudo_interface_dica[1], 366, 192])

            texto_respostas = fonte_fases_corretas.render("1  resposta correta", True, branco)
            janela.blit(texto_respostas, [1013,337])

            pergunta_fase_6_1 = fonte_perguntas.render("Deve-se inspecionar diariamente os pés em busca" , True, preto)
            janela.blit(pergunta_fase_6_1, [250,30])
            pergunta_fase_6_2 = fonte_perguntas.render("de ferimentos com a ajuda de um espelho." , True, preto)
            janela.blit(pergunta_fase_6_2, [250,60])
            pergunta_fase_6_3 = fonte_perguntas.render("Qual opção representa corretamente?" , True, preto)
            janela.blit(pergunta_fase_6_3, [250,110])


            if event.type == pygame.MOUSEBUTTONDOWN:
                if not mouse_pressionado:

                    if botao_proxima_fase.collidepoint(event.pos):

                        fase_6 = False
                        fase_7 = True

                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True
                        aparece_6 = True

                        posicoes_definidas = [False, False, False, False, False, False]

                        tempo_inicial = pygame.time.get_ticks()

                        som_comeco_jogo.play()
                        
                    elif botao_fase_anterior.collidepoint(event.pos):

                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True
                        aparece_6 = True
                        aparece_7 = True
                        aparece_8 = True

                        posicoes_definidas = [False, False, False, False, False, False, False, False]

                        tempo_inicial = pygame.time.get_ticks()

                        fase_5 = True
                        fase_6 = False
                        
                        som_comeco_jogo.play()


                mouse_pressionado = True
            else:
                mouse_pressionado = False


        # conteudo da fase 7
        elif fase_7:

            item_1 = pygame.image.load(Imagens.IMAGEM_POSTO_SAUDE)
            item_2 = pygame.image.load(Imagens.IMAGEM_PROFISSIONAL_SAUDE)
            item_3 = pygame.image.load(Imagens.IMAGEM_POSTO_SAUDE_2)
            item_4 = pygame.image.load(Imagens.IMAGEM_NAO_FAZ_NADA)
            item_5 = pygame.image.load(Imagens.IMAGEM_LIMPEZA)
            item_6 = pygame.image.load(Imagens.IMAGEM_CURATIVO)

            aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6 = andamento_jogo_6(item_1, item_2, item_3, item_4, item_5, item_6, proxima_fase, fase_anterior, aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6)

            tempo_decorrido = contador_de_tempo(tempo_inicial)
            if tempo_decorrido <= 0:

                fase_7 = False
                fase_8 = True

                aparece_1 = True
                aparece_2 = True
                aparece_3 = True
                aparece_4 = True
                aparece_5 = True
                aparece_6 = True

                posicoes_definidas = [False, False, False, False, False, False]

                tempo_inicial = pygame.time.get_ticks()

            n_fase = fonte_n.render("7", True, branco)
            janela.blit(n_fase, [conteudo_interface_fase[0], conteudo_interface_fase[1], 366, 192])

            pontos = fonte_pontuacao.render(str(pontuacao[0]) + " pontos", True, branco)
            janela.blit(pontos, (conteudo_interface_pontuacao))

            dica = fonte_dica.render("Buscar profissionais", True, branco)
            janela.blit(dica, [conteudo_interface_dica[0], conteudo_interface_dica[1], 366, 192])

            texto_respostas = fonte_fases_corretas.render("3  respostas corretas", True, branco)
            janela.blit(texto_respostas, [1013,337])

            pergunta_fase_7_1 = fonte_perguntas.render("Identificando um problema ou alteração nos pés," , True, preto)
            janela.blit(pergunta_fase_7_1, [250,30])
            pergunta_fase_7_2 = fonte_perguntas.render("deve-se procurar a ajuda de um profissional." , True, preto)
            janela.blit(pergunta_fase_7_2, [250,60])
            pergunta_fase_7_3 = fonte_perguntas.render("Quais dessas opções possuem orientações corretas?" , True, preto)
            janela.blit(pergunta_fase_7_3, [250,110])


            if event.type == pygame.MOUSEBUTTONDOWN:
                if not mouse_pressionado:

                    if botao_proxima_fase.collidepoint(event.pos):
                        
                        fase_7 = False
                        fase_8 = True

                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True
                        aparece_6 = True

                        posicoes_definidas = [False, False, False, False, False, False]

                        tempo_inicial = pygame.time.get_ticks()

                        som_comeco_jogo.play()
                        
                    elif botao_fase_anterior.collidepoint(event.pos):

                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True
                        aparece_6 = True
                        aparece_7 = True
                        aparece_8 = True

                        posicoes_definidas = [False, False, False, False, False, False, False, False]

                        tempo_inicial = pygame.time.get_ticks()

                        fase_6 = True
                        fase_7 = False

                        som_comeco_jogo.play()


                mouse_pressionado = True
            else:
                mouse_pressionado = False


        # conteudo da fase 8
        elif fase_8:

            item_1 = pygame.image.load(Imagens.IMAGEM_PES_UMIDOS_1)
            item_2 = pygame.image.load(Imagens.IMAGEM_PES_UMIDOS_2)
            item_3 = pygame.image.load(Imagens.IMAGEM_PES_UMIDOS_3)
            item_4 = pygame.image.load(Imagens.IMAGEM_PES_SECOS_1)
            item_5 = pygame.image.load(Imagens.IMAGEM_PES_SECOS_2)
            item_6 = pygame.image.load(Imagens.IMAGEM_PES_SECOS_3)

            aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6 = andamento_jogo_6(item_1, item_2, item_3, item_4, item_5, item_6, proxima_fase, fase_anterior, aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6)

            tempo_decorrido = contador_de_tempo(tempo_inicial)
            if tempo_decorrido <= 0:

                fase_8 = False
                fase_9 = True

                aparece_1 = True
                aparece_2 = True
                aparece_3 = True
                aparece_4 = True
                aparece_5 = True
                aparece_6 = True

                posicoes_definidas = [False, False, False, False, False, False]

                tempo_inicial = pygame.time.get_ticks()

            n_fase = fonte_n.render("8", True, branco)
            janela.blit(n_fase, [conteudo_interface_fase[0], conteudo_interface_fase[1], 366, 192])

            pontos = fonte_pontuacao.render(str(pontuacao[0]) + " pontos", True, branco)
            janela.blit(pontos, (conteudo_interface_pontuacao))

            dica = fonte_dica.render("Pés molhados", True, branco)
            janela.blit(dica, [conteudo_interface_dica[0], conteudo_interface_dica[1], 366, 192])

            texto_respostas = fonte_fases_corretas.render("3  respostas corretas", True, branco)
            janela.blit(texto_respostas, [1013,337])

            pergunta_fase_8_1 = fonte_perguntas.render("Pés úmidos são a porta principal de entrada" , True, preto)
            janela.blit(pergunta_fase_8_1, [250,30])
            pergunta_fase_8_2 = fonte_perguntas.render("para frieiras e infecções, portanto seque-os bem!" , True, preto)
            janela.blit(pergunta_fase_8_2, [250,60])
            pergunta_fase_8_3 = fonte_perguntas.render("Quais dessas opções não estão secas?" , True, preto)
            janela.blit(pergunta_fase_8_3, [250,110])


            if event.type == pygame.MOUSEBUTTONDOWN:
                if not mouse_pressionado:

                    if botao_proxima_fase.collidepoint(event.pos):

                        fase_8 = False
                        fase_9 = True

                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True
                        aparece_6 = True

                        posicoes_definidas = [False, False, False, False, False, False]

                        tempo_inicial = pygame.time.get_ticks()

                        som_comeco_jogo.play()
                        
                    elif botao_fase_anterior.collidepoint(event.pos):

                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True
                        aparece_6 = True
                        aparece_7 = True
                        aparece_8 = True

                        posicoes_definidas = [False, False, False, False, False, False, False, False]

                        tempo_inicial = pygame.time.get_ticks()

                        fase_7 = True
                        fase_8 = False

                        som_comeco_jogo.play()
    

                mouse_pressionado = True
            else:
                mouse_pressionado = False


        # conteudo da fase 9
        elif fase_9:

            item_1 = pygame.image.load(Imagens.IMAGEM_RELOGIO_17H)
            item_2 = pygame.image.load(Imagens.IMAGEM_RELOGIO_18H)
            item_3 = pygame.image.load(Imagens.IMAGEM_RELOGIO_19H)
            item_4 = pygame.image.load(Imagens.IMAGEM_RELOGIO_8H)
            item_5 = pygame.image.load(Imagens.IMAGEM_RELOGIO_11H)
            item_6 = pygame.image.load(Imagens.IMAGEM_RELOGIO_16H)

            aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6 = andamento_jogo_6(item_1, item_2, item_3, item_4, item_5, item_6, proxima_fase, fase_anterior, aparece_1, aparece_2, aparece_3, aparece_4, aparece_5, aparece_6)

            tempo_decorrido = contador_de_tempo(tempo_inicial)
            if tempo_decorrido <= 0:

                fase_9 = False
                fase_10 = True

                aparece_1 = True
                aparece_2 = True
                aparece_3 = True
                aparece_4 = True

                posicoes_definidas = [False, False, False, False, False, False]

                tempo_inicial = pygame.time.get_ticks()

            n_fase = fonte_n.render("9", True, branco)
            janela.blit(n_fase, [conteudo_interface_fase[0], conteudo_interface_fase[1], 366, 192])

            pontos = fonte_pontuacao.render(str(pontuacao[0]) + " pontos", True, branco)
            janela.blit(pontos, (conteudo_interface_pontuacao))

            dica = fonte_dica.render("Final da tarde", True, branco)
            janela.blit(dica, [conteudo_interface_dica[0], conteudo_interface_dica[1], 366, 192])

            texto_respostas = fonte_fases_corretas.render("3  respostas corretas", True, branco)
            janela.blit(texto_respostas, [1013,337])

            pergunta_fase_9_1 = fonte_perguntas.render("Podemos comprar calçados durante o dia todo," , True, preto)
            janela.blit(pergunta_fase_9_1, [250,30])
            pergunta_fase_9_2 = fonte_perguntas.render("porém o fim da tarde é mais adequado para isso." , True, preto)
            janela.blit(pergunta_fase_9_2, [250,60])
            pergunta_fase_9_3 = fonte_perguntas.render("Quais desses horários são os mais indicados?" , True, preto)
            janela.blit(pergunta_fase_9_3, [250,110])


            if event.type == pygame.MOUSEBUTTONDOWN:
                if not mouse_pressionado:

                    if botao_proxima_fase.collidepoint(event.pos):

                        fase_9 = False
                        fase_10 = True
                        
                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True

                        posicoes_definidas = [False, False, False, False]

                        tempo_inicial = pygame.time.get_ticks()

                        som_comeco_jogo.play()

                    elif botao_fase_anterior.collidepoint(event.pos):

                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True
                        aparece_6 = True
                        aparece_7 = True
                        aparece_8 = True

                        posicoes_definidas = [False, False, False, False, False, False, False, False]

                        tempo_inicial = pygame.time.get_ticks()

                        fase_8 = True
                        fase_9 = False

                        som_comeco_jogo.play()


                mouse_pressionado = True
            else:
                mouse_pressionado = False



        # conteudo da fase 10
        elif fase_10:

            item_1 = pygame.image.load(Imagens.IMAGEM_PES_SENSIVEIS)
            item_2 = pygame.image.load(Imagens.IMAGEM_PES_ULCERAS)
            item_3 = pygame.image.load(Imagens.IMAGEM_PES_PELE_FINA)
            item_4 = pygame.image.load(Imagens.IMAGEM_PES_POUCA_SENSIBILIDADE)

            aparece_1, aparece_2, aparece_3, aparece_4 = andamento_jogo_4(item_1, item_2, item_3, item_4, proxima_fase, fase_anterior, aparece_1, aparece_2, aparece_3, aparece_4)

            tempo_decorrido = contador_de_tempo(tempo_inicial)
            if tempo_decorrido <= 0:

                fase_10 = False
                janela2 = False

                aparece_1 = True
                aparece_2 = True
                aparece_3 = True
                aparece_4 = True
                aparece_5 = True
                aparece_6 = True
                aparece_7 = True
                aparece_8 = True

                posicoes_definidas = [False, False, False, False, False, False, False, False]

                janela3 = True
                

            n_fase = fonte_n.render("10", True, branco)
            janela.blit(n_fase, [conteudo_interface_fase[0], conteudo_interface_fase[1], 366, 192])

            pontos = fonte_pontuacao.render(str(pontuacao[0]) + " pontos", True, branco)
            janela.blit(pontos, (conteudo_interface_pontuacao))

            dica = fonte_dica.render("Fatos válidos", True, branco)
            janela.blit(dica, [conteudo_interface_dica[0], conteudo_interface_dica[1], 366, 192])

            texto_respostas = fonte_fases_corretas.render(" *** SURPRESA ***", True, branco)
            janela.blit(texto_respostas, [1013,337])


            pergunta_fase_10_1 = fonte_perguntas.render("O autocuidado é fundamental no tratamento e na" , True, preto)
            janela.blit(pergunta_fase_10_1, [250,30])
            pergunta_fase_10_2 = fonte_perguntas.render("identificação de feridas em pés por vários motivos." , True, preto)
            janela.blit(pergunta_fase_10_2, [250,60])
            pergunta_fase_10_3 = fonte_perguntas.render("Quais são esses motivos?" , True, preto)
            janela.blit(pergunta_fase_10_3, [250,110])


            if event.type == pygame.MOUSEBUTTONDOWN:
                if not mouse_pressionado:

                    if botao_proxima_fase.collidepoint(event.pos):

                        fase_10 = False
                        janela2 = False
                        janela3 = True

                        posicoes_definidas = [False, False, False, False, False, False, False, False]

                        pygame.mixer.music.stop()
                        musica_fase_finalizada = pygame.mixer.music.load(Audios.MUSICA_FASE_FINALIZADA)#) # tela reforco e qr code
                        pygame.mixer.music.play()

                    elif botao_fase_anterior.collidepoint(event.pos):

                        aparece_1 = True
                        aparece_2 = True
                        aparece_3 = True
                        aparece_4 = True
                        aparece_5 = True
                        aparece_6 = True
                        aparece_7 = True
                        aparece_8 = True

                        posicoes_definidas = [False, False, False, False, False, False, False, False]

                        tempo_inicial = pygame.time.get_ticks()

                        fase_9 = True
                        fase_10 = False

                        som_comeco_jogo.play()


                mouse_pressionado = True
            else:
                mouse_pressionado = False

    # tela de reforço e qr code
    elif janela3:

        janela.fill(azul_2)
        janela.blit(Bloco_de_notas, (-100,45))

        texto_Bloco_de_notas_1 = fonte_reforço_relembrando.render("Relembrando:", True, vermelho_2)
        janela.blit(texto_Bloco_de_notas_1, [340,170])

        texto_Bloco_de_notas_2 = fonte_reforço.render("1- Use sapatos adequados!", True, azul)
        janela.blit(texto_Bloco_de_notas_2, [255,226])

        texto_Bloco_de_notas_3 = fonte_reforço.render("2- Use meias de cores claras!", True, azul)
        janela.blit(texto_Bloco_de_notas_3, [255,265])

        texto_Bloco_de_notas_4 = fonte_reforço.render("3- Use hidratante!", True, azul)
        janela.blit(texto_Bloco_de_notas_4, [255,304])

        texto_Bloco_de_notas_5 = fonte_reforço.render("4- Corte unhas em linha reta!", True, azul)
        janela.blit(texto_Bloco_de_notas_5, [255,342])

        texto_Bloco_de_notas_6 = fonte_reforço.render("5- Lave os pés com água morna!", True, azul)
        janela.blit(texto_Bloco_de_notas_6, [255,376])

        texto_Bloco_de_notas_7 = fonte_reforço.render("6- Cheque seus pés diariamente!", True, azul)
        janela.blit(texto_Bloco_de_notas_7, [255,412])

        texto_Bloco_de_notas_8 = fonte_reforço.render("7- Procure uma Unidade de Saúde!", True, azul)
        janela.blit(texto_Bloco_de_notas_8, [255,452])

        texto_Bloco_de_notas_9 = fonte_reforço.render("8- Seque bem entre os dedos!", True, azul)
        janela.blit(texto_Bloco_de_notas_9, [255,488])

        texto_Bloco_de_notas_10 = fonte_reforço.render("9- Compre sapatos ao final do dia!", True, azul)
        janela.blit(texto_Bloco_de_notas_10, [255,528])

        texto_Bloco_de_notas_11 = fonte_reforço.render("10- Seja cuidadoso(a) com seus pés!", True, azul)
        janela.blit(texto_Bloco_de_notas_11, [244,563])

        texto_qr_CODE = fonte_qr_code.render("Para mais informações acesse", True, vermelho_2)
        janela.blit(texto_qr_CODE, [975,360])
    
        janela.blit(qr_code, (1040,100))
        janela.blit(borda_qr_code, (917,47))
        janela.blit(next, (1065,450))
        janela.blit(logo_medicina, (750,450))


        if pontuacao[0] >= 4000:
            porcentagem_conscientizado = fonte_pontuacao.render("Você foi 100% conscientizado(a)", True, vermelho_2)
            janela.blit(porcentagem_conscientizado,(185,680))
        elif pontuacao[0] >= 2000 and pontuacao[0] < 4000:
            porcentagem_conscientizado = fonte_pontuacao.render("Você foi 50% conscientizado(a)", True, vermelho_2)
            janela.blit(porcentagem_conscientizado,(185,680))
        elif pontuacao[0] >= 1000 and pontuacao[0] < 2000:
            porcentagem_conscientizado = fonte_pontuacao.render("Você foi 25% conscientizado(a)", True, vermelho_2)
            janela.blit(porcentagem_conscientizado,(185,680))
        elif pontuacao[0] >= 500 and pontuacao[0] < 1000:
            porcentagem_conscientizado = fonte_pontuacao.render("Você foi 12% conscientizado(a)", True, vermelho_2)
            janela.blit(porcentagem_conscientizado,(185,680))
        else:
            porcentagem_conscientizado = fonte_pontuacao.render("Jogue novamente com mais atenção!!!", True, vermelho_2)
            janela.blit(porcentagem_conscientizado,(115 ,680))
        

        aparece_1 = True
        aparece_2 = True
        aparece_3 = True
        aparece_4 = True
        aparece_5 = True
        aparece_6 = True
        aparece_7 = True
        aparece_8 = True

        posicoes_definidas = [False, False, False, False, False, False, False, False, False]


        if event.type == pygame.MOUSEBUTTONDOWN:
            if not mouse_pressionado:

                if botao_next.collidepoint(event.pos):
                    janela3 = False
                    janela4 = True
                    pygame.mixer.music.stop()
                    musica_final = pygame.mixer.music.load(Audios.MUSICA_FINAL) # tela creditos
                    pygame.mixer.music.play()

            mouse_pressionado = True
        else:
            mouse_pressionado = False
        

    # tela creditos
    elif janela4:

        janela.fill(preto)   
            
        texto_agradecimento = fonte_agradecimento.render("OBRIGADO POR JOGAR!!" , True, amarelo)
        janela.blit(texto_agradecimento, [240,50])

        titulo_creditos = fonte_creditos.render("CRÉDITOS:" , True, amarelo)
        janela.blit(titulo_creditos, [540,170]) 

        nome_1 = fonte_creditos.render("Eugênio José de Oliveira Silva" , True, amarelo)
        janela.blit(nome_1, [330,250])

        nome_2 = fonte_creditos.render("Richard Pedroso de Souza Filho" , True, amarelo) 
        janela.blit(nome_2, [330,320])

        nome_3 = fonte_creditos.render("Tiago Vilela Cerqueira do Carmo", True, amarelo)
        janela.blit(nome_3, [330,390])

        nome_4 = fonte_creditos.render("Kamila Raele Ribeiro", True, amarelo)
        janela.blit(nome_4, [330,460])

        nome_5 = fonte_creditos.render("Diba Maria Sebba Tosta de Souza", True, amarelo)
        janela.blit(nome_5, [330,530])

        imagem_mario = pygame.image.load(Imagens.MARIO_CREDITOS)
        imagem_mario = pygame.transform.scale(imagem_mario, [480,500])
        janela.blit(imagem_mario, [555,585])

        texto_baseado = fonte_baseado.render("Baseado no personagem Mário da:" , True, amarelo)
        janela.blit(texto_baseado, (15,660))

        janela.blit(nintendo_logo, (55,620))

        janela.blit(volta_inicio, posicao_inicio)


        if event.type == pygame.MOUSEBUTTONDOWN:
            if not mouse_pressionado:

                if botao_voltar_inicio.collidepoint(event.pos):
                    janela4 = False
                    janela3 = False
                    janela2 = False
                    janela1 = True
                    pontuacao[0] = pontuacao_inicial
                    pygame.mixer.music.stop()
                    musica_menu = pygame.mixer.music.load(Audios.MUSICA_MENU) # musica do menu
                    pygame.mixer.music.play()

            mouse_pressionado = True
        else:
            mouse_pressionado = False
    

    # Atualize a janela
    pygame.display.flip()