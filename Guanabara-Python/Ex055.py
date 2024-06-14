for c in range(1,6):
    peso = float(input('Qual o peso da {}° pessoa? '.format(c)))
    if c == 1:
        leve = peso
        pesada = peso
    if peso < leve:
        leve = peso
    if peso > pesada:
        pesada = peso
print('A pessoa mais leve tinha {}Kgs e a mais pessada tinha {}Kgs'.format(leve,pesada))
