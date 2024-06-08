from datetime import date
nascimento = int(input('Em qual ano você nasceu? '))
idade = date.today().year - nascimento

if idade > 18:
    print('Você já passou {} anos do tempo de se alistar no serviço militar'.format(idade - 18))
    print('Seu ano de alistamento era em ', nascimento + 18)
elif idade < 18:
    print('Você ainda vai se alistar no serviço militar daqui a {} anos'.format(idade + 18))
    print('Seu ano de alistamento será em ', nascimento + 18)
else:
    print('Você precisa se alistar no serviço militar, pois já possui 18 anos')
