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
    print(f'O valor R${dinheiro} +10% é igual a R${aumento}')
    print(f'O valor R${dinheiro} -15% é igual a R${diminuicao}')
    print(f'O dobro do valor R${dinheiro} é R${dobrar}')
    print(f'A metade do valor R${dinheiro} é R${dividir}')
else:
    print(f'O valor R${moeda.moeda(dinheiro, True)} +10% é igual a R${moeda.moeda(aumento, True)}')
    print(f'O valor R${moeda.moeda(dinheiro, True)} -15% é igual a R${moeda.moeda(diminuicao, True)}')
    print(f'O dobro do valor R${moeda.moeda(dinheiro, True)} é R${moeda.moeda(dobrar, True)}')
    print(f'A metade do valor R${moeda.moeda(dinheiro, True)} é R${moeda.moeda(dividir, True)}')
