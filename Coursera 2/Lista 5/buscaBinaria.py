#definindo a funçao de busca binaria;
def busca(lista, elemento):
  #primeiro elemento da lista
  primeiro = 0
  #ultimo elemento da lista
  ultimo = len(lista) - 1

  while primeiro <= ultimo:
    #elemento do meio
    meio = (ultimo + primeiro) // 2
    print(meio)

    #se o elemento no meio for igual ao elemento desejado;
    if lista[meio] == elemento:
      return meio
    
    #se não for igual;
    else:
      
      #se o elemento do meio for maior que o desejado ultimo se torna o do meio, abandonando toda a parte maior que o elemento desejado;
      if lista[meio] > elemento:
        ultimo = meio - 1
      
      #se o elemento do meio for menor que o desejado primeiro se torna o do meio, abandonando toda a parte menor que o elemento desejado;
      else:
        primeiro = meio + 1
    

      
  return False


