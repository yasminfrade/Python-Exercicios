valor_casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual seu salário atual? R$ '))
anos_quitar = int(input('Em quanto anos quer quitar a casa? '))
prest = valor_casa / (anos_quitar * 12)

print(f'Para pagar uma casa de R${valor_casa} em {anos_quitar} anos,', end=' ')
print(f'O valor da prestação é de R${prest}')

if prest > salario*30/100:
    print('Emprestimo NEGADO.')
else:
    print('Emprestimo APROVADO.')
