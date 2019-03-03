ta = int(input('Digite um número para ver sua tabuada: '))

for c in range(1, 11):
    m = c * ta
    print('{} * {} é {}'.format(ta, c,  m))

