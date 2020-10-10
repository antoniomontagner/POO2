#A com 10 números inteiros, calculee mostre a soma dos quadrados dos elementos do vetor

#n = 0
#for i in range(10):
#    n += ((int(input(f"{i+1}° Numero: ")))**2)
#print(n)

lista = []
for i in range(10):
    lista.append(int(input(f"{i+1}° Numero inteiro: ")))

soma = 0
for i in lista:
    soma += (i**2)
print(f"a soma dos quadrados dos elementos dados é {soma}")