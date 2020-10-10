from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = None

    """
    Faz o elevador subir um andar. Se jah estiver no ultimo andar, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador 
    @throws ElevadorJahNoUltimoAndarException 
    """

    def subir(self) -> str:
        try:
            self.__elevador.subir()
        except Exception as e:
            print(e)

    """
    Faz o elevador descer um andar. Se jah estiver no terreo, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahNoTerreoException
    """

    def descer(self) -> str:
        try:
            self.__elevador.descer()
        except Exception as e:
            print(e)

    """
    Entra uma pessoa no Elevador. Se nao for possivel permitir a entrada da pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorCheioException
    """

    def entraPessoa(self) -> str:
        try:
            self.__elevador.entraPessoa()
        except Exception as e:
            print(e)

    """
    Sai uma pessoa no Elevador. Se nao for possivel permitir a saida de uma pessoa, dispara excecao
    @return Mensagem informando o que ocorreu com o elevador
    @throws ElevadorJahVazioException
    """

    def saiPessoa(self) -> str:
        try:
            self.__elevador.saiPessoa()
        except Exception as e:
            print(e)

    """
    @return Elevador
    """

    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    @elevador.setter
    def elevador(self, elevador: Elevador):
        if elevador is not None:
            self.__elevador = elevador

    """
    @param andarAtual andar atual do elevador
    @param totalAndaresPredio total de andares do predio
    @param capacidade capacidade maxima do elevador
    @param totalPessoas total de pessoas atual do elevador
    """

    def inicializarElevador(
        self,
        andarAtual: int,
        totalAndaresPredio: int,
        capacidade: int,
        totalPessoas: int,
    ):
        if totalAndaresPredio >= 0 and capacidade >= 0:
            self.__elevador = Elevador(
                andarAtual, totalAndaresPredio, capacidade, totalPessoas
            )
