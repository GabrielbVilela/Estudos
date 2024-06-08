v = float(input('Qual o valor da casa? R$'))
s = float(input('Qual o valor do seu salário? R$'))
a = int(input('Em quantos anos você vai pagar? '))

if s * 0.3 > (v / a) / 12:
    print('Você pagará {:.2f} por mês'.format((v / a) / 12))
else:
    print('Seu empréstimo foi negado, as prestações mensais altas para o seu salário')
