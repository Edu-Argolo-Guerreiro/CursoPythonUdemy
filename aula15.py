#aula 15 ----------------------------------------
def soma(*numeros):
    resultado = 1

    for num in numeros:
        resultado += num
    return resultado


x = soma(2,4,6,7)
print(x)