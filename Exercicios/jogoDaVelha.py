from random import randint
from time import sleep


def menu(text):
    print('-'*40)
    print(f'{"Bem vindo ao jogo da velha!":^40}')
    print('-'*40)
    select = ' '
    while select not in 'OX':
        select = str(input(text)).upper().strip()[0]
        if select not in 'OX':
            print('Não existe essa opção tente novamente')
    return select


def gaming(game, select, pc):
    print('\n')
    print('-'*17)
    for i, v in enumerate(game):
        if v == '0':
            if str(i) not in '258':
                print(f'{str(i):^5}|', end='')
            else:
                print(f'{str(i):^5}\n', end='')
                for l in range(0,3):
                    print(f'-'*5, end='') if l != 2 else print(f'{"-"*7}\n', end='')
        elif v == select or v == pc:
            if str(i) not in '258':
                print(f'\033[32m{v:^5}\033[m|', end='') if v == select else print(f'\033[31m{v:^5}\033[m|', end='')
            else:
                print(f'\033[32m{v:^5}\033[m\n', end='') if v == select else print(f'\033[31m{v:^5}\033[m\n', end='')
                for l in range(0,3):
                    print(f'-'*5, end='') if l != 2 else print(f'{"-"*7}\n', end='')
            

def play(game, select, pc):
    while True:
        gaming(game, select, pc)
        print('\n')
        win = champ(game, select, pc)
        if win == 1:
            break
        print('\n')
        print('Sua vez de jogar')
        pl = selection(f'Olá {select} defina onde você irá jogar pelo indice: ', game)
        game[pl] = select
        print('Agora o pc vai jogar')
        gm = selection('pc', game)
        game[gm] = pc
        sleep(1)


def selection(text, game):
    if text != 'pc':
        play = int(input(text))
    else:
        play = randint(0, 8)
    while game[play] in 'OX':
        if text != 'pc':
            print('Infelizmente esse indice já foi selecionado, tente novamente com outro indice')
            play = int(input(text))
        elif text == 'pc':
            play = randint(0, 8)

    if text != 'pc':
        return play
    else:
        return play
    

def champ(game, select, pc):
    win = 0
    if ((select in game[0] and select in game[1] and select in game[2]) or
        (select in game[3] and select in game[4] and select in  game[5]) or
        (select in game[6] and select in game[7] and select in  game[8]) or
        (select in game[0] and select in game[4] and select in  game[8]) or
        (select in game[2] and select in game[4] and select in  game[6]) or
        (select in game[0] and select in game[3] and select in  game[6]) or
        (select in game[1] and select in game[4] and select in  game[7]) or
        (select in game[2] and select in game[5] and select in  game[8])):
        camp = f'O \033[32m{select}\033[m venceu o jogo!'
        print(f'{camp:^40}')
        win = 1
        return win
    elif ((pc in game[0] and pc in game[1] and pc in game[2]) or
        (pc in game[3] and pc in game[4] and pc in  game[5]) or
        (pc in game[6] and pc in game[7] and pc in  game[8]) or
        (pc in game[0] and pc in game[4] and pc in  game[8]) or
        (pc in game[2] and pc in game[4] and pc in  game[6]) or
        (pc in game[0] and pc in game[3] and pc in  game[6]) or
        (pc in game[1] and pc in game[4] and pc in  game[7]) or
        (pc in game[2] and pc in game[5] and pc in  game[8])):
        camp = f'O \033[31m{pc}\033[m venceu o jogo!'
        print(f'{camp:^40}')
        win = 1
        return win
    else:
        win = 0
        return win


game = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
select = menu('Selecione (O) ou (X) para jogar: ')
if select == 'X':
    pc = 'O'
else:
    pc = 'X'

play(game, select, pc)
print(f'{"Fim de jogo!":^40}')
