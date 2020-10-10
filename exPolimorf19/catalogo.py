from transporte import Transporte
from transporteAereo import TransporteAereo
from transporteTerrestre import TransporteTerrestre
from transporteAquatico import TransporteAquatico


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
                aviao = TransporteAereo()
                aviao.add(q, w, e, r, t, autonomia, envergadura)
                self.veiculos.append(a)
            elif cmd == '2':
                q, w, e, r, t = entrada()
                boca = input("Boca: ")
                calado = float(input("Calado: "))
                barco = TransporteAquatico()
                barco.add(q, w, e, r, t, boca, calado)
                self.veiculos.append(b)
            elif cmd == '3':
                q, w, e, r, t = entrada()
                motor = input("Motor: ")
                rodas = input("Rodas: ")
                carro = TransporteTerrestre()
                carro.add(q, w, e, r, t, motor, rodas)
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
