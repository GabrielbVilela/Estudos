v = int(input('Qual a distancia (em Km) da sua viagem? '))
if v <= 200:
    print('O preço da viagem é de R$', v*0.50)
else:
    print('O preço da viagem é de R$', v*0.45)
