'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


num = int(input('Digite um numero inteiro: '))
fator = fatorial(num)
print(f'O fatorial de {fator}')'''


def ehPar(n):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um valor: '))
if ehPar(num):
    print(f'{num} é par!')
else:
    print(f'{num} não é par!')
