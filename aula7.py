#aula 7 ----------------------------------------
for numero1 in range (1, 6):
    print('produto ' + str(numero1))
    for numero2 in range(5):
        print(numero1, numero2)
palavra = 'pneumoultramicroscopicossilicovulcanoconiótico'

for space in palavra:
    print(f' {space.upper()}', end='')