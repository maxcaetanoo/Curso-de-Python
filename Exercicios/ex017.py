import math

print('Vamos calcular o comprimento da hipotenusa')

co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))

h = math.sqrt(math.pow(co, 2) + math.pow(ca, 2))

print('A soma dos quadrados dos catetos é igual à porra da hipotenusa {:.2f}'.format(h))
