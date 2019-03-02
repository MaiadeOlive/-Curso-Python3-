import math

v = int(input('Digite a velocidade do carro: '))
g = (v-80)*7

if v > 80:
    print('Sinto muito, porém você foi multado em R${:.2f}!'.format(g))
