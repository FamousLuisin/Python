#definir funçao de busca binaria
def busca_binaria(lista, elemento, min=0, max=None):
  #se o max ainda nn possui um valor (Não foi chamado recursivamente), ele recebe o tamanha da lista
  if max == None:
    max = len(lista) - 1
  
  #se o min é maior que o max, significa que o algoritmo ja percorreu toda a lista e nn tem o que se procura;
  if min > max:
    return False
  
  #se não, continua a busca
  else:
    meio = (min + max) // 2
    #se o elemento do meio for igual ao que se procurar, encontramos o que queria;
    if lista[meio] == elemento:
      #retornar aonde esta o elemento;
      return meio
    
    #se não encontrar e o elemento no meio da lista for maior, o max recebe esse elemento - 1, anulando todo o fim da lista
    elif lista[meio] > elemento:
      return busca_binaria(lista, elemento, min, meio - 1)
    
    #se não encontrar e o elemento no meio da lista for menor, o mmin recebe esse elemento + 1, anulando todo o inicio da lista
    else:
      return busca_binaria(lista, elemento, min + 1, max)
  
    
