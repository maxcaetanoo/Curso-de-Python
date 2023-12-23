'''Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

jogadores = []
jogador = {}
totalGols = 0
opt = ' '

while True:
    print('-'*60)
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    partidas = int(input(f'Qtd de partidas que {jogador['nome']} jogou: '))
    jogador['gols'] = []
    totalGols = 0
    for i in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {i+1}: '))
        jogador['gols'].append(gols)
        totalGols += gols
    jogador['total gols'] = totalGols
    jogadores.append(jogador.copy())
    jogador.clear()
    print('-' * 60)

    opt = ' '
    while opt not in 'SN':
        opt = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if opt in 'SN':
            break
        print('Errado, digite apenas S(sim) ou N(não).')
    if opt == 'N':
        break


print('-'*37)
print(f'|\033[1;32m{"ID":^10}\033[m |\033[1;32m{"Nome":^10}\033[m |\033[1;32m{"Tot Gols":^10}\033[m |')
print('-'*37)
for i in jogadores:
    print(f'|\033[1;34m{jogadores.index(i):^10}\033[m', end=' ')
    for k, v in i.items():
        if k == 'nome':
            print(f'|\033[1;34m{v:^10}\033[m', end=' ')
        elif k == 'gols':
            pass
        elif k == 'total gols':
            print(f'|\033[1;34m{v:^10}\033[m |')
print('-'*37)
print()
while True:
    print('-='*30)
    select = -1
    while select not in range(0, 999):
        select = int(input('Para aproveitamento digite \033[32mID\033[m ou \033[31m999\033[m para sair: '))
        if select == 999:
            print('-='*30)
            print('Saindo...')
            break
        elif select not in range(0, len(jogadores)):
            select = -1
            print('ID não encontrado, tente novamente.')
    if select == 999:
        print('Volte sempre.')
        break
    print('-=' * 30)
    for k, v in jogadores[select].items():
        if k == 'nome':
            print(f'O {v}:', end=' ')
        elif k == 'gols':
            for i, g in enumerate(v):
                if i == 0:
                    print(f'jogou {len(jogadores[select]['gols'])} partidas.')
                print(f'  => Na partida {i+1}, marcou {g} gols')
        elif k == 'total gols':
            print(f'O total de gols marcados foi {v}')
