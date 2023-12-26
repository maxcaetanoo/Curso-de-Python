def aumentar(n):
    a = (n * 10 / 100) + n
    return a


def diminuir(n):
    d = n - (n * 15 / 100)
    return d


def dobro(n):
    dob = n * 2
    return dob


def metade(n):
    m = n / 2
    return m


def moeda(n, boll=False):
    if boll:
        n = f'R$ {n:.2f}'.replace('.', ',')
        return n
