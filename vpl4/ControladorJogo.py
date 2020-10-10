from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__baralho = []
        self.__personagems = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__personagems

    def inclui_personagem_na_lista(self, energia: int, habilidade: int,
                                   velocidade: int, resistencia: int,
                                   tipo: Tipo) -> Personagem:
        personagem = Personagem(energia, habilidade,
                                velocidade, resistencia, tipo)
        self.__personagems.append(personagem)

        return personagem

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        carta = Carta(personagem)
        self.__baralho.append(carta)
        return carta

    '''
    Inicia o jogo, distribuindo aleatoriamente 5 cartas do baralho
    para cada jogador, a distribuicao nao precisa ser aleatoria

    @param jogador1 Jogador 1
    @param jogador2 Jogador 2
    '''

    def iniciaJogo(self, jogador1: Jogador, jogador2: Jogador):
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2

        # distribuir para jogador 1
        for i in range(0, 5):
            cartaAleatoria = random.randint(0, len(self.__baralho) - 1)
            self.__jogador1.inclui_carta_na_mao(self.__baralho[cartaAleatoria])
            self.__baralho.pop(cartaAleatoria)

        # distribuir para jogador 2
        for j in range(0, 5):
            cartaAleatoria = random.randint(0, len(self.__baralho) - 1)
            self.__jogador1.inclui_carta_na_mao(self.__baralho[cartaAleatoria])
            self.__baralho.pop(cartaAleatoria)

    def jogada(self, mesa: Mesa) -> Jogador:
        totalCarta1 = mesa.carta_jogador1.valor_total_carta()
        totalCarta2 = mesa.carta_jogador2.valor_total_carta()

        # se jogador1 ganhou
        if totalCarta1 > totalCarta2:
            mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)
            mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador2)
            return mesa.jogador1

        # se jogador2 ganhou
        elif totalCarta2 > totalCarta1:
            mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador1)
            mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
            return mesa.jogador2

        # se houver empate
        else:
            mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)
            mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
            return None
