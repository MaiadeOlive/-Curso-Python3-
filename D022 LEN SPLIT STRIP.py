nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiuscula é...{}'.format(nome.upper()))
print('Seu nome em minuscula é...{}'.format(nome.lower()))
print('O seu nome ao todo tem {} letras...'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
primeironome = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeironome[0], len(primeironome[0])))
