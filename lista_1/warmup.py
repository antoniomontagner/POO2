# ex1 
class Televisao():
    def __init__(self):
        self.ligada = False
        self.canal = 2
# ex2 
class Televisao():
    def __init__(self,tamanho,marca):
        self.ligada = False
        self.canal = 2
        self.tamanho = tamanho
        self.marca = marca

tv1 = Televisao(40,"LG")
tv2 = Televisao(45,"SANSUNG")
print(tv1.tamanho,tv1.marca)
print(tv2.tamanho,tv2.marca)

#3
class Televisao():
    def __init__(self,tamanho,marca):
        self.ligada = False
        self.canal = 2
        self.tamanho = tamanho
        self.marca = marca

    def muda_canal_para_cima(self):
        self.canal+=1

    def muda_canal_para_baixo(self):
        self.canal-=1
        
#4 
class Televisao():
    def __init__(self,tamanho,marca):
        self.ligada = False
        self.canal = 2
        self.tamanho = tamanho
        self.marca = marca
        self.canal_minimo = 1
        self.canal_maximo = 99

    def muda_canal_para_cima(self):
        if self.canal == self.canal_maximo:
            self.canal = 1
        else:
            self.canal+=1

    def muda_canal_para_baixo(self):
        if self.canal == self.canal_minimo:
            self.canal =99
        else:
            self.canal-=1

#5
class Televisao():
    def __init__(self,tamanho,marca,canal_minimo=2,canal_maximo=14):
        self.ligada = False
        self.canal = 2
        self.tamanho = tamanho
        self.marca = marca
        self.canal_minimo = canal_minimo
        self.canal_maximo = canal_maximo

    def muda_canal_para_cima(self):
        if self.canal == self.canal_maximo:
            self.canal = self.canal_minimo
        else:
            self.canal+=1

    def muda_canal_para_baixo(self):
        if self.canal == self.canal_minimo:
            self.canal = self.canal_maximo
        else:
            self.canal-=1

#6
class Televisao():
    def __init__(self,tamanho,marca,canal_minimo=2,canal_maximo=14):
        self.ligada = False
        self.canal = 2
        self.tamanho = tamanho
        self.marca = marca
        self.canal_minimo = canal_minimo
        self.canal_maximo = canal_maximo

    def muda_canal_para_cima(self):
        if self.canal == self.canal_maximo:
            self.canal = self.canal_minimo
        else:
            self.canal+=1

    def muda_canal_para_baixo(self):
        if self.canal == self.canal_minimo:
            self.canal = self.canal_maximo
        else:
            self.canal-=1

tv1 = Televisao(25,"LG",canal_minimo=11,canal_maximo=78)
tv2 = Televisao(52,"SANSUNG",canal_minimo=4,canal_maximo=44)

#7
class Cidade():
    def __init__(self,pop,nome):
        self.nome = nome
        self.pop = pop
    
class Estado():
    def __init__(self,nome_est,sigla,citys):
        self.nome_est = nome_est
        self.sigla = sigla
        self.citys = citys
    def pop(self):
        self.pop = 0
        for i in self.citys:
            self.pop += i.pop
        return self.pop

a1 = Cidade(200,"a1")
a2 = Cidade(400,"a2")
a3 = Cidade(500,"a3")

c1 = Cidade(500,"c1")
c2 = Cidade(12000,"c2")
c3 = Cidade(3000,"c3")

est1 = Estado("jaca","jc",[a1,a2,a3])
est2 = Estado("est2","s2",[c1,c2,c3])
print(est1.pop())
print(est2.pop())

#8 lasse Coordenada
import math

class Coordenada():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def coordenada(self):
        return (f"{self.x},{self.y}")
    
    def distancia(self,xy):
        self.dist = 0
        a = (xy.x - self.x)**2
        b = (xy.y - self.y)**2
        self.dist = (a + b)**(1/2)
        return self.dist

    def comp(self,xy):
        return (f"""
        coordenada x : {self.x} e {xy.x} 
        coordenada y : {self.y} e {xy.y} """)

    def polar(self):
        r = 6371.0
        xp = math.cos(self.x/r)
        yp = math.sin(self.y/r)
        return (f"{xp}, {yp}")

#9
class Quadrado():
    def __init__(self,base,altura):
        self.base = base
    def quad(self):
        self.area = self.base**2
        return self.area

class Retangulo():
    def __init__(self,x,y,z):
        self.largura = x
        self.altura = y
    def ret(self):
        self.area = self.altura*self.largura
        return self.area

class Circulo():
    def __ini__(self,r):
        self.raio = r
    def cir(self):
        self.area = (self.raio**2)*3.14
        return self.area

#10 classe Fracao
class Fracao():
    def __init__(self,n1,n2):
        self.numerador = n1
        self.denominador = n2
        self.fracion = n1/n2
    
    def soma(self,x):
        self.soma = self.fracion + x.fracion
        return self.soma

    def subtracao(self,x):
        self.sub = self.fracion - x.fracion
        return self.sub
    
    def multiplicacao(self,x):
        self.mult = self.fracion * x.fracion
        return self.mult

    def divisao (self,x):
        self.div = self.fracion / x.fracion
        return self.div
    
    def div_n1_n2(self,x):
        self.num = self.numerador*x.numerador
        self.den = self.denominador*x.denominador
        print(f"{self.num}/{self.den}")

    def invert_fracao (self):
        self.reverse = self.denominador / self.numerador
        return self.reverse

    def real(self):
        self.real = self.numerador/self.denominador
        return self.real
    
    def n1_n1(self,n):
        self.numer
    
    def to_int(self,x):
        self.numerador = 0
        self.denominador = 0
        for i in range(2,999):
            if x%i == 0:
                self.numerador = x*i
                self.denominador= i
                return f"{self.numerador}/{self.denominador}"


#2 biblioteca


#3 polinomio


#4 fibonati
