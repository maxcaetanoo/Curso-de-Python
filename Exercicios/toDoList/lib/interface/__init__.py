from datetime import datetime

from Exercicios.toDoList.lib import archive
from Exercicios.toDoList.lib.classes import Tarefa


def title(t):
    print('-' * 40)
    print(f'\033[1;32m{t:^40}\033[m')
    print('-' * 40, end='\n')


def menu(arq='list.txt'):
    from time import sleep
    title('Bem vindo ao To-Do List')

    menus = ["Ver tarefas", "Criar nova tarefa", "Adiar tarefa", "Finalizar tarefa", "Sair do To-Do List"]

    while True:
        for i, v in enumerate(menus):
            print(f'\033[34m{i + 1:<2}\033[m- \033[34m{v:<10}\033[m')

        print('-' * 40)
        select = int(input('Digite o indice da opção desejada: '))
        print('-' * 40, end='\n')

        if select == 1:
            title(menus[select - 1])
            sleep(1)
            reader = archive.arqRead(arq)
            reading(reader)
        elif select == 2:
            title(menus[select - 1])
            sleep(1)
            register(arq)
        elif select == 3:
            title(menus[select - 1])
            sleep(1)
            pass
        elif select == 4:
            title(menus[select - 1])
            sleep(1)
            pass
        elif select == 5:
            title('Encerrando To-Do List...')
            sleep(1)
            break


def register(arq='list.txt'):
    tarefas = []

    while True:
        title = str(input('Digite o nome da tarefa: '))
        try:
            date = str(input('Digite o dia e mês da tarefa separados por /: ')).strip()
            while True:
                order = date.strip().split('/')
                if order[0].isnumeric() and order[1].isnumeric() and len(order[0]) < 3 and len(order[1]) < 3:
                    orderDate = f'{order[0]}-{order[1]}-{datetime.now().year}'
                else:
                    print(f'Formato {date} é um formato de data inválido, estamos cadastrando com o dia e mês atuais.')
                    orderDate = f'{datetime.now().day}-{datetime.now().month}-{datetime.now().year}'
                date = orderDate
                break
        except:
            print('houve um erro ao cadastrar a data, estamos cadastrando com o dia e mês atuais.')
            dates = f'{datetime.now().day}-{datetime.now().month}-{datetime.now().year}'
        else:
            dates = date
        check = 0

        tarefa = Tarefa(title, dates, check)
        tarefas.append(tarefa)

        opt = ' '
        while opt not in 'SN':
            opt = str(input('Deseja cadastrar mais uma tarefa? [S/N] ')).strip().upper()[0]
            if opt in 'SN':
                break
            else:
                print(f'valor {opt} não é uma opção válida, digite uma opção válida.')

        if opt == 'N':
            break

    registers = archive.arqRead(arq)
    registers.extend(tarefas)

    archive.arqRegister(registers, arq)


def reading(l):
    from time import sleep
    for i in l:
        print(f'{i[0]:<10}| prazo:{i[1]:^20}| {"A fazer" if i[2] == "0" else "Finalizada"}')
        sleep(1)
