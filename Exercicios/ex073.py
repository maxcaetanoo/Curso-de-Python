'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

# 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol na ordem de colocação.
times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR',
         'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia',
         'Santos', 'Goiás', 'Coritiba', 'América-MG')

# Depois mostre:
# a) Os 5 primeiros times.
print('-'*50)
print('Os 5 primeiros times são: ')
for n, t in enumerate(times[0: 5]):
    print(f'{n+1} - {t}')

# b) Os últimos 4 colocados.
print('-'*50)
print('Os últimos 4 colocados são: ')
for t in times[-4:]:
    print(f'{times.index(t) + 1} - {t}')

# c) Times em ordem alfabética.
print('-'*50)
print('Os times em ordem alfabética são: ')
for n, t in sorted(enumerate(times[:])):
    print(f'{n + 1} - {t}')

# d) Em que posição está o time da Chapecoense.
print('-'*50)
print('A posição está o time da Chapecoense é: ') if 'Chapecoense' in times == True \
    else print('A posição está o time da Corinthians é: ')
position = times.index('Chapecoense') if 'Chapecoense' in times == True \
    else times.index('Corinthians')
print(f'Ele é o {position + 1}º colocado')
