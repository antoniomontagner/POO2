#ex 8
# Antonio Silverio Montagner / 19203742

import os
from random import randint
import string
import random
class Drow():
    def __init__ (self,x,y):
        self.x = x
        self.y = y

    def forca(self): #imprimir um desenho no terminal
        if self.x == 0:
            print("------------")
            print("|          |")
            print("|          ")
            print("|          ")
            print("|          ")
            print("|          ")
            print("|          ")
            print("|")
            print(self.y)
            print("-="*20)
        elif self.x == 1:
            print("------------")
            print("|          |")
            print("|          0")
            print("|          ")
            print("|          ")
            print("|          ")
            print("|          ")
            print("|")
            print(self.y)
            print("-="*20)
        elif self.x == 2:
            print("------------")
            print("|          |")
            print("|          0")
            print("|          |")
            print("|          ")
            print("|          ")
            print("|          ")
            print("|")
            print(self.y)
            print("-="*20)
        elif self.x == 3:
            print("------------")
            print("|          |")
            print("|          0")
            print("|         -|")
            print("|          ")
            print("|          ")
            print("|          ")
            print("|")
            print(self.y)
            print("-="*20)
        elif self.x == 4:
            print("------------    ")
            print("|          |    ")
            print("|          0    ")
            print("|         -|-   ")
            print("|               ")
            print("|               ")
            print("|               ")
            print("|")
            print(self.y)
            print("-="*20)
        elif self.x == 5:
            print("------------    ")
            print("|          |    ")
            print("|          0    ")
            print("|         -|-   ")
            print("|         /      ")
            print("|               ")
            print("|               ")
            print("|")
            print(self.y)
            print("-="*20)
        elif self.x == 6:
            print("------------    ")
            print("|          |    ")
            print("|          0    ")
            print("|         -|-   ")
            print("|         / \\    ")
            print("|               ")
            print("|    Lamento! Perdeu! ")
            print("|")
            print(self.y)
            print("-="*20)
class Play():
    def __init__(self,str):
        self.str = str

    def game(self):  # def principal com a longica
        chave = []
        resposta = []
        for i in range(len(self.str)):   #converter a str em uma lista de letras e uma de "_"
            chave.append(self.str[i])
            resposta.append("_")

        vida = 0  #contador de vidas, vai ate 6
        win = False     #flag de vitoria
        while win == False:
            flag = False    #flag de erro ou acerto
            letra = input("Letra: ").upper()

            for i in range(len(chave)):     #verifica se o input esta na lista
                if letra == chave[i]:
                    resposta[i] = letra
                    flag = True

            win = True
            for i in range(0,len(resposta)):    #verifica se ainda falta letras a serem descobertas
                if resposta[i] == "_":
                    win = False 

            if win==False:  #verifica se teve um acerto ou um erro para contar uma vida
                if flag == False:
                    vida+=1
                    if vida == 6: #verificar se morreu
                        print(f"A palavra era: {chave}")
                        forca = Drow(vida,resposta)
                        forca.forca()
                        break
                    else:
                        forca = Drow(vida,resposta)
                        forca.forca()
                else:
                    forca = Drow(vida,resposta)
                    forca.forca()
            elif win==True: #verificar se venceu
                print("PARABENS!! Voce acertou!! ")
                forca = Drow(vida,resposta)
                forca.forca()
while True:
    opcao = int(input("""
        OPCOES:
                1: Palavra aleatoria
                2: Jogar com o amiguinho
                3: Escolher uma fruta
                4: Sair
                : """))
    if opcao == 1:
        def generator(s,chars=string.ascii_uppercase):  #gerar uma str aleatoria
            return ''.join(random.choice(chars) for i in range(s))
            
        tamanho = int(input("Digite o numero de caracteres da palavra: "))
        palavra = generator(tamanho)
        play = Play(palavra)
        play.game()

    elif opcao == 2:  # o jogo dependo de um input
        palavra = input("Digite a palavra: ").upper().replace(" ","")
        play = Play(palavra)
        play.game()

    elif opcao == 3:
        x = open("Frutas.txt","r")
        z = []
        for i in x:
            a = i.replace("\n","")
            z.append(a)
        palavra = (z[randint(0,len(z))])
        play = Play(palavra)
        play.game()
    
    elif opcao == 4:
        print("Obrigado.")
        break
    else:
        pass