import PySimpleGUI as sg
from Crypto.PublicKey import RSA
from random import randint
import os

def RSA_generate(bits):
    key = RSA.generate(bits)
    rand = randint(0,999)
    publickey = key.publickey()
    y = str(key.export_key()).replace("\\n","")
    x = str(publickey.export_key()).replace("\\n","")
    print(y)

    
class Tela():
    def __init__(self):
        sg.theme('DarkAmber') 
        layout = [ 
            [sg.Text("nome",size=(5,0)), sg.InputText(key="nome",size=(20,0))],
            #[sg.Text("BITS",size=(5,0)), sg.Input(key="BITS",size=(20,0))],
            [sg.Checkbox("1014",key="BITS_1024"),sg.Checkbox("2048",key="BITS_2048")],
            #[sg.Checkbox("GAY",key="gay"),sg.Checkbox("HOMOSEXUAL",key="gay")],

            #[sg.Radio("SIM", "CARTAO",key="cartao_sim"),sg.Radio("NAO","CARTAO",key="cartao_nao")],
            [sg.Button("jaca",size=(5,0))],
            [sg.Output(size=(60,40))]
        ]

        self.janela = sg.Window("DADOS ").layout(layout)

        self.button, self.values = self.janela.Read()

    def Iniciar(self):
        while True:
            self.button,self.values = self.janela.Read()
            if self.values["BITS_2048"] == False:
                RSA_generate(1024)
            else:
                RSA_generate(2048)
            print(self.values)
            print()
            a=15
            print("-="*a)

tela = Tela()
tela.Iniciar()