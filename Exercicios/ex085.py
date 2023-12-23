'''Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''

num = [[], []]
entrada = 0

for i in range(0, 7):
    entrada = int(input(f'Digite o {i+1}º número: '))
    if entrada % 2 == 0:
        num[0].append(entrada)
    else:
        num[1].append(entrada)

print('_'*40)
num[0].sort()
print(f'Os numeros pares digitados foram {num[0]}')
num[1].sort()
print(f'E os números impares foram {num[1]}')
