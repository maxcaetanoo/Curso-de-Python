boasVindas = 'Wellcome to School'

print('_'*30)
print('|{:^28}|'.format(boasVindas))
print('-'*30)

nome = str(input('Diga o nome do aluno: '))
print('_'*30)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a ultima nota do ano: '))
print('_'*30)

media = (n1 + n2 + n3 + n4)/4

print('O nome do aluno é {} e a media foi de {}'.format(nome, media))
