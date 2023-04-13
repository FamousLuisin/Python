def insertion_sort(lista):
    #Definindo o fim da lista;
    fim = len(lista)
    #Laço vai pegar um numero por vez;
    for i in range(1, fim):
      #A chave esta guardando o numero da posiçao i;
      chave = lista[i]
      j = i 
      """Como o a chave ta guardando o numeor na posição i, pode mudar de posição os outros numeros, 
      sem se preocupar em perde a aquele numero;"""
      #While que vai correr por todo array de tras até a frente;
      while j > 0 and chave < lista[j - 1]:
        lista[j] = lista[j - 1]
        j -= 1
      
      #No final se coloca a chave na posição de j, a qual foi a ultima q houve alteração no array;
      lista[j] = chave
    
    return lista