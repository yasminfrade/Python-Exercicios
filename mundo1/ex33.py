a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite um outro número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c< b:
    menor = c

maior = c
if a > c and a > b:
    maior = a
if b > c and b > a:
    maior = b

print(f'o menor valor é {menor}')
print(f'o maior valor é {maior}')
