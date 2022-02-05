from math import hypot
co = float(input('comprimento do cateto oposto? '))
ca = float(input('comprimento do cateto adjacente? '))
print(f'O triângulo retângulo tem a hipotenusa com o comprimento de {hypot(co, ca):.2f}')

co = float(input('comprimento do cateto oposto? '))
ca = float(input('comprimento do cateto adjacente? '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'{hi:.2f}')
