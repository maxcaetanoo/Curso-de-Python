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
    for i, v in enumerate(game):
        if v == '0':
            if i not in '258':
                print(f'{i}|', end='')
            else:
                print(f'{i}\n', end='')
                for l in range(0,3):
                    print(f'_', end='') if l != 2 else print(f'{"_"}\n', end='')
        elif v == select or v == pc:
            if i not in '258':
                print(f'{v}|', end='')
            else:
                print(f'{v}\n', end='')
                for l in range(0,3):
                    print(f'_', end='') if l != 2 else print(f'{"_"}\n', end='')
            

def play(game, select, pc):
    while True:
        gaming(game, select, pc)
        print('Sua vez de jogar')
        selection(f'Olá {select} defina onde você irá jogar pelo indice: ', select, pc, game)
        print('Agora o pc vai jogar')
        selection('pc', select, pc, game)
        sleep(1)
        win = champ(game, select, pc)
        if win == 1:
            break


def selection(text, select, pc, game):
    if text != 'pc':
        play = int(input(text))
        game[play] = select
    else:
        play = randint(0, 8)
        game[play] = pc
    while game[play] in 'OX':
        if text != 'pc':
            print('Infelizmente esse indice já foi selecionado, tente novamente com outro indice')
            play = int(input(text))
        else:
            play = randint(0, 8)
    if text != 'pc':
        game[play] = select
    else:
        game[play] = pc
    

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
        print(f'O {select} venceu o jogo!')
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
        print(f'O {pc} venceu o jogo!')
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
