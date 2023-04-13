#Definir função bolha (bubbleSort)
def bubble_sort(lista):
  #Definindo o fim da lista
  fim = len(lista)
  """Ao fim da primeira interação coma lista o valor mais"pesada" estará ordenado, 
  logo não será necessario a verificação dele, excluindo-o das proximas interações"""
  for i in range(fim-1, 0, -1):
    for j in range(i):
      if lista[j] > lista[j+1]:
        lista[j], lista[j+1] = lista[j+1], lista[j]
        print(lista)

  return lista
