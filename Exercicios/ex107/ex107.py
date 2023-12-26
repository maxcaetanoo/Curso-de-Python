'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
import moeda

dinheiro = float(input('Digite um valor em R$: '))
aumento = moeda.aumentar(dinheiro)
diminuicao = moeda.diminuir(dinheiro)
dobrar = moeda.dobro(dinheiro)
dividir = moeda.metade(dinheiro)

print()
print(f'O valor R${dinheiro} +10% é igual a R${aumento}')
print(f'O valor R${dinheiro} -15% é igual a R${diminuicao}')
print(f'O dobro do valor R${dinheiro} é R${dobrar}')
print(f'A metade do valor R${dinheiro} é R${dividir}')
