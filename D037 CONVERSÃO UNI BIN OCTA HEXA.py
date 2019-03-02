num = int(input('\033[1;4mPor favor, digite um número:\033[m '))
print('\033[1;31mPor favor, escolha qual a base de conversão:\033[m')
numco = int(input('''\033[1;35m1 - Binário\033[m
\033[34;1m2 - Octal\033[m
\033[36;1m3 - Hexadecimal\033[m\n'''))


if numco == 1:
    print('{} Convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif numco == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif numco == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Por favor, escolha uma base de conversão válida')