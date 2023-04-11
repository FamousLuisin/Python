"""
for i in lista:

for i in range(fim):

for i in range(inicio, fim):

for i in range(inicio, fim, passo):

for i in lista: print(i)

"""


def main():
  numero = int(input("Digite: "))
  lista = []

  while numero != 0:
    
    lista.append(numero)
    numero = int(input("Digite: "))
  
  """tamanho = len(lista) - 1
  for x in range(tamanho, -1, -1):
    print(lista[x])
    
  OU

  while tamanho >= 0
    print(lista[tamanho])
    tamanho -= 1
  """

  lista.reverse()

  for item in lista:
    print(item)



main()