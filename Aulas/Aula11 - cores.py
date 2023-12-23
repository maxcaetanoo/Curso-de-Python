'''
Style: 0 = none, 1 = bold, 4 = underline, 7 = negative
Text: 30=branco, 31=vermelho, 32=verde, 33=amarelo, 34=azul_claro, 35=roxo, 36=ciano, 37=cinza
background: 30=branco, 31=vermelho, 32=verde, 33=amarelo, 34=azul_claro, 35=roxo, 36=ciano, 37=cinza
'''
# Código ANSI in line
print('\033[7;36;41mOlá mundo!\033[m')

# Format código ANSI
nome = 'Max'
print('Olá, prazer em te conhecer {}{}{}!'.format('\033[4;34m', nome, '\033[m'))

# Dictionary ANSI
cores = {
    'limpar':'\033[m',
    'underlineazul':'\033[4;34m'
}
print('Olá {}{}{}'.format(cores['underlineazul'],nome, cores['limpar']))
