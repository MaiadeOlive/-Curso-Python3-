a = int(input('\033[7;30mQuanto você tem na carteira ? \033[m'))
b = a/3.27
print('\033[4;33mCom R${} , você consegue comprar U${:.2f}!\033[m'.format(a,b))
