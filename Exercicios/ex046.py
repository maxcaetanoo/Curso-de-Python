'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
from time import sleep
import emoji

print('*'*40)
print('*{:^38}*'.format('Contagem Regressiva'))
print('*'*40)

for i in range(10, -1, -1):
    print('{:^40}'.format(i))
    sleep(1)


print('{:^40}'.format(
    emoji.emojize("Feliz ano novooo!!! :fogos_de_artifício:", language='pt')))
