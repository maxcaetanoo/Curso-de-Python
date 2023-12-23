'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8'''

nTermo = int(input('Digite quantos termos da sequência de FIBONACCI você deseja ver: '))
anterior = 0
proximo = 1
soma = 0
cont = 1
texto = ''

while cont < nTermo:
    if cont == 1:
        texto = '{} - {} -'.format(anterior, proximo)
    else:
        soma = anterior + proximo
        texto += ' {} -'.format(soma) if cont < nTermo-1 else ' {}'.format(soma)
        anterior = proximo
        proximo = soma
    cont += 1

print('A sequência de FIBONACCI até o \033[1;35m{}\033[m termo são:'.format(nTermo))
print('\033[1;32m{}\033[m'.format(texto))
