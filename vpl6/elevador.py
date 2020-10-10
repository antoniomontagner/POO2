from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(
        self,
        andarAtual: int,
        totalAndaresPredio: int,
        capacidade: int,
        totalPessoas: int,
    ):
        self.__andarAtual = andarAtual
        self.__totalAndaresPredio = totalAndaresPredio
        self.__capacidade = capacidade
        self.__totalPessoas = totalPessoas

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

    # ElevadorCheioException
    def entraPessoa(self) -> str:
        if self.__totalPessoas == self.__capacidade:
            raise ElevadorCheioException
        else:
            self.__totalPessoas += 1
            return 'Entrou uma pessoa!'

    # ElevadorJahVazioException
    def saiPessoa(self) -> str:
        if self.__totalPessoas > 0:
            self.__totalPessoas -= 1
            return" saiu pessoa"
        else:
            raise ElevadorJahVazioException

    # ElevadorJahNoTerreoException
    def descer(self) -> str:
        if self.__andarAtual > 0:
            self.__andarAtual -= 1
            return "desceu"
        else:
            raise ElevadorJahNoTerreoException

    # ElevadorJahNoUltimoAndarException
    def subir(self) -> str:
        if self.__andarAtual < self.__totalAndaresPredio:
            self.__andarAtual += 1
            return "subiu"
        else:
            raise ElevadorJahNoUltimoAndarException