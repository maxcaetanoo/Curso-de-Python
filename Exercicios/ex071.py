'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('-'*40)
print('|{:^38}|'.format('Um Banco Aí (UBA)'))
print('-'*40)

cont = 0

while True:
    saque = int(input('Digite o valor que deseja sacar: R$'))
    cont += 1

    while saque != 0:
        cinquenta = saque // 50
        saque -= 50 * cinquenta
        vinte = saque // 20
        saque -= 20 * vinte
        dez = saque // 10
        saque -= 10 * dez
        um = saque // 1
        saque -= 1 * um

    print('\n')
    print(f'''    R$50.00 {cinquenta} cédulas
    R$20.00 {vinte} cedulas
    R$10.00 {dez} cedulas
    R$1.00 {um} cedulas''')

    print('\n')
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Deseja sair? [S/N]: ')).strip().upper()[0]

    if sair == 'S':
        break

print(f'-{"Saindo...":^38}-')
print(f'Você efetuou {cont} saques')
