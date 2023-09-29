#Aula 3
velocidade = 100
texto = f'Sua velocidade está em {velocidade} km/h'

if velocidade > 110:
    print(texto)
    print('reduza a velocidade')

elif velocidade < 60:
    print(texto)
    print('aumente sua velocidade para 70KM/H')

else:
    print(texto)
    print('velocidade permitida')