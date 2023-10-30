from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def funcao_reduce(acumulador, produto):
    return acumulador + produto['preco']

# reduce faz a sima de uma lista de dicionarios, ou lista de listas ou tuplas
total = reduce(
    # lambda acumulador, produto: acumulador + produto['preco'],
    funcao_reduce,
    produtos, 
    0
)

print(total)

total2 = 0
for p in produtos:
    total2 += p['preco']

print(total2)