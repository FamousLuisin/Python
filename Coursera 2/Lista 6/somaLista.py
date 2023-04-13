def soma_lista(lista):

  tamanho = len(lista) - 1
  
  if tamanho == 0:
    return lista[0]
  
  else: 
    return lista[tamanho] + soma_lista(lista[:tamanho])

