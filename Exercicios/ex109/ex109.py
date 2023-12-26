'''Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.'''
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
