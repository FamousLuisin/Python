lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

print('\nList Comprehension')
lista2 = [
    numero * 2
    for numero in range(10)
]
print(lista2)


# Mapeamento de dados
# (gerar uma lista, atraves de outra, mantendo o numero de dados e talves alterando alguns valores)
# Filtro de dados (filtrar os valores que voce qr e os que vc nn quer)

print('\nMapeamento e filtragem de dados')
produtos = [
    {'nome': 'p1', 'preco': 50},
    {'nome': 'p2', 'preco': 60},
    {'nome': 'p3', 'preco': 70}
]

# Copiando e mapeando "produtos"
novos_produtos = [
    {'nome': produto['nome'], 'preco': produto['preco']} for produto in produtos
]

# Copiando e mapeando "produtos", mas mudando o valor de algumas chaves
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.5} 
    if produto['preco'] > 60 else {**produto} # esse if antes faz parte do mapeamento
    for produto in produtos
    if produto['preco'] > 50 # esse if dps do for é para filtrar os dados
]
print(*novos_produtos, sep='\n')

print('\nDois for')
lista = [
    (x, y) # O que vai ser entregue a lista
    for x in range(3)
    for y in range(3)
]
print(lista)