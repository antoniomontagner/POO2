"""try:
    a = int(input("N: "))
    if not 1<=a<= 20:
        raise ValueError
    else:
        pass
except ValueError:
    a=0
    print("Jaca")
finally:
    print(a)
"""

lista = []
for i in range(3):
    while True:
        try:
            n = int(input("N: "))
            if n in [1,2]:
                break
            else:
                raise ValueError
        except IndexError:
            pass
        except ValueError:
            # assert n != [1,2], 'sefude' #comentario para quando da erro
            pass
        except (IndexError, ValueError):
            print("JACA")
            pass
        except:     #abrange todas as excecoes< tem que colocar porultimo
            pass
        finally:
            print("bitch")
    lista.append(n)
print(lista)