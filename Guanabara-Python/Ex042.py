n1 = float(input('Digite o valor de uma reta: '))
n2 = float(input('Digite o valor de outra reta: '))
n3 = float(input('Digite o valor de mais uma reta: '))

if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
    print('É possivel formar um triângulo com essas retas')
    if n1 == n2 and n2 == n3:
        print('Com essas retas o seu triângulo será equilátero')
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print('Com essas retas o seu triângulo será isósceles')
    else:
        print('Com essas retas o seu triângulo será escaleno')
else:
    print('Não é possivel formar um triângulo com essas retas')
