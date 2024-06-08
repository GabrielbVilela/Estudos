n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print('O número {} é maior do que o número {}'.format(n1,n2))
elif n1 < n2:
    print('O número {} é menor do que o número {}'.format(n1,n2)) 
else:
    print('O número {} é igual ao número {}'.format(n1,n2))
