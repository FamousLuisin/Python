from exercicio01_dump import Carro
import json

def carregar():
    dados = []
    caminho_arquivo = "C:\\Users\\lufim\\Documents\\GitHub\\Python\\Udemy\\Section 5\\exercicios\\exercicio01\\Dados.json"
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        print('Arquivo não existe')
    return dados

def mostrar(carros):
    carros = instanciar(carros)

    for carro in carros:
        print(carro.marca)

def instanciar(carros):
    carros_instanciados = []
    for carro in carros:
        carros_instanciados.append(Carro(**carro))
    
    return carros_instanciados

carros = carregar()
mostrar(carros)