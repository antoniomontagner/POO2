# ex 3
# Antonio Silverio Montagner / 19203742

class Polinomio():
    def __init__(self, n:list):
        self.coeficiente = n

    def grau(self):
        x = self.coeficiente
        grau = 0
        for i in x[0]:
            if i > grau:
                grau = i
        print ('grau',grau)

    def resultado(self, x):
        self.polinomios = x
        s = 0
        for i in range(len(self.polinomios[0])):
            s+= (self.polinomios[1][i]*(self.polinomios[2]**self.polinomios[0][i])) 
        print('resultado',s)

    def soma(self,x):
        self.x = x
        for i in range(len(self.x[0])): # [ ["Coe"], [ "c"], self.x]
            for j in range(len(self.coeficiente[0])):
                if self.x[0][i] == self.coeficiente[0][j]:
                    self.coeficiente[1][j] += self.x[1][i]
                elif self.x[0][i] not in self.coeficiente[0]:
                    self.coeficiente[0].append(self.x[0][i])
                    self.coeficiente[1].append(self.x[1][i])
        print(self.coeficiente[1])
    
    def multi(self,x):
        self.x = x
        for i in range(len(self.x[0])):
            for i in range(len(self.coeficiente[0])):
                print(i, self.coeficiente[0][i], self.x[0][i])
                self.coeficiente[0][i] += self.x[0][i]
                self.coeficiente[1][i] *= self.x[1][i]
        print(self.coeficiente)

def poli():
    L = []
    coe = []
    c = []
    while True:
            add = input("adicionar (cX^n)?  S/N").upper()
            if add == 'S':
                N = int(input("coeficiente n (cX^n): "))
                C = float(input("valor de c  (cX^n): "))
                c.append(C)
                coe.append(N)
            elif add == 'N':
                break
            else:
                pass
    x = float (input("valor de um x para o polinomio : "))
    L.append(coe)
    L.append(c)
    L.append(x)
    return L


while True:
    comando = input(""" 
            1 - consultar grau  
            2 - resultado para um valor de x
            3 - somar polinomios
            4 - multiplicar polinomios

            0- exit
    """)
    if comando == '1':
        x = Polinomio(poli()).grau()
    elif comando == '2':
        x = Polinomio(poli())
        x.resultado(x.coeficiente)
    elif comando =='3':
        x = Polinomio(poli())
        y = Polinomio(poli())
        y.soma(x.coeficiente)
    elif comando == '4':
        x = Polinomio(poli())
        y = Polinomio(poli())
        y.multi(x.coeficiente)
    elif comando == '0':
        break
    else:
        pass