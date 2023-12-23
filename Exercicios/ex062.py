'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

init = int(input('Digite o termo inicial da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = init
cont = 1
total = 0
mais = 10
text = '{} -> '.format(termo)

while mais != 0:
    total += mais
    while cont <= total:
        termo += razao
        text += '{} -> '.format(termo)
        cont += 1
    print(text)
    mais = int(input('Digite 0 para sair ou qualquer número para aumentar a quantidade de opções: '))

print('\n\nEncerramos em com um total de {} termos: \n{} \033[1;32mFIM'.format(total, text))
