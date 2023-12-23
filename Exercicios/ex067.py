'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

cont = 0

while True:
    print('¨'*80)
    num = int(input('Digite valor para tabuada [Ou valor negativo para encerrar}: '))

    if num < 0:
        break

    cont += 1
    for i in range(1,11):
        mult = num * i
        print(f'{num:^6} X {i:^6} = {mult:^6}')
print(f'\n\nEncerrado, a quantidade de tabuadas apresentada foi {cont}')