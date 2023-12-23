'''Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[], [], []]
somaPar = somaC3 = maiorL2 = 0

for l in range(0, 3):
    for c in range(0, 3):
        val = int(input(f'Digite o valor [{l}-{c}] valor: '))
        matriz[l].append(val)

print(f'{"-"*5}A matriz ficou assim{"-"*5}')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')

        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]

        if c == 2:
            somaC3 += matriz[l][c]
        if l == 1:
            if c == 1:
                maiorL2 = matriz[l][c]
            elif maiorL2 < matriz[l][c]:
                maiorL2 = matriz[l][c]

    print()
print(f'A soma de todos os valores pares é: {somaPar}')
print(f'A soma de todos os valores da coluna 3 é: {somaC3}')
print(f'O maior valor da linha 2 é: {maiorL2}')
