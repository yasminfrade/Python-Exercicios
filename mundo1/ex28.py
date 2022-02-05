import random
num = random.randrange(0, 5)
n = int(input('Adivinhe o numero que estou pensando: '))
if n == num:
    print('Acertou! Você é vidente?')
else:
    print('Errooouuuuuu!!!')
