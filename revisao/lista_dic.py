"""grupo = []
pessoa = {}
for i in range(4):
    pessoa.clear()
    pessoa["nome"] = input("nome: ")
    pessoa["idade"] = int(input("idade: "))
    grupo.append(pessoa.copy())
print(grupo)

for i in grupo:
    if i["nome"]=="a":
        print(i)"""
class Jaca():
    def __init__(self,a,b):
        self.a=a
        self.b=b

class Gay(Jaca):
    def __init__(self,a,b):
        super().__init__(a,b)
x = Gay(1,2)
print(x.a,x.b)
class X(Jaca):
    def __init__(self, a, b):
        super().__init__(a, b)
        