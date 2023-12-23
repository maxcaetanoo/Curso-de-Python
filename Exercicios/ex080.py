'''Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''

nuns = []
prox = 0
for i in range(0, 5):
    n = int(input('Digite um valor: '))

    if i == 0 or n > nuns[-1]:
        print('Adicionado ao fim da lista.')
        nuns.append(n)
    else:
        while prox < len(nuns):
            if n <= nuns[prox]:
                nuns.insert(prox, n)
                print(f'Adicionado na posição {prox}.')
                break
            prox += 1

print('='*30)
print(nuns)
print('='*30)
