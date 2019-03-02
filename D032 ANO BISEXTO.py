import math

a = int(input('Digite o ano que gostaria de analisar: '))

if int(a) % 4 == 0:
    print('Este ano é bissexto!')
else:
    print('Este ano não é bissexto!')