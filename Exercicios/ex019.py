import random

print('Vamos sortear um dos alunos \nPrimeiro vamos definir seus nomes ')
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceio aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

select = random.randint(1, 4)

if select == 1:
    print('O selecionado para limpar o quadro é {}'.format(aluno1))
elif select == 2:
    print('O selecionado para limpar o quadro é {}'.format(aluno2))
elif select == 3:
    print('O selecionado para limpar o quadro é {}'.format(aluno3))
else:
    print('O selecionado para limpar o quadro é {}'.format(aluno4))