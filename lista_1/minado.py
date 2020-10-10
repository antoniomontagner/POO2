# ex 9
# Antonio Silverio Montagner / 19203742
# so isso ta certo ne? falava so para projetar atributos e metodos

import random

class Campo_minado():
    def __init__(self,campo,bombas):
        self.campo = [["-" for x in range(20)] for x in range(20)]
        self.bombas = [[ randint(0,19) for x in range(2)] for x in range(40)]
        for i in range(len(self.bombas)):
            v = 0
            for j in range(len(self.bombas)):
                if self.bombas[i][0] == self.bombas[j][0] and self.bombas[i][1] == self.bombas[j][1]:
                    v+=1
                if v == 2:
                    self.bombas = [[ randint(0,19) for x in range(2)] for x in range(40)]
    
    def play(self): #para jogar
        pass
    
    def mostrar(self): #para mostrar o campo minado
        pass
    
    def jogada(self): #fazer uma jogada
        pass

    def win(self): #verificar de foi acerto ou erro
        pass
