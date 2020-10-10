from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):

    def __init__(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        self.__andarAtual = andarAtual
        self.__totalAndaresPredio = totalAndaresPredio
        self.__capacidade = capacidade
        self.__totalPessoas = totalPessoas

    # ElevadorJahNoTerreoException
    def descer(self) -> str:
        if self.__andarAtual > 0:
            self.__andarAtual -= 1
        else:
            raise ElevadorJahNoTerreoException
    
    # ElevadorCheioException
    def entraPessoa(self) -> str:
        if self.__totalPessoas < self.__capacidade:
            self.__totalPessoas += 1
        else:
            raise ElevadorCheioException

    # ElevadorJahVazioException
    def saiPessoa(self) -> str:
        if self.__totalPessoas > 0:
            self.__totalPessoas -= 1
        else:
            raise ElevadorJahVazioException
    
    # ElevadorJahNoUltimoAndarException
    def subir(self) -> str:
        if self.__andarAtual < self.__totalAndaresPredio:
            self.__andarAtual += 1        
        else:
            raise ElevadorJahNoUltimoAndarException

    @property
    def capacidade(self) -> int:
        return self.__capacidade
    
    @property
    def totalPessoas(self) -> int:
        return self.__totalPessoas
    
    @property
    def totalAndaresPredio(self) -> int:
        return self.__totalAndaresPredio
    
    @property
    def andarAtual(self) -> int:
        return self.__andarAtual
    
    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade
    
    @totalPessoas.setter
    def totalPessoas(self, totalPessoas: int):
        self.__totalAndaresPredio = totalPessoas
    
    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio: int):
        self.__totalAndaresPredio = totalAndaresPredio

    @andarAtual.setter
    def andarAtual(self, andarAtual: int):
        self.__andarAtual = andar