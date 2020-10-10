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
    altura: {self.altura}
    comprimento: {self.comprimento}
    carga: {self.carga}
    velocidade: {self.velocidade}
        """)


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
    altura: {self.altura}
    comprimento: {self.comprimento}
    carga: {self.carga}
    velocidade: {self.velocidade}
    autonomia: {self.autonomia}
    envergadura: {self.envergadura}
        """)


class TransporteTerrestre (Transporte):
    def __init__(self):
        self.motor = None
        self.rodas = None

    def add(self, nome: str, altura: float, comprimento: float,
            carga: float, velocidade: float, motor, rodas):
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
    altura: {self.altura}
    comprimento: {self.comprimento}
    carga: {self.carga}
    velocidade: {self.velocidade}
    motor: {self.motor}
    rodas: {self.rodas}
        """)


class TransporteAquatico(Transporte):
    def __init__(self):
        self.boca = None
        self.calado = None

    def add(self, nome: str, altura: float, comprimento: float,
            carga: float, velocidade: float, boca, calado):
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
    altura: {self.altura}
    comprimento: {self.comprimento}
    carga: {self.carga}
    velocidade: {self.velocidade}
    boca: {self.boca}
    calado: {self.calado}
        """)


def entrada():
    a = input("Nome: ")
    b = float(input("Altura: "))
    c = float(input("Comprimento: "))
    d = float(input("Carga: "))
    e = float(input("Velocidade: "))
    return a, b, c, d, e


class Catalogo:
    def __init__(self):
        self.veiculos = []

    def addVeiculo(self):
        while True:
            cmd = input("""
            O veiculo é:
                        1- Aereo
                        2- Aquatico
                        3- Terrestre

                        0- exit
            """)
            if cmd == '1':
                q, w, e, r, t = entrada()
                autonomia = float(input("Autonomia: "))
                envergadura = float(input("Envergadura: "))
                a = TransporteAereo()
                a.add(q, w, e, r, t, autonomia, envergadura)
                self.veiculos.append(a)
            elif cmd == '2':
                q, w, e, r, t = entrada()
                boca = input("Boca: ")
                calado = float(input("Calado: "))
                b = TransporteAquatico()
                b.add(q, w, e, r, t, boca, calado)
                self.veiculos.append(b)
            elif cmd == '3':
                q, w, e, r, t = entrada()
                motor = input("Motor: ")
                rodas = input("Rodas: ")
                c = TransporteTerrestre()
                c.add(q, w, e, r, t, motor, rodas)
                self.veiculos.append(c)
            elif cmd == '0':
                break
            else:
                pass

    def getVeiculo(self):
        for i in self.veiculos:
            i.mostra()


c = Catalogo()
while True:
    cmd = input("""
    1- add veiculo
    2- ver catalogo

    0- exit: """)
    if cmd == '1':
        c.addVeiculo()
    elif cmd == '2':
        c.getVeiculo()
    elif cmd == '0':
        print("VLW PELO APOIO.")
        break
    else:
        print("Comando invalido.")
#
#a = TransporteTerrestre()
#q, w, e, r, t = entrada()
#a.add(q, w, e, r, t, 1, 2)
# a.mostra()
