#6
alunos = []
for i in range(10):
    notas = 0
    for j in range(4):
        notas += float(input(f"Nota alno {i+1}: "))
    media = (notas/4)
    alunos.append(media)

nota7a10 = 0
for i in alunos:
    if i >= 7 :
        nota7a10+=1
print(f"Numero de alunos com notas maiores ou igual a 7 sao {nota7a10}")