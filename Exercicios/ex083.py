'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

contesquerda = 0
contdireita = 0
expression = str(input('Digite uma expressão matemática com parênteses:\n'))
for c, v in enumerate(expression):
    if v == '(':
        contesquerda += 1
    elif v == ')':
        contdireita += 1

if contesquerda == contdireita:
    print(f'A expressão {expression} está correta')
else:
    print(f'A expressão está incorreta \n{f"Faltou {contesquerda-contdireita} )"if contesquerda > contdireita 
    else f"Faltou {contdireita-contesquerda} ("}')
