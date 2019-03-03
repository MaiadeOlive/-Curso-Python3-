import math

num = float(input('\033[31mDigite um número:\033[m'))
print('\033[1;33mO valor digitado foi {} e a sua parte inteira é {}\033[m'.format(num, math.trunc(num)))