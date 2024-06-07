Numero = input("Digite um número: ")
Tamanho = len(Numero)

print("Milhar: {:^5.0f}".format((int(Numero) // 1000) % 10))
print("Centena:{:^5.0f}".format((int(Numero) // 100) % 10))
print("Dezena: {:^5.0f}".format((int(Numero) // 10) % 10))
print("Unidade:{:^5.0f}".format(Numero[len(Numero)-1]))
