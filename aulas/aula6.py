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