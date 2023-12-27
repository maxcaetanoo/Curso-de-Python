from Exercicios.ex111.utilidadescev import moeda


def leiaDinheiro(val):
    '''
    => Testa se é um valor monetário válido
    :param val: Valor de Str recebido pelo programa principal
    :return: Float da variavel dinheiro após a validação
    '''
    while True:
        dinheiro = str(input(val)).replace(',', '.').strip()

        if dinheiro.isalpha() or dinheiro == '':
            print(f'\033[31mErro! \"{dinheiro}\" é um valor inválido!\033[m')
        else:
            return float(dinheiro)
