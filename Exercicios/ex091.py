'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from operator import itemgetter

jogadores = {}
ranking = []

for i in range(0, 4):
    pessoa = str(input('Digite o nome da pessoa: '))
    jogadores[pessoa] = randint(1, 6)

print('='*50)
for k, v in jogadores.items():
    print(f'O jogador {k} tirou {v}')
print('='*50)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print()
print(f'{"=== Ranking dos Jogadores ===":>35}')
for i, v in enumerate(ranking):
    print(f'{i+1:>10}º colocado {v[0]} com {v[1]}')