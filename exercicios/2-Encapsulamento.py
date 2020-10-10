class Carro:
    def __init__(self, modelo: str, cor: str, placa: str):
        self.__modelo = modelo
        self.__cor = cor
        self.__placa = placa
        self.__velocidade = 0
    
    @property
    def modelo(self):
        return self.__modelo
    @property 
    def cor(self):
        return self.__cor
    @property
    def placa(self):
        return self.__placa
    @property
    def velocidade(self):
        return self.__velocidade

    @placa.setter
    def placa(self, nova_placa: str):
        self.__placa = nova_placa

    @cor.setter
    def cor(self, nova_cor: str):
        self.__cor = nova_cor

carro1 = Carro("jaca", "azul bebe", "4002 8922")
print(carro1.modelo, carro1.cor, carro1.placa, carro1.velocidade)
carro1.placa = "123213213"
carro1.cor = "teste"
print(carro1.modelo, carro1.cor, carro1.placa, carro1.velocidade)
