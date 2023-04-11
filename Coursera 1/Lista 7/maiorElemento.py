def maior_elemento(lista):
  maior = lista[0]
  for x in range(len(lista)):
    if lista[x] > maior:
      maior = lista[x]
  
  return maior

