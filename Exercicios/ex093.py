'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

aprovetamento = {}
totalGols = 0

aprovetamento['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
partidas = int(input(f'Qtd de partidas que {aprovetamento['nome']} jogou: '))
aprovetamento['gols'] = []
for i in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {i+1}: '))
    aprovetamento['gols'].append(gols)
    totalGols += gols
aprovetamento['total gols'] = totalGols

print('-='*30)
print(aprovetamento)
print('-='*30)
for k, v in aprovetamento.items():
    print(f'O {k} tem valor {v}')
print('-='*30)
print(f'O jogador {aprovetamento['nome']} jogou {len(aprovetamento['gols'])} partidas.')
for i, v in enumerate(aprovetamento['gols']):
    print(f'  => Na partida {i+1}, fez {v} gols.') if v != 1 else print(f'  => Na partida {i+1}, fez {v} gol.')
print(f'Foi um total de {aprovetamento['total gols']} gols')
