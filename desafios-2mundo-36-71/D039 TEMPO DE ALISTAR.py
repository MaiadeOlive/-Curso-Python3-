from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: ').strip())
idade = atual - nasc
print('Quem nasceu no ano {} tem {} anos em {}.'.format(nasc, idade, atual))


if idade == 18:
    print('Está na hora de se alistar!')

elif idade < 18:
    falta = 18 - idade
    print('Ainda tem tempo para se alistar!')
    print('Faltam exatamente {} ano(s)!'.format(falta))
elif idade > 18:
    falta = idade - 18
    print('Já passou o tempo de seu alistamento!')
    print('Você deveria ter se alistado a tantos {} ano(s) atrás!'.format(falta))


