# Metodos
print('=====METODOS=====')

# set vazio
s1 = set()
print(s1)

# Adicionar elemento
print()
s1.add('Noki')
s1.add(666)
print('Adicionar:', s1)

# fazer update
print()
s1.update(('olá mundo',)) # Adiciona de maneira iterada (colocar a frase completa usar tupla/entre colchetes)
print('Update:', s1)

# descartar valor
print()
s1.discard('Noki') # já que nn tem indice, deve digitar o valor do valor
print('Descartar:', s1)


# limpar
print()
s1.clear()
print('limpar:', s1)

# Operadores
print()
print('=====OPERADORES=====')

s2 = {1, 2, 3}
s3 = {3, 4, 5}

# União de sets
s4 = s2 | s3 

print(s2)
print(s3)
print('União:', s4)

# Intersecção de sets
print()
s4 = s2 & s3
print(s2)
print(s3)
print('Intersecção:', s4)

# Diferença de sets
print()
s4 = s2 - s3 # O que tem no primeiro e não nem no segundo
print(s2)
print(s3)
print('Difreneça 1:', s4)

s4 = s3 - s2 # O que tem no primeiro e não nem no segundo
print('Difreneça 2:', s4)

# Diferença simetrica
print()
s4 = s2 ^ s3 # O que tem em um e nn tem no outro
print(s2)
print(s3)
print('Difreneça simatrica:', s4)