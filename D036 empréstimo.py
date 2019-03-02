réscasa = float(input('\033[1;4mQual o valor da casa que você gostaria de comprar? R$ \033[m'))
salario = float(input('\033[1;4mQual o valor do seu salário? R$\033[m'))
anos = int(input('\033[1;4mEm quantos anos pretende pagar? \033[m'))
parcela = casa/(anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a parcela será de R${:.2f}'.format(parcela))
minimo = salario*30 / 100

if parcela >= minimo:
    print('\033[1;31mSentimos muito porém seu empréstimo foi negado!\033[m')
else:
    print('\033[1;32mSeu empréstimo foi aprovado com sucesso!\033[m')
