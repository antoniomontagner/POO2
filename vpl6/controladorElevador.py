from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = None

    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    def subir(self) -> str:
        try:
            self.__elevador.subir()
        except Exception as e:
            print(e)

    def descer(self) -> str:
        try:
            self.__elevador.descer()
        except Exception as e:
            print(e)

    def entraPessoa(self) -> str:
        try:
            self.__elevador.entraPessoa()
        except Exception as e:
            print(e)

    def saiPessoa(self) -> str:
        try:
            self.__elevador.saiPessoa()
        except Exception as e:
            print(e)

    def inicializarElevador(
        self,
        andarAtual: int,
        totalAndaresPredio: int,
        capacidade: int,
        totalPessoas: int,
    ):

        self.__elevador = Elevador(
            andarAtual,
            totalAndaresPredio,
            capacidade,
            totalPessoas,
        )


# a = ControladorElevador()
# a.inicializarElevador(4, 5, 5, 1)
# a.entraPessoa()
# a.subir()
