'''Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''
nome = str(input('Digite seu nome completo: ')).strip()
print("Tem 'SILVA' = {}".format('SILVA' in nome.upper()))
