# set são mutaveis, porém so aceitam elementos imutaveis
# Não possuem ordens ou indices

# Criar set ( são "parecidos" com dicionarios, porem não possuem chave, apenas o valor)
set1 = set() # set vazio
set1 = {'Noki', 1, 2, 3} # set com dados
print(set1)

# São eficientes para remover valores duplicados de interaveis
set2 = {1, 2, 3, 3, 3, 1}
print(set2)

l1 = [1, 2, 3, 3, 3, 1]
set3 = set(l1)
l2 = list(set3)
print(set3)
print(l2)

# Mesmo não tendo indices, eles ainda podem ser iteraveis (usar: for in not in)
set4 = {1, 2, 3}
print(4 in set4, 1 in set4, 3 not in set4)

for numero in set4:
    print(numero)
