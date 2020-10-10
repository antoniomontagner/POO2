"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

class Ordenacao():

    def __init__(self, array_para_ordenar:[]):
        """Recebe o array com o conteudo a ser ordenado"""
        self.array_para_ordenar = array_para_ordenar
        self.ordem = []
        
    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        for i in range(len(self.array_para_ordenar)):
            numero = self.array_para_ordenar[i]
            for chave, valor in enumerate(self.ordem):
                if numero < valor:
                    self.ordem.insert(chave, numero)
                    break
            else:
                self.ordem.append(numero)

        return self.ordem

    def toString(self):
        """Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
        """
        self.estring = ','.join([str(x) for x in self.ordem])

        return self.estring

x = [9, 0, 5, 2, 10]
z = Ordenacao(x)
z.ordena()
print(z.toString())