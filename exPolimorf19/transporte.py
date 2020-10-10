class Transporte():
    def __init__(self):
        self.__nome = None
        self.__altura = None
        self.__comprimento = None
        self.__carga = None
        self.__velocidade = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura: float):
        self.__altura = altura

    @property
    def comprimento(self):
        return self.__comprimento

    @comprimento.setter
    def comprimento(self, comprimento: float):
        self.__comprimento = comprimento

    @property
    def carga(self):
        return self.__carga

    @carga.setter
    def carga(self, carga: float):
        self.__carga = carga

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, velocidade: float):
        self.__velocidade = velocidade

    def add(self, nome: str, altura: float, comprimento: float,
            carga: float, velocidade: float):
        self.nome = nome
        self.altura = altura
        self.comprimento = comprimento
        self.carga = carga
        self.velocidade = velocidade

    def mostra(self):
        print(f"""
    nome: {self.nome}
    altura: {self.altura} m
    comprimento: {self.comprimento} m
    carga: {self.carga} t
    velocidade: {self.velocidade} km/h
        """)
