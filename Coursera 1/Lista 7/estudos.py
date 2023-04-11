"""
.type --> vê o tipo de uma variavel (int, float, str);

.append --> adciona um elemento ao final da lista;

len() --> Informa quantos caracteres, ha em uma str, ou quantas variaveis há dentro de uma lista;

lista = [] --> [] serve para criar uma lista, no casi vazia;



========================================
for i in lista:
  comandos

for i in range(fim):
  comandos

for i in range(inicio, fim):
  comandos

for i in range(inicio, fim, passo):
  comandos

for i in lista: print(i)


========================================
lista[x:y] --> Pega os elementos de x até y - 1;

lista[x: ] --> Pega os elementos de x até o fim da lista;

lista[ :y] --> Pega os elementos do inicio da lista até y - 1;


========================================
def clonagem(lista):
  clone = []
  for iten in lista:
    clone.append(iten)
  return clone

OU

lista[:] --> Clona uma lista


========================================
[1, 2] + [3, 4] == [1, 2, 3, 4] --> + serve para concaternar listas

[1, 2, 3] * 3 = [1, 2, 3, 1, 2, 3, 1, 2, 3] --> * serve para repeti uma lista
"""


