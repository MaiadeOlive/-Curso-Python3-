a = int(input('Digite o primeiro número inteiro: '))
b = int(input('Digite o segundo número inteiro: '))

maior = a

if b > a:
    print('O segundo número é o maior!')
elif a > b:
    print('O primeiro número é o maior!')
elif a == b:
    print('Ambos tem o mesmo valor!')
else:
    print('Digite um valor válido!')
