print('CONDIÇÃO DE PAGAMENTO')

valor = float(input('Digite o preço do produto: '))
print('ESCOLHA SEU MÉTODO DE PAGAMENTO')
fpag = int(input(''' 
1 - Dinheiro ou Cheque 
2 - Á vista no Cartão
3 - 2x no Cartão
4 - 3x ou mais no Cartão
 '''))

if fpag == 1:
    valor = valor - ((valor*10)/100)
    print('O valor a pagar no produto com desconto é {}'.format(valor))
elif fpag == 2:
    valor = valor - ((valor*5)/100)
    print('O valor a pagar no produto com desconto é {}'.format(valor))
elif fpag == 3:
    print('O valor a pagar é {}'.format(valor))
elif fpag == 4:
    valor = valor + ((valor*20)/100)
    print('O valor a pagar no produto com juros é {}'.format(valor))