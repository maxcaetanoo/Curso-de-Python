'''Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.

No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

pessoas = []
mulheres = []
acimaMedia = []
pessoa = {}
soma = 0

while True:
    print('-'*60)
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    pessoa['sexo'] = ' '
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] not in 'MF':
            print('Errado, por favor digite apenas M(masculino) ou F(feminino)')
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    print('-'*60)

    opt = ' '
    while opt not in 'SN':
        opt = str(input('Desenja continuar? [S/N]: ')).strip().upper()[0]
        if opt not in 'SN':
            print('Errado, digite apenas S ou N.')
    if opt == 'N':
        break

print('-='*30)
print(f'A quantidade de pessoas cadastradas é \033[1;34m{len(pessoas)}\033[m')
for i in range(0, len(pessoas)):
    soma += pessoas[i]['idade']
    if pessoas[i]['sexo'] == 'F':
        mulheres.append(pessoas[i])
media = soma / len(pessoas)
print(f'A média de idade do grupo de pessoas é \033[1;34m{media:.0f}\033[m')
print(f'Todas as mulheres do grupo são: ')
for i in mulheres:
    for k, v in i.items():
        if k == 'nome':
            print(f'  - \033[1;34m{v}\033[m', end=' ')
        elif k == 'sexo':
            pass
        elif k == 'idade':
            print(f'com idade igual a \033[1;34m{v}\033[m')
for i in range(0, len(pessoas)):
    if pessoas[i]['idade'] > media:
        acimaMedia.append(pessoas[i])
print(f'As pessoas com a idade acima de {media:.0f} são:')
for i in acimaMedia:
    for k, v in i.items():
        if k == 'nome':
            print(f'  - \033[1;34m{v}\033[m', end=' ')
        elif k == 'sexo':
            print(f'do sexo \033[1;34m{v}\033[m', end=' ')
        elif k == 'idade':
            print(f'com idade igual a \033[1;34m{v}\033[m')
