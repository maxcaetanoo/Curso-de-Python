'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
pt = sum = pc = cont = 0
print('-'*40)
print('|{:^38}|'.format('Impar ou par'))
print('-'*40)

while True:
    num = int(input('Escolha um número: '))
    pc = randint(0, 100)
    choice = ' '

    while choice not in 'PI':
        choice = str(input('Par ou Impar [P / I]: ')).strip().upper()[0]

    sum = num + pc

    print(f'Você jogou {num} e o computador jogou {pc}\n')
    if sum % 2 == 0:
        if choice == 'I':
            pt = 0
            print(f'Que pena, você perdeu, o resultado foi {sum}.')
            print('-' * 40)
        elif choice == 'P':
            pt = 1
            print(f'Parabéns, você venceu, o resultado foi {sum}.')
            print('-'*40)
    else:
        if choice == 'I':
            pt = 1
            print(f'Parabéns, você venceu, o resultado foi {sum}.')
            print('-' * 40)
        elif choice == 'P':
            pt = 0
            print(f'Que pena, você perdeu, o resultado foi {sum}.')
            print('-' * 40)

    if pt == 0:
        break
    else:
        cont += 1
print(f'\n\nVocê venceu {cont}X antes da derrota, Parabéns!' if cont > 0 else f'Você não venceu nenhuma vez, que pena.')
