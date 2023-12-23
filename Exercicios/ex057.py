'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = 'x'
while "F" != sexo != "M":
    sexo = str(input('Digite o seu sexo [M masculino / F feminino] : ')).upper().strip()[0]

if sexo == 'M':
    print('Dale mano, tudo certo?')
elif sexo == 'F':
    print('Dale Mina, suave?')
