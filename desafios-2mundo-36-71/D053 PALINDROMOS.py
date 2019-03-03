fras = str(input('Digite sua frase: ')).strip().upper()
list = fras.split()
junto = ''.join(list)

if junto == junto[::-1]:
    print('Sua frase é {} e invertida é "{}" por isso é palindroma'.format(junto, junto[::-1]))
else:
    print('Sua frase é {} e invertida é "{}" por isso não é palindroma'.format(junto, junto[::-1]))
