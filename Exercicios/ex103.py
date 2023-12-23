'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''


def ficha(nome='<Nome não definido>', gols=0):
    """
    => O programa deverá mostrar a ficha do jogador com a quantidade de gols e o seu nome, caso nada seja digitado deve
    ser funcionar mesmo assim.
    :param nome: É o nome do jogador em str() definido pelo usuário, ou <Nome não definido> para vazio.
    :param gols: É a quantidade de gols definida pelo usuário, ou 0 para vazio.
    :return:
    """
    print(f'O jogador {nome} marcou {gols} na partida.')


name = str(input('Nome: '))
gol = str(input('Gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if name.strip() == '':
    ficha(gols=gol)
else:
    ficha(name, gol)

