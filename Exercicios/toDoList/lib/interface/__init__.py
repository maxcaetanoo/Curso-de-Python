def menu():
    print('-'*40)
    print(f'{"Bem vindo ao To-Do List":^40}')
    print('-' * 40, end='\n')

    menus = ["Ver tarefas", "Criar nova tarefa", "Adiar tarefa", "Remover tarefa", "Sair do To-Do List"]

    for i, v in enumerate(menus):
        print(f'{i:<2}- {v:<10}')