from datetime import date
idade = date.today().year - int(input('Em qual ano o atleta nasceu: '))

print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('E pertence à categoria mirim')
elif idade <= 14:
    print('E pertence à categoria infantil')
elif idade <= 19:
    print('E pertence à categoria junior')
elif idade <= 20:
    print('E pertence à categoria Sênior')
else:
    print('E pertence à categoria Master')
    