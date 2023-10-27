import copy

produtos = [
    {'nome': 'Mustang', 'preco': 50000.00},
    {'nome': 'Supra', 'preco': 20000.00},
    {'nome': 'Miata', 'preco': 15000.00},
    {'nome': 'Opala', 'preco': 25000.00},
    {'nome': 'Ferrari', 'preco': 100000.00}
]

produtos_ordenados_nome = copy.deepcopy(produtos)

produtos_ordenados_nome.sort(reverse=True, key=lambda item: item['nome'])

print('=====Valor Antigo====='.center(40))
print(*produtos, sep='\n')

print()

print('=====Valor Novo====='.center(40))
print(*produtos_ordenados_nome, sep='\n')

