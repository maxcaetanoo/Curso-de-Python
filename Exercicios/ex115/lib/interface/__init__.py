def linha(tam = 40):
    l = '-'* tam
    return l


def cabecalho(txt):
    print(linha())
    print(f'{txt:^40}')
    print(linha())


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mErro, digite um valor válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def menu(lista):
    cabecalho('Menu Principal')

    for i, v in enumerate(lista):
        print(f'{i+1} - \033[1;34m{v}\033[m')
    opt = leiaInt('\033[32mDigite um valor: \033[m')
    return opt
