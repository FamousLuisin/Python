lista = ["Luis", "Noc", "Flinton"]

for indice in range(len(lista)):
    print(indice, lista[indice])

for i, item in enumerate(lista):
    print(i, item)

for item in enumerate(lista): # Devolve tuplas
    print(item)