'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = str(input('Digite o nome de uma cidade, e vamos ver se nela tem "Santo": ')).capitalize().strip()

if cidade.find("Santo") == 0:
    print('Aqui tem "Santo" no começo da cidade.')
else:
    print('Aqui não tem "Santo" no começo da cidade.')'''

# Outra solução

cidade = str(input('Digite o nome da cidade e vamos ver se tem "Santo": ')).capitalize().strip()

print("Santo" in cidade[0:5])
