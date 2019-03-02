import math

d = int(input('Quantos kilometros tem sua viagem? '))

e = (d * 0.50)
f = (d * 0.45)
if d <= 200:
    print('Sua passagem irá custar, R${:.2f}'.format(e))
else:
    print('Sua passagem irá custar, R${:.2f}'.format(f))
