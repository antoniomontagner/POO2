class Atleta:
    def __init__(self, nome, d):
        self.nome = nome
        self.d


dis = []
while True:
    add = input("Adicionar atleta? S/N").upper()
    if add == "S":
        d = []
        for i in range(5):
            d.append(float(input(f"Distancia {i+1}: ")))
        nome = input("Nome: ")
        dis.append(Atleta(nome, d))
    elif add == "N":
        break
    else:
        pass
