'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
from Exercicios.ex109 import moeda

valor = str(input('Digite um valor em R$: ')).replace(',', '.').strip()
dinheiro = float(valor)
opcao = '.'
while opcao not in 'SN':
    opcao = str(input('Deseja formatar o valor? [S/N]')).strip().upper()[0]
    if opcao in 'SN':
        break

if opcao == 'S':
    formatar = True
else:
    formatar = False

print()
print(f'O valor {moeda.moeda(dinheiro, formatar)} +10% é igual a {moeda.aumentar(dinheiro, 10, formatar)}')
print(f'O valor {moeda.moeda(dinheiro, formatar)} -15% é igual a {moeda.diminuir(dinheiro, 15, formatar)}')
print(f'O dobro do valor {moeda.moeda(dinheiro, formatar)} é {moeda.dobro(dinheiro, formatar)}')
print(f'A metade do valor {moeda.moeda(dinheiro, formatar)} é {moeda.metade(dinheiro, formatar)}')
