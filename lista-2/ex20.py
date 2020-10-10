class MinhaLista:
    def __init__(self):
        self.lista = ()
        self.ord = ()

    def append(self, item):
        self.lista = self.lista + tuple(item, )
        return self.lista

    def remove(self, element):
        self.element = element
        b = ()
        for i in range(len(self.lista)):
            if (self.lista[i] != self.element):
                b = b + (self.lista[i],)
        self.lista = b
        return self.lista

    def sort(self):
        lis = list(self.lista)
        lis.sort()
        self.ord = tuple(lis)
        return self.ord

    def reverse(self):
        lis = list(self.lista)
        lis.sort()
        lis.reverse()
        self.lista = tuple(lis)
        return self.lista

    def pop(self):
        self.lista = self.lista[1:]
        return self.lista


a = MinhaLista()
a.append("a")
print(a.append("b"))
print(a.append("c"))
print(a.remove("a"))
c = MinhaLista()
c.append((1, 4, 2, 3))
print(c.sort())
print(c.reverse())
print(c.append("a"))
print(c.pop())
