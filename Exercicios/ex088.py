'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep

mega = []
sorteio = []
palpite = 0
val = 0

while palpite == 0:
    palpite = int(input('Digite quantos palpites você deseja: '))

for i in range(0, palpite):
    for v in range(0, 6):
        val = randint(1, 60)
        while val in sorteio:
            val = randint(1, 60)
        sorteio.append(val)
        sorteio.sort()
    mega.append(sorteio[:])
    sorteio.clear()

print('-+-'*5, f'{"Os valores sorteados foram":^10}', '-+-'*5, '\n')
for i, l in enumerate(mega):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

print('='*15, f'{"Boa Sorte":^9}', '='*15)
