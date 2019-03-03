raz = int(input('Digite a razão da PA: '))
term = int(input('Digite o primeiro termo da PA: '))
dec = term + (10 - 1)*raz
for c in range(term, dec + raz, raz):
        print('{}'.format(c), end=' -> ')
print('FIM')
