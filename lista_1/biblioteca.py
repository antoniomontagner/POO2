#ex 2
# Antonio Silverio Montagner / 19203742

class Livro():
    def __init__(self,titulo,autor,ano,editora,edicao,volume):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.editora = editora
        self.edicao = edicao
        self.volume = volume
    
    def retornar (self):
        return self.titulo,self.autor,self.ano,self.editora,self.edicao,self.volume

class Biblioteca():
    def __init__(self,livros):
        self.livros = livros
    
    def pesquisar(self):
        while True:
            comando = input("""
        pesquisar:
            1- nome
            2- autor
            3- ano
            4- editora
            5- edicao
            6- volume

            0- exit
            """)
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
def gerenciamento():
    lista = []
    while True:
        comando = input("1- adicionar livro 2- buscar livro  0- exit")
        if comando == '1':
            a = input("titulo ")
            b = input("autor ")
            c = input("ano ")
            d = input("editora ")
            e = input("edicao ")
            f = input("volume ")
            add = Livro(a,b,c,d,e,f)
            lista.append(add)
        elif comando == '2':
            play=Biblioteca(lista)
            play.pesquisar()

        elif comando == '0':
            break
        else:
            pass

gerenciamento()