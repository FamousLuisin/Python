def multiplica(m1, m2):
  matriz_multiplicada = []
  #Mudar linha do primeiro;
  for lin in range(len(m1)):
    matriz_multiplicada.append([])
    #Mudar coluna do segundo;
    for col in range(len(m2[0])):
      matriz_multiplicada[lin].append(0)
      #fazer o calculo linha X coluna;
      for k in range(len(m1[0])):
        matriz_multiplicada[lin][col] += m1[lin][k] * m2[k][col]
  
  return matriz_multiplicada


def sao_multiplicaveis(m1, m2):
  num_col1 = len(m1[0])
  num_lin2 = len(m2)
  if num_col1 == num_lin2:
    return multiplica(m1, m2)
  
  else:
    return False

print(sao_multiplicaveis([[2, 3], [1, 0], [4, 5]], [[3, 1], [2, 4]]))