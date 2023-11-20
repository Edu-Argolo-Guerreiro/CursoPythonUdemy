#aula 21 ----------------------------------------

#dicionario
aluno = {
    'nome': 'Edu',
    'idade': 23,
    'curso': 'Sistemas de Informação',
    'Aprovação': True
}
print(aluno['nome'])

aluno.update({'nome': 'Laís', 'Aprovação': False})
print(aluno)
print(aluno.get('endereço', 'Não foi informado este dado'))
del aluno['idade']
print(aluno)