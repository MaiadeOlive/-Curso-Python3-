import math
a = float(input('Digite um valor para a primeira reta: '))
b = float(input('Digite um valor para a segunda reta: '))
c = float(input('Digite um valor para a terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('Essas retas podem se tornar um triângulo.')
else:
    print('Essas retas não podem se tornar um triângulo')