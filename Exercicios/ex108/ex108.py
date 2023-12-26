'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
from Exercicios.ex108 import moeda

dinheiro = float(input('Digite um valor em R$: '))
opcao = '.'
while opcao not in 'SN':
    opcao = str(input('Deseja formatar o valor? [S/N]')).strip().upper()[0]
    if opcao in 'SN':
        break
aumento = moeda.aumentar(dinheiro)
diminuicao = moeda.diminuir(dinheiro)
dobrar = moeda.dobro(dinheiro)
dividir = moeda.metade(dinheiro)

print()
if opcao == 'N':
    print(f'O valor {dinheiro} +10% é igual a {aumento}')
    print(f'O valor {dinheiro} -15% é igual a {diminuicao}')
    print(f'O dobro do valor {dinheiro} é {dobrar}')
    print(f'A metade do valor {dinheiro} é {dividir}')
else:
    print(f'O valor {moeda.moeda(dinheiro, True)} +10% é igual a {moeda.moeda(aumento, True)}')
    print(f'O valor {moeda.moeda(dinheiro, True)} -15% é igual a {moeda.moeda(diminuicao, True)}')
    print(f'O dobro do valor {moeda.moeda(dinheiro, True)} é {moeda.moeda(dobrar, True)}')
    print(f'A metade do valor {moeda.moeda(dinheiro, True)} é {moeda.moeda(dividir, True)}')
