'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

cont = maior18 = qtdHomens = mulher20 = 0

while True:
    cont += 1
    print('-'*40)
    idade = int(input(f'Digite a idade da {cont} pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
    print('-' * 40)

    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        qtdHomens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1

    opt = ' '
    while opt not in 'SN':
        opt = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).strip().upper()[0]

    if opt == 'N':
        print('-'*40)
        break

print(f'''Programa encerrado, as quantidades são:

A) quantas pessoas tem mais de 18 anos.
    = {maior18}

B) quantos homens foram cadastrados.
    = {qtdHomens}

C) quantas mulheres tem menos de 20 anos.
    = {mulher20}''')
