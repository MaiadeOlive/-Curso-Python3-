from datetime import date
cont = 0
cont2 = 0
for c in range(0,7):
    nasc = int(input('Digite seu ano de nascimento: ').strip())
    hoje = date.today().year
    idade = hoje - nasc

    if idade >= 18:
        cont += 1
    elif idade < 18:
        cont2 += 1
print('{} pessoas já são maiores de idade e {} pessoas ainda vão chegar a maioridade'.format(cont, cont2))

