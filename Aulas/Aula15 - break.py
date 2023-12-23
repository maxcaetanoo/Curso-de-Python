# Todas as variaveis recebem 0
cont = maior = menor = soma = 0

# Loop infinito
while True:

    # Número digitado
    num = int(input('Digite um número ou [100 - sair]: '))

    # Condição de saída do loop
    if num == 100:
        break

    # Contador que verifica quantos números foram digitados
    cont += 1

    # Somador, que soma um valor ao total anterior
    soma += num

    # Condição de o contador estiver iniciando agora
    if cont == 1:
        # Maior e Menor irão receber o primeiro numero digitado
        maior = menor = num

    # Caso o contador seja acima de 1
    else:
        # Comparador de maior numero entre maior e num
        if num > maior:

            # Se num foi maior então Maior recebe num
            maior = num

        # Comparador de menor numero ente menor e num
        elif num < menor:

            # Se num foi menor então Menor recebe num
            menor = num

# Prints com f'String
print(f'Foram digitados {cont} números, e:')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}, e a soma de todos números digitados foi {soma}')