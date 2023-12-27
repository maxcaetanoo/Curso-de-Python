'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''
import urllib.error
import urllib.request

try:
    urllib.request.urlopen('https://pudim.com.br/')
except urllib.error.URLError:
    print('Não conectado!')
else:
    print('Conectado com sucesso!')
