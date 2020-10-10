lis = []
s = 0
while True:
    n = float(input("Numero: "))
    if n == -1:
        break
    elif n != -1:
        lis.append(n)
        s += n
    else:
        pass

media = (s/(len(lis)))

invert = []
cima = []
baixo = []
for i in range(len(lis)-1, -1, -1):
    invert.append(lis[i])
    if lis[i] < 7:
        baixo.append(lis[i])
    elif lis[i] > media:
        cima.append(lis[i])
    else:
        pass

print(f"""Numero de valores lidos: {len(lis)}

        valores: {lis}

        ordem invertida: {invert}

        soma: {s}

        media: {media}

        quantidade de valores acima da media são {len(cima)} 
                        e foram os elementos: {cima}

        quantidade de valores abaixo de 7 são {len(baixo)} 
                        e foram os elementos: {baixo}

""")

print(" uma mensagem; ")
print("programa encerrado. ")
