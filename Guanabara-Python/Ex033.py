n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

Ma = n1 #Verificando quem é o maior
if n2 > n3 and n2 > n1:
    Ma = n2
if n3 > n1 and n3> n2:
    Ma = n3

me = n2 #Verificando quem é o menor
if n1 < n2 and n1 < n3:
    me = n1
if n3 < n2 and n3 < n1:
    me = n3

print('O maior número digitado foi ',Ma)
print('O menor número digitado foi ',me)
