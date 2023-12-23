'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

products = ('Smatphone', 1350.00, 'Fogão', 799.90, 'Frigobar', 898.99, 'Monitor Gamer', 1260.00)

print("="*50)
print(f'{"Produtos":^50}')
print("="*50)
for i in range(0, len(products)):
    if i % 2 == 0:
        print(f'{products[i]:.<39}', end='')
    else:
        print(f'R$ {products[i]:>8.2f}')
print("_"*50)
