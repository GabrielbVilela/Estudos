from random import randint
print('Computador: Vamos jogar Jokenpô ou Pedra, Papel ou Tesoura')
print('Escolha:')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
J = int(input('Qual você irá jogar? '))
C = randint(1,3)

JStr = "PEDRA"
if J == 2:
    JStr = "PAPEL"
elif J == 3:
    JStr = "TESOURA"

CStr = "PEDRA"
if C == 2:
    CStr = "PAPEL"
elif C == 3:
    CStr = "TESOURA"

print('\nJOKENPÔ!!')
print('Computador: Eu escolho', CStr)
print('Você: Eu escolho', JStr)

if J == C + 1 or J == C - 2:
    print('Computador: Parabéns, você ganhou')
elif J == C:
    print('Computador: Infelizmente, empatamos')
else:
    print('Computador: HA! Eu ganhei!!')
