# leia 20 números inteiros e armazene-os numvetor. Armazene os números pares no vetor PAR e os números IMPARES no vetorimpar. Imprima os três vetores.
vetor = []
for i in range(20):
    vetor.append(int(input(f"Numero inteiro: ")))
vetor.sort()
par = []
impar = []

for i in vetor:
    if i%2 == 0:
        par.append(i)
    elif i%2 == 1:
        impar.append(i)
    else:
        pass
print("Numeros: ",vetor)
print("Numeros pares: ",par)
print("Numeros impares: ",impar)