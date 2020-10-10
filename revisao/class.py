class Conta():
    nome_banco = "jaca"             #atributo estatico
    __total = 10000                     #  atributos privados "__"
    def __init__ (self, ID, saldo):
        self.__ID = ID                  #  atributos privados, nao acessa fora da classe
        self.saldo = saldo
    def abstrato(self):
        pass                #abstracao para ser preenchida depois

    def saque(self, valor):
        """ Saque caraio"""
        if self.saldo >= valor:
            self.saldo -= valor
            Conta.__total -= valor
            print(self.__ID)
    def deposito(self, valor):
        self.saldo += valor
        Conta.__total += valor
        Conta.__reserva()               #acesso so dentro da classe
    def __reserva():                #metodo estatico
        print(Conta.__total)

    def __str__(self):          #sempre tem que retornar str
        return "str"
    def __add__(self, a):        #quando somar dois ob (a + b) vai automatico aplicar essa funcao
        self.saldo += a.saldo
    # def __sub__ \ __div__\ __mult__   para trabalhar com obj
    
    def __jaca ():
        print("jaca")


a = Conta(123,1000)
b = Conta(2,2000)
a.deposito(2000)
a.saque(1000)
print(a.saldo)
#Conta.reserva()     #so vai ser acessado pela conta 
a+b
print(a.saldo())
print(a.__dict__())           # retorna um dicionario
print(a.saque.__doc__())      #vai retornar o comentario do metodo



class Pai():
    pass
class Filha(Pai):
    pass
class Neta(Filha):
    pass
print(issubclass(Filha,Pai))        #para saber se é subclass
print(callable(Pai))            #para saber se da para chamar diretamente

