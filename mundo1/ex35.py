print('-='*12)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*12)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Parabéns. As medidas formam um triângulo.')
else:
    print('As medidas NÃO formam um triângulo.')
