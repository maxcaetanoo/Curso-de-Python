'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2)/2

if media < 5.0:
    print('Você foi reprovado e irá repetir a segunda série, sua média foi {:.1f}'.format(media))
elif 5.0 <= media < 7:
    print("Vai ficar de recuperação, ainda tem chance de passar para a terceira série, sua media foi {:.1f}".format(media))
else:
    print('Você foi aprovado com honras agora pode correr no parquinho, sua média foi {:.1f}'.format(media))
