'''Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
Importante: use cores.'''
c = ['\033[m', '\033[7;31;40m', '\033[7;32;40m', '\033[7;33;40m', '\033[7;34;40m']


def title(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('-'*tamanho)
    print(f'  {msg}')
    print('-'*tamanho)
    print(c[0])


def helper(function):
    title(f'Acessando manual do \'{function}\'', 4)
    print(c[3], end='')
    print(f' {help(function)}')
    print(c[0], end='')


title('Bem vimdo ao sistema de ajuda python', 2)
while True:
    comando = input('Digite uma função ("FIM" para sair): ')
    if comando.upper() == 'FIM':
        break
    else:
        helper(function=comando)
title('Saindo', 1)