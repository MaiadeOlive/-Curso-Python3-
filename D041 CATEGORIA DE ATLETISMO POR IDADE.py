from datetime import date

print('\033[32mConfederação Nacional de Natação\033[m')
hoje = date.today().year
nasc = int(input('Para saber sua categoria digite seu ano de Nascimento: '))
idade = hoje - nasc

if idade <= 9:
    print('Você tem {} anos!'.format(idade))
    print('Sua categoria é Nadador Mirim!')

elif idade <= 14:
    print('Você tem {} anos!'.format(idade))
    print('Sua categoria é Nadador Infantil!')

elif idade <= 19:
    print('Você tem {} anos!'.format(idade))
    print('Sua categoria é Nadador Junior!')

elif idade <= 25:
    print('Você tem {} anos!'.format(idade))
    print('Sua categoria é Nadador Sênior!')
else:
    print('Você tem {} anos!'.format(idade))
    print('Sua categoria é Nadador Master!')
