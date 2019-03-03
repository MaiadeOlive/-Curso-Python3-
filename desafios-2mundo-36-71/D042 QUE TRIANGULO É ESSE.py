import math

a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if a == b == c:
    print('Este é um triângulo equilátero!')
elif a == b or b == c or a == c:
    print('Este é um triângulo Isósceles!')
elif a != b != c and a < b + c and b < a + c and c < b + a:
       print('Este é um triângulo Escaleno!')
else:
    print('Essas retas não podem se tornar um triângulo.')