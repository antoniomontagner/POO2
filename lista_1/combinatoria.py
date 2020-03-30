from itertools import product

class Permutacao():
    def __init__(self,caract):
        self.caracter = caract

    def perm(self):
        perm_list = list(product(self.caracter, repeat=2))
        return perm_list
x=[0, 1, 2]
y=Permutacao(x)
print(y.perm())