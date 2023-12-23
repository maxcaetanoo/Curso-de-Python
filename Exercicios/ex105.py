'''Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
'''


def notas(nota, situacao=False):
    """
    => Gera um relátório com base nas notas da turma
    :param nota: Recebe uma lista de notas para 'n' alunos
    :param situacao: (Opcional) Apresenta a situação atual da turma entre: BOA, RAZOAVEL E RUIM
    :return result: Retorna um dict() das seguintes informações– Quantidade de notas – A maior nota – A menor nota –
    A média da turma – A situação (opcional)
    """
    result = dict()
    somatoria = 0
    result['Quantidade de notas:'] = len(nota)
    result['Maior nota:'] = max(nota)
    result['Menor nota:'] = min(nota)
    for i in nota:
        somatoria += i
    result['Media da turma:'] = f'{somatoria/len(nota):.1f}'

    if situacao:
        if result['Media da turma:'] >= 6:
            situa = 'BOA!'
        elif result['Media da turma:'] >= 4:
            situa = 'RAZOAVEL'
        else:
            situa = 'RUIM'
        result['Situação da turma:'] = situa
        return result
    else:
        return result


n = []
while True:
    n.append(float(input('Digite uma nota: ')))

    while True:
        opt = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if opt in 'SN':
            break
        print('Erro, digite um valor válido!')
    if opt == 'N':
        break
while True:
    situacao = str(input('Deseja mostrar situação dos alunos? [S/N]: ')).strip().upper()[0]
    if situacao in 'SN':
        if situacao == 'S':
            val = notas(n, True)
        else:
            val = notas(n)
        break
    print('\033[0;31mInvalido! Digite apenas S(para Sim) ou N(para Não).\033[m')
print()
print('-='*20)
for k, v in val.items():
    print(f'\033[1;32m{k}  \033[1;34m{v}\033[m')

help(notas)
