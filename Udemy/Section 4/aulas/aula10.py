import copy

carro = {
    'marca': 'Honda',
    'modelo': 'Civic',
    'ano': 1994,
    'lista': ['Pato', 'Mike', 'Noc']
}

# copy faz uma copia de tudo que for imutável e linka os valores mutaveis (copia rasa),
# se tiver uma lista(mutavel) dentro do dic ele irá apontar os dois para a mesma lista,
carro2 = carro.copy()

# Copia profunda (copia tudo inclusive as listas sem linkar)
carro3 = copy.deepcopy(carro)

carro2['ano'] = 2001
carro2['lista'][0] = 'Lulu' # Aqui trocou tanto do carro quanto do carro2

carro3['lista'][1] = 'Gigi' # Aqui so trocou do carro3 e nn sofreu a alteração não é afetado

print(carro)
print(carro2)
print(carro3)