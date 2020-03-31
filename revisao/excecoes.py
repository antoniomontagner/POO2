try:
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