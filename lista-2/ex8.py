#8

lista = []
for i in range(5):
    pessoa = []
    pessoa.append(int(input("Idade: ")))
    pessoa.append(float(input("Altura: ")))
    print("#####")
    lista.append(pessoa)

for i in range(len(lista)-1,-1,-1):
    print(f"idade: {lista[i][0]} , altura: {lista[i][1]}")