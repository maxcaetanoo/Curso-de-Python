import asyncore


def containsArq(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def create(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print(f'Houve um erro na criação do arquivo {arq}')
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def readArch(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro, não foi possível ler o arquivo.')
    else:
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'\033[1;35m{dado[0]:<30}{dado[1]:>3} anos\033[m')
    finally:
        a.close()


def cadastrar(arq, nome='<Desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Um erro inesperado aconteceu!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Aconteceu um erro no escrita dos dados.')
        else:
            print(f'{nome} adcionado com sucesso.')
