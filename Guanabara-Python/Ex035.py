r1 = float(input('Digite o tamanho de uma reta: '))
r2 = float(input('Digite o tamanho de outra reta: '))
r3 = float(input('Digite o tamanho de mais uma reta: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('As suas retas podem formar um triângulo')
else:
    print('As suas retas não podem formar um triângulo')
