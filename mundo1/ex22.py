nome = str(input('Digite seu nome: ')).strip()
print(f'Seu nome todo em maiuscula: {nome.upper()}')
print(f'Seu nome todo em minuscula: {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras.')
print(f'Seu primeiro nome tem {nome.find(" ")} letras.')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras.')
