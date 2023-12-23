'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

# Primeira solução
num = int(input('Digite um número inteiro: '))
primo = []

for i in range(2, num):
    if num % i != 0:
        primo.append('sim')
    else:
        primo.append('nao')


if 'nao' in primo:
    print('{}{}{} não é um número primo'.format('\033[1;32m', num, '\033[m'))
else:
    print('{}{}{} é um número primo'.format('\033[1;32m', num, '\033[m'))

'''
# Segunda solução
num = int(input('Digite um número inteiro: '))
cont = 0

for c in range(1, num+1):
    if num % c == 0:
        print('\033[1;31m', end=' ')
        cont += 1
    else:
        print('\033[1;32m', end=' ')
    print(c, '\033[m ', end=' ')

print('\n\nO numero {} foi divisivel {} vezes'.format(num, cont))

if cont == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo')
'''