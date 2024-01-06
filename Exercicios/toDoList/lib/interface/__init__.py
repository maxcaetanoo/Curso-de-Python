from Exercicios.toDoList.lib import archive
from Exercicios.toDoList.lib.classes import Tarefa


def title(t):
    print('-' * 40)
    print(f'\033[1;32m{t:^40}\033[m')
    print('-' * 40, end='\n')


def menu(arq):
    from time import sleep
    title('Bem vindo ao To-Do List')

    menus = ["Ver tarefas", "Criar nova tarefa", "Adiar tarefa", "Remover tarefa", "Sair do To-Do List"]

    while True:
        for i, v in enumerate(menus):
            print(f'\033[34m{i+1:<2}\033[m- \033[34m{v:<10}\033[m')

        print('-'*40)
        select = int(input('Digite o indice da opção desejada: '))
        print('-' * 40, end='\n')

        if select == 1:
            title(menus[select-1])
            sleep(1)
            archive.arqRead(arq)
        elif select == 2:
            title(menus[select-1])
            sleep(1)
            pass
        elif select == 3:
            title(menus[select-1])
            sleep(1)
            pass
        elif select == 4:
            title(menus[select-1])
            sleep(1)
            pass
        elif select == 5:
            title('Encerrando To-Do List...')
            sleep(1)
            break
