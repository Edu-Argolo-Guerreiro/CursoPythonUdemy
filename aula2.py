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

#aula 17 ----------------------------------------
import math

print(math.factorial(4))
print(math.ceil(3.7))
print(math.floor(3.7))

#aula 18 ----------------------------------------

frutas_usuario = input('Digite suas frutas favoritas: ')

frutas_lista = frutas_usuario.split(', ')
print(frutas_lista)

from array import array

#aula 19 ----------------------------------------

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [12, 10, 8, 6, 4, 2])
numeros_f = array('f', [1.2, 1.5, 1.7, 1.9, 2.1, 2.3])

print(letras)
print(numeros_i)
print(numeros_f)

#aula 20 ----------------------------------------

list1 = [10, 20, 30, 40, 50]
list2 = [10, 30, 50, 70, 90]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) #Union
print(num1 & num2) #And
print(num1 - num2) #Diferença
print(num1 ^ num2) #Diferença simétrica

#aula 21 ----------------------------------------

#dicionario
aluno = {'nome': 'Edu', 'idade': 23, 'curso': 'Sistemas de Informação', 'Aprovação': True}
print(aluno['nome'])

aluno.update({'nome': 'Laís', 'Aprovação': False})
print(aluno)
print(aluno.get('endereço', 'Não foi informado este dado'))
del aluno ['idade']
print(aluno)

#aula 22 ----------------------------------------

#dicionario
aluno = {'nome': 'Edu', 'idade': 23, 'curso': 'Sistemas de Informação', 'Aprovação': True}

for keys, values in aluno.items():
    print(keys, values)

#aula 23 ----------------------------------------

'''def somar(x):
   return x + 10
'''
somar10 = lambda x,y: x + y + 10
print(somar10(2, 4))


#aula 24 ----------------------------------------

def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4

print(somar(2))

#aula 25 ----------------------------------------

lista1 = [1, 2, 3, 4]

def mult(x):
   return x * 2

lista2 = map(mult, lista1)
print(list(lista2))

#aula 26 ----------------------------------------

valores = [10, 15, 20, 25, 30, 35]

print(list(filter(lambda x: x >=20, valores)))

#aula 27 ----------------------------------------

setup = ['python', '-m', 'pip', 'install', '-r', 'requirements.txt']

setup2 = [iten for iten in setup if 'i' in iten]
print(setup2)

#aula 28 ----------------------------------------
from sys import getsizeof

valores = [x * 10 for x in range(10)]
print (getsizeof(valores))

print ('======')

valores = (x * 10 for x in range (10))
print(getsizeof(valores))

#aula 29 ----------------------------------------

try:
    letras = [1, 2, 3]
    print(letras[3])
except IndexError:
    print('Não existe esse número')

#aula 30 ----------------------------------------

class Funcionarios:
    nome = 'Edu'
    idade = 19
    curso = 'Engenharia da Computação'

usuario1 = Funcionarios()
print(usuario1.nome)

#aula 31 ----------------------------------------
from datetime import datetime

class Funcionarios:

    def __init__(self, nome, sobrenome, curso, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.curso = curso
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    def idade_funcionario(self):
        ano_atual = datetime.now() .year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

usuario1 = Funcionarios('Edu', 'Guerreiro', 'Eng. Computação', 2009)
usuario2 = Funcionarios('laís', 'Viana', 'Eng. Computação', 2001)
usuario3 = Funcionarios('Lyca', 'Silva', 'Eng. Elétrica', 2002)

print(usuario1.nome)
print(usuario2.sobrenome)
print(usuario3.curso)
print(Funcionarios.nome_completo(usuario3))
print(Funcionarios.idade_funcionario(usuario3))