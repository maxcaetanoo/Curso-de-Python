'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

numeros = []
impar = []
par = []
azul = '\033[1;34m'
padrao = '\033[m'
while True:
    print('=_=' * 30)
    numeros.append(int(input('Digite um valor: ')))

    opt = ' '
    while opt not in 'SN':
        opt = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opt in 'N':
        break

for i, v in enumerate(numeros):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print('=_='*30)
print(f'Todos os valores digitados foram: {azul}{numeros}{padrao}')
print(f'Os valores pares digitados foram: {azul}{par}{padrao}')
print(f'E os impares digitados foram: {azul}{impar}{padrao}')
