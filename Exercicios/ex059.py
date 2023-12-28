'''Exercício Python 059: Crie um programa que leia dois valores e mostre um interface na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

sair = False

while sair is not True:
    print('''Selecione uma opção

    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} e {} é igual a {}'.format(n1, n2, soma))

    elif opcao == 2:
        multi = n1 * n2
        print('A multiplicação de {} com {} é igual a {}'.format(n1, n2, multi))

    elif opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print('O maior número é {}'.format(maior))

    elif opcao == 4:
        n1 = int(input('Digite o novo valor do primeiro número: '))
        n2 = int(input('Digite o novo valor do segundo número: '))

    elif opcao == 5:
        print('Saindo...')
        sair = True

    else:
        print('Essa não é uma opção válida, tente novamente.')
