n = int(input('Digite um número para verificar seu fatorial: '))
c = n
f = 1
print(f'Calculando fatorial do número {n}!')
while c > 0:
    print(f'{c}', end='')
    print(' x 'if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')