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
        print(a.read())
