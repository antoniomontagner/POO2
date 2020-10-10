#leia um vetor de 5 números inteiros, mostre asoma, a multiplicação e os números.
n = []
soma = 0
multi = 1
for i in range(5):
    x = int(input("Numero: "))
    soma += x
    multi *= x
    n.append(x)

print(f""" 
        os numeros foram {n}
        a soma deles é {soma}
        a multipliçaõ deles é {multi}
""")