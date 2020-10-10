s = 0
per = ["Telefonou para a vítima?", "Esteve no local do crime?",
       "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
for i in per:
    print(i)
    r = input("Resposta: S/N ").upper()
    if r == "S":
        s += 1

if s == 2:
    print("Suspeita")
elif s == 3 or s == 4:
    print("Cumplice")
elif s == 5:
    print("Assassino")
