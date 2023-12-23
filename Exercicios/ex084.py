'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

pessoas = []
pessoa = []
pesadas = []
leves = []
maior = menor = 0
while True:
    print('_=' * 30)
    pessoa.append(str(input('Nome da pessoa: ')))
    pessoa.append(float(input('Peso da pessoa: Kg')))

    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        elif pessoa[1] < menor:
            menor = pessoa[1]

    pessoas.append(pessoa[:])
    pessoa.clear()

    print('_=' * 30)
    opt = ' '
    while opt not in 'SN':
        opt = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opt == 'N':
        break

for i, v in enumerate(pessoas):
    if v[1] >= 80.00:
        pesadas.append(pessoas[i])
    else:
        leves.append(pessoas[i])

print('_='*30)
print(f'A listagem de pessoas digitadas foi {pessoas}')
print(f'A quantidade de pessoas digitadas foi {len(pessoas)}')
print(f'O maior peso foi {maior}')
print('-As pessoas com peso maior ou igual a 80kg')
print('*'*35)
for i, v in enumerate(pesadas):
    print(f'{v[0]} com peso de {v[1]}')
print('*'*35)
print(f'O menor peso foi {menor}')
print(f'-As pessoas com peso menor que 80Kg')
print('*'*35)
for i, v in enumerate(leves):
    print(f'{v[0].capitalize()} com peso de {v[1]:.1f}')
print('*'*35)
