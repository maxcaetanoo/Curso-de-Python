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
    from time import sleep
    tarefas = []
    try:
        archive = open(arq, 'rt')
    except:
        print('Não foi possível ver as tarefas, sentimos muito.')
    else:
        for indice, linha in enumerate(archive):
            dados = linha.split(';')
            dados[2] = dados[2].replace('\n', '')
            tarefa = Tarefa(dados[0], dados[1], dados[2])
            tarefas.append(tarefa)
        archive.close()
    finally:
        return tarefas


def arqRegister(val, arq='list.txt'):
    try:
        archive = open(arq, 'wt')
    except:
        print('Não foi possivel ler o arquivo.')
    else:
        for l in val:
            archive.write(f"{l.title};{l.date};{str(l.check)}\n")
        archive.close()
