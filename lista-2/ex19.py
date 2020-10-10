print('"Qual o melhor Sistema Operacional para uso em servidores?"')
print("As possíveis respostas são:")
print("""
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

0-exit:
    """)
lis = []
while True:
    comd = int(input())
    if comd == 0:
        break
    elif 1 <= comd <= 23:
        lis.append(comd)
    elif comd >= 7 or comd < 0:
        print("Informe um valor entre 1 e 6 ou 0 para sair! ")
    else:
        pass
mais = 0
fron = (1, 2, 3, 4, 5, 6)
for i in fron:
    if lis.count(i) > lis.count(mais):
        mais = i
l = ["Windows Server", "Unix", "Linux", "Netware", "Mac Os", "Outro"]
print(f"""
Sistema Operacional     Votos      %
-------------------     -----     ---
Windows Server          {lis.count(1)}          {((lis.count(1))*100)/(len(lis)):.2f}
Unix                    {lis.count(2)}          {((lis.count(2))*100)/(len(lis)):.2f}
Linux                   {lis.count(3)}          {((lis.count(3))*100)/(len(lis)):.2f}
Netware                 {lis.count(4)}          {((lis.count(4))*100)/(len(lis)):.2f}
Mac OS                  {lis.count(5)}          {((lis.count(5))*100)/(len(lis)):.2f}
Outro                   {lis.count(6)}          {((lis.count(6))*100)/(len(lis)):.2f}
-------------------    ------
Total                    {len(lis)}
-------------------
O Sistema Operacional mais votado foi o {l[mais-1]}, com {lis.count(mais)} votos, correspondendo a {((lis.count(mais))*100)/(len(lis)):.2f}% dosvotos.
""")
