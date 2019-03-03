import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
m = co**2
n = ca**2
o = m + n
h = math.sqrt(o)
print('O comprimento da hipotenusa é {}'.format(h))