'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão'''

init = int(input('Digite um número inteiro para iniciar a PA: '))
razao = int(input('Digite o valor da razão da PA: '))
final = init

for i in range(1,11):
    print(final, '->', end=' ')
    final += razao
print('\033[34mFim')