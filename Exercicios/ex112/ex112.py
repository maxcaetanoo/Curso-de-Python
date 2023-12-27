'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
from Exercicios.ex112.utilidadescev.moeda import resumo
from Exercicios.ex112.utilidadescev.dado import leiaDinheiro

valor = leiaDinheiro('Digite o valor: R$ ')
print()
resumo(valor, 20, 15)
