'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
from time import sleep

print('*'*40)
print('*{:^38}*'.format('Jogo da adivinha!'))
print('*'*40)

print('\nO computador vai pensar em um número de 0 a 10')
pc = randint(0, 10)
print('\nPensando...')
sleep(3)

print('\n\nTente adivinhar')
num = int(input('Qual foi o número que o computador pensou? '))
cont = 1

while num != pc:
    if num < pc:
        print('\033[1;31mErrou\033[m, é maior que isso')
    else:
        print('\033[1;31mErrou\033[m, é menor que isso')

    num = int(input('Tente novamente: '))
    print('_'*40)
    cont += 1

print('Isso mesmo, o número correto era \033[1;34m{}\033[m, você acertou após \033[1;34m{}\033[m tentativas'.format(
    num, cont))
