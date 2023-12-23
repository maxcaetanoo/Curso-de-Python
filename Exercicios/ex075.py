'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''
nuns = (
    int(input('Digite um valor inteiro: ')),
    int(input('Digite um valor inteiro: ')),
    int(input('Digite um valor inteiro: ')),
    int(input('Digite um valor inteiro: '))
)

print(f'\n\nA quantidade de vezes que apareceu o número 9 foi: \033[1;34m{nuns.count(9)}\033[m')
print(f'O primeiro número 3 está na posição: \033[1;34m{nuns.index(3)+1}\033[m') if 3 in nuns \
    else print('O 3 não foi digitado em nenhuma posição.')
print('Os numeros pares fora:\033[1;34m', end=' ')
for n in nuns:
    if n % 2 == 0:
        print(f'{n}', end=' ')