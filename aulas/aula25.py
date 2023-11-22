#aula 25 ----------------------------------------

lista1 = [1, 2, 3, 4]


def mult(x):
    return x * 2


lista2 = map(mult, lista1)
print(list(lista2))