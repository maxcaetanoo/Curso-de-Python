# # Entrada de valores
# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
#
# # Processamento
# soma = n1 + n2
#
# # Saída de dados
# print('A soma entre {} e {} é: {}'.format(n1, n2, soma))

var = input('Diga o que és e eu te direi quem sou: ')

print('Sou um número? {}'.format(var.isnumeric()))
print('Sou um texto? {}'.format(var.isalpha()))
print('Sou um Alfanumérico? {}'.format(var.isalnum()))