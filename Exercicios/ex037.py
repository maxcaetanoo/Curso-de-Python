'''Escreva um programa em Python que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.'''

num = int(input('Digite um número inteiro para conversão: '))
print('''Digite um tipo de conversão
      1 - binário;
      2 - octal;
      3 - hexadecimal;''')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print('O número {} convertido para base Binária é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} convertido para base Octal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} convertido para base Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção não encontrada, tente novamente mais tarde.')
