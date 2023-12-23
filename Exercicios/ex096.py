'''Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''


def area(l, c):
    a = l * c
    print(f'A área do terreno de {l:.2f} X {c:.2f} é {a:.2f}²')


area(float(input('Digite a Largura em metros: ')), float(input('Digite o comprimento em metros: ')))
