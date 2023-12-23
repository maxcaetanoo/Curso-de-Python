'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('Palavra', 'Texto', 'Vogais', 'Paragrafos', 'Consoantes', 'Tuplas', 'Coisas', 'Alfabeto')
cont = 0
vogais = ''

while True:
    for i in palavras:
        print(f'{palavras.index(i)+1:-<30}{i:->10}')

    opt = int(input('Digite o número da palavra desejada de 1 a 8 ou 0 para sair: '))
    if opt == 0:
        break
    while True:
        if opt > len(palavras) or opt < 0:
            opt = int(input('Opção inválida, tente novamente com uma opção entre 1 e 8 ou 0 para sair: '))
        else:
            break
    if opt == 0:
        break

    print('='*50)
    print(f'{"A palavra selecionada foi: "}\033[1;32m{palavras[opt-1]:>15}\033[m')
    for v in palavras[opt-1]:
        if v.lower() in 'aeiou':
            cont += 1
            vogais += f'{v.lower()} '
    print(f'Essa palavra tem \033[1;34m{cont}\033[m vogais que são \033[1;34m{vogais}\033[m')
    print('=' * 50)
