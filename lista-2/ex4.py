#leia um vetor de 10 caracteres, e diga quantasconsoantes foram lidas. Imprima as consoantes.
lista = []
for i in range(10):
    lista.append(input(f"{i+1} caracter: ").lower())

consoantes = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
list_conso = []
for i in lista:
    if i in consoantes:
        list_conso.append(i)

print(f"Numero de consoantes {len(list_conso)}")
print(f"As consoantes foram {list_conso}")