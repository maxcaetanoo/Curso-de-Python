from math import floor
print('Arredondador de real para baixo')

# entrada
num = float(input('Digite um número real: '))

# processamento
redondo = floor(num)

# saída
print('O número {} arredondado é {}'.format(num, redondo))
