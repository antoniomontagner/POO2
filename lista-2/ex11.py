a = []
b = []
c = []
d = []
for i in range(10):
    a.append(input(f"{i+1}° elemento de A: "))
for i in range(10):
    b.append(input(f"{i+1}° elemento de B: "))
for i in range(10):
    c.append(input(f"{i+1}° elemento de C: "))

for x,y,z in zip(a,b,c):
    d.append(x)
    d.append(y)
    d.append(z)

print(f"Lista intercalada {d}")