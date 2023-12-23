# Típos primitivos
# int : numéros inteiros
# int = 1, 23, 1980, 3000056

# float : números de ponto flutuante
# float = 1.1, 230.43, 1690.5, 23.0

# bool : condições lógicas, verdadeio e falso
# bool = True ou False

# str : textos ou conjuntos de caracteres textuais
# str = 'Olá', 'Meu nome é robervaldo', 'etc', '12'

# # Desafio da aula 5 que deu errado
# # Entrada de valores
# n1 = input('Digite um número: ')
# n2 = input('Digite outro número: ')
#
# # Processamento
# soma = n1 + n2
#
# # Saída de dados
# print('A soma é: {}'.format(soma))

#Como resolver
# Entrada de valores
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

# Processamento
soma = n1 + n2

# Saída de dados
print('A soma é: {}'.format(soma))

# Podemos ver o típo com o comando type
print(type(soma))
