import random

print(' JOKENPÔ ')
print('Vamos jogar?')

eu = int(input('''Qual sua jogada? 
Escolha 
1 - pedra
2 - papel 
3 - tesoura '''))

jogada = [1, 2, 3]
pc = random.choice(jogada)

print('Sua jogada é {} e a minha é {}'.format(eu, pc))
if eu == pc:
    print('Empatamos!')
elif eu == 1 and pc == 2:
    print('Ganhei!')
elif eu == 2 and pc == 3:
    print('Ganhei!')
elif eu == 3 and pc == 1:
    print('Ganhei!')
elif eu == 2 and pc == 1:
    print('Você ganhou!')
elif eu == 3 and pc == 2:
    print('Você ganhou!')
elif eu == 1 and pc == 3:
    print('Você ganhou!')
else:
    print('Joga direito!')
