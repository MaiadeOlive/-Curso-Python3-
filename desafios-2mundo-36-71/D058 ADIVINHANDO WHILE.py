import random

cont = 0
print('---JOGO DA ADIVINHAÇÃO---')
num = int(input('Digite seu palpite de 1 a 10: '))

a = (1, 11)
l = random.choice(a)

while a != l:
    cont = cont + 1
    a = int(input('Tente novamente: '))
print('Bingo" \nO número {} que você escolheu esta correto!\nVocê levou {} tentativas!'.format(a,cont))


