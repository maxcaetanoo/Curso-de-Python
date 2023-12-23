'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

lista = []
valor = 0

while True:
    valor = int(input('Digite um número inteiro: '))

    if valor not in lista:
        lista.append(valor)
    else:
        print(f'Valor não adcionado, ele já existe na posição {lista.index(valor)} dessa lista')

    opt = ' '
    while opt not in 'SN':
        opt = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opt == 'N':
        break

lista.sort()
print(f'Todos os valores digitados foram {lista}')
