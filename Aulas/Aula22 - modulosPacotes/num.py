# Código simples para modularizar funções
import utils

num = int(input('Digite um valor inteiro: '))
fat = utils.fatorial(num)
dob = utils.dobro(num)
tri = utils.triplo(num)

print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dob}')
print(f'O triplo de {num} é {tri}')
