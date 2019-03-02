sal= float(input('Digite o valor de seu salário atual: '))

a = sal * 15
b = a / 100
c = sal + b

e = sal * 10
f = e / 100
g = sal + f

if sal < 1250.00:
    print('Seu novo salário com aumento de 15% ficou R${}'.format(c))
if sal > 1250.00:
    print('Seu salário com seu novo aumento de 10% ficou R${}'.format(g))
