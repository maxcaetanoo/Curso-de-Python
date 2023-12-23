'''Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    lista.append(int(input('Digite um número inteiro: ')))

    opt = ' '
    while opt not in 'SN':
        opt = str(input('Deseja sair? [S/N}: ')).strip().upper()[0]
    if opt == 'S':
        break

print(f'A quantidade de números digitada foi {len(lista)}')
lista.sort(reverse=True)
print(f'A listagem de valores de forma decrescente é: {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista')
else:
    print('O valor 5 não foi encontrado.')