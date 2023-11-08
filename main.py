# Exercício

ponto = int(input(f'Quantos graus está a sua carne? '))

if ponto < 48:
    print('Cozinhar por mais alguns minutos')
elif ponto in range (48, 53):
    print('Selada')
elif ponto in range (54, 59):
    print('Ao ponto para mal')
elif ponto in range (60, 64):
    print('Ao ponto')
elif ponto in range (65, 70):
    print('Ao ponto para bem')
else:
    print('Bem passada')
