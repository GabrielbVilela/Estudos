a = float(input('Digite qual a sua altura, em metros: '))
p = float(input('Digite qual o seu peso, em quilos: '))

print('Seu IMC é de {:.2f}'.format(p / a ** 2))
if p / a ** 2 < 18.5:
    print('De acordo com a tabela de IMC, você está na faixa abaixo do peso')
elif p / a ** 2 < 25:
    print('De acordo com a tabela de IMC, você está na faixa de peso ideial')
elif p / a ** 2 < 30:
    print('De acordo com a tabela de IMC, você está na faixa de sobrepeso')
elif p / a ** 2 < 40:
    print('De acordo com a tabela de IMC, você está na faixa de obesidade')
else:
    print('De acordo com a tabela de IMC, você está na faixa de obesidade mórbida')
