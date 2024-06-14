from datetime import date
maiores = 0
menores = 0
for c in range(1,8):
    nascimento = int(input('Em qual ano a {}° pessoa nasceu: '.format(c)))
    if date.today().year - nascimento >= 21:
        maiores += 1
    else:
        menores += 1
print('Da lista fornecida, {} pessoas são maiores de idade e {} são menores'.format(maiores,menores))
