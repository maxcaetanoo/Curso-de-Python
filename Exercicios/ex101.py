'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''


def voto(ano):
    """
    Calcula se uma pessoa 'X' tem a situação de voto: NEGADO, OPCIONAL e OBRIGATÓRIO
    :param ano: parametro que recebe valor inteiro correspondente ao ano de nascimento
    :return txt: str() com texto falando sobre a situação de voto.
    """
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade > 60 or idade < 18 or idade == 16:
        text = 'OPCIONAL'
    elif idade < 16:
        text = 'NEGADO'
    else:
        text = 'OBRIGATÓRIO'
    txt = f'A situação de voto para quem tem {idade} é {text}'
    return txt


print(help(voto))

nascimento = int(input('Digite o ano de nascimento: '))
print('-' * 50)
print(voto(nascimento))
print('-' * 50)

