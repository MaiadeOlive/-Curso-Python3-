import random

alu1 = input("\033[4;32mDigite o primeiro aluno: \033[m")
alu2 = input('\033[4;33mDigite o segundo aluno: \033[m')
alu3 = input('\033[4;34mDigite o terceiro aluno: \033[m')
alu4 = input('\033[4;36mDigite o quarto aluno: \033[m')

lista = [alu1, alu2, alu3, alu4]
escolhido = random.choice(lista)

print("\033[1;35mO aluno escolhido é {}!\033[m".format(escolhido))
