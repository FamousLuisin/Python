# Desempacotamento

lista = ["Luis", "Noc", "Flinton"]

lista_dois = [['mike', 'tominaga', 'japones'], ['Luis', 'Noc', 'Flinston'], ['Pato', 'Gui', 'Vagabundo']]

nome1, *_1 = lista
_, nome2, *_2 = lista # o * é para desempacotar criando outra lista
_, _, nome3, *_3 = lista

print(nome1, _1)
print(nome2, _2)
print(nome3, _3)


# Tuplas = Lista imutavel
tupla = ("Luis", "Noc", "Flinton")
tupla_dois = tuple(lista)
print(tupla[1])

# Desempacotamento em função
for nome in lista:
    print(nome, end=" ")

print()

# Igual ao for só que mais simples
print(*lista)
print(*lista[1])

# Desempacotamento de lista dentro de lista
print(*lista_dois, sep="\n")

# Desempacotar listas
lista = [
    [50, 'noki'],
    [27, 'flinston'],
    [78, 'jhonson']
]

for i, nome in lista:
    print(i, nome)