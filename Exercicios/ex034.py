'''
Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

sal = float(input('Digite o valor do seu salário: '))

if sal <= 1250.00:
    aumento = (sal * 15)/100
    print('Seu salário é {} após o aumento de 15% igual a {}'.format(sal+aumento, aumento))
else:
    aumento = (sal * 10)/100
    print('Seu salário é {} após o aumento de 10% igual a {}'.format(sal + aumento, aumento))
