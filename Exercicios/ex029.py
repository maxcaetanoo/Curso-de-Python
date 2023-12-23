'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

# Lendo velocidade
velocidade = float(input('Digite qual foi a velocidade do veículo: '))

# Testando se foi multado
if velocidade > 80.0:
    print('Você foi multado por estar a {:.1f}Km/h'.format(velocidade))
    print('Sua multa foi de R${:.2f} para a velocidade de {:.1f}'.format((velocidade-80.0)*7.0, velocidade))
# Testando se não foi multado
else:
    print('Fica de boa, não vai ter multa')
print('Tenha um ótimo dia e dirija com cuidado!')
