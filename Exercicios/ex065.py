'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

num = sum = med = maior = menor = cont = 0
opt = 'S'

while opt != 'N':
    num = int(input('Digite um valor inteiro: '))
    cont += 1
    sum += num
    if maior == menor == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    opt = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    print('_'*50)
med = sum / cont
print('''\n\nCom base nos valores digitados temos que:
Media = {}
Maior = {}
Menor = {}
'''.format(med, maior, menor))
