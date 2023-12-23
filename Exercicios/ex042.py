'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É possivel formar um triangulo')
    if reta1 == reta2 == reta3:
        print('Esse é um triângulo EQUILÁTERO, pois todos os seus lados são iguais')
    elif reta1 != reta2 != reta3 != reta1:
        print('Esse é um triângulo ESCALENO, pois tem dois lados iguais e um diferente')
    else:
        print('Esse é um triângulo ISÓSCELES, pois todos os seus lados tem tamanhos diferentes')
else:
    print('Não é possível formar um triangulo')
