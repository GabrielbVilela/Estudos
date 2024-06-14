idadeDoGrupo = 0
mulheresNovas = 0
idadeHomemMaisVelho = 0
for c in range(1,5):
    nome = input('Qual o nome da {}° pessoa: '.format(c)).strip()
    idade = int(input('Qual a idade da {}° pessoa: '.format(c))) 
    sexo = input('Qual o sexo da {}° pessoa (M/F): '.format(c)).strip()
    idadeDoGrupo += idade
    if sexo.lower() == 'm' and idade > idadeHomemMaisVelho:
        idadeHomemMaisVelho = idade
        nomeHomemMaisVelho = nome
    if sexo.lower() == 'f' and idade < 20:
        mulheresNovas += 1

idadeDoGrupo = idadeDoGrupo / 4
print('A média de idade do grupo é de {} anos'.format(idadeDoGrupo))
print('O homem mais velho do grupo é o {} com {} anos'.format(nomeHomemMaisVelho, idadeHomemMaisVelho))
print('No grupo {} mulher(es) tem menos de 20 anos'.format(mulheresNovas))
