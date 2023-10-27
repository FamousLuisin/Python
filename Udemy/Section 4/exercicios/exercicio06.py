import copy

produtos = [
    {'nome': 'Mustang', 'preco': 50000.00},
    {'nome': 'Supra', 'preco': 20000.00},
    {'nome': 'Miata', 'preco': 15000.00},
    {'nome': 'opala', 'preco': 25000.00},
    {'nome': 'ferrari', 'preco': 100000.00}
]

novos_produtos = [
   {'preco': round(produto['preco'] * 1.1, 2)} 
   for produto in copy.deepcopy(produtos)
]

print('=====Valor Antigo====='.center(40))
print(*produtos, sep='\n')

print()

print('=====Valor Novo====='.center(40))
print(*novos_produtos, sep='\n')