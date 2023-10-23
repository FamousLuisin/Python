pessoa = {
    'nome': 'Luís Filipe',
    'sobrenome': 'Melo',
    # 'idade': 21,
}

# Vai mostrar quantas chaves há naquele dicionario
print('===len===')
print(len(pessoa)) 

# Entrega um tipo de lista com todas as chaves daquele dicionario (entrega um dict)
print('\n===keys===')
print(tuple(pessoa.keys())) # Podemos converser em tuplas
print(list(pessoa.keys())) # Ou em uma lista

# Entrega os valores de cada chaves (entrega um dict)
print('\n===value===')
print(list(pessoa.values()))

# Entrega as chaves e os valores delas (entrega um dict)
print('\n===items===')
print(list(pessoa.items())) # Podemos converter igual o ".keys"

for chave, valor in pessoa.items(): # Enumarate
    print(f"{chave}: {valor}")

# Valor padrão (evita erros caso não exista aquela chave)
print('\n===setdefault===')
pessoa.setdefault('idade', None)
print(pessoa['idade'])