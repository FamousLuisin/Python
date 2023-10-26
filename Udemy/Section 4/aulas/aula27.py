def generator(lista): # generator com for
    for item in lista:
        yield item
    return 'FIM'

gen = generator([1, 2, 3, 4])

for n in gen: # passar por cada item do generator (nesse caso for funciona como uma especie de next())
    print(n)