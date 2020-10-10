#leia dois vetores com 10 elementos cada. Gereum terceiro vetor de 20 elementos, cujos valores deverão ser compostos peloselementos intercalados
a = []
b = []
c = []
for i in range(10):
    a.append(input(f"{i+1}° elemento de A: "))
for i in range(10):
    b.append(input(f"{i+1}° elemento de B: "))

for x,y in zip(a,b):
    c.append(x)
    c.append(y)

print(f"Lista intercalada {c}")