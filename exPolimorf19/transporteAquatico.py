from transporte import Transporte


class TransporteAquatico(Transporte):
    def __init__(self):
        self.boca = None
        self.calado = None

    def add(self, nome: str, altura: float, comprimento: float,
            carga: float, velocidade: float, boca: float, calado: float):
        self.nome = nome
        self.altura = altura
        self.comprimento = comprimento
        self.carga = carga
        self.velocidade = velocidade
        self.boca = boca
        self.calado = calado

    def mostra(self):
        print(f"""
    nome: {self.nome}
    altura: {self.altura} m
    comprimento: {self.comprimento} m
    carga: {self.carga} t
    velocidade: {self.velocidade} km/h
    boca: {self.boca} m
    calado: {self.calado} m
        """)
