v = int(input('Qual a velocidade do carro? '))
if v > 80:
    print('Você foi multado, estava acima do limite de velocidade de 80Km/h')
    print('Valor da multa é de R$', (v-80)*7.00)
else:
    print('O carro está dentro do limite de velocidade')
