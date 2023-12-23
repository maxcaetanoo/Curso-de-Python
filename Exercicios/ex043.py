'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

peso = float(input('Nos informe seu peso: Kg'))
altura = float(input('Nos informe sua altura: M'))
IMC = peso / pow(altura, 2)

print('Seu IMC é de {:.1f} '.format(IMC), end='')

# – IMC abaixo de 18,5: Abaixo do Peso
if IMC < 18.5:
    print('Seu indice é de SUBPESO')

# – Entre 18,5 e 25: Peso Ideal
elif IMC < 25:
    print('Seu indice é de PESO IDEAL')

# – 25 até 30: Sobrepeso
elif IMC < 30:
    print('Seu indice é de SOBREPESO')

# – 30 até 40: Obesidade
elif IMC < 40:
    print('Seu indice é de OBESIDADE')

# – Acima de 40: Obesidade Mórbida
else:
    print('Seu indice é de OBESIDADE MORBIDA')
