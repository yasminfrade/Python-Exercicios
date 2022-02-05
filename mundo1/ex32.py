from datetime import date
ano = int(input('Qual ano quer saber? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year  # date.today().yer  pega o ano configurado na máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO é bissexto.')
