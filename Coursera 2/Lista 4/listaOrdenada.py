#Função para verificar se uma lista esta ordenada;
def ordenada(lista):
  #Laço que percorrerá os elementos da lista;
  for i in range(len(lista)):

    #Laço que percorrerá os elemntos em busca de algum que não esteja ordenado;
    for j in range(i+1, len(lista)):
      #se o elemento i da lista for maior que o elemento j da lista, ela não estará ordenada;
      if lista[i] > lista[j]:
        return False
  
  #se o algoritmo passou por toda a lista significa que ela esta ordenada;
  return True
