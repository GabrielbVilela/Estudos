from datetime import date
a = int(input('Digite um ano e veja se ele é bissexto (colocar 0 irá analisar o ano atual): '))
if a == 0:
    a = date.today().year
if (a % 100) % 4 == 0 and (a // 100) % 4 == 0:
    print('Este é um ano bissexto')
else:
    print('Este não é um ano bissexto')
