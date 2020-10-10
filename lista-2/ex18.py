def porc(a, b):
    x = ((lis.count(a))*100)/(len(b))
    return x


print("""Enquete: Quem foi o melhor jogador?
""")
lis = []
while True:
    comd = int(input("Número do jogador de 1 a 23, (0=fim): "))
    if comd == 0:
        break
    elif 1 <= comd <= 23:
        lis.append(comd)
    elif comd >= 24 or comd < 0:
        print("Informe um valor entre 1 e 23 ou 0 para sair! ")
    else:
        pass
print("""
Resultado da votação:
""")

print(f"Foram computados {len(lis)} votos.")

fron = frozenset(lis)
melhor = 0
print("""
    Jogador     Votos       %
""")
for i in fron:
    if lis.count(i) > lis.count(melhor):
        melhor = i
    print(f"""
     {i}             {lis.count(i)}        {porc(i,lis):.2f}
""")

print(f"""
O melhor jogador foi {melhor} com numero de votos {lis.count(melhor)} e porcentagem de {porc(melhor,lis):.2f}
""")
