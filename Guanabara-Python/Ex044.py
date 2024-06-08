p = float(input('Qual o preço das compras? R$'))
print('''FORMAS DE PAGAMENTO:
1 - para pagar à vista, dinheiro ou cheque
2 - para pagar à vista no cartão
3 - para pagar em até 2x no cartão
4 - para pagar 3x ou mais no cartão''')
f = int(input('Qual a forma de pagamento? '))

print('\nO valor do produto era R${:.2f}'.format(p))
if f == 1:
    p= p * 0.9
elif f == 2:
    p = p * 0.95
elif f == 4:
    p = p * 1.2

print('Agora vale R${:.2f}, por conta da forma de pagamento'.format(p))

if f == 3:
    print('Você pagará R${:.2f} em 2x parcelas'.format(p / 2))
elif f == 4:
    f = int(input('\nEm quantas parcelas irá pagar? '))
    print('Você pagará R${:.2f} em {}x parcelas'.format(p / f, f))
