from datetime import datetime

from Exercicios.toDoList.lib import archive
from Exercicios.toDoList.lib.classes import Tarefa


def title(t):
    print('-' * 40)
    print(f'\033[1;32m{t:^40}\033[m')
    print('-' * 40, end='\n')


def menu(arq):
    from time import sleep
    title('Bem vindo ao To-Do List')

    menus = ["Ver tarefas", "Criar nova tarefa", "Adiar tarefa", "Finalizar tarefa", "Sair do To-Do List"]

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
            register(arq)
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


def register(arq):
    tarefa = Tarefa
    tarefa.title = str(input('Digite o nome da tarefa: '))
    try:
        date = str(input('Digite o dia e mês da tarefa separados por /: ')).strip()
        while True:
            order = date.split('/')
            if order[0].isnumeric() and order[1].isnumeric() and len(order[0]) < 3 and len(order[1]) < 3:
                ordeDate = f'{order[0]}/{order[1]}/{datetime.now().year}'
            else:
                print(f'Formato {date} é um formato de data inválido, estamos cadastrando com o dia e mês atuais.')
                ordeDate = f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year}'
            date = ordeDate
            break
    except:
        print('houve um erro ao cadastrar a data, estamos cadastrando com o dia e mês atuais.')
        date = f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year}'
    else:
        tarefa.date = date
    tarefa.check = False

    archive.arqRegister(arq, tarefa)
