nota1 = float(input('Nota primeiro semestre: '))
nota2 = float(input('Nota segundo semestre: '))
media = (nota1 + nota2) / 2
print('A primeira nota é {} a segunda é {} e a média do aluno é {}'.format(nota1, nota2, media))


if media > 7:
    print('Aluno Aprovado!')
elif media < 5:
    print('Aluno Reprovado!')
elif 7 > media >= 5:
#elif media >=5 and media < 7: pode ser usada assim tmb
    print('Aluno em Recuperação!')