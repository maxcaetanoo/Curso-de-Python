'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

termo = int(input('Digite um número inteiro para iniciar a PA: '))
razao = int(input('Digite o valor da razão da PA: '))
cont = 1

while cont != 11:
    print(termo, '->' if cont < 10 else ' ', end=' ')
    termo += razao
    cont += 1
print('\033[34mFim')
