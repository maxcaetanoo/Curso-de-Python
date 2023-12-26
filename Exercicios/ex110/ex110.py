'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
from Exercicios.ex110 import moeda

valor = float(str(input('Digite um valor em R$: ')).strip().replace(',', '.'))

moeda.resumo(valor, 20, 15)
