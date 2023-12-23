# Recebendo o número do usuário
n = int(input('Digite um número: '))

# Iniciando o laço de 1 até o 'n' + 1 porque assim ele conta até o valor digitado,
# já que ele não considera o ultimo número
for i in range(1, n+1):
    # Mostrando na tela o valor de i de acordo com o número da repetição atual
    print(i)

# Ao sair do laço de repetição printamos fim
print('Fim.')
