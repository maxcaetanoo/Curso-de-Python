'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''


def leiaInt(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um valor inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'\033[1;32mO valor digitado foi {n}\033[m')
