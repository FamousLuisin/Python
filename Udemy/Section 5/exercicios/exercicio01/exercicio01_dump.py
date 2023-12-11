import json
import os

class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

def salvar_json(dados):
    caminho_arquivo = "C:\\Users\\lufim\\Documents\\GitHub\\Python\\Udemy\\Section 5\\exercicios\\exercicio01\\Dados.json"
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(dados, arquivo, indent=2, ensure_ascii=False)
    return dados

def adicionar(dados):
    marca = input("Digite a marca: ")
    modelo = input("Digite a modelo: ")
    ano = input("Digite a ano: ")
    cor = input("Digite a cor: ")

    carro = Carro(marca=marca, modelo=modelo, ano=ano, cor=cor)

    dados.append(vars(carro))

def main():
    dados = []
    while True:
        os.system('cls')
        adicionar(dados)
        
        continuar = int(input("\nDeseja continuar? [1]Sim [2]Não: "))
        if continuar == 2:
            salvar_json(dados)
            break
    
    print('Fim')

if __name__ == '__main__':
    main()