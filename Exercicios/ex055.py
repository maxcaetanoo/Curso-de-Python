'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

idmaior = 0
maior = 0
menor = 0
idmenor = 0

for i in range(1, 6):
    peso = float(input('Digite o peso em Kg da {} pessoa: Kg'.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            idmaior = i
        if peso < menor:
            menor = peso
            idmenor = i

print('A {} pessoa tem o maior peso, pesando {}'.format(idmaior, maior))
print('A {} pessoa tem o menor peso, pesando {}'.format(idmenor, menor))