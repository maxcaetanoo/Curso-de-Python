# Print comum, mostra toda a frase
frase = 'Curso em Vídeo Python'
print(frase)

# Print fatiado começando do indice 9 e indo até o final
print(frase[9:])

# Print fatiado começando do indice 0 e indo até o 9
print(frase[:10]) # Note que foi adcionado um indice a mais, essa é apenas a marca de corte, ela não deve aparecer

# Print fatiado pulando de 2 em 2
print(frase[::2])

# Print com mais de uma linha
print("""Uma coisa
qualquer para
testar esse texto """)

# Print com count para contar uma string específica
print(frase.count('e')) # Aqui ele apresenta o valor 2 pois existem duas letras 'e' no texto

# Print com o len para saber o tamanho da frase
print(len(frase))

# Adcionando espaços no texto frase com o format
frase = '  {}  '.format(frase)
print(frase)

# Removendo os espaços da esquerda de frase
print(frase.lstrip())

# Removendo os espaços da direita de frase
print(frase.rstrip())

# Removendo os espaços de antes e depois da frase exceto os do meio
frase = frase.strip()
print(frase)

# Alterando parte do texto da frase
print(frase.replace('Python', 'PY'))

# Confirmando se contem uma palavra em frase
print('em' in frase)

# Informa onde inicia um texto em frase caso exista
print(frase.find('Python'), 'Python') # Esse existe e começa a partir da posição 15
print(frase.find('Java'), 'Java') # Esse não existe por isso inicia da posição -1(dando noção de que falta)

# Caixa alta
print(frase.upper())

# Caixa baixa
print(frase.lower())

# Capitular titulo
print(frase.capitalize())

# Separando em lista
print(frase.split())
