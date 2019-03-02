print('CALCULE SEU IMC')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura*altura)

print('Seu IMC é {:.2f}'. format(imc))

if imc <= 18.5:
    print('Você está abaixo do peso!')
elif imc <= 25:
    print('Você está no seu peso ideal!')
elif imc <= 30:
    print('Você está com sobrepeso!')
elif imc <= 40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade morbida!')


