# Exercício
 
altura = float(input('Qual a sua altura em cm? '))
peso = float(input('Qual é o seu peso em kg: '))
imc = peso / (altura / 100) ** 2
imc = round(imc, 2)

if imc < 18.5:
    print(f'Seu IMC é {imc} = Magreza')
elif imc > 18.5 and imc < 25:
    print(f'Seu IMC é {imc} = Normal')
elif imc > 25 and imc < 30:
    print(f'Seu IMC é {imc} = Sobrepeso')
elif imc > 30 and imc < 40:
    print(f'Seu IMC é {imc} = Obesidade')
else:
     print(f'Seu IMC é {imc} = Obesidade Grave')

#Menor que 18,5 Magreza
#Entre 18,5 e 24,9 normal
#Entre 25 e 29,9 Sobrepeso
#Entre 30 e 39,9 Obesidade
#Maior que 40 Obesidade Grave