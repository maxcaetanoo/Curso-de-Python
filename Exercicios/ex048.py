'''Faça um programa que calcule a soma entre todos os números que são múltiplos de três
e que se encontram no intervalo de 1 até 500.'''
n = 0
c = 0

for i in range(1, 501):
    if i % 3 == 0 and i % 2 != 0:
        n += i
        c += 1

print('A soma de todos os {} valores mútiplos de 3 é: {}'.format(c, n))
