'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep


def contador(inicio, fim, passo):
    print('-='*30)
    if passo == 0:
        passo = 1
    if inicio < fim and passo < 0:
        passo *= -1

    print(f'De {inicio} até {fim} de {passo} em {passo}')

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'\033[1;34m{cont},', end=' ') if cont + passo <= fim else print(f'{cont}\033[m')
            cont += passo
            sleep(.5)
    else:
        cont = inicio
        if passo > 0:
            while cont >= fim:
                print(f'\033[1;34m{cont},', end=' ') if cont - passo >= fim else print(f'{cont}\033[m')
                cont -= passo
                sleep(.5)
        else:
            while cont >= fim:
                print(f'\033[1;34m{cont},', end=' ') if cont + passo >= fim else print(f'{cont}\033[m')
                cont += passo
                sleep(.5)

    print()


contador(1, 10, 1)
contador(10, 0, 2)
print(f'{"=":<}'*2, f'{"Agora é sua vez":^15}', f'{"=":<}'*2)
init = int(input('Início: '))
end = int(input('Fim: '))
step = int(input('Passo: '))

contador(inicio=init, fim=end, passo=step)
print('-='*30)
