print('Conversor de medidas')

metro = float(input('Digite um valor em metros para que possamos converter \nEm Milimetros ou em Centimetros: '))

print('M - Milimetros')
print('C - Centimetros')
opcao = str(input('Digite qual a conversão que deseja: '))

if opcao == 'M' or opcao == 'm':
    mil = metro * 1000
    print('A conversão em Milimetros é {}'.format(mil))

elif opcao == 'C' or opcao == 'c':
    cen = metro * 100
    print('A conversão em Centimetros é {}'.format(cen))

else:
    print('Opção inválida...')
