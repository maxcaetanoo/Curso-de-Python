def aumentar(n=0, v=0, format=False):
    '''
    => Aumenta um percentual do valor definido
    :param n: Número digitado pelo usuário que será considerado para o cálculo
    :param v: Valor de acrecimo recebido através de outro método
    :param format: Bool que define se haverá ou não formatação dos valores.
    :return: Retorna valor da variavél "a" após o acrecimo
    '''
    a = (n * v / 100) + n
    return a if format is False else moeda(a, True)


def diminuir(n=0, v=0, format=False):
    '''
    => Diminui um percentual do valor definido
    :param n: Número digitado pelo usuário que será considerado para o cálculo
    :param v: Valor de decrecimo recebido através de outro método
    :param format: Bool que define se haverá ou não formatação dos valores.
    :return: Retorna valor da variavél "d" após o decrecimo
    '''
    d = n - (n * v / 100)
    return d if format is False else moeda(d, True)


def dobro(n=0, format=False):
    '''
    => Calcula o dobro do valor definido
    :param n: Número digitado pelo usuário que será considerado para o cálculo
    :param format: Bool que define se haverá ou não formatação dos valores.
    :return: Retorna valor da variavél "dob" após o dobrar o valor
    '''
    dob = n * 2
    return dob if format is False else moeda(dob, True)


def metade(n=0, format=False):
    '''
    => Calcula a metade do valor definido
    :param n: Número digitado pelo usuário que será considerado para o cálculo
    :param format: Bool que define se haverá ou não formatação dos valores.
    :return: Retorna valor da variavél "m" após o dividir o valor ao meio
    '''
    m = n / 2
    return m if format is False else moeda(m, True)


def moeda(n=0, format=False):
    '''
    => Formata os valores para padrão monetario em R$(Real Brasileiro)
    :param n: Número digitado pelo usuário que será considerado para o cálculo
    :param format: Bool que define se haverá ou não formatação dos valores.
    :return: Retorna valor da variavél "n" após formatar o número e converter em Str
    '''
    if format:
        n = f'R$ {n:.2f}'.replace('.', ',')
    else:
        pass
    return n


def resumo(v, a, s):
    '''
    => Exibe a tabela formatada de resumo dos metodos contidos em moeda.py
    :param v: Valor Float digitado em ex112.py ou qualquer outro arquivo que usar esse pacote
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
    print(f'\t{moeda(v, True)}')
    # L2
    print('Dobro do preço:', end=f'{" "*10}')
    print(f'\t{dobro(v, True)}')
    # L3
    print('Metade do preço:', end=f'{" "*10}')
    print(f'\t{metade(v, True)}')
    # L4
    print(f'Preço mais {a}%:', end=f'{" "*10}')
    print(f'\t{aumentar(v, a, True)}')
    # L5
    print(f'Preço menos {s}%:', end=f'{" "*10}')
    print(f'\t{aumentar(v, s, True)}')