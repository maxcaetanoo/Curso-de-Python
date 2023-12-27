'''Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.'''
from Exercicios.ex110 import moeda

valor = float(str(input('Digite um valor em R$: ')).strip().replace(',', '.'))

moeda.resumo(valor, 20, 15)
