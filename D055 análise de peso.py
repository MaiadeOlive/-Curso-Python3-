maior = 0
menor = 0

for c in range(1, 6):

    peso = float(input('Digite o {}º peso '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O menor peso digitado é {}kg.'.format(menor))
print('O maior peso digitado é {}kg.'.format(maior))








        #menorpeso = float(peso < c)
        # maiorpeso = float(peso > c)

    #if peso > c:
       # print('O maior peso inserido foi {}'.format(maiorpeso))
    #elif c > peso:
    #   print('O menor peso inserido é {} '.format(menorpeso))
