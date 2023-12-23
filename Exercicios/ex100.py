'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint
from time import sleep


def sorteia(l, s):
    for i in range(0, 5):
        l.append(randint(0, 20))
    somaPar(l, s)


def somaPar(l, s):
    conte = 0
    for i, v in enumerate(l):
        if v % 2 == 0:
            conte += v
    s.append(conte)


lista = []
soma = []
sorteia(lista, soma)

print(f'A lista de valores sorteados foi:', end=' ')
for i in lista:
    sleep(1)
    print(f'\033[1;34m{i} ', end=' ') if lista.index(i) != len(lista)-1 else print(f'{i}\033[m')
print(f'E a soma dos valores pares da lista foi igual a \033[1;34m{soma[0]}\033[m')
