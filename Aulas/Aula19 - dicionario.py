# Criando um dicionário
pessoa = {'nome': 'Maxsuel', 'idade': 26, 'sexo': 'M'}
print(pessoa)
print('\n')

# Exibindo o nome de forma literal
print(pessoa['nome'])
print('\n')

# Print formatado com dados do dicionário
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos de idade')
print('\n')

# Printando chaves, valores e itens
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print('\n')

# Deletando apartir de chaves
del pessoa['sexo']

# For keys, values e items

# Keys
for k in pessoa.keys():
    print(k)
print('\n')

# Values
for v in pessoa.values():
    print(v)
print('\n')

# Items
for k, v in pessoa.items():
    print(f'{k} = {v}')
print('\n')

# Alterando valores através das chaves
pessoa['nome'] = 'Max'
print(pessoa)
print('\n')

# Adicionando um novo indice
pessoa['sexo'] = 'M'
print(pessoa)
print('\n')

# Copiando dados de um dicionário para uma lista
estado = dict()
brasil = list()
for e in range(0, 3):
    estado['uf'] = str(input('Digite o estado: '))
    estado['sigla'] = str(input('Digite a sigla: '))
    brasil.append(estado.copy())
print(brasil)
print('\n')

# Print formatado de uma lista que contem um dicionário
for b in brasil:
    for k, v in b.items():
        print(f'O {k} tem valor {v}')
print('\n')

