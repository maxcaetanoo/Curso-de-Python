'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mErro, digite um valor válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mAntrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            v = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31mErro, digite um valor válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mAntrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


n = leiaInt('Digite um número inteiro: ')
print(f'\033[1;32mO valor digitado foi {n}\033[m')
n = leiaFloat('Digite um número real: ')
print(f'\033[1;32mO valor digitado foi {n}\033[m')
