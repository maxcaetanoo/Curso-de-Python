'''Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''
cont = upper = lower = sum = 0

while True:
    num = int(input('Digite um número ou \033[31m[999 para parar]\033[m: '))
    if num == 999:
        break
    else:
        cont += 1
        sum += num
        if cont == 1:
            upper = lower = num
        else:
            if upper < num:
                upper = num
            elif lower > num:
                lower = num

print(f'\n\nAcabou, a quantidade de números digitados foi {cont}')
print(f'''O maior foi {upper}
O menor foi {lower}
E a soma de todos foi {sum}''')
