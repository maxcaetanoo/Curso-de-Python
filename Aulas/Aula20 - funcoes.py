'''# Função para somar dois valores
def some(a, b):
    soma = a + b
    print(soma)


# Laço de repetição para repetir essa função
while True:
    # Chamada da função passando os dois valores através de entrada de texto
    some(int(input('Digite um número ')), int(input('Digite outro numero ')))

    while True:
        opt = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if opt not in 'SN':
            print('Erro digite um valor válido')
        elif opt == 'N':
            print('Saindo...')
            break
        else:
            break
    if opt == 'N':
        break'''

'''from random import randint


# Desmpacotador representado o * antes do parâmetro, e permite mais valores sem precisar definir a quantidade.
def contador(*num):
    print(len(num))


contador(1, 3, 5, 6, 8)'''


def dobra(list):
    for i in range(0, len(list)):
        list[i] *= 2


valores = [1, 3, 5, 7, 8]
dobra(valores)
print(valores)
