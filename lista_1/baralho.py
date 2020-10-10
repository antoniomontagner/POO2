#6 
# Antonio Silverio Montagner / 19203742

import random

class Baralho:
    def __init__(self):
        self.cards = []
        self.tipo_baralho = 52
        naipe = ["copas", "paus", "espadas", "ouros"]
        n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Q", "J", "K"]
        for i in n:
            for j in naipe:
                self.cards.append([i,j])
    def getBaralho(self):
        print(self.cards)

class Gamer(Baralho):
    def __init__(self,n_cartas):
        super().__init__()
        self.mao = []
        self.n_cartas = n_cartas

    def rodada (self, n_jogador, n_cartas):
        self.n_jogador = n_jogador
        self.n_cartas = n_cartas
        self.mesa_jogadores = []
        for j in range(self.n_jogador):
            self.mao_jogador = []
            for i in range(self.n_cartas):
                a = random.choice(self.cards)
                self.mao_jogador.append(a)
            self.mesa_jogadores.append(self.mao_jogador)


#b = Baralho()
#g = Gamer(b)
#g.rodada(4,4)
#print(g.mesa_jogadores)