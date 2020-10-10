# ex 1
# Antonio Silverio Montagner / 19203742


class User():
    def __init__(self,usuarios,senha,conta):
        self.usuarios = usuarios
        self.senha = senha
        self.conta = conta 

class Conta():
    def __init__(self,saldo,vip=False):
        self.saldo = saldo
        self.vip = vip
        self.limite = saldo
        self.poupanca = 0

    def conta_vip(self,poupanca=0,x=False):
        self.vip = x
        if self.vip == True:
            self.limite = self.saldo+(self.saldo*0.1)
            self.poupanca = poupanca
        else:
            pass
    
    def saldo_conta(self):
        if self.vip == True:
            print(f"saldo: {self.saldo} , conta poupanca: {self.poupanca} , limite: {self.limite}")
        else:
            print(f"saldo: {self.saldo}, limite: {self.limite}")
    
    def saque(self,x):
        if self.vip == True:
            s = int(input("sacar: 1-poupanca / 2-conta   :"))
            if s==1:
                if self.poupanca>=x:
                    self.poupanca-=x
                    print(f"{self.poupanca}")
                else:
                    print(f"{self.poupanca}")
                    print("saldo insuficiente")
            elif self.saldo>=x:
                self.limite-=x
                self.saldo-=x
                print(f"{self.saldo}")
        else:
            if self.saldo>=x:
                self.saldo-=x
                print(f"{self.saldo}")
            else:
                print("saldo insuficiente")

    def deposito(self,x):
        if self.vip == True:
            s = int(input("deposito: 1- poupanca \ 2- conta"))
            if s==1:
                self.poupanca+=x
                print(f"{self.poupanca}")
            else:
                self.saldo+=x
                print(f"{self.saldo}")
        else:
            self.saldo+=x
            print(f"{self.saldo}")
banco = []

while True:
    comando = int(input(f"""
        1- Criar usuario
        2- Acessar conta

        0- sair
    """))
    if comando == 1:
        usuario = []
        users=[]
        while True:
            comand = int(input("1- add user \ 2-exit"))
            if comand == 1:
                users.append(input("Digite o usuario: "))
            elif comand == 2:
                break
            else:
                pass
        senha = input("Senha: ")
        valor = int(input("Saldo inicial: "))
        x = User(users,senha,Conta(valor))
        banco.append(x)
        #print(users)
        #print(banco)
    elif comando==2:
        users = input("Digite o usuario: ")
        senha = input("Senha: ")
        acesso = False
        for i in banco:
            for j in i.usuarios:
                if j == users:
                    if i.senha == senha:
                        acesso = True
                
        if acesso == True:
            while True:
                operacao = int(input("""
                operacao:
                    1- adicionar conta vip
                    2- saldo
                    3- saque
                    4- deposito

                    0- sair
                """))
                if operacao == 1:
                    dinheiro_pup = int(input("dinheiro para a poupanca: "))
                    i.conta.conta_vip(dinheiro_pup,True)
                elif operacao == 2:
                    i.conta.saldo_conta()
                elif operacao == 3:
                    x = int(input("Valor que quer sacar: "))
                    i.conta.saque(x)
                elif operacao == 4:
                    x = int(input("Valor que quer depositar:"))
                    i.conta.deposito(x)

                elif operacao == 0:
                    break
                else:
                    pass
    elif comando == 0:
        break
    else:
        pass
            