# Podem me salvar futuramente
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*iterator, sep='\n')
    print()

pessoas = [
    'João', 'Luís', 'Noki', 'Jhonson'
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliester']
]

print('Combinações')
combinacao_duas_pessoas = list(combinations(pessoas, 2))
print_iter(combinacao_duas_pessoas)

print('Permutações')
permutar_duas_pessoas = list(permutations(pessoas, 2))
print_iter(permutar_duas_pessoas)

print('Produtos')
print_iter(product(*camisetas))


