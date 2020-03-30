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
            comando = int(input("""
        pesquisar:
            1- nome
            2- autor
            3- ano
            4- editora
            5- edicao
            6- volume

            0- exit
            """))
            if comando == 1:
                titulo=input("titulo: ")
                for i in self.livros:
                    if i.titulo == titulo:
                        print(i.retornar())

            elif comando == 2:
                autor=input("autor: ")
                for i in self.livros:
                    if i.autor == autor:
                        print(i.retornar())
            elif comando == 3:
                ano=input("ano: ")
                for i in self.livros:
                    if i.ano == ano:
                        print(i.retornar())
            elif comando == 4:
                editora=input("editora: ")
                for i in self.livros:
                    if i.editora == editora:
                        print(i.retornar())
            elif comando == 5:
                edicao=input("edicao: ")
                for i in self.livros:
                    if i.edicao == edicao:
                        print(i.retornar())
            elif comando == 6:
                volume=input("volume: ")
                for i in self.livros:
                    if i.volume == volume:
                        print(i.retornar())
            elif comando == 0:
                break
            else:
                pass
livros = []
while True:
    acao = int(input("""
        comando:
            1- cadastrar livro
            2- pesquisar livro

            0- sair

    """))
    if acao == 1:
        titulo = input("titulo: ")
        autor = input("autor: ")
        ano = input("ano: ")
        editora = input("editora: ")
        edicao = input("edicao: ")
        volume = input("volume: ")
        x = Livro(titulo,autor,ano,editora,edicao,volume)
        livros.append(x)
    elif acao ==2:
        b = Biblioteca(livros)
        b.pesquisar()

    elif acao == 0:
        break

    else:
        pass