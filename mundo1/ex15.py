dias = float(input('Quantos dias de aluguel? '))
qnt_km = float(input("Quilometragem rodada: "))
pago = (dias * 60) + (qnt_km * 0.15)

print(f'Total a pagar por {dias} dias de aluguel com {qnt_km} km rodados\né de R${pago:.2f}')
