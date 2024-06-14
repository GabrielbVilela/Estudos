n = int(input('Digite um número: '))
v = True
for c in range(1, n):
    if c != 1 and n % c == 0:
        v = False

if v == False:
    print('Esse número NÃO é primo')
else:
    print('Esse número é primo')
