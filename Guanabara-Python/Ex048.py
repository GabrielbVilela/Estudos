soma = 0
for c in range(1,501):
    if (c % 2 == 1 and c % 3 == 0):
        soma += c
print('A soma de todos os números impares multiplos de 3 até 500 é de', soma)