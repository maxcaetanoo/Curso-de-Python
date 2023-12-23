'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

list = []
positionmax = []
positionmin = []
maior = menor = 0
blue = '\033[1;34m'
default = '\033[m'

for l in range(0, 5):
    list.append(int(input(f'Digite o valor na posição {l}: ')))

maior = max(list)
menor = min(list)
positionmax.append(list.index(max(list)))
positionmin.append(list.index(min(list)))

for k, v in enumerate(list):
    if maior == v and positionmax[0] != k:
        positionmax.append(k)
    elif menor == v and positionmin[0] != k:
        positionmin.append(k)


print(f'A lista completa é: {blue}{list}{default}')
print(f'O maior valor digitado é: {blue}{max(list)}{default} localizado na posição: {blue}{positionmax}{default}')
print(f'O menor valor digitado é: {blue}{min(list)}{default} localizado na posição: {blue}{positionmin}{default}')
