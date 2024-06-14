n = int(input('Digite um número que você queira saber a tabuada: '))
for c in range(0,11):
    print('{:^3} X {:^3} = {:^3}'.format(n, c, n*c))
