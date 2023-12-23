'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    print('*' * 50)
    val = int(input('Digite um valor entre 0 e 20 para ver seu nome por extenso: '))
    while val not in range(0, len(cont)):
        val = int(input('Valor invalido, Digite um valor entre 0 e 20 para ver seu nome por extenso: '))

    print(f'O valor \033[1;32m{val}\033[m por extenso é \033[1;32m{cont[val]}\033[m')
    print('*'*50)

    opt = str(input('Deseja ver mais? [S/N]: ')).strip().upper()[0]
    if opt == 'N':
        break