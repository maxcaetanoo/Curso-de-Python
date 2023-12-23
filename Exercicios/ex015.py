km = float(input('Digite quantos Km você rodou na sua viagem: Km'))
dias = int(input('Digite quantos dias você passou com o carro: '))

diaria = dias*60
kilometragem = km*.15
print('Considerando que para cada Km rodado você pagará R$0,15 então de acordo com os Km rodados você pagará {:.2f}'.format(kilometragem))
print('Considerando que a cada dia você pagará R$60 então o valor pago por dias é {:.2f}'.format(diaria))

total = diaria + kilometragem
print('O total pago será {:.2f}'.format(total))
