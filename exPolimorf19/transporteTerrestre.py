from transporte import Transporte


class TransporteTerrestre (Transporte):
    def __init__(self):
        self.motor = None
        self.rodas = None

    def add(self, nome: str, altura: float, comprimento: float,
            carga: float, velocidade: float, motor: str, rodas: str):
        self.nome = nome
        self.altura = altura
        self.comprimento = comprimento
        self.carga = carga
        self.velocidade = velocidade
        self.motor = motor
        self.rodas = rodas

    def mostra(self):
        print(f"""
    nome: {self.nome}
    altura: {self.altura} m
    comprimento: {self.comprimento} m
    carga: {self.carga} t
    velocidade: {self.velocidade} km/h
    motor: {self.motor}
    rodas: {self.rodas}
        """)
