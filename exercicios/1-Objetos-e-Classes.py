class Geo:
    def __init__(self,nome: str):
        self.nome = nome
    
    def area_quadrado(self, base: float):
        self.base = base
        area = self.base * self.base
        return area
    
    def area_retangulo(self, base: float, altura:float):
        self.base = base
        self.altura = altura
        area = self.base * self.altura
        return area

    def area_triangulo(self, base:float, altura: float):
        self.base = base
        self.altura = altura
        area = (self.base * self.altura)/2
        return area

    def area_circulo(self, raio: float):
        self.raio = raio
        area = 3.14*self.raio
        return area

def main():
    g = ['triangulo', 'circulo', 'retangulo', 'quadrado']
    while True:
        s = input(f"""forma geométrica: {g} 
                            ou exit para sair: """).lower()
        if s == "circulo":
            raio = float(input("raio: "))
            c = Geo('circulo')
            print(c.area_circulo(raio))
        elif s == "triangulo":
            b = float(input("Base: "))
            a = float(input("Altura: "))
            t = Geo('triangulo')
            print(t.area_triangulo(b,a))
        elif s == "retangulo":
            b = float(input("Base: "))
            a = float(input("Altura: "))
            r = Geo("retangulo")
            print(r.area_retangulo(b,a))
        elif s == "quadrado":
            b = float(input("Base: "))
            q = Geo("quadrado")
            print(q.area_quadrado(b))
        elif s == "exit":
            break
        else:
            pass

main()