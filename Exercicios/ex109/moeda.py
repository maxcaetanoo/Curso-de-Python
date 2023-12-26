def aumentar(n=0, v=0, format=False):
    a = (n * v / 100) + n
    return a if format is False else moeda(a, True)


def diminuir(n=0, v=0, format=False):
    d = n - (n * v / 100)
    return d if format is False else moeda(d, True)


def dobro(n=0, format=False):
    dob = n * 2
    return dob if format is False else moeda(dob, True)


def metade(n=0, format=False):
    m = n / 2
    return m if format is False else moeda(m, True)


def moeda(n=0, format=False):
    if format:
        n = f'R$ {n:.2f}'.replace('.', ',')
    else:
        pass
    return n
