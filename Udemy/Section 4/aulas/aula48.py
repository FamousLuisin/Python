# melhor forma de salvar um dicionario em python é usando json
# USado para salve dados simples (tuplas são convertidas para listas)

import json
import os

caminho_pasta = os.path.dirname(__file__) + '/aula48/'

# pessoa = {
#     'nome': 'Luiz Otávio 2',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# criar o arquivo json e salvar os dados nele
# with open(caminho_pasta + 'aula48.json', 'w', encoding='utf-8') as arquivo:
#     # fazer um dump em um arquivo
#     json.dump(
#         pessoa, arquivo,
#         ensure_ascii=False, # Não usar padrões da tabela ascii
#         indent=2, # identar bonitinho no arquivo
#     )

# Puxar os dados de um arquivo json e salvar eles
with open(caminho_pasta + 'aula48.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    for chave in pessoa:
        print(chave, pessoa[chave])