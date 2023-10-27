from itertools import zip_longest

def unir_listas(lista_one, lista_two):
    
    maximo_range = min(len(lista_one), len(lista_two))
    lista_unida = []

    for i in range(maximo_range):
        lista_unida.append((lista_one[i], lista_two[i]))

    return [
        (lista_one[i], lista_two[i]) for i in range(maximo_range)
    ]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

teste = unir_listas(l1, l2)

print(teste)

# Ela esta unindo os valores pelo indice de cada lista, usando como base a lista menor
print(list(zip(l1, l2))) # A função zip faz o mesmo que a função unir_listas

# Ela esta unindo os valores pelo indice de cada lista, usando como base a lista maior
# Caso acabe uma das listas ele irá retornar None, junto com o valorees restantes da lista maior
print(list(zip_longest(l1, l2, fillvalue='...')))