nome = str(input('Digite seu nome: '))

# apenas com if é uma condição simples
if nome.lower() == 'maxsuel':
    print('Que nome bonito {} parabéns.'.format(nome))
# Aqui já se torna uma condição aninhada
elif nome.lower() == 'ana' or nome.lower() == 'joão' or nome.lower() == 'maria' or nome.lower() == 'pedro':
    print('Seu nome é muito comum no Brasil.')
# Aqui podemos ver um segundo aninhamento, e podemos ter quantos quizermos.
elif nome.lower() in 'roberta joana paula creuza':
    print('Que belo nome feminino.')
# sendo apenas if e else seria uma condição composta apenas, mas com o elif se torna uma condição composta aninhada
else:
    print('Hum, não sei o que pensar do seu nome.')

print('Tenha um ótimo dia, {}!'.format(nome))