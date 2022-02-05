import math                                       
ang = float(input("Qual o valor do ângulo? "))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print(f'{sen:.2f} é o valor do seno.')
print(f'{cos:.2f} é o valor do cosseno.')
print(f'{tang:.2f} é o valor da tangente')
