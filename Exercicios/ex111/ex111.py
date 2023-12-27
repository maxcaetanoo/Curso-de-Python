'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
from utilidadescev import dado

valor = float(str(input('Digite um valor em R$: ')).strip().replace(',', '.'))

dado.resumo(valor, 20, 15)
