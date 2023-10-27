# count é um iterador sem fim
from itertools import count

c1 = count(10) # podemos colocar um inicio
r1 = range(10)

print('count')
for i in c1:
    if i > 100:
        break
    print(i)

print('range')
for i in r1:
    print(i)