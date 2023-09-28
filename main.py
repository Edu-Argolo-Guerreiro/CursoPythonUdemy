#aula 11
valor = int(input('Qual o valor da sua conta bancaria atualmente em R$: '))

if valor >= 1000:
    valor = (valor * 0.10) + valor
    print(f'Com o acressimo do branco, você terá: R$ {valor}')
else:
    valor_perdendo = int((valor * 0.10))
    print(f'Caso faça algum contato com o banco, você irá perder R$ {valor_perdendo}')
    print(f'Ficando com o saldo atual de R$ {valor - valor_perdendo}')
