from datetime import datetime

from Exercicios.toDoList.lib import archive
from Exercicios.toDoList.lib.classes import Tarefa


def title(t):
    print('=' * 52)
    print(f'\033[1;32m{t:^40}\033[m')
    print('=' * 52, end='\n')


def menu(arq='list.txt'):
    from time import sleep
    title('Bem vindo ao To-Do List')

    menus = ["Ver tarefas", "Criar nova tarefa", "Adiar tarefa", "Finalizar tarefa", "Sair do To-Do List"]

    while True:
        print('-' * 52)
        for i, v in enumerate(menus):
            print(f'\033[34m{i + 1:<2}\033[m- \033[34m{v:<10}\033[m')

        print('-' * 52)
        select = int(input('Digite o indice da opção desejada: '))
        print('-' * 52, end='\n')

        if select == 1:
            title(menus[select - 1])
            sleep(1)
            reader = archive.arqRead(arq)
            read(reader)
        elif select == 2:
            title(menus[select - 1])
            sleep(1)
            register(arq)
        elif select == 3:
            title(menus[select - 1])
            sleep(1)
            reader = archive.arqRead(arq)
            updateDate(reader, arq)
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
        date = datesReg('Digite o dia e o mês separados por "/" igual o modelo ao lado [00/00]: ')
        check = "0"

        tarefa = Tarefa(title, date, check)
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


def datesReg(txt):
    try:
        date = str(input(txt)).strip()
        while True:
            order = date.strip().split('/')
            if order[0].isnumeric() and order[1].isnumeric() and len(order[0]) < 3 and len(order[1]) < 3:
                orderDate = f'{order[0]}-{order[1]}-{datetime.now().year}'
            else:
                print(f'Formato {date} é um formato de data inválido, estamos cadastrando com o dia e mês atuais.')
                orderDate = f'{datetime.now().day}-{datetime.now().month}-{datetime.now().year}'
            date = orderDate
            break
        dates = date
    except:
        print('houve um erro ao cadastrar a data, estamos cadastrando com o dia e mês atuais.')
        dates = f'{datetime.now().day}-{datetime.now().month}-{datetime.now().year}'
    finally:
        return dates


def read(l):
    from time import sleep

    print(f'{"ID":>3} | {"TAREFA":<10}| {"PRAZO":^12} | {"SITUAÇÃO"}')
    print('-' * 52)
    for i, v in enumerate(l):
        print(f'{i+1:>3}', end=' | ')
        print(f'{v.title:<10}| {v.date:^12} | {"A fazer" if v.check == "0" else "Finalizada"}')
        sleep(1)
    print('-' * 52)


def updateDate(leitura, arq):
    try:
        read(leitura)

        update = int(input(f'Digite o ID do valor que deseja adiar: '))
        print('Para adiar o prazo basta digitar o dia e o mês atualizados')
        date = datesReg('Digite o dia e o mês separados por "/" igual o modelo ao lado [00/00]: ')

        dates = leitura[update - 1]
        before = str(dates.date)
        now = dates.date = date

        tarefa = Tarefa(dates.title, now, dates.check)
    except:
        print('Não foi possível editar a data!')
    else:
        registers = archive.arqRead(arq)
        del registers[update-1]
        registers.insert(update-1, tarefa)

        archive.arqRegister(registers, arq)
        print(f'Tarefa adiada de {before} para {now} com sucesso!')
