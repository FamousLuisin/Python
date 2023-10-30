# map, partial, GeneratorType e esgotamento de Iterators

from functools import partial
from types import GeneratorType


# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * 1.1, 2)

def muda_preco(produto):
    return {
        **produto, 
        'preco': aumentar_dez_porcento(produto['preco'])} 


# Partial, faz algo parecido com clousere (algo parecido com aula 7 e 17 dessa section)
aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

print_iter(produtos)

# novos_produtos = [
#     {**produto, 'preco': aumentar_dez_porcento(produto['preco'])} 
#     for produto in produtos
# ]


# É o mesmo que fazer o mapeamento de dados aula 20
novos_produtos = list(map( # Cria um iterator do tipo map (tem q converter em uma lista se nn quiser esgotar)
    muda_preco, produtos
))

print_iter(novos_produtos) 