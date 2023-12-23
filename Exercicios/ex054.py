'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import datetime

contMaior = 0
contMenor = 0

for i in range(1,8):
    ano = int(input('Digite o ano de nascimento da {}a pessoa: '.format(i)))

    if datetime.now().year - ano >= 18:
        contMaior += 1
    else:
        contMenor += 1
print('A quantidade de pessoas maiores de 18 anos é {} e as menores de 18 anos é igual a {}'.format(
    contMaior, contMenor))
