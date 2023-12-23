'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime

trabalhador = {}

trabalhador['nome'] = str(input('Nome: ')).strip().capitalize()
trabalhador['sexo'] = ' '
while trabalhador['sexo'] not in 'MF':
    trabalhador['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
nascimento = int(input('Ano Nascimento: '))
trabalhador['idade'] = datetime.now().year - nascimento
trabalhador['CTPS'] = int(input('Numero da CTPS (0 = não tem): '))
if trabalhador['CTPS'] != 0:
    trabalhador['ano contrato'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário em R$: '))
    if trabalhador['sexo'] == 'M':
        trabalhador['aponsentadoria'] = (35 - (datetime.now().year - trabalhador['ano contrato'])) + trabalhador['idade']
    elif trabalhador['sexo'] == 'F':
        trabalhador['aponsentadoria'] = (30 - (datetime.now().year - trabalhador['ano contrato'])) + trabalhador['idade']

print('-='*30)
for k, v in trabalhador.items():
    print(f'{k.capitalize():<20} = {v}')
