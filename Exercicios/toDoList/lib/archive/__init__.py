def arqExists(arq):
    try:
        archive = open(arq, 'rt')
        archive.close()
    except FileNotFoundError:
        return False
    else:
        return True


def arqCreate(arq):
    try:
        archive = open(arq, 'wt+')
        archive.close()
    except:
        print(f'Arquivo {arq} não pode ser criado.')
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def arqRead(arq):
    from time import sleep
    try:
        archive = open(arq, 'rt')
    except:
        print('Não foi possível ver as tarefas, sentimos muito.')
    else:
        for i in archive:
            tarefas = i.split(';')
            tarefas = tarefas[2].replace('\n', '')
            print(tarefas[0])
            print(f'{tarefas[0]:<10}| prazo:{tarefas[1]:<10}| {"A finalizar" if tarefas[2] == "0" else "Finalizada"}')
            sleep(1)
    finally:
        archive.close()


def arqRegister(arq, val):
    try:
        archive = open(arq, 'wt')
    except:
        print('Não foi possível cadastrar uma nova tarefa.')
    else:
        try:
            archive.write(f'{val.title};{val.date};{"1" if val.check else "0"}\n')
        except:
            print(f'Não foi possivel cadastrar a tarefa {val.title}')
        else:
            print(f'A tarefa {val.title} foi cadastrada com sucesso!')
