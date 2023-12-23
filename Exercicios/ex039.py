'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date

ano = int(input('Digite o ano de nascimento de um jovem: '))
idade = date.today().year - ano

if idade == 18:
    print('É hora de se alistar, e combater a grama e a dengue!!')
elif idade > 18:
    print('Tá atrasado, vai ter que pagar multa em!')
    print('Era para você ter se alistado em {}'.format(date.today().year - (idade - 18)))
else:
    print('Você é muito jovem, mas vai chegar sua hora!')
    print('Você precisará se alistar em {}'.format(date.today().year + (18 - idade)))
