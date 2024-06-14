frase = input('Escreva uma frase qualquer: ').strip().lower().split()
frase = ''.join(frase)
fraseInversa = ''
for c in range(0, len(frase)):
    fraseInversa += frase[len(frase) - 1 - c]

if frase == fraseInversa:
    print('Sua frase é um palindromo')
else:
    print('Sua frase NÃO é um palindromo')
