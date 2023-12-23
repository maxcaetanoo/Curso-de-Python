'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input("Digite uma frase para compararmos quantos A's ela tem: ")).strip().upper()
print('A quantidade de "A" é {}, \nO primeiro "A" sem encontra na posição {} \nE o ultimo "A" na posição {}'.format(frase.count('A'), frase.find('A')+1, frase.rfind('A')+1))
