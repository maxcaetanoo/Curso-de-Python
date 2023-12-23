'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

text = ''
maior = 0
menor = 0

nuns = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))

for i in range(0, 5):
    if i == 0:
        maior = menor = nuns[i]
    else:
        if maior < nuns[i]:
            maior = nuns[i]
        elif menor > nuns[i]:
            menor = nuns[i]


print(f'Todos os valores sorteados foram: {nuns}')
print(f'O maior valor foi {maior}')
print(f'E o menor foi {menor}')
