# Dicionario são esturturas de dados do tipo par de "chave" e "valor".
# Chaves podem ser considerado indices.
# recebe tipos imutaveis.
# Dicionarios são mutaveis assim como as listas.
# O valor pode ser qualquer outro, incluindo outro dicionario.
# Usamos chaves {} ou a classe dict para criar.
# Usado geralmente para objetos que possuem atributos (pessoa, produto , ...)

pessoa = dict(
    nome='Luís Filipe',
    sobrenome='Melo',
)

pessoa = {
    'nome': 'Luís Filipe',
    'sobrenome': 'Melo',
    'idade': 18,
    'altura': 1.75,
    'endereços': [
        {'cidade': 'Gama'},
        {'cidade': 'Brasília'}
    ]
}

print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])