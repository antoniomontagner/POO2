from transporte import Transporte


class TransporteAereo(Transporte):
    def __init__(self):
        self.envergadura = None
        self.autonomia = None

    def add(self, nome: str, altura: float, comprimento: float,
            carga: float, velocidade: float, autonomia: float, envergadura: float):
        self.nome = nome
        self.altura = altura
        self.comprimento = comprimento
        self.carga = carga
        self.velocidade = velocidade
        self.autonomia = autonomia
        self.envergadura = envergadura

    def mostra(self):
        print(f"""
    nome: {self.nome}
    altura: {self.altura} m
    comprimento: {self.comprimento} m
    carga: {self.carga} t
    velocidade: {self.velocidade} km/h
    autonomia: {self.autonomia} km
    envergadura: {self.envergadura} m
        """)
