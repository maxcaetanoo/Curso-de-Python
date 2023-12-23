# Primeira forma de construir uma lista composta
print('Estrutura composta 1')
teste = list()# Criando uma lista
teste.append('Maxsuel')# Adicionando um valor [0]
teste.append(26)# Adicionando outro valor [1]

galera = []# Criando uma lista composta
galera.append(teste[:])# Fazendo uma cópia dos valores de teste[]

teste[0] = ('Milena')# Alterando o valor de teste[0]
teste[1] = (24)# Alterando o valor de teste[1]

galera.append(teste[:])# Fazendo uma cópia dos valores de teste[]

print(galera)# Exibindo os valores salvos em galera que são [['Maxsuel', 26], ['Milena', 24]]

print('-'*50)
# Segunda forma de construir uma lista composta
print('Estrutura composta 2')

gente = [['João', 20], ['Maria', 25], ['Maxsuel', 26], ['Milena', 25]]# Criando a lista já com as sub-listas inclusas
print(gente)# Exibindo gente [['João', 20], ['Maria', 25], ['Maxsuel', 26], ['Milena', 25]]

# Print com fatiamento da lista e sub-lista
print(gente[1][1])# Exibindo o valor da lista 1 sub-lista 1 que seria 25

# Populando lista através do for
pessoas = []# Lista de pessoas
dados = []# Coleta de dados de pessoas
for data in range(0, 3): # laço de repetição
    dados.append(str(input('Nome: ')))# Inserção do dado na posição [0]
    dados.append(int(input('Idade: ')))# Inserção do dado na posição [1]
    pessoas.append(dados[:])# Cópia de todos os dados anteriormente inseridos para a lista de pessoas
    dados.clear()# Limpesa dos dados preenchidos na lista de dados

print(pessoas)# Exibindo dados coletados
