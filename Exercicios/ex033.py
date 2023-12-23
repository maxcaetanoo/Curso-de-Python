'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Por fim digite mais um número: '))

if n1 > n2 and n1 > n3:
    print('O primeiro número {} é maior que {} e {}'.format(n1, n2 if n2 > n3 else n3, n3 if n3 < n2 else n2))
elif n2 > n1 and n2 > n3:
    print('O primeiro número {} é maior que {} e {}'.format(n2, n1 if n1 > n3 else n3, n3 if n3 < n1 else n1))
else:
    print('O primeiro número {} é maior que {} e {}'.format(n3, n2 if n2 > n1 else n1, n1 if n1 < n2 else n2))
