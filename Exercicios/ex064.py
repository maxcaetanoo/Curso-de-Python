'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

num = sum = cont = 0

blue = '\033[34m'
red = '\033[31m'
green = '\033[32m'
default = '\033[m'

while num != 999:
    if cont == 0:
        cont += 1

    num = int(input('Digite um número inteiro entre {}0{} e {}998{} ou {}999{} para sair: '.format(
         blue, default, blue, default, red, default)))

    if num != 999:
        cont += 1
        sum += num
    else:
        cont -= 1


print('"'*80)
print('A quantidade de números digitados foi {}{}{} e a soma deles é igual a {}{}{}'.format(
    blue, cont, default, blue, sum, default))
print('"'*80)