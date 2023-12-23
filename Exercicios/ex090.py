'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''

escola = list()
alunos = dict()

while True:
    alunos["nome"] = str(input('Nome do aluno: ')).capitalize().strip()
    alunos["media"] = float(input('Media do aluno: '))
    if alunos["media"] >= 7:
        alunos["situacao"] = 'Aprovado'
    elif alunos["media"] >= 5:
        alunos["situacao"] = 'Recuperação'
    else:
        alunos["situacao"] = 'Reprovado'

    escola.append(alunos.copy())

    opt = ' '
    while opt not in 'SN':
        opt = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opt == 'N':
        break

print(f'|{"Aluno":^10}|{"Média":^10}|{"Situação":^10}|')
print('_'*34)
for i in escola:
    for v in i.values():
        print(f'|{v:<10}', end='')
    print()
    print('-'*34)
