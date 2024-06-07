Frase = input("Escreva uma frase: ").strip()
print('Sua frase tem {} "a"s'.format(Frase.lower().count("a")))
print('O primeiro "a" aparece na posição', Frase.lower().find("a")+1)
print('O ultimo "a" aparece na posição', Frase.lower().rfind("a")+1)
