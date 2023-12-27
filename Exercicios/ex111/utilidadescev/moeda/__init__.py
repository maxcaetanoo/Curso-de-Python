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
