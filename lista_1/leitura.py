#import biblioteca
# Antonio Silverio Montagner / 19203742

class User:
    def __init__(self,nome,senha):
        self.nome = nome
        self.senha = senha
        self.lendo = False

    def userLendo(self):
        self.lendo = True
        print(self.nome," esta lendo")

    def userNaoLendo(self):
        self.lendo = False
        print(self.nome, " não esta lendo")

class Livro:
    def __init__(self,titulo,autor,ano,editora,edicao,volume):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.editora = editora
        self.edicao = edicao
        self.volume = volume
    
    def retornar (self):
        return self.titulo,self.autor,self.ano,self.editora,self.edicao,self.volume

class Biblioteca:
    def __init__(self):
        self.livros = []
    
    def pesquisar(self):
        while True:
            comando = input("""
                #############################
                #                           #
                #    pesquisar:             #
                #        1- nome            #
                #        2- autor           #
                #        3- ano             #
                #        4- editora         #
                #        5- edicao          #
                #        6- volume          #
                #                           #
                #        0- exit            #
                #                           #
                #############################
                                Resposta: """)
            if comando == '1':
                titulo=input("titulo: ")
                for i in self.livros:
                    if i.titulo == titulo:
                        print(i.retornar())

            elif comando == '2':
                autor=input("autor: ")
                for i in self.livros:
                    if i.autor == autor:
                        print(i.retornar())
            elif comando == '3':
                ano=input("ano: ")
                for i in self.livros:
                    if i.ano == ano:
                        print(i.retornar())
            elif comando == '4':
                editora=input("editora: ")
                for i in self.livros:
                    if i.editora == editora:
                        print(i.retornar())
            elif comando == '5':
                edicao=input("edicao: ")
                for i in self.livros:
                    if i.edicao == edicao:
                        print(i.retornar())
            elif comando == '6':
                volume=input("volume: ")
                for i in self.livros:
                    if i.volume == volume:
                        print(i.retornar())
            elif comando == '0':
                break
            else:
                pass

    def gerenciamento(self,s):
        self.s = s
        while True:
            comando = input("""
                    ####################################
                    #                                  #
                    #        1- adicionar livro        #
                    #        2- buscar livro           #
                    #                                  #
                    #        0- exit                   #
                    #                                  #
                    ####################################
                                        Resposta: """)
            if comando == '1':
                a = input("titulo ")
                b = input("autor ")
                c = input("ano ")
                d = input("editora ")
                e = input("edicao ")
                f = input("volume ")
                add = Livro(a,b,c,d,e,f)
                self.livros.append(add)
            elif comando == '2':
                self.pesquisar()
            elif comando == '0':
                break
            else:
                pass

class Sistema:
    def __init__(self,s):
        self.s = s
        self.usuarios_sistema = []
        self.livros = ''
    
    def addUser(self):
        while True:
            comand = int(input("1- add user \ 2-exit"))
            nome = ''
            if comand == 1:
                nome = (input("""
                                Digite o usuario: 
                                """))
            elif comand == 2:
                break
            else:
                pass
            senha = input("""
                                Senha: 
                                """)
            a = User(nome,senha)
        self.usuarios_sistema.append(a)
    
    def gerenciar(self):
        while True:
            com = input(""" 
                    #####################################
                    #                                   #
                    #        1- adicioar usuario        #
                    #        2- fazer login             #
                    #                                   #
                    #        0- exit                    # 
                    #                                   #
                    #####################################

                                Respost: """)
                        
            if com == "1":
                self.addUser()
            elif com =="2":
                for i in self.usuarios_sistema:
                    login = input("""
                                Nome: 
                                """)
                    senha = input("""
                                Senha: 
                                """)
                    if i.nome == login and i.senha == senha:
                        x = Biblioteca()
                        x.gerenciamento(1)
                        cc = input("""
                          =============================
                          =  Esta lendo livro? S/N    =
                          =============================
                            """).upper()
                        if cc == "S":
                            i.userLendo()
                        elif cc == "N":
                            i.userNaoLendo()
                        else:
                            pass
                    else:
                        print(" Erro! ")
                        pass

            elif com == "0":
                break
            else:
                pass

s = Sistema(1)
s.gerenciar()
                    