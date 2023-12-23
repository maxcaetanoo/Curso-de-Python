'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:'''
import datetime

data = int(input('Digite ano de nascimento: '))
ano = datetime.date.today().year
idade = ano - data

# – Até 9 anos: MIRIM
if idade <= 9:
    print('Você está na categoria MIRIM por {} anos de idade'.format(idade))
# – Até 14 anos: INFANTIL
elif idade <= 14:
    print('Você está na categoria INFANTIL por {} anos de idade'.format(idade))
# – Até 19 anos: JÚNIOR
elif idade <= 19:
    print('Você está na categoria JÚNIOR por {} anos de idade'.format(idade))
# – Até 25 anos: SÊNIOR
elif idade <= 25:
    print('Você está na categoria SÊNIOR por {} anos de idade'.format(idade))
# – Acima de 25 anos: MASTER
else:
    print('Você está na categoria MASTER por {} anos de idade'.format(idade))
