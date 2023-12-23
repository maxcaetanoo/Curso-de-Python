import random

print('Vamos sortear a ordem de apresentação dos alunos \nPrimeiro vamos definir seus nomes ')
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceio aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

number = [1, 2, 3, 4]

for i in range(1, 5):
    select = random.choice(number) #Também é possivel usar o metodo shuffle para embaralhar a lista

    if select == 1:
        print('O {} aluno selecionado é {}'.format(i, aluno1))
    elif select == 2:
        print('O {} aluno selecionado é {}'.format(i, aluno2))
    elif select == 3:
        print('O {} aluno selecionado é {}'.format(i, aluno3))
    else:
        print('O {} aluno selecionado é {}'.format(i, aluno4))

    number.remove(select)
