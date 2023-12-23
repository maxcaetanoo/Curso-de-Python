altura = float(input('Digite a altura da parede que será considerada: '))
largura = float(input('Digite a largura da parede que será considerada: '))

area = altura * largura

print('A área da parede em questão é de {}'.format(area))

tinta = area / 2

print('A quantidade de tinta necessária é {}L para a área de {}M quadrados'.format(tinta, area))
