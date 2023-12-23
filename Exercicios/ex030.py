'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''
from time import sleep
from random import randint

print('Vamos jogar o jogo do par ou impar?')
escolha = str(input('Você vai ser par ou impar, digite "Par" para escolher par ou "Impar" para escolher impar: '))
valor1 = int(input('Digite um número: '))
valor2 = randint(0, 10)

valorfinal = valor1 + valor2

print('Impar ou par... borar arrastar...')
sleep(2)

if valorfinal % 2 == 0 and escolha.lower() == "par":
    print('='*40)
    print('Parabens você ganhou, seu número {} + {} que foi o número do computador é igual a {} \nE {} é PAR'.format(
        valor1, valor2, valorfinal, valorfinal))
    print('=' * 40)
elif valorfinal % 2 == 1 and escolha.lower() == "par":
    print('=' * 40)
    print('Que pena, você perdeu, seu número {} + {} que foi o número do computador é igual a {} \nE {} é IMPAR'.format(
        valor1, valor2, valorfinal, valorfinal))
    print('=' * 40)
elif valorfinal % 2 == 0 and escolha.lower() == "impar":
    print('=' * 40)
    print('Que pena, você perdeu, seu número {} + {} que foi o número do computador é igual a {} \nE {} é PAR'.format(
        valor1, valor2, valorfinal, valorfinal))
    print('=' * 40)
elif valorfinal % 2 == 1 and escolha.lower() == "impar":
    print('=' * 40)
    print('Parabens você ganhou, seu número {} + {} que foi o número do computador é igual a {} \nE {} é IMPAR'.format(
        valor1, valor2, valorfinal, valorfinal))
    print('=' * 40)
