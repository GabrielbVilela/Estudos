from random import randint
from time import sleep
print('Estou pensando em um número de 0 a 5, tente acertar qual é')
n = int(input('Pense em um número: '))
c = randint(0,5)
print('PROCESSANDO...')
sleep(2)
print('Parábens, você acertou o número' if n == c else 'ERROU, Eu pensei no número',c) #Compara a resposta do usuário 'n' com um número aleatório 'c'
