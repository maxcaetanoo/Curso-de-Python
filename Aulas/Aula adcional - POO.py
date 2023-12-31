class Carro:# Classe carro
    def __init__(self, marca, modelo):# Como deve ser instanciado o objeto
        self.marca = marca
        self.modelo = modelo

    def __str__(self):# Retorno do objeto em formato str()
        return f"{self.marca} {self.modelo}"


def cadastrar_carros():# Função para cadastrar os carros
    quantidade = int(input("Quantos carros você deseja cadastrar? "))
    carros = []

    for i in range(quantidade):
        marca = input(f"Digite a marca do carro {i+1}: ")
        modelo = input(f"Digite o modelo do carro {i+1}: ")
        carro = Carro(marca, modelo)
        carros.append(carro)

    return carros


def salvar_carros_em_arquivo(carros):# Função para salvar os carros em um arquivo
    with open("carros.txt", "w") as arquivo:
        for carro in carros:
            arquivo.write(f"{carro.marca},{carro.modelo}\n")


def ler_carros_do_arquivo():# Função para ler os carros do arquivo
    carros = []
    try:
        with open("carros.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                carro = Carro(dados[0], dados[1])
                carros.append(carro)
    except FileNotFoundError:
        pass
    return carros


def exibir_carros(carros):# Função para exibir os carros cadastrados
    if not carros:
        print("Não há carros cadastrados.")
    else:
        print("Carros cadastrados:")
        for i, carro in enumerate(carros, start=1):
            print(f"{i}. {carro}")


# Main - Execução do programa
carros_cadastrados = ler_carros_do_arquivo()
exibir_carros(carros_cadastrados)

novos_carros = cadastrar_carros()
carros_cadastrados.extend(novos_carros)

salvar_carros_em_arquivo(carros_cadastrados)
exibir_carros(carros_cadastrados)
