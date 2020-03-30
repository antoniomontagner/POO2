class Polinomio():
    def __init__(self, n):
        self.coeficiente = n

    def grau(self):
        return len(self.coeficiente) - 1

    def resultado(self, x):
        s = 0
        for (e, c) in enumerate(self.coeficiente):
            s += (c * x ** e ) 
        return s

    def soma(self,p2,x,y): 
        soma = p2.resultado(x) + self.resultado(y)
        return soma
    
    def multi(self,p2,x,y): 
        multi = p2.resultado(x) * self.resultado(y)
        return multi
