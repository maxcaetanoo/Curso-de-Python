from Exercicios.ex111.utilidadescev import moeda


def resumo(v, a, s):
    '''
    => Exibe a tabela formatada de resumo dos metodos contidos em moeda.py
    :param v: Valor Float digitado em ex111.py ou qualquer outro arquivo que usar esse pacote
    :param a: Valor que será feito o acrecimo/adição percentual Int
    :param s: Valor que será feito o decrecimo/subtração percentual Int
    :return: N/A
    '''
    # Titulo
    print('-'*40)
    print(f'{"Resumo":^40}')
    print('-'*40)

    # L1
    print('Preço digitado:', end=f'{" "*10}')
    print(f'\t{moeda.moeda(v, True)}')
    # L2
    print('Dobro do preço:', end=f'{" "*10}')
    print(f'\t{moeda.dobro(v, True)}')
    # L3
    print('Metade do preço:', end=f'{" "*10}')
    print(f'\t{moeda.metade(v, True)}')
    # L4
    print(f'Preço mais {a}%:', end=f'{" "*10}')
    print(f'\t{moeda.aumentar(v, a, True)}')
    # L5
    print(f'Preço menos {s}%:', end=f'{" "*10}')
    print(f'\t{moeda.aumentar(v, s, True)}')