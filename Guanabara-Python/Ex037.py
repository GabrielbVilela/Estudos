n = int(input('Qual número você deseja converter? '))
print('1 - para binário')
print('2 - para octal')
print('3 - para hexadecimal')
o = int(input('Qual operação você quer realizar? '))

if o == 1:
    print('{} na base binária é igual a'.format(n), bin(n)[2:])
elif o == 2:
    print('{} na base octal é igual a'.format(n), oct(n)[2:])
elif o == 3:
    print('{} na base hexadecimal é igual a'.format(n), hex()[2:])
else:
    print('Opção Inválida')
    