v = float(input('A que velocidade está? '))
if v > 80:
    print('MULTADO. Você ultrapassou o limite de velocidade de 80km/h')
    multa = (v - 80) * 7
    print(f'Sua multa é de R${multa}')

print('Prossiga!')
