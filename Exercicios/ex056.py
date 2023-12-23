'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

nvelho = ''
ivelho = 0
novas = 0
midade = 0

for p in range(1, 5):
    print('-'*50)
    nome = str(input('Digite o nome da {} pessoa: '.format(p))).capitalize()
    idade = int(input('Digite a idade da {} pessoa: '.format(p)))
    sexo = str(input('Digite M para masculino e F para feminino para o sexo da {} pessoa: '.format(p))).upper()
    print('-' * 50)

    if sexo == 'M' and idade > ivelho:
        nvelho = nome
        ivelho = idade
    elif sexo == 'F' and idade < 20:
        novas += 1

    midade += idade

print('*'*50)
print('O homem mais velho é o {} com a idade de {} anos'.format(nvelho, ivelho))
print('A quantidade de mulheres com menos de 20 anos é {}'.format(novas))
print('E a media da idade do grupo é {}'.format(midade/4))
print('*'*50)