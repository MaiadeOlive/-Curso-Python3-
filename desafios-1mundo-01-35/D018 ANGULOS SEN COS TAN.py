import math
angulo = float(input('Digite um angulo: '))

seno = math.sin(math.radians(angulo))
print(' O seno do angulo {} é {:.2f}!'.format(angulo, seno))
coseno = math.cos(math.radians(angulo))
print('O coseno do angulo {} é {:.2f}'. format(angulo, coseno))
tangente = math.tan(math.radians(angulo))
print('A tangente do angulo {} é {:.2f}'.format(angulo, tangente))

