'''
Autor: Edu
Data: 27/09/2023
Versão: 1.0
'''
# Comentário

# aula1 ----------------------------------------
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
idade = str(idade)
cidade = input('Onde você mora? ')
texto = f'{nome} tem {idade} anos e mora na cidade de {cidade}.'

print(texto)

#Aula 2 ----------------------------------------
ano_nascimento = input('Em que ano você nasceu? ')

idade = 2023 - int(ano_nascimento)
idade = str(idade)
print('Você tem ' + idade + ' anos.' )

#aula 5 ----------------------------------------
for numero in range(1, 21, 3):
    print(numero)

palavra = 'Homem'

for letras in palavra:
    print(f'{letras} é uma letra que pertence a {palavra}')

#aula 6 ----------------------------------------
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

#aula 7 ----------------------------------------
for numero1 in range (1, 6):
    print('produto ' + str(numero1))
    for numero2 in range(5):
        print(numero1, numero2)
palavra = 'pneumoultramicroscopicossilicovulcanoconiótico'

for space in palavra:
    print(f' {space.upper()}', end='')

#aula 8 ----------------------------------------
linhas = 4
colunas = 8
simbolo = '#'

for l in range (linhas):
    for c in range (colunas):
        print(simbolo, end= '')
    print()

#aula 9 ----------------------------------------
valor = 100
dia = 0

while valor >= 20:
    dia += 1
    print(f'No dia {dia} o valor do produto estará em R$ {valor}')
    valor -= 10

#aula 10 ----------------------------------------
idade = 13

resultado = 'Voto permitido' if idade >= 16 else 'Voto não permitido'

print(resultado)

#aula 11 ----------------------------------------
valor = int(input('Qual o valor da sua conta bancaria atualmente em R$: '))

if valor >= 1000:
    valor = (valor * 0.10) + valor
    print(f'Com o acressimo do branco, você terá: R$ {valor}')
else:
    valor_perdendo = int((valor * 0.10))
    print(f'Caso faça algum contato com o banco, você irá perder R$ {valor_perdendo}')
    print(f'Ficando com o saldo atual de R$ {valor - valor_perdendo}')

#aula 12 ----------------------------------------
def funcao():
    numero1 = 5
    numero2 = 10
    result = numero1 + numero2
    print(result)
    print('Olá, eu sou a função!')


funcao()

def funcao1():
    numero1 = 5
    numero2 = 15
    result = numero1 + numero2
    print(result)
    print('Prazer em te conhecer!')


funcao1()

#aula 13 ----------------------------------------
def ola(nomes, quantidade):
    print(f'Olá, {nomes}!')
    print(f'Temos {str(quantidade)} laptops em estoque!')


ola('Marcos', 5)
ola('Joana', 4)
ola('Laís', 3)

#aula 14 ----------------------------------------
def cliente(nome):
    print(f'Bem-vindo, {nome}!')

def cliente1(nome):
    return (f'Bem-vindo, {nome}!')


x = cliente('Maria')
y = cliente1('Edu Guerreiro')
print(x, y)

#aula 15 ----------------------------------------
def soma(*numeros):
    resultado = 1
    
    for num in numeros:
        resultado += num
    return resultado


x = soma(2,4,6,7)
print(x)

#aula 16 ----------------------------------------
def agencia(**carro):
    return carro

print(agencia(marca = 'BMW', cor = 'azul', placa = '162123', motor = 2.0))
print(agencia(marca = 'BMW', cor = 'preto', motor = 2.0))
print(agencia(marca = 'GOL', cor = 'azul', placa = '162123'))