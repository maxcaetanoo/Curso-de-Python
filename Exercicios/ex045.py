# Crie um programa que faça o computador jogar Jokenpô com você.
import random

print('{:-^40}'.format('Jokenpô'))
print('''Escolha uma opção
    [1] - Pedra;
    [2] - Papel;
    [3] - Tesoura.''')

pc = random.randint(1, 3)
opcao = int(input('Digite a opção desejada: '))

# Pedra
if opcao == 1:
    opcao = 'Pedra'

    # Pedra
    if pc == 1:
        pc = 'Pedra'
        print('Empate, você selecionou {} e o jogo selecionou {}'.format(opcao, pc))

    # Papel
    elif pc == 2:
        pc = 'Papel'
        print('Derrota, você selecionou {} e o jogo selecionou {}'.format(opcao, pc))

    # Tesoura
    else:
        pc = 'Tesoura'
        print('Vitória, você selecionou {}  e o jogo selecionou {}'.format(opcao, pc))

# Papel
elif opcao == 2:
    opcao = 'Papel'

    # Pedra
    if pc == 1:
        pc = 'Pedra'
        print('Vitória, você selecionou {}  e o jogo selecionou {}'.format(opcao, pc))

    # Papel
    elif pc == 2:
        pc = 'Papel'
        print('Empate, você selecionou {} e o jogo selecionou {}'.format(opcao, pc))

    # Tesoura
    else:
        pc = 'Tesoura'
        print('Derrota, você selecionou {} e o jogo selecionou {}'.format(opcao, pc))

# Tesoura
elif opcao == 3:
    opcao = 'Tesoura'

    # Pedra
    if pc == 1:
        pc = 'Pedra'
        print('Derrota, você selecionou {} e o jogo selecionou {}'.format(opcao, pc))

    # Papel
    elif pc == 2:
        pc = 'Papel'
        print('Vitória, você selecionou {}  e o jogo selecionou {}'.format(opcao, pc))

    # Tesoura
    else:
        pc = 'Tesoura'
        print('Empate, você selecionou {} e o jogo selecionou {}'.format(opcao, pc))

else:
    print('Opção invalida\n{:_^20}'.format('GAME OVER'))

