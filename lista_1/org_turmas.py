#10
# Antonio Silverio Montagner / 19203742

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    def retutn_nome(self):
        return self.nome
    def retutn_dados(self):
        print(f"""
            Nome: {self.nome}
            CPF: {self.cpf}
        """)

class sala:
    def __init__(self, turma_id, prof, alunos_sala):
        self.turma_id = turma_id
        self.prof = prof
        self.alunos_sala = alunos_sala
        self.dicio = {}
        self.P_Aluno = []
        self.notas_alunos = []
    
    def R_Prof(self):
        self.prof.retutn_dados()

    def mudar_nota(self, nomeAluno, nota):
        s = "n"
        for i in self.alunos_sala:
            if i.retutn_nome() == nomeAluno:
                self.dicio["nota"] = nota
                self.dicio["aluno"] = i
                self.notas_alunos.append(self.dicio.copy())
                self.dicio.clear()
                s = "s"
                break
        
        if s == "n":
            print("Aluno não encontrado")
        else:
            print("Atualizado! ")
    
    def addP_Aluno(self, nomeAluno, diaP_Aluno):
        s = "n"
        for i in self.alunos_sala:
            if i.retutn_nome() == nomeAluno:
                self.dicio["aluno"] = i
                self.dicio["diaP_Aluno"] = diaP_Aluno
                self.P_Aluno.append(self.dicio.copy())
                self.dicio.clear()
                s = "s"
                break
        if s == "n":
            print("Aluno não encontrado")
        else:
            print("Atualizado! ")

    def R_AlunosData(self):
        for i in self.alunos_sala:
            print(f"Nome: {i.retutn_nome()}")
            print("Notas: ")
            for j in self.notas_alunos:
                if j["aluno"] == i:
                    print(j["nota"])
            print("Presença: ")
            for k in self.P_Aluno:
                if k["aluno"] == i:
                    print(k["diaP_Aluno"])
            print()
    
    def R_Aluno(self, aluno):
        for i in self.alunos_sala:
            if i == aluno:
                print(f"Nome: {i.retutn_nome()}")
                print("Notas: ")
                for j in self.notas_alunos:
                    if j["aluno"] == i:
                        print(j["nota"])
                print("Presença: ")
                for k in self.P_Aluno:
                    if k["aluno"] == i:
                        print(k["diaP_Aluno"])

class Usuario:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
    def R_Prof_sala(self, sala):
        sala.R_Prof()
    def R_Alunos_sala(self, sala):
        sala.R_AlunosData()
    def R_Aluno_sala(self, sala, aluno):
        sala.R_Aluno(aluno)

#aluno1 = Pessoa("aluno1", 123)
#prof = Pessoa("prof", 123)
#poo2 = sala(2, prof, [aluno1])
#poo2.mudar_nota("aluno1", 10)
#poo2.addP_Aluno("aluno1", "01/01")
#usuario = Usuario("teste", 123)
#usuario.R_Prof_sala(poo2)
#usuario.R_Aluno_sala(poo2, aluno1)
#