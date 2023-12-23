'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

distancia = float(input('Digite a distancia da viagem: Km'))

if distancia > 200.00:
    valor = distancia * .45
    print('O custo da viagem baseado na kilometragem digitada é R${:.2f}'.format(valor))
else:
    valor = distancia * .50
    print('O custo da viagem baseado na kilometragem digitada é R${:.2f}'.format(valor))

print('Agora que já sabe o valor, vamos viajar?')
