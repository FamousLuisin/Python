# List comprehension

print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

# para cada laço do for adcionar o numero na lista
lista2 = [
    numero * 2
    for numero in range(10)
] # para cada laço do for adcionar o numero na lista
print(lista2)