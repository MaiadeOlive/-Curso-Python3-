somaidade = 0
mediaidade = 0
nomehomem = 0
idadehomem = 0
mulhermenos20 = 0

for c in range(1, 5):
    print('-----{}° PESSOA -----'.format(c))
    nome = str(input('Digite seu nome: ').strip())
    idade = int(input('Digite sua idade: '))
    generosex = str(input('Digite seu sexo [M/F]: ').strip())

    somaidade += idade
    mediaidade = somaidade / 4

    if c == 1 and generosex in 'Mm':
        idadehomem = idade
        nomehomem = nome
    if generosex in "Mm" and idade > idadehomem:
        idadehomem = idade
        nomehomem = nome
    if idade < 20 and generosex in "Ff":
        mulhermenos20 += 1


print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O nome do Homem mais velho é {} e ele tem {} anos'.format(nomehomem, idadehomem))
print('Existem {} mulheres menos de 20 anos'.format(mulhermenos20))

    #if idade < 20 and se == 'f':
        #cont2 += 1
    #if se == 'm' and idade > c:

        #print('A média de idade do grupo é de {}'.format(med))
        #print('O nome do homem mais velho é {}'.format(nome))
        #print('{} mulheres tem menos de 20 anos.'.format(cont2))
