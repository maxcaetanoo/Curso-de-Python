'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

maior = reta1
if reta2 > reta1 and reta2 > reta3:
    maior = reta2
elif reta3 > reta1 and reta3 > reta2:
    maior = reta3

menor = reta1
if reta2 < reta1 and reta2 < reta3:
    menor = reta2
elif reta3 < reta1 and reta3 < reta2:
    menor = reta3

medio = reta1
if menor <= reta2 < maior:
    medio = reta2
elif menor <= reta3 < maior:
    medio = reta3

if menor + medio > maior:
    print('É possivel formar um triangulo')
else:
    print('Não é possível formar um triangulo')
