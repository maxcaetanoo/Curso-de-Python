''' Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

total = cont = quant = barato = 0
Nbarato = ' '
while True:
    print('_'*40)
    nam = str(input('Nome produto: '))
    val = float(input('Valor: R$'))
    cont += 1

    total += val

    if val > 1000:
        quant += 1

    if cont == 1 or val < barato:
        barato = val
        Nbarato = nam

    parar = ' '
    while parar not in 'NS':
        parar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    if parar == 'N':
        break

print('-'*40)
print(f'Encerrou, a compra custou \033[1;32m{total:.2f}\033[m')
print(f'Foram \033[1;32m{quant}\033[m produtos custando acima de R$1000')
print(f'E o produto mais barato foi \033[1;32m{Nbarato}\033[m custando \033[1;32mR${barato:.2f}\033[m.')
print('-'*40)