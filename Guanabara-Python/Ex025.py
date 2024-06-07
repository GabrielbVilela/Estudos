Nome = input('Digite seu nome completo: ').strip().lower()
print('Você possui "Silva" em seu nome? ', Nome[Nome.find('silva'):Nome.find('silva')+5] == "silva")
# Ou
print('Você possui "Silva" em seu nome? ', "silva" in Nome)
