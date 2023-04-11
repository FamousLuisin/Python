def remove_repetidos(lista):
  lista2 = []

  for item in lista:
    if not item in lista2:
      lista2.append(item)
  
  lista2.sort()

  return lista2



#FUNCIONA MAS NÃO DEVERIA ^-^
"""def remove_repetidos(lista):
  lista.sort()
  tamanho = len(lista) - 1

  x = 0

  while x < tamanho:
    verifica = True
    while x != tamanho and verifica:
      if lista[x] == lista[x + 1]:
        del lista[x + 1]
        tamanho -= 1

      else:
        verifica = False

    x += 1

  print(lista)

remove_repetidos([1,1,2,2,3,3])"""
