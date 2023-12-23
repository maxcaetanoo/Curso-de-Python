'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from random import randint
from time import sleep


def maior(x):
    maiorn = max(*x)
    print(f'E o maior número é \033[1;35m{maiorn}\033[m')


def apresentacao(l):
    print('-=' * 30)
    print('Analizando valores passados...')
    if len(l) == 0:
        print(f'Foram analizados \033[1;35m{(len(l))}\033[m valores ao todo.')
        print('Não existe maior valor')
    else:
        for i in l:
            print(f'\033[1;35m{i} ', end='') if l.index(i) < len(l)-1 else print(f'{i}\033[m')
            sleep(.5)
        print(f'Foram analizados \033[1;35m{len(l)}\033[m valores ao todo.')
        maior(l)
    print('-=' * 30)


lista = []
while True:
    lista.clear()
    cont = int(input('Digite quantos valores você deseja: '))
    for i in range(0, cont):
        val = randint(0, 100)
        lista.append(val)

    if cont == 0:
        lista.clear()
        apresentacao(lista)
    else:
        apresentacao(lista)

    opt = ' '
    while opt not in 'SN':
        opt = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if opt == 'N':
        break
