'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa,o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
print('#'*35)
print('Bem vindo ao banco 30, onde só é aprovado o emprestimo se for menor ou igual a 30% da sua renda salárial')
print('#'*35)

casa = float(input('Digite o valor da casa desejada: '))
sal = float(input('Digite quanto você recebe de salário: '))
ano = int(input('Digite em quantos anos será feito o pagamento: '))

prestacao = casa / (ano * 12)

print('#'*35)
if prestacao > (sal * 30)/100:
    print('Infelizmente você não pode obter um emprestimo para uma casa no valor de {:.2f}'
          '\nPois a prestação de {:.2f} excede 30% do valor do seu salário'.format(casa, prestacao))
elif prestacao == (sal *30)/100:
    print('Parabéns você pode obter um emprestimo para uma casa no valor de {:.2f}'
          '\nPois a prestação de {:.2f} é igual a 30% do valor do seu salário\n'
          'Ufa, foi por pouco.'.format(casa, prestacao))
else:
    print('Parabéns você pode obter um emprestimo para uma casa no valor de {:.2f}'
          '\nPois a prestação de {:.2f} é inferior a 30% do valor do seu salário\n'
          'Parabens, que salário gordo!'.format(casa, prestacao))
print('#'*35)

print('Tenha um ótimo dia e volte sempre')
