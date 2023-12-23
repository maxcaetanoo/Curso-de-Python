'''Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[], [], []]

for i in range(0, 3):
    for v in range(0, 3):
        val = int(input(f'Digite o valor [{i}-{v}] valor: '))

        matriz[i].append(val)

print(f'{"-"*5}A matriz ficou assim{"-"*5}')
print(f'''[{matriz[0][0]:^6}] [{matriz[0][1]:^6}] [{matriz[0][2]:^6}]
[{matriz[1][0]:^6}] [{matriz[1][1]:^6}] [{matriz[1][2]:^6}]
[{matriz[2][0]:^6}] [{matriz[2][1]:^6}] [{matriz[2][2]:^6}]''')
