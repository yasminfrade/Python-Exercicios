d = float(input('qual a distancia? '))
if d <= 200:
    p = d * 0.50
    print(f'Valor da passagem: R${p:.2f}')
else:
    print(f'Valor da passagem: R${d * 0.45:.2f}')
print('Tenha uma boa viagem!')
