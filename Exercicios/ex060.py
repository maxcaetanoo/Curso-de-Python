'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''

num = int(input('Digite um número inteiro: '))
fat = num
mult = 1
text = ''

while num != 0:
    mult *= num
    text += '{} X '.format(num) if num != 1 else '{}'.format(num)
    num -= 1

print('O fatorial de {}! = {} = {}'.format(fat, text, mult))
