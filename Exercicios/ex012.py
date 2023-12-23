print('Estamos passando por uma redução de 5% nos preços dos produtos')
valor = float(input('Para que possamos clacular o novo preço de um produto nos informe seu valor: '))

desconto = valor - ((valor * 5) / 100)

print('O produto após o desconto de 5% passa a ser {}'.format(desconto))
