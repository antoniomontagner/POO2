# leia um vetor de 10 números reais e mostre-os naordem inversa
lista = []
for i in range(10):
    lista.append(float(input(f"{i+1}° numero: ")))
    
lista.sort()
lista.reverse()

print("lista inversa", lista)