num = str(input('Digite um número entre 0 e 9999: ')).strip()
lista = []

for i in num:
    lista.append(i)

if len(lista) == 4:
    milhar = lista[0]
    centena = lista[1]
    dezena = lista[2]
    unidade = lista[3]

    print('''A lista é composta por
    milhar  = {}
    centena = {}
    dezena  = {}
    unidade = {}
    '''.format(milhar, centena, dezena, unidade))
elif len(lista) == 3:
    centena = lista[0]
    dezena = lista[1]
    unidade = lista[2]

    print('''A lista é composta por
        centena = {}
        dezena  = {}
        unidade = {}
        '''.format(centena, dezena, unidade))
elif len(lista) == 2:
    dezena = lista[0]
    unidade = lista[1]

    print('''A lista é composta por
        dezena  = {}
        unidade = {}
        '''.format(dezena, unidade))
elif len(lista) == 1:
    unidade = lista[0]

    print('''A lista é composta por
        unidade = {}
        '''.format(unidade))

'''
# Forma Guanabara
# Entrada de dados
num = int(input('Digite um número entre 0 e 9999: ))

# Unidade é divisão inteira de numero por 1 e o resultado é feito com módulo de 10
u = num // 1 % 10
# Dezena é divisão inteira de numero por 10 e o resultado é feito com módulo de 10
d = num // 10 % 10
# Centena é divisão inteira de numero por 100 e o resultado é feito com módulo de 10
c = num // 100 % 10
# Milhar é divisão inteira de numero por 1000 e o resultado é feito com módulo de 10
m = num // 1000 % 10

print('Unidade = {}'.format(u))
print('Dezena  = {}'.format(d))
print('Centena = {}'.format(c))
print('Milhar = {}'.format(m))
'''