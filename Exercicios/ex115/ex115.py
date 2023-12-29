from time import sleep

from Exercicios.ex115.lib import archive, interface

arch = 'pessoas.txt'
if not archive.containsArq(arch):
    archive.create(arch)

while True:
    lista = ['Ver pessoas cadastradas;', 'Cadastrar pessoa;', 'Sair do sistema.']
    opt = interface.menu(lista)

    if opt == 1:
        interface.cabecalho('Ver Pessoas Cadastradas')
        archive.readArch(arch)
    elif opt == 2:
        interface.cabecalho('Cadastrar Pessoa')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        archive.cadastrar(arch, nome, idade)
    elif opt == 3:
        interface.cabecalho('Saindo do Sistema...')
        break
    else:
        print('\033[31mErro, opção inválida!')
        print('Tente novamente!\033[m')
    sleep(2)
