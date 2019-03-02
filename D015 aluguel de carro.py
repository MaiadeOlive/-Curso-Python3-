import math
dia = float(input('\033[1;4mQuantos dias o carro ficou alugado? \033[m'))
km = float(input('\033[1;4mQuantos kilometros foram rodados? \033[m'))

total = (dia*60)+(km*0.15)
print('\033[1;4;30mO total a pagar é {}\033[m'.format(total))
