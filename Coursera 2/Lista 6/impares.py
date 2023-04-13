def encontra_impares(lista):
  listaImpar = []
  tamanho = len(lista) - 1

  if tamanho == 0:

    if lista[0] % 2 != 0:
      listaImpar.append(lista[0])
  
  else:

    if lista[0] % 2 != 0:
      listaImpar.append(lista[0])
      listaImpar.extend(encontra_impares(lista[1:]))
    
    else:
      listaImpar.extend(encontra_impares(lista[1:]))
  
  return listaImpar

print(encontra_impares([1,2,3,5,7,9,11]))

