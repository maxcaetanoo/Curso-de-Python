from Exercicios.toDoList.lib.classes import Tarefa


def arqExists(arq='list.txt'):
    try:
        archive = open(arq, 'rt')
        archive.close()
    except FileNotFoundError:
        return False
    else:
        return True


def arqCreate(arq='list.txt'):
    try:
        archive = open(arq, 'wt+')
        archive.close()
    except:
        print(f'Arquivo {arq} não pode ser criado.')
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def arqRead(arq='list.txt'):
    tarefas = []
    try:
        with open(arq, 'rt') as archive:
            for indice, linha in enumerate(archive):
                dados = linha.split(';')
                dados[2] = dados[2].replace('\n', '')
                tarefa = Tarefa(dados[0], dados[1], dados[2])
                tarefas.append(tarefa)
    except:
        print('Não foi possível ver as tarefas, sentimos muito.')
    finally:
        return tarefas


def arqRegister(val, arq='list.txt'):
    try:
        with open(arq, 'wt') as archive:
            for l in val:
                archive.write(f"{l.title};{l.date};{str(l.check)}\n")
    except:
        print('Não foi possivel ler o arquivo.')
