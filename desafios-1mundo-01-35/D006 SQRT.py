n1 = int(input('\033[36;1mDigite um número: \033[m'))
a = n1 * 2
b = n1 * 3
c = n1 ** (1/2)
print('\033[31mSeu número é {}\033[m\n\033[33mO dobro dele é {}\033[m\n\033[35mSeu triplo é {}\033[m\n\033[32mSua raiz quadrada é {}\033[m'.format(n1, a, b, c))