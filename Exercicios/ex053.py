'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase = str(input('Digite uma frase para conferirmos se é um Palíndromo: ')).lower().strip()
pal = str('')

for i in frase:
    if i != ' ':
        pal += i

print('A frase digitada sem considerar os espaços foi {}'.format(pal))

if pal[::-1] == pal:
    print('A frase é um PALÍNDROMO pois "{}" ao contrario ainda é "{}"'.format(pal, pal[::-1]))
else:
    print('Não é um PALÍNDROMO pois "{}" ao contrario é diferente "{}"'.format(pal, pal[::-1]))
