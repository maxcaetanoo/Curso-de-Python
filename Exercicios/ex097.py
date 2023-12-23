''' Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex:escreva(‘Olá, Mundo!’) Saída:
~~~~~~~~~
Olá, Mundo!
~~~~~~~~~'''


def escreva(txt):
    tamanaho = len(txt)+2
    print('~'*tamanaho)
    print(' {} '.format(txt))
    print('~'*tamanaho)


escreva(str(input('Texto: ')).upper())