class Vendedor:
    def __init__(self, vendas):
        self.vendas = vendas
        self.salario = 200 + (0.09 * self.vendas)


vendedores = []

while True:
    add = input("""
                    adicionar vendedor: 1    
                                    exit: 0 
                                            """)
    if add == '1':
        valor = float(input("Valor das vendas da semana: "))
        vendedores.append((Vendedor(valor)))

    elif add == '0':
        break

    else:
        pass
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
x = 0
for i in vendedores:
    if 200 <= i.salario <= 299:
        a += 1
    elif 300 <= i.salario <= 399:
        b += 1
    elif 400 <= i.salario <= 499:
        c += 1
    elif 500 <= i.salario <= 599:
        d += 1
    elif 600 <= i.salario <= 699:
        e += 1
    elif 700 <= i.salario <= 799:
        f += 1
    elif 800 <= i.salario <= 899:
        g += 1
    elif 900 <= i.salario <= 999:
        h += 1
    elif 1000 <= i.salario:
        x += 1
    else:
        pass

print(f""" 

R$200 - R$299       {a}
R$300 - R$399       {b}
R$400 - R$499       {c}
R$500 - R$599       {d}
R$600 - R$699       {e}
R$700 - R$799       {f}
R$800 - R$899       {g}
R$900 - R$999       {h}
R$1000 em diante    {x}

""")
