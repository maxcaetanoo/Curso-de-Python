'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from time import sleep
from random import randint
print('-=-'*20)
print('Olá, te apresento o jogo da adivinha')
print('-=-'*20)

print('Nesse jogo o nosso cumputador vai pensar em um número de 0 a 5')
pc = randint(0, 5)
print('Ummm, deixa eu ver...')
sleep(3)
print('Pronto, pensei.')

num = int(input('Digite um número inteiro de 0 a 5 para ver se você consegue adivinhar: '))

if pc == num:
    print('Parabens você acertou o valor, o valor foi {}'.format(pc))
elif pc == num+1:
    print('Poxa você errou por um, o valor é {}'.format(pc))
elif pc == num-1:
    print('Poxa você errou por um, o valor é {}'.format(pc))
elif pc == num-2:
    print('Poxa essa não foi tão perto assim, o número é {}'.format(pc))
elif pc == num+2:
    print('Poxa essa não foi tão perto assim, o número é {}'.format(pc))
elif pc == num-3:
    print('Errrooou, o valor correto é {}'.format(pc))
elif pc == num+3:
    print('Errrooou, o valor correto é {}'.format(pc))
elif pc == num-4:
    print('Foi muito longe em, o número é {}'.format(pc))
elif pc == num+4:
    print('Foi muito longe em, o número é {}'.format(pc))
elif pc == num-5:
    print('Dessa vez acho que você tentou errar com todas as forças em, o número é {}'.format(pc))
elif pc == num+5:
    print('Dessa vez acho que você tentou errar com todas as forças em, o número é {}'.format(pc))
else:
    print('Mano, acho que vc não entendeu as regras kkkk é de 0 a 5')
