'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.'''
som = 0
for i in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        som += num
    else:
        pass
print('A soma apenas dos pares foi igual a \033[1;36m{}'.format(som))
