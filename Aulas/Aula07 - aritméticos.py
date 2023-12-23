# Operadores aritiméticos ou matemáticos:

# + Adição
# - Subtração
# / Divisão
# * Multiplicação
# ** Potenciação
# // Divisão inteira
# % Resto da divisão
# == Igualdade

# Ordem de precedencia

# 1 - ()
# 2 - **
# 3 - *, /, //, %
# 4 - +, -

# Alinhamento com python
nome = input('Manda teu nome: ')

print('Prazer em te conhecer {:>20}!'.format(nome))
# Alinha à direita vinte espaços

# print('Prazer em te conhecer {:<20}!'.format(nome))
# Alinha à esquerda vinte espaços

# print('Prazer em te conhecer {:^20}!'.format(nome))
# Centraliza entre vinte espaços

# Definindo casas decimais
num1 = float(input('Digite um número: '))
num2 = float(input('Digite mais um número: '))

divi = num1 / num2

print('A divisão resultou em {:.5f}'.format(divi))
# Cinco casas decimais após o ponto.

# Juntando prints
print('O seu nome é {}'.format(nome), end= ' ')
# Com o end= ' ' definimos que o print vai terminar apenas com um espaço
print('E você divide como ninguem a divisão foi {:.2}'.format(divi))