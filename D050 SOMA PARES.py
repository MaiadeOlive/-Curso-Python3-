some = 0
cont = 0

for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        some += num
        cont += 1
print('Você informou {} números e a soma de todos os números é {}'.format(cont, some))
