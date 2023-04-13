class ordena:

  #Definir função bolha (bubbleSort)
  def bubble_sort(self, lista):
    #Definindo o fim da lista
    fim = len(lista)
    """Ao fim da primeira interação coma lista o valor mais"pesada" estará ordenado, 
    logo não será necessario a verificação dele, excluindo-o das proximas interações"""
    for i in range(fim-1, 0, -1):
      #Analisa (Faz uma varredura) i vezes na lista;
      for j in range(i):
        #analisa o elemento na posição j com o na posiçao j+1
        if lista[j] > lista[j+1]:
          #se o elemnto em j for amiro q j+1, elese invertem de local
          lista[j], lista[j+1] = lista[j+1], lista[j]
          print(lista)

    return lista

  
  #Função para ordenção apartir da selection sort;
  def selection_sort(self, lista):
    
    #Laço que passará por todos os elemntos da lista;
    for i in range(len(lista)):
    
      #Laço que passará por todos elementos da lista procurando o menor e ordenando;
      for j in range(i+1, len(lista)):
        
        #if que servirá para decidir se o elemntos i da lista é menor ou maior que o elemnto j;
        if lista[j] < lista[i]:
          
          #Se j for menor ele inverterá os valores de i e j na lista;
          lista[i], lista[j] = lista[j], lista[i] 

    return lista
    #Definir função bolha (bubbleSort)
  
  
  def bubble_curta(self, lista):
    #Definindo o fim da lista
    fim = len(lista)
    """Ao fim da primeira interação coma lista o valor mais"pesada" estará ordenado, 
    logo não será necessario a verificação dele, excluindo-o das proximas interações"""
    for i in range(fim-1, 0, -1):
      trocou = False
      for j in range(i):
        if lista[j] > lista[j+1]:
          lista[j], lista[j+1] = lista[j+1], lista[j]
          trocou = True
    
      if not trocou:
        return lista
      
    return lista

  #BRABO
  def insertion_sort(self, lista):
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
