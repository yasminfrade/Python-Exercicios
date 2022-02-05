sal = float(input('Qual o seu salario atual: R$ '))
if sal > 1250:
    aum = sal * 10/100
    print(f'Quem ganhava R${sal:.2f} passa a ganhar R${(sal + aum):.2f}')
if sal <= 1250:
    aum = sal * 15/100
    print(f'Quem ganhava R${sal:.2f} passa a ganhar R${(sal + aum):.2f}')

# outra forma mais simples
# if sal <= 1250:
#     novo = sal + (sal * 15 / 100)
# else:
#     novo = sal + (sal * 10 / 100)
# print(f'Quem ganhava R${sal:.2f} passa a ganhar R${novo:.2f}')
