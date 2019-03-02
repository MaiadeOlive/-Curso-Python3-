n1 = int(input('\033[36mDigite um número: \033[m'))
a = n1 - int(1)
b = n1 + int(1)
print('\033[32mO número escolhido é {}\nSeu antecessor é {}\nSeu sucessor é {}\033[m'.format(n1, a, b))