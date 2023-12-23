'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''

for i in range(1, 51):
    if i%2 == 0:
        print('\033[1;32m{}, '.format(i), end='')
print('\033[1;34m{:>4}'.format('Acabou!'))