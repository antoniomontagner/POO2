#leia 4 notas, mostre as notas e a média na tela
lista = []

for i in range(4):
    lista.append(float(input(f"{i+1}° Nota: ")))

print(lista)

media = 0
for i in range(len(lista)):
    print(f"{i+1}° Nota: {lista[i]} ")
    media += lista[i]
print(f"Média: {media/4}")