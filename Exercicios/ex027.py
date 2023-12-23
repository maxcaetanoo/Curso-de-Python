'''Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: ')).strip()
listaN = nome.split()
print('Seu primeiro nome é {}'.format(listaN[0]))
print('E seu ultimo nome é {}'.format(nome[nome.rfind(' ') + 1:]))
'''

# Solução 2
n = str(input('Digite seu nome completo: '))
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
