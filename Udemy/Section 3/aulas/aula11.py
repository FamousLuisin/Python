lista = ["Luis", "Noc", "Flinton"]
lista.append("Jhonson")



for item in enumerate(lista): # devolve um interator enumerando cada item da lista
    print(item)

print()
    
for item in enumerate(lista): # devolve um interator enumerando cada item da lista
    indice, nome = item # Desempacotar
    print(indice, nome)

print()

for indice, nome in enumerate(lista):
    print(indice, nome)


# OBS: não é bom colcoar enumarate dentro de lista, pois só vai conseguir usar aquela nova lista apenas uma vez
