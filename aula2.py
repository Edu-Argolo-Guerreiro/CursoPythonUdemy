'''
Autor: Edu
Data: 27/09/2023
Versão: 1.0
'''
# Comentário

# aula1
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
idade = str(idade)
cidade = input('Onde você mora? ')
texto = f'{nome} tem {idade} anos e mora na cidade de {cidade}.'

print(texto)

#Aula 2
ano_nascimento = input('Em que ano você nasceu? ')

idade = 2023 - int(ano_nascimento)
idade = str(idade)
print('Você tem ' + idade + ' anos.' )

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

#aula 4
valor = 20

if 21 <= valor < 40:
    print('valor permitido')

else:
    print ('valor negado')

#aula 5
for numero in range(1, 21, 3):
    print(numero)

palavra = 'Homem'

for letras in palavra:
    print(f'{letras} é uma letra que pertence a {palavra}')

#aula 6
compra_confirmada = False
detalhe_compra = 'O pagamento da compra foi confirmado'

for enviar in range (3):
    if compra_confirmada:
        print(detalhe_compra)
        print('Mais detalhes no Email')
        break
    else:
        print('pagamento não realizado')
        break

#aula 7
for numero1 in range (1, 6):
    print('produto ' + str(numero1))
    for numero2 in range(5):
        print(numero1, numero2)
palavra = 'pneumoultramicroscopicossilicovulcanoconiótico'

for space in palavra:
    print(f' {space.upper()}', end='')

#aula 8
linhas = 4
colunas = 8
simbolo = '#'

for l in range (linhas):
    for c in range (colunas):
        print(simbolo, end= '')
    print()

#aula 9
valor = 100
dia = 0

while valor >= 20:
    dia += 1
    print(f'No dia {dia} o valor do produto estará em R$ {valor}')
    valor -= 10

#aula 10
idade = 13

resultado = 'Voto permitido' if idade >= 16 else 'Voto não permitido'

print(resultado)

#aula 11
valor = int(input('Qual o valor da sua conta bancaria atualmente em R$: '))

if valor >= 1000:
    valor = (valor * 0.10) + valor
    print(f'Com o acressimo do branco, você terá: R$ {valor}')
else:
    valor_perdendo = int((valor * 0.10))
    print(f'Caso faça algum contato com o banco, você irá perder R$ {valor_perdendo}')
    print(f'Ficando com o saldo atual de R$ {valor - valor_perdendo}')