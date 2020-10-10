# ex 5
# Antonio Silverio Montagner / 19203742

from fractions import Fraction

class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def impime(self):
        print(Fraction(self.numerador, self.denominador))


class Fatorial:
    def __init__(self, numero):
        self.numero = numero

    def fatorial(self):
        def fat(numero):
            if numero == 0 or numero == 1:
                return 1
            else:
                return numero * fat(numero-1)
        return fat(self.numero)


class Combinacao:
    def __init__(self, elementos, posicoes):
        self.elementos = elementos
        self.posicoes = posicoes 
        self.n = len(self.elementos)

    def arranjo(self):
        numerador = Fatorial(self.n).fatorial()
        denominador = Fatorial(self.n - self.posicoes).fatorial()
        fracao = Fracao(numerador, denominador).impime()

    def permutacao(self):
        resultado = Fatorial(self.n).fatorial()
        print(resultado)

    def combinacao(self):
        numerador = Fatorial(self.n).fatorial()
        denominador = Fatorial(self.posicoes).fatorial() * Fatorial(self.n - self.posicoes).fatorial()
        fracao = Fracao(numerador, denominador).impime()

arranjo = Combinacao(['A', 'M', 'O', 'R'], 2)
arranjo.arranjo()