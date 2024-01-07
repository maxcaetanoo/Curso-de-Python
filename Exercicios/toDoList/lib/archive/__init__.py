from Exercicios.toDoList.lib import classes


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
        archive = open(arq, 'rt')
    except:
        print('Não foi possível ver as tarefas, sentimos muito.')
    else:
        for linha in archive:
            dados = linha.split(';')
            dados = dados[2].replace('\n', '')
            for n, v in enumerate(dados):
                print(f'{n} - {v}', end='')
            tarefa = classes.Tarefa(dados[0], str(dados[1]), dados[2])
            tarefas.append(tarefa)
        archive.close()

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
