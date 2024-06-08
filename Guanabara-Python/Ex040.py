n1 = float(input('Qual a sua nota da primeira prova? '))
n2 = float(input('Qual a sua nota da primeira prova? '))

print('A sua média foi de {:.1f} pontos'.format((n1 + n2)/2))
if (n1 + n2)/2 >= 7:
    print('Você foi aprovado, Parabéns')
elif (n1 + n2)/2 < 5:
    print('Infelizmente, você foi reprovado')
else :
    print('Você precisará fazer a recuperação para ser aprovado')