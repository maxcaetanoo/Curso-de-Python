'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e segundo chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''


def fatorial(num, show=False):
    """
    Função que apresenta o resultado do calculo fatorial (Opicional mostra também o processo do calculo.)
    :param num: Numero int() que será utilizado para o calculo.
    :param show: Valor lógico True or False para se deve ou não ser exibido o processo de calculo.
    :return: N/A
    """
    from time import sleep
    fator = 0
    text = ''
    cont = 0
    if show:
        for i in range(num, 0, -1):
            if cont == 0:
                fator = i
                print(f'{i}! = \033[1;34m{i} x ', end='')
                sleep(.5)
            else:
                fator *= i
                print(f'{i} x ', end='') if i > 1 else print(f'{i}\033[m', end=' ')
                sleep(.5)
            cont += 1
        print(f'= \033[1;32m{fator}\033[m')
    else:
        for i in range(num, 0, -1):
            if cont == 0:
                fator = i
            else:
                fator *= i
            cont += 1
        print(f'Resultado é = \033[1;32m{fator}\033[m')


opt = ' '
show = bool(False)
val = int(input('Digite o valor para calcular o seu fatorial: '))
while opt not in 'SN':
    opt = str(input('Deseja que apareça o calculo? [S/N]: ')).upper().strip()[0]
    if opt == 'S':
        show = True
        fatorial(val, show)
    else:
        fatorial(val)
