print('\033[1;4;31mSeu salário recebeu um aumento de 15%, faça aqui seu cálculo!\033[m')
a = int(input('\033[1;34mQual é o seu salário atual? \033[m'))
b = a*15
c = b/100
d = a+c

print("\033[1;32mSeu salário atualizado é R$\033[m", d)
