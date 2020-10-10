temp_mes = []
soma_temp = 0
for i in range(12):
    t = float(input(f"Temperatura mes {i+1}: "))
    soma_temp += t
    temp_mes.append(t)
media_temp = (soma_temp/12)

for i in range(len(temp_mes)):
    if temp_mes[i] > media_temp:
        print(f"Temperatura acima da media: {temp_mes[i]}  do mes {i+1}")
