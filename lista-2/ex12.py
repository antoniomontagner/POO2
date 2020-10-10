from random import randint
pessoas = []
soma = 0
for i in range(30):
    aluno = []
    #aluno.append(int(input("Idade: ")))     #usa randint pra nao sofrer
    aluno.append(randint(0,20))
    #a = float(input("Altura: "))            #
    a = randint(0,10)
    soma += a
    aluno.append(a)
    pessoas.append(aluno)

media = soma/30
n = 0
for i in pessoas:
    if i[0] > 13:
        if i[1] < media:
            n += 1
        else:
            pass
    else:
        pass
print(f"numero de alunos om mais de 13 anos possuem altura inferior à média dealtura: {n}")