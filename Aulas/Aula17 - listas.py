# Lista é criada com colchetes [ ]
num = [2, 5, 9, 1]

# Subistituindo o 9 pelo 3
num[2] = 3

# Adicionando o valor 7 ao fim da lista
num.append(7)

# Ordenando a lista inversamente
num.sort(reverse=True)

# Inserindo o valor 2 no inicio da lista
num.insert(0, 2)

# Removendo o ultimo item da lista
num.pop()

# Removendo o valor 2
num.remove(2) # Só remove a primeira vez que o npumero aparece

# Remover um valor sem saber se ele existe
num.remove(4) if 4 in num else print('Não encontrado.')

# Mostrando o tamanho da lista
print(len(num))

# Mostrando a lista completa
print(num)

# Pegando chave e valor
for c, v in enumerate(num):
    print(f'A chave é {c} e o valor é {v}')

# Criando uma nova lista
a = [1, 2, 3, 4]
b = a # recebendo ela através de outra lista
b[2] = 5 # Alterando o valor da lista B
# Resultado, a lista A também será alterada no indice 2
print(f'Lista A: {a} - Lista B: {b}')

# Criando uma nova lista
a = [1, 2, 3, 4]
b = a[:] # Recebendo uma cópia de todos os valores de A através de B
b[2] = 5 # Alterando o valor da lista B
# Resultado, a lista A não será alterada no indice 2
print(f'Lista A: {a} - Lista B: {b}')
