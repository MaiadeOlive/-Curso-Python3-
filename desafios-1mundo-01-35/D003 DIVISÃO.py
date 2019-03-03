n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
ds = n1 % n2
e = n1 ** n2
print('\033[1;32mA soma vale {}, o produto vale {} e a divisão vale {}\033[m'. format(s, m, d))
print('\033[1;35mA divisão inteira vale {}, a sobra da divisão vale {}, e a exponenciação vale {:.2f}\033[m'.format(di, ds, e))
