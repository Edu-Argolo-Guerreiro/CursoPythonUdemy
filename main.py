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