valor_normal = float(input("Preço: R$ "))
porcent = valor_normal * 5 / 100
novo_valor = (valor_normal - porcent)
print(f'Desconto de R${porcent:.2f}\nTotal de R${novo_valor:.2f}')
