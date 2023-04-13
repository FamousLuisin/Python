#Função para ordenção apartir da selection sort;
def ordena(lista):
    
  #Laço que passará por todos os elemntos da lista;
  for i in range(len(lista)):
    
    #Laço que passará por todos elementos da lista procurando o menor e ordenando;
    for j in range(i+1, len(lista)):
        
      #if que servirá para decidir se o elemntos i da lista é menor ou maior que o elemnto j;
      if lista[j] < lista[i]:
          
        #Se j for menor ele inverterá os valores de i e j na lista;
        lista[i], lista[j] = lista[j], lista[i] 

  return lista