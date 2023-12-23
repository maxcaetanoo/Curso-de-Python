'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e
permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

alunos = []
nome = ''
nota1 = nota2 = media = 0
escolha = ' '
opcao = 0
while True:
    nome = str(input('Nome do aluno: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    alunos.append([nome, [nota1, nota2], media])

    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break

print('\033[1;34m')
print('_' * 30)
print(f'|{"ID":>3}| {"NOME":>10} | {"MÉDIA":>11}|')
print('-' * 30, '\033[m')
for i, a in enumerate(alunos):
    print(f'|{i:>3}| {alunos[i][0]:>10} | \033[32m{alunos[i][2]:>11.1f}\033[m|') if alunos[i][2] >= 7.0 \
        else print(f'|{i:>3}| {alunos[i][0]:>10} | \033[31m{alunos[i][2]:>11.1f}\033[m|')
print('-' * 30, '\n\n')

while True:
    opcao = ' '
    while opcao not in range(0, 1000):
        print('=' * 70)
        opcao = int(input(f'{"Digite o \033[1;34mID\033[m de um aluno para ver suas notas, ou \033[1;31m999\033[m para sair:":^70} '))
    if opcao == 999:
        print('=' * 70)
        print(f'{'Encerrando...':^70}')
        break
    else:
        if opcao in range(0, len(alunos)):
            print('=' * 70)
            print(f'O(A) Aluno(a) do id {opcao} é {alunos[opcao][0]}:')
            print('- Suas notas foram:', end=' ')
            for i, v in enumerate(alunos[opcao][1]):
                if i == 0:
                    print(f'\033[32m{v}\033[m', end=', ') if alunos[opcao][1][i] >= 7.0 \
                        else print(f'\033[31m{v}\033[m', end=', ')
                else:
                    print(f'\033[32m{v}\033[m') if alunos[opcao][1][i] >= 7.0 \
                        else print(f'\033[31m{v}\033[m')
        else:
            print('ID não encontrado, tente novamente.')
