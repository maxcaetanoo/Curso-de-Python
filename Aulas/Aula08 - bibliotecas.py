# biblioteca
from math import sqrt, floor

# entrada de valor
num = int(input('Digite um número: '))

# processamento
raiz = sqrt(num)
# sqrt serve para calcular a raiz quadrada

# saída
print('A raiz de {} é igual a {}'.format(num,floor(raiz)))
# ceil serve para arredondar para cima o valor e floor para baixo
