# Ler nome completo
nome = str(input('Digite o seu nome completo: '))

# nome com todas as letras maiusculas e minúsculas
print(nome.upper())
print(nome.lower())

# Quantas letras tem ao todo sem considerar os espaços
print(len(nome) - nome.count(' '))

# Quantas letras tem o primeiro nome
print(len(nome[:nome.find(' ')]))
