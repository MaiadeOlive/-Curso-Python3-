num = int(input('Digite um valor: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        cont += 1
    else:
        print('\033[35m', end=' ')

    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido {} vezes!'.format(num, cont))
if cont == 2:
    print('É um número primo!')
else:
    print('Não é um número primo!')
