from itertools import zip_longest

lista = [1, 2, 3, 4, 10]
lista_2 = [1, 2, 3, 4]

lista_unida_menor = [
    (x + y) 
    for x, y in zip(lista, lista_2)
]

lista_unida_maior = [
    (x + y) 
    for x, y in zip_longest(lista, lista_2, fillvalue=0)
]


print(lista_unida_menor)
print(lista_unida_maior)
