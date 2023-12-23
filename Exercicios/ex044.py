'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''

produto = float(input('Digite o valor de um produto R$: '))
print('''Selecione a condiçãod e pagamento
         1 - À vista dinheiro/cheque(10% desconto)
         2 - À vista cartão(5% desconto)
         3 - 2X cartão(Sem descontos)
         4 - 3x ou mais cartão(20% juros)''')
opcao = int(input('Digite a opção: '))

if opcao == 1:
    desconto = produto * 10 / 100
    print('O seu desconto foi de R${:.2f}, o valor final é de R${:.2f}'.format(desconto, produto - desconto))
elif opcao == 2:
    desconto = produto * 5 / 100
    print('O seu desconto foi de R${:.2f}, o valor final é de R${:.2f}'.format(desconto, produto - desconto))
elif opcao == 3:
    parcela = produto / 2
    print('O seu produto custa o valor integral de R${:.2f}, você pagará duas parcelas de R${:.2f}'.format(
        produto, parcela))
elif opcao == 4:
    juros = produto * 20 / 100
    parcela = int(input('Defina a quantidade de parcelas que deseja pagar entre 3X e 12X: '))
    print('O produto teve um acrécimo de R${:.2f}, o valor final ficou em R${:.2f}'
          '\nVocê escolheu dividir em {}X suas parcelas serão de R${:.2f}'.format(
        juros, produto+juros, parcela, (produto+juros)/parcela))
else:
    print('Opção não válida, tente novamente mais tarde.')