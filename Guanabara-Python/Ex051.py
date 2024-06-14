termo = int(input('Digite o 1° termo (número) da PA (Progressão Aritmética): '))
razao = int(input('Digite qual a razão da PA (Progressão Aritmética): '))
for c in range(1, 11):
    print(termo, end=' ')
    termo += razao
print('\nEssa é sua PA')
