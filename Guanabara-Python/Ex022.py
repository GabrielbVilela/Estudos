Nome = input('Qual o seu nome completo? ').strip()
print(Nome.upper())
print(Nome.lower())
print('Seu nome possui {} letras ao todo'.format(len(Nome)-Nome.count(" ")))
Nome = Nome.split()
print('Seu primeiro nome {} tem {} letras'.format(Nome[0], len(Nome[0])))
