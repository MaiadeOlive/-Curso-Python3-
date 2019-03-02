import random

a = (0,1,2,3,4,5)
l = random.choice(a)
m = int(input("De 0 a 5 qual seria sua aposta? "))
if l == m:
    print("Caramba acertou!!!")
else:
    print('Não foi dessa vez!')




