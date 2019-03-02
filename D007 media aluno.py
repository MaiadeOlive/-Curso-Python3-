n1 = float(input('\033[1;33mNota 1º Semestre: \033[m'))
n2 = float(input('\033[1;36mNota 2º Semestre: \033[m'))
me = n1 + n2 // int(2)
print(me)
if me >= 6:
    print('\033[1;34mAluno aprovado!\033[m')
else:
    print('\033[1;31mAluno reprovado!\033[m')
